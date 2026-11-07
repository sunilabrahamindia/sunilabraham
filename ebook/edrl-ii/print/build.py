#!/usr/bin/env python3
"""Build the EDRL II print interior and cover review PDFs with Typst."""
from pathlib import Path
import re
import shutil
import subprocess
import urllib.request
import yaml
from bs4 import BeautifulSoup, NavigableString
from copy import deepcopy

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "ebook" / "edrl-ii"
PRINT = BASE / "print"
OUT = PRINT / "output"
OUT.mkdir(parents=True, exist_ok=True)
COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-v0.2.jpg"
COVER = OUT / "edrl-ii-cover.jpg"

def run(args):
    subprocess.run(args, cwd=ROOT, check=True)

def fetch_cover():
    request = urllib.request.Request(COVER_URL, headers={"User-Agent": "EDRL-II-print-build"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    if len(data) < 10000 or not data.startswith(b"\xff\xd8\xff"):
        raise SystemExit("Cover download failed validation; expected a JPEG image.")
    COVER.write_bytes(data)

def inline_markdown(node):
    """Preserve emphasis in HTML-authored footnote text."""
    if isinstance(node, NavigableString):
        return str(node)
    name = getattr(node, "name", None)
    content = "".join(inline_markdown(child) for child in getattr(node, "children", []))
    if name in ("em", "i"):
        return f"*{content}*"
    if name in ("strong", "b"):
        return f"**{content}**"
    if name == "br":
        return "\n"
    return content


def note_inline(node):
    """Render inline content inside a source footnote."""
    if isinstance(node, NavigableString):
        return str(node)
    name = getattr(node, "name", None)
    if name == "a" and node.get("href", "").startswith("#ref-"):
        return ""
    content = "".join(note_inline(child) for child in getattr(node, "children", []))
    if name in ("em", "i"):
        return f"*{content}*"
    if name in ("strong", "b"):
        return f"**{content}**"
    if name == "br":
        return " "
    return content


def note_blocks(node, list_indent=0):
    """Preserve paragraphs and nested lists within longer footnotes."""
    parts = []
    inline_buffer = []

    def flush_inline():
        value = re.sub(r"\s+", " ", "".join(inline_buffer)).strip()
        if value:
            parts.append(value)
        inline_buffer.clear()

    for child in node.children:
        if isinstance(child, NavigableString):
            inline_buffer.append(str(child))
            continue
        name = getattr(child, "name", None)
        if name == "a" and child.get("href", "").startswith("#ref-"):
            continue
        if name in ("p", "div"):
            flush_inline()
            value = note_inline(child).strip()
            if value:
                parts.append(value)
        elif name in ("ol", "ul"):
            flush_inline()
            parts.append(note_list(child, list_indent))
        else:
            inline_buffer.append(note_inline(child))
    flush_inline()
    return "\n\n".join(part for part in parts if part).strip()


def note_list(listing, indent=0):
    """Retain list boundaries and alphabetic labels inside source notes."""
    entries = []
    list_type = listing.get("type", "1")
    for index, item in enumerate(listing.find_all("li", recursive=False), start=1):
        if list_type == "a":
            marker = f"{chr(96 + index)}."
        elif list_type == "A":
            marker = f"{chr(64 + index)}."
        else:
            marker = f"{index}."
        body = note_blocks(item, indent + 4)
        if not body:
            continue
        lines = body.splitlines()
        prefix = " " * indent
        continuation = " " * (indent + len(marker) + 1)
        entry = prefix + marker + " " + lines[0]
        if len(lines) > 1:
            entry += "\n" + "\n".join(
                continuation + line if line else "" for line in lines[1:]
            )
        entries.append(entry)
    return "\n".join(entries)


def footnote_markdown(item):
    """Extract a source note without flattening paragraphs or nested lists."""
    return note_blocks(item)

def html_table_to_markdown(table):
    """Preserve an HTML table as a Pandoc pipe table before generic HTML cleanup."""
    rows = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        values = []
        for cell in cells:
            value = re.sub(r"\s+", " ", inline_markdown(cell).strip())
            values.append(value.replace("|", r"\|"))
        rows.append(values)
    if not rows:
        return ""
    thead = table.find("thead")
    header_rows = thead.find_all("tr") if thead else []
    if header_rows:
        header_cells = header_rows[0].find_all(["th", "td"], recursive=False)
        header = [re.sub(r"\s+", " ", inline_markdown(cell).strip()).replace("|", r"\|") for cell in header_cells]
        all_rows = table.find_all("tr")
        header_index = next(i for i, row in enumerate(all_rows) if row is header_rows[0])
        data_rows = rows[:header_index] + rows[header_index + 1:]
    else:
        header, data_rows = rows[0], rows[1:]
    width = max([len(header)] + [len(row) for row in data_rows])
    header += [""] * (width - len(header))
    data_rows = [row + [""] * (width - len(row)) for row in data_rows]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in data_rows)
    return "\n".join(lines)


def extract_footnotes_and_clean(markdown):
    """Convert HTML tables and website footnotes before generic HTML cleanup."""
    soup = BeautifulSoup(markdown, "html.parser")
    notes = []
    for item in soup.select('li[id^="note-"]'):
        match = re.search(r"note-(\d+)", item.get("id", ""))
        if not match:
            continue
        number = match.group(1)
        for backlink in item.select('a[href^="#ref-"]'):
            backlink.decompose()
        note_text = footnote_markdown(item).strip()
        if note_text:
            notes.append((int(number), note_text))
        item.decompose()
    for listing in soup.find_all("ol"):
        if not listing.get_text(" ", strip=True):
            listing.decompose()

    for table in soup.find_all("table"):
        converted = html_table_to_markdown(table)
        table.replace_with(NavigableString("\n\n" + converted + "\n\n"))

    for marker in soup.select('sup[id^="ref-"]'):
        match = re.search(r"ref-(\d+)", marker.get("id", ""))
        if match:
            marker.replace_with(NavigableString(f"[^{match.group(1)}]"))

    for anchor in soup.find_all("a"):
        anchor.unwrap()
    for tag in soup.find_all(["strong", "b"]):
        tag.insert_before(NavigableString("**"))
        tag.insert_after(NavigableString("**"))
        tag.unwrap()
    for tag in soup.find_all(["em", "i"]):
        tag.insert_before(NavigableString("*"))
        tag.insert_after(NavigableString("*"))
        tag.unwrap()
    for tag in soup.find_all("br"):
        tag.replace_with(NavigableString("\n"))
    for tag in soup.find_all(True):
        tag.unwrap()

    cleaned = soup.decode_contents()
    cleaned = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", cleaned)
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.S)
    cleaned = re.sub(r"(?m)^\s*<[^>]+>\s*$", "", cleaned)
    cleaned = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", cleaned)
    cleaned = cleaned.strip()
    if notes:
        # These source headings introduce endnote lists that are converted above
        # into page-bottom footnotes. Remove the now-redundant heading only
        # when note entries were successfully extracted.
        cleaned = re.sub(
            r"(?mi)^[ \t]*#{1,6}[ \t]+Notes(?:[ \t]+\{#notes\})?[ \t]*\n?",
            "",
            cleaned,
        )
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
        cleaned += "\n\n" + "\n".join(
            f"[^{n}]: {text}" for n, text in sorted(notes)
        )
    return cleaned

