#!/usr/bin/env python3
"""Build the EDRL II print interior and cover review PDFs with Typst."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import time
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
AUTHOR_PHOTO_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/a-m-a-ayrookuzhiel-print-book-photo-01.png"
AUTHOR_PHOTO = OUT / "author-portrait.png"
COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-v0.2.jpg"
COVER = OUT / "edrl-ii-cover.jpg"

BODY_PAR = "#set par(justify: true, leading: 1.2em, first-line-indent: 1.1em, spacing: 16pt)"


def run(args):
    subprocess.run(args, cwd=ROOT, check=True)


def download(url, dest, label, validator):
    last_error = None
    for attempt in range(1, 4):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "EDRL-II-print-build"})
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read()
            if len(data) < 10000 or not validator(data):
                raise ValueError(f"{label} failed validation")
            dest.write_bytes(data)
            return
        except Exception as error:
            last_error = error
            time.sleep(2 * attempt)
    raise SystemExit(f"{label} download failed after 3 attempts: {last_error}")


def fetch_author_photo():
    download(AUTHOR_PHOTO_URL, AUTHOR_PHOTO, "Author photograph",
             lambda d: d.startswith(bytes.fromhex("89504e470d0a1a0a")))


def fetch_cover():
    download(COVER_URL, COVER, "Cover", lambda d: d.startswith(b"\xff\xd8\xff"))


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
    raw = re.sub(
        r'<div class="poem"[^>]*>(.*?)</div>',
        lambda match: "\n\n@@POEM_START@@\n" + match.group(1).strip("\n") + "\n@@POEM_END@@\n\n",
        raw,
        flags=re.S | re.I,
    )
    raw = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.S)
    raw = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", raw)
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)

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

    # Protect Markdown ATX headings while BeautifulSoup handles embedded HTML.
    # Parsing Markdown as HTML can otherwise alter heading boundaries and turn
    # the tail of a long heading into an ordinary paragraph.
    heading_tokens = {}
    def protect_heading(match):
        token = f"TSAP_MARKDOWN_HEADING_{len(heading_tokens)}_PRESERVE"
        heading_tokens[token] = match.group(0)
        return token

    body = re.sub(r"(?m)^#{1,6}[ \t]+[^\n]+$", protect_heading, body)

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
    cleaned = extract_footnotes_and_clean(body)
    for token, heading in heading_tokens.items():
        # BeautifulSoup wraps standalone Markdown headings in paragraph tags.
        # Remove the wrapper before restoring the Markdown heading.
        cleaned = cleaned.replace("<p>" + token + "</p>", "\n\n" + heading + "\n\n")
        cleaned = cleaned.replace(token, "\n\n" + heading + "\n\n")
    return cleaned


def md_to_typst(markdown, stem):
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
        # Paragraph separation is controlled only by the Typst par rules in
        # the template. Never inject spacing into the converted content.
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


def lint_typst(source):
    """Fail if a document-level par rule other than the two approved ones exists."""
    top_level = [
        (number, line) for number, line in enumerate(source.splitlines(), start=1)
        if line.startswith("#set par(")
    ]
    if len(top_level) != 2:
        details = "; ".join(f"line {n}: {l}" for n, l in top_level)
        raise SystemExit(
            "Unscoped #set par rules found (expected exactly 2: template and body restore). "
            + details
        )


def check_pdf_overlaps(pdf):
    """Flag text lines whose bounding boxes actually overlap vertically."""
    result = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf), "-"],
        capture_output=True, text=True, check=True,
    )
    issues = []
    line_re = re.compile(
        r'<line xMin="([\\d.]+)" yMin="([\\d.]+)" '
        r'xMax="([\\d.]+)" yMax="([\\d.]+)"'
    )

    for page_number, page in enumerate(result.stdout.split("<page ")[1:], start=1):
        lines = [
            tuple(float(v) for v in match.groups())
            for match in line_re.finditer(page)
        ]

        for i, a in enumerate(lines):
            for b in lines[i + 1:]:
                horizontal_overlap = min(a[2], b[2]) - max(a[0], b[0])
                vertical_overlap = min(a[3], b[3]) - max(a[1], b[1])

                if horizontal_overlap > 1 and vertical_overlap > 1:
                    issues.append(
                        f"page {page_number}: "
                        f"vertical overlap of {vertical_overlap:.1f}pt"
                    )

    if issues:
        message = f"{len(issues)} possible line collisions: " + "; ".join(issues[:20])
        if os.environ.get("EDRL_OVERLAP_CHECK", "fail") == "warn":
            print("WARNING: " + message)
        else:
            raise SystemExit(message)
    else:
        print("Overlap check passed: no colliding lines detected.")

manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

fetch_cover()
fetch_author_photo()
common = r"""
#set document(
  title: "Essays on Dalits, Religion and Liberation II",
  author: "A. M. Abraham Ayrookuzhiel",
  keywords: ("Dalits", "religion", "liberation", "A. M. Abraham Ayrookuzhiel"),
)
#set text(font: "Linux Libertine O", size: 11pt, lang: "en", hyphenate: false)
""" + BODY_PAR + r"""
#set heading(numbering: none)
#set footnote.entry(
  separator: line(length: 30%, stroke: 0.5pt + luma(90)),
  clearance: 0.6em,
  gap: 0.35em,
)
#show footnote.entry: it => context {
  let values = counter(footnote).at(it.note.location())
  let number = numbering(it.note.numbering, ..values)
  grid(
    columns: (1.4em, 1fr),
    gutter: 0.3em,
    align: top,
    [#text(size: 9.5pt)[#number.]],
    [
      #set text(size: 8.5pt, number-type: "lining")
      #set par(
        justify: false,
        first-line-indent: 0pt,
        hanging-indent: 0pt,
        leading: 1em,
        spacing: 0pt,
      )
      #it.note.body
    ],
  )
}
#let running-header = context {
  let current-page = here().page()
  let chapters = query(heading.where(level: 1)).filter(
    item => item.body != [Foreword]
      and item.body != [Editor's Note]
      and item.body != [About the Author]
      and item.body != [Contents]
  )
  let first-chapter = if chapters.len() > 0 { chapters.first() } else { none }
  let intentional-blank = first-chapter != none and first-chapter.location().page() == current-page + 1
  let before-first-chapter = first-chapter != none and first-chapter.location().page() > current-page
  let chapter-starts-here = chapters.any(item => item.location().page() == current-page)
  let previous-chapters = chapters.filter(item => item.location().page() < current-page)
  let current-chapter = if previous-chapters.len() > 0 { previous-chapters.last() } else { none }
  if intentional-blank {
    []
  } else if before-first-chapter {
    []
  } else if chapter-starts-here {
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
#show heading.where(level: 1): it => block(above: 0pt, below: 7pt, breakable: false)[
  #set text(font: "Linux Libertine O", size: 19pt, weight: "bold", hyphenate: false)
  #set par(justify: false, first-line-indent: 0pt, leading: 1.15em, spacing: 0pt)
  #align(left)[#it]
]
#show heading.where(level: 2): it => block(above: 16pt, below: 12pt, breakable: false)[
  #text(size: 16pt, weight: "bold", hyphenate: false)[#it.body]
]
#show heading.where(level: 3): it => block(above: 11pt, below: 10pt, breakable: false)[
  #text(size: 14pt, weight: "bold", hyphenate: false)[#it.body]
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
signature_typst = r"""#block(width: 100%, breakable: false)[
  #align(right)[
    #set par(justify: false, first-line-indent: 0pt, leading: 0.75em, spacing: 0pt)
    #text(size: 10.5pt, weight: "bold")[Dr. Y. T. Vinayaraj]
    #linebreak()
    #text(size: 9pt)[Director,]
    #linebreak()
    #text(size: 8.5pt)[Christian Institute for the Study of]
    #linebreak()
    #text(size: 8.5pt)[Religion and Society]
  ]
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
  #text(size: 22pt, weight: "bold")[Essays on]
  #linebreak()
  #text(size: 22pt, weight: "bold")[Dalits, Religion and Liberation II]
]
#pagebreak()
#pagebreak()
#align(center)[
  #v(25mm)
  #v(24mm)
  #text(size: 22pt, weight: "bold")[Essays on]
  #linebreak()
  #text(size: 22pt, weight: "bold")[Dalits, Religion and Liberation II]
  #v(14mm)
  #text(size: 17pt, weight: "bold")[A. M. Abraham Ayrookuzhiel]
]
#pagebreak()
#set page(header: none, footer: none, numbering: none)
#v(18mm)
#block(width: 100%, height: 170mm)[
  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt, leading: 1.25em)
  #text(size: 17pt, weight: "bold")[Essays on Dalits, Religion]
  #linebreak()
  #text(size: 17pt, weight: "bold")[and Liberation II]
  #v(1.1em)
  #text(size: 12pt)[A. M. Abraham Ayrookuzhiel]

  #v(1fr)

  #set text(size: 10pt)
  Website: https://sunilabraham.in
  #linebreak()
  Email: sunilabrahamindia\@gmail.com
  #linebreak()
  Mobile: +91 96111 00817
  #v(1.2em)
  #text(style: "italic", fill: luma(75))[Edited by Tito Dutta]
  #linebreak()
  #text(style: "italic", fill: luma(75))[Design and Print Production Advisor: Herbert Paul]

  #v(1fr)

  #set text(size: 10pt)
  First paperback edition published on 29 November 2026
  #linebreak()
  by The Sunil Abraham Project.
  #v(1.2em)
  ISBN: 978-93-345-8524-7
  #linebreak()
  Printed price: ₹250
  #v(1.2em)
  #text(size: 9pt, style: "italic", fill: luma(75))[Published in India]
]
#pagebreak()
#set page(header: none, footer: none, numbering: none)
#v(1fr)
#align(center)[
  #image("author-portrait.png", height: 178mm, fit: "contain")
]
#pagebreak()
#set page(header: none, footer: none, numbering: none)
#v(62mm)
#align(center)[
  #block(width: 82%)[
    #set text(size: 11.5pt)
    #set par(justify: false, first-line-indent: 0pt, leading: 0.85em, spacing: 0pt)
    #align(center)[
      So dance snake, dance!
      #linebreak()
      We'll set fire to divisions of caste,
      #linebreak()
      We'll debate philosophical questions in the market place;
      #linebreak()
      We'll have dealings with despised households,
      #linebreak()
      We'll go around in different paths.
    ]
    #v(6pt)
    #align(right)[
      #set par(justify: false, first-line-indent: 0pt, leading: 0.9em, spacing: 0pt)
      #text(size: 9.5pt)[— #emph[Cittar Gnanakkovai]]
      #linebreak()
      #text(size: 9.5pt)[Pambatti Cittar, verse 123.]
    ]
  ]
]
#pagebreak()
#set page(
  numbering: "i",
  header: running-header,
  footer: context {
    let current-page = here().page()
    let chapters = query(heading.where(level: 1)).filter(
      item => item.body != [Foreword]
        and item.body != [Editor's Note]
        and item.body != [About the Author]
        and item.body != [Contents]
    )
    let first-chapter = if chapters.len() > 0 { chapters.first() } else { none }
    let intentional-blank = first-chapter != none and first-chapter.location().page() == current-page + 1
    if not intentional-blank {
      set text(size: 8pt, fill: luma(65))
      align(center)[#counter(page).display("i")]
    }
  }
)
#counter(page).update(1)
""" + '#set par(justify: true, leading: 1.15em, first-line-indent: 1.1em, spacing: 16pt)' + r"""
#set heading(outlined: true)
= Foreword
@@FOREWORD_BODY@@
#pagebreak()
#set heading(outlined: true)
= Editor's Note
#v(14pt)
_Essays on Dalits, Religion and Liberation II_ by A. M. Abraham Ayrookuzhiel is being published on the occasion of the thirtieth death anniversary of the author. This volume continues the work begun with the publication of _Essays on Dalits, Religion and Liberation_ in 2006, marking the tenth anniversary of his death. The first volume was published by the Asian Trading Corporation, Bangalore, for the Christian Institute for the Study of Religion and Society (CISRS), with a foreword by Dr. Godwin Shiri and an introduction by Dr. K. C. Abraham.

In October 2025, work began on The Sunil Abraham Project. One of the project's objectives from its inception was to document, preserve and make the writings of A. M. Abraham Ayrookuzhiel more widely accessible. The work has since grown to include the collection of his writings, biographical documentation, publication records and related archival materials, brought together through the A. M. A. Ayrookuzhiel portal.

The present volume brings together nine essays that were not included in the earlier collected volume. These essays first appeared in different journals and publications over several decades, from the 1970s to the 1990s. Most were published in _Religion and Society_, the journal of the Christian Institute for the Study of Religion and Society. One appeared in the _Indian Journal of Theology_, while "Dalit Theology: A Movement of Counter-Culture" was published in _Towards a Dalit Theology_ in 1988. Their republication in one volume makes writings that were previously dispersed across publications and decades available together.

The essays reflect A. M. Abraham Ayrookuzhiel's sustained engagement with Dalit experience, religion, theology and liberation. Bringing them together is part of the continuing effort to preserve his intellectual contribution and make it accessible to readers, researchers and future generations.

The work of collecting and documenting his writings remains ongoing. Further essays and related materials may be identified as the archival work proceeds. Any errors or inaccuracies brought to the editors' attention will be examined and, where necessary, addressed in a subsequent edition.

#v(10pt)
#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.85em, spacing: 0pt)
  #text(size: 11pt, weight: "bold")[Tito Dutta]
  #linebreak()
  #text(size: 9.5pt)[Co-founder and Administrator]
  #linebreak()
  #text(size: 9pt)[The Sunil Abraham Project]
  #linebreak()
  #text(size: 8.5pt)[29 November 2026]
]
#pagebreak()
#set heading(outlined: true)
= About the Author
#v(10pt)
A. M. Abraham Ayrookuzhiel (18 September 1933 – 29 November 1996) was an Indian theologian, scholar and researcher whose work brought questions of religion into close conversation with the social and cultural realities of marginalised communities. Born in Chengannur, Kerala, he grew up in a region with a deep Christian heritage. His early schooling was in the villages around Puthenkavu. He later entered seminary formation in Thiruvananthapuram and pursued higher studies in philosophy and theology in Pune. He continued his academic formation in Rome and the United Kingdom, and was ordained in 1963.

A. M. Abraham Ayrookuzhiel's academic and professional journey took him across different church traditions and cultural settings. After his studies abroad, he joined the Anglican Church and served as a curate at St. Paul High Anglican Church in Wokingham, Berkshire, from 1970 to 1973. His time in the United Kingdom brought him into contact with wider ecumenical conversations and debates about the place of religion and the church in a changing society. He married Ponnamma Thekedath during this period. They returned to India in 1973.

In 1974, Abraham Ayrookuzhiel joined the Christian Institute for the Study of Religion and Society (CISRS) in Bangalore. He later became Associate Director, contributing to the institute's research, seminars and wider theological engagement. At CISRS, he turned sustained attention to the religious and cultural lives of Dalit communities and to the ways caste and social hierarchy shape religious identity. His research brought field studies into conversation with theological and social analysis, taking the experiences and cultural expressions of marginalised people seriously as sources for understanding religion.

A central concern in Abraham Ayrookuzhiel's writing was the relationship between faith and social emancipation. He questioned accounts of religion that obscured caste oppression or treated inherited social arrangements as natural. His studies explored Dalit identity, popular religious traditions, oral culture and forms of resistance expressed through stories, songs, myths and festivals. He argued that theology must engage with the lives and struggles of the oppressed, rather than remain confined to doctrine and institutional practice. His work therefore crossed the boundaries of theology, sociology and cultural study.

His publications include _The Sacred in Popular Hinduism: An Empirical Study in Chirakkal, North Malabar_ (1983) and _Swami Anand Thirth: Untouchability, Gandhian Solution on Trial_ (1987). He edited _The Dalit Desiyata: The Kerala Experience in Development and Class Struggle_ (1990), and later co-edited and co-authored works on Dalit poetry and literature. His essays addressed Dalit theology, religious identity and interfaith dialogue.

At the time of his death on 29 November 1996, A. M. Abraham Ayrookuzhiel was working on a study of Dalit and Hindu religious identity that remained incomplete. His writings brought together academic research, theological reflection and close attention to the social realities of his time. This volume makes a further part of his work available to readers.
#pagebreak()
= Contents
#show outline.entry: it => {
  let title = it.element.body
  let prefix = if title == [The State of Hinduism in 2000 A.D.—Some Emerging Trends] {
    [1.]
  } else if title == [Religion, Spirituality and Aspirations of the People] {
    [2.]
  } else if title == [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue] {
    [3.]
  } else if title == [The Church and the Study of Religion] {
    [4.]
  } else if title == [Religions and the Aspirations of the People] {
    [5.]
  } else if title == [Religion: A Way of Salvation or an Ideology of Oppression?] {
    [6.]
  } else if title == [Dalit Theology: A Movement of Counter-Culture] {
    [7.]
  } else if title == [Dalit Liberation — Some Reflections on Their Ideological Predicament] {
    [8.]
  } else if title == [The Ideological Nature of the Emerging Dalit Consciousness] {
    [9.]
  } else {
    it.prefix()
  }
  link(it.element.location(), it.indented(prefix, it.inner()))
}

#outline(
  title: none,
  depth: 1,
  target: heading.where(level: 1),
)
#pagebreak()
""")

