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
FOREWORD_SOURCE = BASE / "foreword.md"
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

def typst_escape(value):
    """Escape plain source text for safe insertion into Typst content blocks."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("#", "\\#")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("$", "\\$")
    )


def html_table_to_typst(table):
    """Create readable, accessible Typst tables with repeatable headers."""
    rows = []
    header_rows = table.find("thead")
    header_row = header_rows.find("tr") if header_rows else None
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        values = [
            re.sub(r"\s+", " ", inline_markdown(cell).strip())
            for cell in cells
        ]
        rows.append((row is header_row, [
            (value, cell.name == "th")
            for value, cell in zip(values, cells)
        ]))

    if not rows:
        return ""

    header_index = next(
        (index for index, (is_header, _) in enumerate(rows) if is_header),
        0,
    )
    header = rows[header_index][1]
    # Use concise, reader-facing labels in the print edition. The full wording
    # remains unchanged in the source article; these labels preserve its meaning
    # while preventing dense multi-line headings at A5 size.
    header_labels = {
        "Number of families": "Families",
        "Number of families with land": "Families with land",
        "Land-holding in acres": "Land held (acres)",
        "Percentage of total land": "Share of total land (%)",
        "No. of borewells and pumpsets": "Borewells and pumpsets",
        "No. of bullock carts": "Bullock carts",
        "No. of draught animals": "Draught animals",
        "No. of milk animals": "Milk animals",
        "No. of sheep and goats": "Sheep and goats",
        "Amount in Rs.": "Amount (Rs.)",
        "Fully employed in one's own farm and other occupations": "Fully employed: own farm / other work",
        "Partly agriculture and wage labourer": "Agriculture + wage labour",
        "Landless wage labourer": "Landless wage labour",
    }
    header = [
        (header_labels.get(value, value), is_header)
        for value, is_header in header
    ]
    data_rows = [
        cells for index, (_, cells) in enumerate(rows)
        if index != header_index
    ]
    width = max([len(header)] + [len(row) for row in data_rows])
    header += [("", False)] * (width - len(header))
    data_rows = [
        row + [("", False)] * (width - len(row))
        for row in data_rows
    ]

    # Give descriptive row labels more room and keep numerical columns compact.
    if width == 6:
        ratios = [2.1] + [0.85] * 5
        font_size = "8pt"
    elif width == 5:
        ratios = [2.2] + [0.85] * 4
        font_size = "8pt"
    elif width == 4:
        ratios = [1.8, 1.1, 1.1, 1.1]
        font_size = "8pt"
    elif width == 3:
        ratios = [2.0, 0.9, 1.1]
        font_size = "8.2pt"
    else:
        ratios = [2.0] + [1.0] * (width - 1)
        font_size = "8pt"

    def cell_content(value, header_cell=False, row_label=False):
        value = typst_escape(value)
        if header_cell or row_label:
            return f"table.cell(align: left, breakable: false)[*{value}*]"
        return f"table.cell(breakable: false)[{value}]"

    header_cells = ",\n    ".join(
        cell_content(value, header_cell=True)
        for value, _ in header
    )
    body_cells = []
    for row in data_rows:
        for value, is_row_label in row:
            body_cells.append(cell_content(value, row_label=is_row_label))

    cells = ",\n    ".join(body_cells)
    fence = chr(96) * 3
    return (
        fence + "{=typst}\n"
        f"#{{\n  set text(size: {font_size}, hyphenate: false)\n  set par(justify: false, first-line-indent: 0pt, spacing: 0pt)\n"
        "  table(\n"
        f"  columns: ({', '.join(f'{ratio}fr' for ratio in ratios)}),\n"
        "  align: (left, " + ", ".join(["center"] * (width - 1)) + "),\n"
        "  inset: (x: 3pt, y: 3.5pt),\n"
        "  stroke: (x, y) => (\n"
        "    bottom: if y == 0 { 0.8pt + luma(90) } else { 0.35pt + luma(175) },\n"
        "  ),\n"
        "  fill: (_, y) => if y == 0 { luma(94) },\n"
        "  table.header(\n"
        f"    {header_cells},\n"
        "  ),\n"
        f"  {cells},\n"
        "  )\n"
        "}\n"
        + fence + "\n"
    )


def extract_footnotes_and_clean(markdown):
    """Convert HTML tables and source-linked notes into Pandoc footnotes."""
    soup = BeautifulSoup(markdown, "html.parser")
    notes = {}
    for item in soup.select('li[id^="note-"]'):
        note_id = item.get("id", "")[len("note-"):]
        if not note_id:
            continue
        for backlink in item.select('a[href^="#ref-"]'):
            backlink.decompose()
        note_text = footnote_markdown(item).strip()
        if note_text:
            notes[note_id] = note_text
        item.decompose()
    for listing in soup.find_all("ol"):
        if not listing.get_text(" ", strip=True):
            listing.decompose()

    raw_tables = {}
    for index, table in enumerate(soup.find_all("table")):
        converted = html_table_to_typst(table)
        token = f"TSAP_RAW_TYPST_TABLE_{index}_PLACEHOLDER"
        raw_tables[token] = converted
        table.replace_with(NavigableString(token))


    for marker in soup.select('sup[id^="ref-"]'):
        target = marker.find("a", href=re.compile(r"^#note-"))
        if target:
            note_id = target.get("href", "")[len("#note-"):]
            if note_id not in notes:
                raise SystemExit(
                    f"Footnote reference {marker.get('id')} points to missing note-{note_id}."
                )
            marker.replace_with(NavigableString(f"[^{note_id}]"))

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
    for token, raw_table in raw_tables.items():
        cleaned = cleaned.replace(token, "\n\n" + raw_table + "\n\n")
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
        ordered_notes = sorted(
            notes.items(),
            key=lambda item: (int(re.match(r"\d+", item[0]).group()), item[0])
        )
        cleaned += "\n\n" + "\n\n".join(
            f"[^{note_id}]: {text}" for note_id, text in ordered_notes
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

    note_ids = {
        item.get("id", "")[len("note-"):]
        for item in source_note_items
        if item.get("id", "").startswith("note-")
    }
    references = set()
    for marker in body_soup.select('sup[id^="ref-"]'):
        target = marker.find("a", href=re.compile(r"^#note-"))
        if target:
            references.add(target.get("href", "")[len("#note-"):])
    missing = sorted(references - note_ids)
    unreferenced = sorted(note_ids - references)
    if missing or unreferenced:
        problems = []
        if missing:
            problems.append("missing note entries: " + ", ".join(missing))
        if unreferenced:
            problems.append("unreferenced note entries: " + ", ".join(unreferenced))
        raise SystemExit(f"Footnote audit failed for {path.name}: {'; '.join(problems)}")
    return extract_footnotes_and_clean(body)

def md_to_typst(markdown, stem):
    # Footnote definitions normally sit at the end of the complete essay.
    # Poems are converted in separate Typst blocks, so each conversion segment
    # must receive the definitions as well; otherwise references in earlier
    # segments are emitted as literal [^N] text by Pandoc.
    definition_pattern = re.compile(
        r"(?ms)^\[\^([^\]]+)\]:[ \t]*(.*?)(?=^\[\^[^\]]+\]:|\Z)"
    )
    definitions = []
    markdown_without_definitions = definition_pattern.sub(
        lambda match: definitions.append(match.group(0).strip()) or "",
        markdown,
    ).strip()

    def convert(segment, suffix):
        segment = segment.strip()
        if definitions:
            segment += "\n\n" + "\n\n".join(definitions)
        md = OUT / f"{stem}-{suffix}.md"
        typ = OUT / f"{stem}-{suffix}.typ"
        md.write_text(segment, encoding="utf-8")
        run(["pandoc", str(md), "--from=markdown+smart+raw_attribute", "--to=typst", "--output", str(typ)])
        content = typ.read_text(encoding="utf-8")
        if re.search(r"</?(?:p|div|span|li|ol|ul|a|sup|br|strong|em|h[1-6])(?:\s|/?>)", content, re.I):
            raise SystemExit(f"Raw HTML survived conversion in {stem}; refusing to publish a malformed proof.")
        raw_markers = re.findall(r"\[\^(\d+)\](?!:)", content)
        raw_definitions = re.findall(r"(?m)^\[\^(\d+)\]:", content)
        if raw_markers or raw_definitions:
            raise SystemExit(
                f"Unconverted footnote syntax in {stem}: "
                f"markers={','.join(raw_markers)}; definitions={','.join(raw_definitions)}"
            )
        return content

    # Convert prose normally, but centre explicitly marked poems without prose indentation.
    parts = []
    cursor = 0
    pattern = re.compile(r"@@POEM_START@@(.*?)@@POEM_END@@", re.S)
    for index, match in enumerate(pattern.finditer(markdown_without_definitions), start=1):
        prose = markdown_without_definitions[cursor:match.start()].strip()
        if prose:
            parts.append(convert(prose, f"prose-{index}"))
        poem = convert(match.group(1).strip(), f"poem-{index}")
        parts.append(
            "#block(width: 100%, above: 1em, below: 1em)[\n"
            "  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)\n"
            "  #align(center)[\n" + poem + "\n  ]\n]"
        )
        cursor = match.end()
    remainder = markdown_without_definitions[cursor:].strip()
    if remainder:
        parts.append(convert(remainder, "prose-final"))
    if not parts:
        return convert(markdown_without_definitions, "main")
    return "\n\n".join(parts)

manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

fetch_cover()
common = r"""
#set document(
  title: "Essays on Dalits, Religion and Liberation II",
  author: "A. M. Abraham Ayrookuzhiel",
  keywords: ("Dalits", "religion", "liberation", "A. M. Abraham Ayrookuzhiel"),
)
#set text(font: "Linux Libertine O", size: 11pt, lang: "en")
#set par(justify: true, leading: 0.85em, first-line-indent: 1.1em, spacing: 12pt)
#set heading(numbering: none)
#set block(spacing: 0.55em)
#set footnote.entry(
  separator: line(length: 30%, stroke: 0.5pt + luma(90)),
  clearance: 0.6em,
  gap: 0.35em,
)
#let running-header = context {
  let current-page = here().page()
  let chapters = query(heading.where(level: 1)).filter(
    item => item.body != [Foreword] and item.body != [Editor's Note] and item.body != [Contents]
  )
  let chapter-starts-here = chapters.any(item => item.location().page() == current-page)
  let previous-chapters = chapters.filter(item => item.location().page() < current-page)
  let current-chapter = if previous-chapters.len() > 0 { previous-chapters.last() } else { none }
  if chapter-starts-here {
    []
  } else {
    set text(size: 8pt, fill: luma(85))
    if calc.even(current-page) {
      align(center)[ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    } else if current-chapter != none {
      align(center)[#current-chapter.body]
    } else {
      align(center)[ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    }
    v(3pt)
    line(length: 100%, stroke: 0.5pt + luma(170))
  }
}
#set page(
  paper: "a5",
  binding: left,
  margin: (inside: 18mm, outside: 14mm, top: 18mm, bottom: 17mm),
  header: running-header,
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
#show heading.where(level: 1): it => block(above: 0pt, below: 10pt, breakable: false)[
  #set text(font: "Linux Libertine O", size: 19pt, weight: "bold", hyphenate: false)
  #set par(justify: false, first-line-indent: 0pt, leading: 1.15em, spacing: 0pt)
  #align(center)[#it]
]
#show heading.where(level: 2): it => block(above: 16pt, below: 12pt, breakable: false)[
  #set text(size: 16pt, weight: "bold", hyphenate: false)
  #it
]
#show heading.where(level: 3): it => block(above: 11pt, below: 10pt, breakable: false)[
  #set text(size: 14pt, weight: "bold", hyphenate: false)
  #it
]
"""
if not FOREWORD_SOURCE.is_file():
    raise SystemExit(f"Missing foreword source: {FOREWORD_SOURCE}")
foreword_markdown = FOREWORD_SOURCE.read_text(encoding="utf-8").strip()
poem_pattern = re.compile(r"(?ms)^:::\s*\{\.poem\}\s*\n(.*?)\n:::\s*$")
foreword_markdown, poem_count = poem_pattern.subn(
    lambda match: "\n\n@@POEM_START@@\n" + match.group(1).strip() + "\n@@POEM_END@@\n\n",
    foreword_markdown,
)
if poem_count != 1:
    raise SystemExit(f"Expected one foreword poem block, found {poem_count}.")
foreword_ref_count = len(re.findall(r"\[\^\d+\](?!:)", foreword_markdown))
foreword_note_count = len(re.findall(r"(?m)^\[\^\d+\]:", foreword_markdown))
if foreword_ref_count != 2 or foreword_note_count != 2:
    raise SystemExit(f"Foreword reference check failed: {foreword_ref_count} markers, {foreword_note_count} reference entries.")
signature_source = """**Y.T. Vinayaraj**  
Director, CISRS"""
if signature_source not in foreword_markdown:
    raise SystemExit("Original foreword signature not found")
foreword_markdown = foreword_markdown.replace(signature_source, "TSAPFOREWORDSIGNATURETOKEN")
foreword_typst = md_to_typst(foreword_markdown, "foreword")
signature_typst = r"""#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 1.2em, spacing: 0pt)
  #text(weight: "bold")[Dr. Y. T. Vinayaraj]
  #linebreak()
  #text(size: 9.5pt)[Director,]
  #linebreak()
  #text(size: 9pt)[Christian Institute for the Study of]
  #linebreak()
  #text(size: 9pt)[Religion and Society]
]"""
if "TSAPFOREWORDSIGNATURETOKEN" not in foreword_typst:
    raise SystemExit("Foreword signature marker did not survive conversion")
foreword_typst = foreword_typst.replace("TSAPFOREWORDSIGNATURETOKEN", signature_typst)

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
#set page(header: none, footer: none, numbering: none)
#v(1fr)
#align(center)[
  #block(width: 78%)[
    #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
    #align(left)[
      #text(size: 8pt, weight: "bold", tracking: 1.4pt, fill: luma(75))[THE SUNIL ABRAHAM PROJECT]
      #v(8mm)
      #text(size: 8pt, weight: "bold", tracking: 0.8pt, fill: luma(90))[PUBLICATION DETAILS]
      #v(3mm)
      #text(size: 16pt, weight: "bold", hyphenate: false)[Essays on Dalits, Religion and Liberation II]
      #v(2mm)
      #text(size: 10.5pt)[A. M. Abraham Ayrookuzhiel]
      #v(1mm)
      #text(size: 9pt, style: "italic", fill: luma(75))[Edited by Tito Dutta]
      #v(8mm)
      #line(length: 100%, stroke: 0.6pt + luma(135))
      #v(4mm)
      #grid(
        columns: (1fr, 2fr),
        column-gutter: 8mm,
        row-gutter: 3mm,
        [#text(size: 8pt, fill: luma(75))[PUBLISHER]],
        [#text(size: 9pt)[The Sunil Abraham Project]],
        [#text(size: 8pt, fill: luma(75))[WEBSITE]],
        [#text(size: 9pt)[https://sunilabraham.in]],
        [#text(size: 8pt, fill: luma(75))[EDITION]],
        [#text(size: 9pt)[First paperback edition, 29 November 2026]],
        [#text(size: 8pt, fill: luma(75))[ISBN]],
        [#text(size: 9pt)[978-93-345-8524-7]],
        [#text(size: 8pt, fill: luma(75))[PRINTED PRICE]],
        [#text(size: 9pt)[₹250]],
        [#text(size: 8pt, fill: luma(75))[LANGUAGE]],
        [#text(size: 9pt)[English]],
      )
      #v(4mm)
      #line(length: 100%, stroke: 0.6pt + luma(135))
      #v(4mm)
      #text(size: 8pt, style: "italic", fill: luma(80))[Typesetting and printing credits will be added when the production details are confirmed.]
    ]
  ]
]
#pagebreak()
#set page(
  numbering: "i",
  header: running-header,
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("i")]
  ],
)
#counter(page).update(1)
= Foreword
@@FOREWORD_BODY@@
#pagebreak()
= Editor's Note
#v(14pt)
_Essays on Dalits, Religion and Liberation II_ by A. M. Abraham Ayrookuzhiel is being published on the occasion of the thirtieth death anniversary of the author. This volume continues the work begun with the publication of _Essays on Dalits, Religion and Liberation_ in 2006, marking the tenth anniversary of his death. The first volume was published by the Asian Trading Corporation, Bangalore, for the Christian Institute for the Study of Religion and Society (CISRS), with a foreword by Dr. Godwin Shiri and an introduction by Dr. K. C. Abraham.

In October 2025, work began on The Sunil Abraham Project. One of the project's objectives from its inception was to document, preserve and make the writings of A. M. Abraham Ayrookuzhiel more widely accessible. The work has since grown to include the collection of his writings, biographical documentation, publication records and related archival materials, brought together through the A. M. A. Ayrookuzhiel portal.

The present volume brings together nine essays that were not included in the earlier collected volume. These essays first appeared in different journals and publications over several decades, from the 1970s to the 1990s. Most were published in _Religion and Society_, the journal of the Christian Institute for the Study of Religion and Society. One appeared in the _Indian Journal of Theology_, while "Dalit Theology: A Movement of Counter-Culture" was published in _Towards a Dalit Theology_ in 1988. Their republication in one volume makes writings that were previously dispersed across publications and decades available together.

The essays reflect A. M. Abraham Ayrookuzhiel's sustained engagement with Dalit experience, religion, theology and liberation. Bringing them together is part of the continuing effort to preserve his intellectual contribution and make it accessible to readers, researchers and future generations.

The work of collecting and documenting his writings remains ongoing. Further essays and related materials may be identified as the archival work proceeds. Any errors or inaccuracies brought to the editors' attention will be examined and, where necessary, addressed in a subsequent edition.

#v(18pt)
#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 1.2em, spacing: 0pt)
  #text(size: 9pt)[29 November 2026]
  #v(4pt)
  #text(weight: "bold")[Tito Dutta]
  #linebreak()
  #text(size: 9.5pt)[Co-founder and Administrator]
  #linebreak()
  #text(size: 9pt)[The Sunil Abraham Project]
]
#pagebreak()
= Contents
#outline(title: none, depth: 1, target: heading.where(level: 1))
#pagebreak()
#set heading(outlined: true)
#set page(
  numbering: "1",
  header: running-header,
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
""")

for essay in essays:
    title = essay["title"]
    source = ROOT / essay["source"]
    if not source.is_file():
        raise SystemExit(f"Missing essay source: {essay['source']}")
    raw = source.read_text(encoding="utf-8")
    parts.append("#pagebreak()\n")
    if essay["order"] == 1:
        parts.append("#counter(page).update(1)\n")
    parts.append("#counter(footnote).update(0)\n")
    parts.append("#v(24mm)\n")
    parts.append(f"= {title}\n")
    parts.append(f"""#v(9pt)
#align(center)[
  #text(size: 8pt, weight: "bold", tracking: 1.2pt, fill: luma(90))[ORIGINAL PUBLICATION]
  #v(4pt)
  #text(size: 9pt, style: "italic", fill: luma(75))[{essay['publication_note']}]
]
#v(22pt)
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

if len(parts) < 2 or "@@FOREWORD_BODY@@" not in parts[1]:
    raise SystemExit("Foreword insertion point missing from print template.")
parts[1] = parts[1].replace("@@FOREWORD_BODY@@", foreword_typst)

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