def clean_source(path):
    raw = path.read_text(encoding="utf-8")
    # Preserve explicitly marked poem blocks through HTML cleanup.
    raw = re.sub(
        r'<div class="poem"[^>]*>(.*?)</div>',
        lambda match: "\n\n@@POEM_START@@\n" + match.group(1).strip("\n") + "\n@@POEM_END@@\n\n",
        raw,
        flags=re.S | re.I,
    )
    raw = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.S)
    raw = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", raw)
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)

    # Capture source footnotes before trimming publication metadata. In several
    # essays the Notes list appears after the Publication section.
    source_soup = BeautifulSoup(raw, "html.parser")
    source_note_items = [
        deepcopy(item) for item in source_soup.select('li[id^="note-"]')
    ]

    lines = raw.splitlines()
    full = next((i for i, line in enumerate(lines)
                 if re.match(r"^##\s+Full\s+[Tt]ext\b", line.strip())), None)
    if full is not None:
        lines = lines[full + 1:]
    else:
        contents = next((i for i, line in enumerate(lines)
                         if re.match(r"^##\s+Contents\b", line.strip())), None)
        if contents is not None:
            end = next((i for i in range(contents + 1, len(lines))
                        if re.match(r"^#{1,6}\s+", lines[i].strip())), len(lines))
            lines = lines[end:]
    end = next((i for i, line in enumerate(lines)
                if re.match(r"^##\s+Publication\b", line.strip())
                or re.match(r"^\{%\s*include\s+navbox-amaa", line.strip())
                or re.match(r"^<style\b", line.strip())), len(lines))
    lines = lines[:end]
    body = "\n".join(lines).strip()
    body = re.sub(r"(?m)^\s*>\s?", "", body)
    body = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", body)

    # Replace any partial in-body note list with the complete list captured above.
    body_soup = BeautifulSoup(body, "html.parser")
    for item in body_soup.select('li[id^="note-"]'):
        item.decompose()
    for item in source_note_items:
        body_soup.append(item)
    body = body_soup.decode_contents()

    references = set(re.findall(
        r"""<sup\b[^>]*\bid=["']ref-(\d+)[^"']*["'][^>]*>""", body, re.I
    ))
    note_ids = set(re.findall(
        r"""<li\b[^>]*\bid=["']note-(\d+)["'][^>]*>""",
        "".join(str(item) for item in source_note_items), re.I
    ))
    missing = sorted(references - note_ids, key=int)
    unreferenced = sorted(note_ids - references, key=int)
    if missing or unreferenced:
        problems = []
        if missing:
            problems.append("missing note entries: " + ", ".join(missing))
        if unreferenced:
            problems.append("unreferenced note entries: " + ", ".join(unreferenced))
        raise SystemExit(f"Footnote audit failed for {path.name}: {'; '.join(problems)}")
    return extract_footnotes_and_clean(body)