for essay in essays:
    title = essay["title"]
    source = ROOT / essay["source"]
    if not source.is_file():
        raise SystemExit(f"Missing essay source: {essay['source']}")
    raw = source.read_text(encoding="utf-8")
    parts.append("#pagebreak()\n")
    if essay["order"] == 1:
        parts.append(r"""#set heading(outlined: true)
#set page(
  numbering: "1",
  header: running-header,
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
""")
        parts.append("#counter(page).update(1)\n")
    parts.append("#counter(footnote).update(0)\n")
    parts.append(f"= {title}\n")
    parts.append(f"""#block[
  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
  #v(9pt)
  #line(length: 100%, stroke: 0.55pt + luma(175))
  #v(4pt)
  #text(size: 7.5pt, weight: "bold", tracking: 0.65pt, fill: luma(85))[ORIGINAL PUBLICATION: ]
  #text(size: 9.5pt, style: "italic", fill: luma(65))[{essay['publication_note']}]
  #v(5pt)
  #line(length: 100%, stroke: 0.55pt + luma(175))
  #v(9pt)
]
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

interior_text = "\n".join(parts)
lint_typst(interior_text)
interior_source = OUT / "edrl-ii-interior.typ"
interior_source.write_text(interior_text, encoding="utf-8")
typst = shutil.which("typst")
if not typst:
    raise SystemExit("Typst CLI is not installed.")
interior = OUT / "edrl-ii-interior.pdf"
run([typst, "compile", "--font-path", "/usr/share/fonts/truetype", str(interior_source), str(interior)])
check_pdf_overlaps(interior)

cover_source = OUT / "edrl-ii-front-cover.typ"
cover_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-cover.jpg", width: 148mm, height: 210mm, fit: "contain")
''', encoding="utf-8")
cover_pdf = OUT / "edrl-ii-front-cover-proof.pdf"
run([typst, "compile", str(cover_source), str(cover_pdf)])

run(["pdfunite", str(cover_pdf), str(interior), str(OUT / "edrl-ii-combined-review.pdf")])
for path in (interior, cover_pdf, OUT / "edrl-ii-combined-review.pdf"):
    if not path.is_file() or path.stat().st_size < 10000:
        raise SystemExit(f"Expected PDF missing or unexpectedly small: {path}")
print(f"Interior: {interior} ({interior.stat().st_size:,} bytes)")
print(f"Front cover proof: {cover_pdf} ({cover_pdf.stat().st_size:,} bytes)")
print("Combined review PDF created. Cover and interior remain separate production files.")