def md_to_typst(markdown, stem):
    def convert(segment, suffix):
        md = OUT / f"{stem}-{suffix}.md"
        typ = OUT / f"{stem}-{suffix}.typ"
        md.write_text(segment, encoding="utf-8")
        run(["pandoc", str(md), "--from=markdown+smart", "--to=typst", "--output", str(typ)])
        content = typ.read_text(encoding="utf-8")
        if re.search(r"</?(?:p|div|span|li|ol|ul|a|sup|br|strong|em|h[1-6])(?:\\s|/?>)", content, re.I):
            raise SystemExit(f"Raw HTML survived conversion in {stem}; refusing to publish a malformed proof.")
        return content

    # Convert prose normally, but centre explicitly marked poems without prose indentation.
    parts = []
    cursor = 0
    pattern = re.compile(r"@@POEM_START@@(.*?)@@POEM_END@@", re.S)
    for index, match in enumerate(pattern.finditer(markdown), start=1):
        prose = markdown[cursor:match.start()].strip()
        if prose:
            parts.append(convert(prose, f"prose-{index}"))
        poem = convert(match.group(1).strip(), f"poem-{index}")
        parts.append(
            "#block(width: 100%, above: 1em, below: 1em)[\n"
            "  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)\n"
            "  #align(center)[\n" + poem + "\n  ]\n]"
        )
        cursor = match.end()
    remainder = markdown[cursor:].strip()
    if remainder:
        parts.append(convert(remainder, "prose-final"))
    if not parts:
        return convert(markdown, "main")
    return "\n\n".join(parts)

manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

fetch_cover()
common = r"""
#set text(font: "Linux Libertine O", size: 11pt, lang: "en")
#set par(justify: true, leading: 0.85em, first-line-indent: 1.1em, spacing: 12pt)
#set heading(numbering: none)
#set block(spacing: 0.55em)
#set footnote.entry(
  separator: line(length: 30%, stroke: 0.5pt + luma(90)),
  clearance: 0.6em,
  gap: 0.35em,
)
#set page(
  paper: "a5",
  binding: left,
  margin: (inside: 18mm, outside: 14mm, top: 18mm, bottom: 17mm),
  header: context [
    #set text(size: 7.5pt, fill: luma(85))
    #align(center)[ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    #v(3pt)
    #line(length: 100%, stroke: 0.5pt + luma(170))
  ],
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
#show heading.where(level: 1): it => block(above: 14pt, below: 17pt, breakable: false)[
  #set text(font: "Linux Libertine O", size: 18pt, weight: "bold")
  #align(center)[#it]
]
#show heading.where(level: 2): it => block(above: 16pt, below: 12pt, breakable: false)[
  #set text(size: 16pt, weight: "bold")
  #it
]
#show heading.where(level: 3): it => block(above: 11pt, below: 10pt, breakable: false)[
  #set text(size: 14pt, weight: "bold")
  #it
]
"""
parts = [common]
parts.append(r"""
#set heading(outlined: false)
#set page(header: none, footer: none)
#align(center)[
  #v(45mm)
  #text(size: 22pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
]
#pagebreak()
#pagebreak()
#align(center)[
  #v(25mm)
  #text(size: 12pt, weight: "bold", tracking: 1.8pt)[THE SUNIL ABRAHAM PROJECT]
  #v(24mm)
  #text(size: 22pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
  #v(14mm)
  #text(size: 17pt, weight: "bold")[A. M. Abraham Ayrookuzhiel]
  #v(18mm)
  #text(size: 10.5pt, style: "italic")[Edited by]
  #v(2mm)
  #text(size: 12pt)[Tito Dutta]
]
#pagebreak()
#set page(
  header: context [
    #set text(size: 7.5pt, fill: luma(85))
    #align(center)[ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    #v(3pt)
    #line(length: 100%, stroke: 0.5pt + luma(170))
  ],
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
#align(center)[
  #v(12mm)
  #text(size: 13pt, weight: "bold")[Publication details]
]
#v(8mm)
*Essays on Dalits, Religion and Liberation II*

A. M. Abraham Ayrookuzhiel

Edited by Tito Dutta

Published by The Sunil Abraham Project

https://sunilabraham.in

#v(5mm)
First paperback edition, 29 November 2026

ISBN 978-93-345-8524-7

Printed price: ₹250

#v(5mm)
Language: English

#v(8mm)
#text(size: 8.5pt, style: "italic", fill: luma(80))[Typesetting and printing credits will be added when the production details are confirmed.]
#pagebreak()
= Foreword
#text(style: "italic", fill: luma(90))[Placeholder: Foreword text to be added after it is received and approved.]
#pagebreak()
= Editor's Note
#align(center)[
  #text(size: 9pt)[DRAFT VERSION — NOT YET FINALISED]
]
#v(8pt)
_Essays on Dalits, Religion and Liberation II_ by A. M. Abraham Ayrookuzhiel is being published on the occasion of the thirtieth death anniversary of the author.

The first volume, _Essays on Dalits, Religion and Liberation_, was published in 2006 on the occasion of the tenth death anniversary of A. M. Abraham Ayrookuzhiel. Published by the Asian Trading Corporation, Bangalore, for the Christian Institute for the Study of Religion and Society (CISRS), the volume included a foreword by Dr. Godwin Shiri and an introduction by Dr. K. C. Abraham.

In October 2025, we started working on the Sunil Abraham Project. One of the main objectives of the project from its inception was to document, preserve and make the works of A. M. Abraham Ayrookuzhiel more widely accessible. This work gradually expanded to include the collection of his writings, biographical documentation, publication records and related archival materials, bringing them together through the A. M. A. Ayrookuzhiel portal.

A substantial body of A. M. Abraham Ayrookuzhiel's work has been published on the web portal at https://sunilabraham.in/amaa/portal, including his essays, books and book reviews. The present volume brings together nine essays that were not included in the previously published collected works, continuing the publication of his important writings on Dalits, religion and liberation.

These nine essays were originally published in different journals and publications over several decades, from the 1970s to the 1990s. Most appeared in _Religion and Society_, published by the Christian Institute for the Study of Religion and Society (CISRS). One essay appeared in the _Indian Journal of Theology_, while "Dalit Theology: A Movement of Counter-Culture" was published in _Towards a Dalit Theology_ in 1988. Bringing these writings together makes available work that had remained dispersed across different publications and decades.

As the work of collecting and preparing A. M. Abraham Ayrookuzhiel's writings continues, further essays may be identified for inclusion in a revised and expanded edition of this volume in the future. As this is an initial version, any errors or inaccuracies brought to our attention will be corrected in a subsequent edition.

#v(18pt)
#grid(columns: (1fr, 1fr), [Kolkata

29 November 2026], [#align(right)[Tito Dutta]])
#pagebreak()
= Contents
#outline(title: none, depth: 1, target: heading.where(level: 1))
#pagebreak()
#set heading(outlined: true)
""")

for essay in essays:
    title = essay["title"]
    source = ROOT / essay["source"]
    if not source.is_file():
        raise SystemExit(f"Missing essay source: {essay['source']}")
    raw = source.read_text(encoding="utf-8")
    parts.append("#pagebreak()\n")
    parts.append("#counter(footnote).update(0)\n")
    parts.append(f"= {title}\n")
    parts.append(f"""#block(width: 100%, inset: (top: 7pt, bottom: 8pt), stroke: (top: 0.55pt + luma(150), bottom: 0.55pt + luma(150)))[
  #align(center)[
    #text(size: 7pt, weight: "bold", tracking: 1pt, fill: luma(90))[ORIGINAL PUBLICATION]
    #v(3pt)
    #text(size: 8.5pt, style: "italic", fill: luma(75))[{essay['publication_note']}]
  ]
]
#v(7pt)
""")
    if "under-construction.html" in raw:
        parts.append(r"""#block(inset: 12pt, stroke: 0.6pt + luma(175))[
  *Transcription pending*

  The source page is currently under construction. The complete essay text has not yet been supplied to this print workflow. This placeholder preserves the planned sequence and must be replaced before publication.
]
""")
        continue
    body = clean_source(source)
    if len(body) < 500:
        raise SystemExit(f"Extraction looks incomplete for {title}: only {len(body)} characters.")
    converted = md_to_typst(body, f"essay-{essay['order']}")
    parts.append(converted + "\n")

interior_source = OUT / "edrl-ii-interior.typ"
interior_source.write_text("\n".join(parts), encoding="utf-8")
typst = shutil.which("typst")
if not typst:
    raise SystemExit("Typst CLI is not installed.")
interior = OUT / "edrl-ii-interior.pdf"
run([typst, "compile", "--font-path", "/usr/share/fonts/truetype", str(interior_source), str(interior)])

# The front-cover proof is separate from the interior, as required for book printing.
cover_source = OUT / "edrl-ii-front-cover.typ"
cover_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-cover.jpg", width: 148mm, height: 210mm, fit: "contain")
''', encoding="utf-8")
cover_pdf = OUT / "edrl-ii-front-cover-proof.pdf"
run([typst, "compile", str(cover_source), str(cover_pdf)])

# Convenience reading copy: cover proof followed by the interior. This is NOT the printer's interior file.
run(["pdfunite", str(cover_pdf), str(interior), str(OUT / "edrl-ii-combined-review.pdf")])
for path in (interior, cover_pdf, OUT / "edrl-ii-combined-review.pdf"):
    if not path.is_file() or path.stat().st_size < 10000:
        raise SystemExit(f"Expected PDF missing or unexpectedly small: {path}")
print(f"Interior: {interior} ({interior.stat().st_size:,} bytes)")
print(f"Front cover proof: {cover_pdf} ({cover_pdf.stat().st_size:,} bytes)")
print("Combined review PDF created. Cover and interior remain separate production files.")
