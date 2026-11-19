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
from bs4 import BeautifulSoup, NavigableString, Tag
from copy import deepcopy

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "ebook" / "edrl-ii"
FOREWORD_SOURCE = BASE / "foreword.md"
PRINT = BASE / "print"
OUT = PRINT / "output"
OUT.mkdir(parents=True, exist_ok=True)
FRONTMATTER_DIVIDER = OUT / "frontmatter-divider.svg"
ESSAY_DIVIDER = OUT / "essay-divider.svg"

def write_heading_dividers():
    # Original, restrained engraved-style ornaments drawn as vector SVG.
    FRONTMATTER_DIVIDER.write_text("""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="36" viewBox="0 0 1200 36">
<g fill="none" stroke="#77736d" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round">
  <path d="M2 18 H472 M728 18 H1198"/>
  <path d="M472 18 C492 18 498 8 516 8 C534 8 540 28 558 28 C576 28 584 18 600 18 C616 18 624 28 642 28 C660 28 666 8 684 8 C702 8 708 18 728 18"/>
  <path d="M520 9 C508 2 494 3 486 9 C499 8 510 12 520 9 Z"/>
  <path d="M548 27 C535 35 520 33 512 27 C526 29 538 28 548 27 Z"/>
  <path d="M680 9 C692 2 706 3 714 9 C701 8 690 12 680 9 Z"/>
  <path d="M652 27 C665 35 680 33 688 27 C674 29 662 28 652 27 Z"/>
  <path d="M558 28 C565 21 568 13 564 6 M642 28 C635 21 632 13 636 6"/>
  <path d="M564 6 C554 1 544 3 540 9 C550 8 558 10 564 6 Z"/>
  <path d="M636 6 C646 1 656 3 660 9 C650 8 642 10 636 6 Z"/>
  <path d="M584 18 C590 12 594 12 600 18 C606 12 610 12 616 18 C610 24 606 24 600 18 C594 24 590 24 584 18 Z"/>
</g>
<circle cx="600" cy="18" r="2.2" fill="#77736d"/>
</svg>""", encoding="utf-8")
    HALF_TITLE_ORNAMENT.write_text("""<svg xmlns="http://www.w3.org/2000/svg" width="220" height="32" viewBox="0 0 220 32">
<g fill="none" stroke="#6f6b64" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 16 H78 M142 16 H217"/>
  <path d="M78 16 C88 16 91 7 100 7 C108 7 111 16 110 16 C109 16 112 25 120 25 C129 25 132 16 142 16"/>
  <path d="M100 7 C96 2 89 2 85 6 C91 6 96 8 100 7 Z"/>
  <path d="M120 25 C124 30 131 30 135 26 C129 26 124 24 120 25 Z"/>
  <path d="M110 16 C104 11 99 12 96 16 C100 20 105 21 110 16 Z"/>
  <path d="M110 16 C116 11 121 12 124 16 C120 20 115 21 110 16 Z"/>
</g>
<circle cx="110" cy="16" r="1.5" fill="#6f6b64"/>
</svg>""", encoding="utf-8")
    ESSAY_DIVIDER.write_text("""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="36" viewBox="0 0 1200 36">
<g fill="none" stroke="#918b80" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round">
  <path d="M2 18 H520 M680 18 H1198"/>
  <path d="M520 18 C540 18 548 8 566 8 C581 8 588 14 600 18 C612 14 619 8 634 8 C652 8 660 18 680 18"/>
  <path d="M520 18 C540 18 548 28 566 28 C581 28 588 22 600 18 C612 22 619 28 634 28 C652 28 660 18 680 18"/>
  <path d="M566 8 C558 1 545 2 538 9 C550 7 559 11 566 8 Z"/>
  <path d="M634 8 C642 1 655 2 662 9 C650 7 641 11 634 8 Z"/>
  <path d="M566 28 C558 35 545 34 538 27 C550 29 559 25 566 28 Z"/>
  <path d="M634 28 C642 35 655 34 662 27 C650 29 641 25 634 28 Z"/>
  <path d="M580 18 C586 11 594 11 600 18 C606 11 614 11 620 18 C614 25 606 25 600 18 C594 25 586 25 580 18 Z"/>
  <path d="M600 8 V13 M600 23 V28"/>
</g>
<circle cx="600" cy="18" r="2.2" fill="#918b80"/>
</svg>""", encoding="utf-8")
AUTHOR_PHOTO_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/a-m-a-ayrookuzhiel-print-book-photo-01.png"
AUTHOR_PHOTO = OUT / "author-portrait.png"
HALF_TITLE_ORNAMENT = OUT / "half-title-ornament.svg"
COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-front-cover-v-0.4.png"
COVER = OUT / "edrl-ii-cover.png"
BACK_COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-print-book-back-cover-04.png"
BACK_COVER = OUT / "edrl-ii-back-cover.png"
FULL_WRAP_COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-cover-full-03.png"
FULL_WRAP_COVER = OUT / "edrl-ii-full-wrap-cover.png"

BODY_PAR = "#set par(justify: true, leading: 9pt, first-line-indent: 12.1pt, hanging-indent: 0pt, spacing: 10pt)"

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
    download(COVER_URL, COVER, "Cover", lambda d: d.startswith(bytes.fromhex("89504e470d0a1a0a")))

def fetch_back_cover():
    download(BACK_COVER_URL, BACK_COVER, "Back cover",
             lambda d: d.startswith(bytes.fromhex("89504e470d0a1a0a")))

def fetch_full_wrap_cover():
    download(FULL_WRAP_COVER_URL, FULL_WRAP_COVER, "Full-wrap cover",
             lambda d: d.startswith(bytes.fromhex("89504e470d0a1a0a")))

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
        continuation = prefix
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
        .replace("[", "\\[") .replace("]", "\\]")
        .replace("$", "\\$")
    )

def html_inline_to_typst(node):
    """Preserve inline emphasis when converting HTML headings to Typst."""
    if isinstance(node, NavigableString):
        return typst_escape(str(node))
    content = "".join(html_inline_to_typst(child) for child in node.children)
    if isinstance(node, Tag) and node.name in ("em", "i"):
        return f"#emph[{content}]"
    if isinstance(node, Tag) and node.name in ("strong", "b"):
        return f"*{content}*"
    return content

def typst_heading_body(title):
    """Prevent Arabic-number prefixes from being parsed as Typst list markers."""
    match = re.match(r"^(\d+\.)(\s+)(.*)$", title, re.S)
    if match:
        number, spacing, remainder = match.groups()
        # A zero-width space after the full stop breaks the list-marker
        # pattern without changing the visible heading or its spacing.
        return f"[{number}\u200b{spacing}{remainder}]"
    return f"[{title}]"

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

    # Identify Essay 6 tables for their special numeric formatting.
    essay6_tables = {
        ("Name of caste", "Families", "Families with land",
         "Land held (acres)", "Share of total land (%)"),
        ("Castes", "Borewells and pumpsets", "Bullock carts",
         "Draught animals", "Milk animals", "Sheep and goats"),
        ("Castes", "Families", "Amount (Rs.)"),
        ("Castes", "No. of families", "Amount (Rs.)"),
        ("Caste", "Fully employed: own farm / other work",
         "Agriculture + wage labour", "Landless wage labour"),
        ("Caste", "Up to SSLC", "SSLC and PUC", "Degree",
         "Non-agricultural professions and government jobs"),
    }
    header_key = tuple(value for value, _ in header)
    essay6_table = header_key in essay6_tables
    font_size = "10pt"
    horizontal_inset = "3pt"

    def cell_content(value, header_cell=False, row_label=False):
        is_numeric = bool(re.fullmatch(r"[0-9][0-9,]*(?:\\.[0-9]+)?|[—–-]", value.strip()))
        value = typst_escape(value)
        if header_cell:
            return f"table.cell(align: left, breakable: false)[*{value}*]"
        if row_label:
            return f"table.cell(align: left, breakable: false)[{value}]"
        if essay6_table:
            return f"table.cell(align: right, inset: (left: 3pt, right: 6pt, top: 3.5pt, bottom: 3.5pt), breakable: false)[{value}]"
        if is_numeric:
            return f"table.cell(inset: (left: 3pt, right: 6pt, top: 3.5pt, bottom: 3.5pt), breakable: false)[{value}]"
        return f"table.cell(breakable: false)[{value}]"

    header_cells = ",\n    ".join(
        cell_content(value, header_cell=True)
        for value, _ in header
    )
    body_cells = []
    for row in data_rows:
        for column_index, (value, is_row_label) in enumerate(row):
            if essay6_table and header_key[0] == "Name of caste" and column_index == 3:
                if re.fullmatch(r"\d+", value):
                    value = f"{value}.00"
            body_cells.append(cell_content(value, row_label=is_row_label))

    cells = ",\n    ".join(body_cells)
    fence = chr(96) * 3
    return (
        fence + "{=typst}\n"
        f"#block(breakable: false)[\n  #set text(size: {font_size}, hyphenate: false)\n  #set par(justify: false, leading: 5pt, first-line-indent: 0pt, spacing: 0pt)\n"
        "  #table(\n"
        "    columns: (" + ", ".join(["auto"] * width) + "),\n"
        "    align: (left, " + ", ".join(["center"] * (width - 1)) + "),\n"
        f"    inset: (x: {horizontal_inset}, y: 3.5pt),\n"
        "    stroke: (x, y) => (\n"
        "      bottom: if y == 0 { 0.8pt + luma(90) } else { 0.35pt + luma(175) },\n"
        "    ),\n"
        "    fill: (_, y) => if y == 0 { luma(235) },\n"
        "    table.header(\n"
        f"      {header_cells},\n"
        "    ),\n"
        f"    {cells},\n"
        "  )\n"
        "]\n"
        + fence + "\n"
    )

def extract_footnotes_and_clean(markdown, promote_wrapped_headings=False):
    """Convert HTML headings, tables and source-linked notes for Pandoc."""
    # Protect Markdown blockquotes before the second BeautifulSoup pass.
    # This pass handles embedded HTML and would otherwise treat leading ">"
    # markers as literal text, destroying the Markdown block structure.
    blockquote_tokens = {}
    def protect_blockquote(match):
        token = f"TSAP_FINAL_BLOCKQUOTE_{len(blockquote_tokens)}_PRESERVE"
        blockquote_tokens[token] = match.group(0).rstrip()
        return "\n\n" + token + "\n\n"

    markdown = re.sub(
        r"(?m)(?:^>[^\n]*(?:\n|$))+(?:\n(?=>[^\n]*(?:\n\vert{}$)))*",
        protect_blockquote,
        markdown,
    )
    soup = BeautifulSoup(markdown, "html.parser")

    # Convert HTML headings directly to raw Typst heading elements.
    # This keeps long headings intact: Pandoc must not split a heading line
    # and turn its remainder into ordinary paragraph text.
    for heading in soup.find_all(re.compile(r"^h[1-6]$")):
        # Source notes are rendered as page footnotes, not as a separate
        # end-of-essay section. Remove the heading before converting it to Typst.
        if heading.get_text(" ", strip=True).casefold() == "notes":
            heading.decompose()
            continue
        level = int(heading.name[1])
        # The four wrapper-based essays place their internal headings one
        # level below the omitted H2 "Full text" container. Apply the same
        # one-level promotion used for Markdown headings, but never promote
        # an H2 to H1. Standalone full-text sources pass False.
        if promote_wrapped_headings and level >= 3:
            level -= 1
        title = html_inline_to_typst(heading).strip()
        typst_heading = (
            "\n\n```{=typst}\n"
            f"#heading(level: {level}){typst_heading_body(title)}\n"
            "```\n\n"
        )
        heading.replace_with(NavigableString(typst_heading))

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

    # Convert footnote markers inside protected blockquotes before restoring
    # them. The main BeautifulSoup pass cannot see those markers because the
    # quotation is deliberately held as Markdown text.
    seen_note_ids = set()
    note_numbers = {}
    quote_marker_pattern = re.compile(
        r"""<sup\b[^>]*id=["']ref-[^"']+["'][^>]*>\s*"""
        r"""<a\b[^>]*href=["']#note-(\d+)["'][^>]*>.*?</a>\s*</sup>""",
        re.I | re.S,
    )
    for token, blockquote in blockquote_tokens.items():
        def convert_quote_marker(match):
            note_id = match.group(1)
            if note_id not in notes:
                raise SystemExit(
                    f"Blockquote footnote reference points to missing note-{note_id}."
                )
            if note_id not in note_numbers:
                note_numbers[note_id] = len(note_numbers) + 1
            if note_id in seen_note_ids:
                return f"^{note_numbers[note_id]}^"
            seen_note_ids.add(note_id)
            return f"[^{note_id}]"

        blockquote_tokens[token] = quote_marker_pattern.sub(
            convert_quote_marker, blockquote
        )

    for marker in soup.select('sup[id^="ref-"]'):
        target = marker.find("a", href=re.compile(r"^#note-"))
        if target:
            note_id = target.get("href", "")[len("#note-"):]
            if note_id not in notes:
                raise SystemExit(
                    f"Footnote reference {marker.get('id')} points to missing note-{note_id}."
                )
            if note_id not in note_numbers:
                note_numbers[note_id] = len(note_numbers) + 1
            if note_id in seen_note_ids:
                marker.replace_with(NavigableString(f"^{note_numbers[note_id]}^"))
            else:
                seen_note_ids.add(note_id)
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
        # Pandoc requires every continuation block in a multi-paragraph
        # footnote definition to be indented. Without this, later paragraphs
        # escape the footnote and are rendered as ordinary essay body text.
        definitions = []
        for note_id, text in ordered_notes:
            lines = text.splitlines()
            definition = f"[^{note_id}]: {lines[0]}"
            if len(lines) > 1:
                definition += "\n" + "\n".join(
                    ("    " + line) if line else "" for line in lines[1:]
                )
            definitions.append(definition)
        cleaned += "\n\n" + "\n\n".join(definitions)
    for token, blockquote in blockquote_tokens.items():
        cleaned = cleaned.replace("<p>" + token + "</p>", "\n\n" + blockquote + "\n\n")
        cleaned = cleaned.replace(token, "\n\n" + blockquote + "\n\n")
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
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
    # The source page's H2 "Full text" wrapper is omitted from the print book.
    # Promote its internal Markdown headings by one level beneath the essay H1.
    if full is not None:
        lines = [
            re.sub(r"^(#{3,6})(?=[ \t])", lambda match: match.group(1)[1:], line)
            for line in lines
        ]
    body = "\n".join(lines).strip()
    body = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", body)

    # Exclude the website introduction and Contents list from the print body.
    # The print book supplies its own essay title and contents page, so the
    # website lead and fragment links must not appear in the printed essay.
    # Resume at the first actual essay heading, whether Markdown or HTML.
    body = re.sub(
        r"(?ims)\A.*?^<h2\b[^>]*>\s*Contents\s*</h2>.*?(?=^(?:#{1,6}[ \t]+|<h[1-6]\b)|\Z)",
        "",
        body,
        count=1,
    )

    # Protect Markdown ATX headings while BeautifulSoup handles embedded HTML.
    # Parsing Markdown as HTML can otherwise alter heading boundaries and turn
    # the tail of a long heading into an ordinary paragraph.
    heading_tokens = {}
    def protect_heading(match):
        # Notes are rendered as page footnotes, so suppress the source section heading.
        if re.match(r"^#{1,6}\s+Notes(?:\s+\{#notes\})?\s*$", match.group(0), re.I):
            return ""
        token = f"TSAP_MARKDOWN_HEADING_{len(heading_tokens)}_PRESERVE"
        heading_tokens[token] = match.group(0)
        return token

    body = re.sub(r"(?m)^#{1,6}[ \t]+[^\n]+$", protect_heading, body)

    # Preserve Markdown blockquotes while BeautifulSoup processes embedded HTML.
    # BeautifulSoup treats Markdown's leading ">" as plain text, and its HTML
    # serialisation can collapse the quoted lines into surrounding paragraphs.
    # Protect complete quote blocks, then restore them before Pandoc parses Markdown.
    blockquote_tokens = {}
    def protect_blockquote(match):
        token = f"TSAP_MARKDOWN_BLOCKQUOTE_{len(blockquote_tokens)}_PRESERVE"
        blockquote_tokens[token] = match.group(0).rstrip()
        return "\n\n" + token + "\n\n"

    body = re.sub(
        r"(?m)(?:^>[^\n]*(?:\n|$))+(?:\n(?=>[^\n]*(?:\n|$)))*",
        protect_blockquote,
        body,
    )

    body_soup = BeautifulSoup(body, "html.parser")
    for item in body_soup.select('li[id^="note-"]'):
        item.decompose()
    for item in source_note_items:
        body_soup.append(item)
    body = body_soup.decode_contents()
    for token, blockquote in blockquote_tokens.items():
        body = body.replace("<p>" + token + "</p>", "\n\n" + blockquote + "\n\n")
        body = body.replace(token, "\n\n" + blockquote + "\n\n")
    body = re.sub(r"\n{3,}", "\n\n", body)

    note_ids = {
        item.get("id", "")[len("note-"):]
        for item in source_note_items
        if item.get("id", "").startswith("note-")
    }
    # Include references inside protected Markdown blockquotes in the audit.
    # They are temporarily absent from body_soup until restored for Pandoc.
    reference_soup = BeautifulSoup(
        body + "\n" + "\n".join(blockquote_tokens.values())
        + "\n" + "\n".join(heading_tokens.values()),
        "html.parser",
    )
    references = set()
    for marker in reference_soup.select('sup[id^="ref-"]'):
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
    # Render the Sony! heading and its source note as one explicit Typst
    # heading. This heading's inline HTML footnote marker must not pass
    # through the generic Markdown-heading token path.
    for token, heading in list(heading_tokens.items()):
        if re.match(r"^#{1,6}[ \t]+Sony!<sup\b", heading):
            note_match = re.search(
                r"""href=[\"']#note-([^\"']+)[\"']""", heading, re.I
            )
            if not note_match:
                raise SystemExit("Sony! heading is missing its footnote reference.")
            note_id = note_match.group(1)
            note_item = next(
                (item for item in source_note_items
                 if item.get("id") == f"note-{note_id}"),
                None,
            )
            if note_item is None:
                raise SystemExit(f"Sony! heading points to missing note-{note_id}.")
            note_text = footnote_markdown(note_item).strip()
            if not note_text:
                raise SystemExit(f"Sony! heading note-{note_id} is empty.")
            level = len(re.match(r"^(#{1,6})", heading).group(1))
            if full is not None and level >= 3:
                level -= 1
            typst_heading = (
                "\n\n```{=typst}\n"
                f"#heading(level: {level})[Sony!#footnote[{note_text}]]\n"
                "```\n\n"
            )
            body = body.replace(token, typst_heading, 1)
            del heading_tokens[token]
            break

    cleaned = extract_footnotes_and_clean(body, promote_wrapped_headings=(full is not None))

    # Essay 6: render all parallel festival labels in Sections A and B
    # through the same explicit, flush-left Typst paragraph treatment.
    # Essay 6: render the five parallel festival labels as explicit, flush-left
    # bold paragraph blocks, independent of the surrounding body indentation.
    if path.name == "religion-way-salvation-ideology-oppression-full-text.md":
        festival_labels = [
            (r"\*\*\(a\) \*Makara Sankranti\*\*\*", "(a) #emph[Makara Sankranti]"),
            (r"\*\*\(b\) \*Agate Male Ungalu\* \(\*Hasta Malai\*\)\*\*", "(b) #emph[Agate Male Ungalu] (#emph[Hasta Malai])"),
            (r"\*\*\(c\) \*Gangamma\* festival\*\*", "(c) #emph[Gangamma] festival"),
            (r"\*\*\(d\) \*Sapplamma\* festival\*\*", "(d) #emph[Sapplamma] festival"),
            (r"\*\*\(e\) An egalitarian spiritual practice during the \*Karaga\*\*\*", "(e) An egalitarian spiritual practice during the #emph[Karaga]"),
            (r"\*\*\(a\) \*Sri Ramanavami\*\*\*", "(a) #emph[Sri Ramanavami]"),
            (r"\*\*\(b\) \*Naga Panchami\*\*\*", "(b) #emph[Naga Panchami]"),
            (r"\*\*\(c\) \*Dasara\*\*\*", "(c) #emph[Dasara]"),
            (r"\*\*\(d\) \*Deepavali\*\*\*", "(d) #emph[Deepavali]"),
        ]
        for pattern, label in festival_labels:
            replacement = (
                "```{=typst}\n"
                "#block(width: 100%, above: 14pt, below: 14pt)[\n"
                "  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 12.65pt, spacing: 0pt)\n"
                f'  #text(weight: "bold")[{label}]\n'
                "]\n"
                "```"
            )
            cleaned, count = re.subn(re.compile("^" + pattern + "$", re.M), replacement, cleaned, count=1)
            if count != 1:
                raise SystemExit("Essay 6 festival label formatting check failed: " + label)


    for token, heading in heading_tokens.items():
        # Render Markdown headings through the same raw Typst heading path as
        # HTML headings. This prevents Pandoc from splitting a long heading's
        # final line into ordinary paragraph text.
        match = re.match(
            r"^(#{1,6})[ \t]+(.*?)(?:[ \t]+\{#([A-Za-z0-9:_-]+)\})?$",
            heading,
        )
        if not match:
            raise SystemExit(f"Could not parse preserved heading in {path.name}: {heading}")
        level, title, label = match.groups()

        # Markdown headings are protected before HTML footnote processing.
        # Render any source footnote marker in the heading directly as a
        # Typst footnote, using the corresponding source note text.
        heading_note_pattern = re.compile(
            r"""<sup\b[^>]*id=["']ref-[^"']+["'][^>]*>\s*"""
            r"""<a\b[^>]*href=["']#note-([^"']+)["'][^>]*>.*?</a>\s*</sup>""",
            re.I | re.S,
        )
        heading_note_tokens = {}

        def render_heading_note(note_match):
            note_id = note_match.group(1)
            note_item = next(
                (item for item in source_note_items
                 if item.get("id") == f"note-{note_id}"),
                None,
            )
            if note_item is None:
                raise SystemExit(
                    f"Heading footnote reference points to missing note-{note_id}."
                )
            note_text = footnote_markdown(note_item).strip()
            if not note_text:
                raise SystemExit(f"Heading footnote note-{note_id} is empty.")
            token = f"TSAP_HEADING_FOOTNOTE_{len(heading_note_tokens)}_PRESERVE"
            heading_note_tokens[token] = f"#footnote[{typst_escape(note_text)}]"
            return token

        title = heading_note_pattern.sub(render_heading_note, title)
        title = typst_escape(title)
        for token, footnote in heading_note_tokens.items():
            title = title.replace(token, footnote)
        title = re.sub(r"\*\*(.+?)\*\*", r"*\1*", title)
        title = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"_\1_", title)
        label_suffix = f" <{label}>" if label else ""
        typst_heading = (
            "\n\n```{=typst}\n"
            f"#heading(level: {len(level)}){typst_heading_body(title)}{label_suffix}\n"
            "```\n\n"
        )
        cleaned = cleaned.replace("<p>" + token + "</p>", typst_heading)
        cleaned = cleaned.replace(token, typst_heading)
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

    # In Essay 3, adjacent source quotations are separate Markdown
    # blockquotes, but form one continuous indented extract in the journal.
    # Join only consecutive blockquotes separated by blank lines in the
    # print-only stream. A quoted blank line preserves paragraph boundaries
    # inside one Pandoc blockquote, so outer spacing is applied only once.
    if stem == "essay-3":
        adjacent_quote_pattern = re.compile(
            r"(^>[^\n]*(?:\n>[^\n]*)*)(?:\n[ \t]*\n)(?=>)",
            re.M,
        )
        while adjacent_quote_pattern.search(markdown_without_definitions):
            markdown_without_definitions = adjacent_quote_pattern.sub(
                lambda match: match.group(1) + "\n>\n",
                markdown_without_definitions,
            )

    def convert(segment, suffix):
        segment = segment.strip()
        if definitions:
            segment += "\n\n" + "\n\n".join(definitions)
        md = OUT / f"{stem}-{suffix}.md"
        typ = OUT / f"{stem}-{suffix}.typ"
        md.write_text(segment, encoding="utf-8")
        run(["pandoc", str(md), "--from=markdown+raw_attribute", "--to=typst", "--output", str(typ)])
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

    def convert_post_poem_prose(segment, suffix):
        """Indent only the first ordinary paragraph immediately after a poem."""
        segment = segment.strip()
        if not segment:
            return ""

        blocks = re.split(r"\n[ \t]*\n", segment, maxsplit=1)
        first_block = blocks[0].strip()
        remaining = blocks[1].strip() if len(blocks) > 1 else ""

        lines = first_block.splitlines()
        first_line_raw = lines[0] if lines else ""
        first_line = first_line_raw.strip()
        is_non_paragraph = (
            not first_line
            or first_line.startswith(("#", ">", "```", "~~~", "<", "|"))
            or re.match(r"^(?:[-+*]\s|\d+[.)]\s|:{3,}|\[\^[^]]+\]:)", first_line)
            or re.match(r"^(?:---+|\*\*\*+|___+)\s*$", first_line)
            or (len(lines) > 1 and re.match(r"^\s*(?:=+|-+)\s*$", lines[1]))
            or first_line.startswith(("    ", "\t"))
        )

        if is_non_paragraph:
            return convert(segment, suffix)

        first_typst = convert(first_block, f"{suffix}-first")
        indented_first = (
            "#par(first-line-indent: (amount: 12.1pt, all: true))[\n"
            + first_typst + "\n]"
        )
        if not remaining:
            return indented_first
        return indented_first + "\n\n" + convert(remaining, f"{suffix}-rest")

    parts = []
    cursor = 0
    pattern = re.compile(r"@@POEM_START@@(.*?)@@POEM_END@@", re.S)
    for index, match in enumerate(pattern.finditer(markdown_without_definitions), start=1):
        prose = markdown_without_definitions[cursor:match.start()].strip()
        if prose:
            if cursor > 0:
                prose_typst = convert_post_poem_prose(prose, f"prose-{index}")
            else:
                prose_typst = convert(prose, f"prose-{index}")
            parts.append(prose_typst)
        stanzas = re.split(r"\n[ \t]*\n(?:[ \t]*\n)*", match.group(1).strip())
        stanza_blocks = []
        for stanza_index, stanza in enumerate(stanzas, start=1):
            if not stanza.strip():
                continue
            stanza_typst = convert(stanza.strip(), f"poem-{index}-stanza-{stanza_index}")
            stanza_blocks.append(
                "#block(width: 100%)[\n"
                "  #set par(justify: false, first-line-indent: 0pt, leading: 10pt, spacing: 0pt)\n"
                "  #align(center)[\n" + stanza_typst + "\n  ]\n]"
            )
        poem = ("\n#v(12pt)\n").join(stanza_blocks)
        parts.append(
            "#block(width: 100%, above: 16pt, below: 16pt)[\n"
            + poem + "\n]"
        )
        cursor = match.end()
    remainder = markdown_without_definitions[cursor:].strip()
    if remainder:
        if cursor > 0:
            remainder_typst = convert_post_poem_prose(remainder, "prose-final")
        else:
            remainder_typst = convert(remainder, "prose-final")
        parts.append(remainder_typst)
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
        r'<line xMin="([\d.]+)" yMin="([\d.]+)" '
        r'xMax="([\d.]+)" yMax="([\d.]+)"'
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
fetch_back_cover()
fetch_full_wrap_cover()
common = r"""
#set document(
  title: "Essays on Dalits, Religion and Liberation II",
  author: "A. M. Abraham Ayrookuzhiel",
  keywords: ("Dalits", "religion", "liberation", "A. M. Abraham Ayrookuzhiel"),
)
#set text(font: "Linux Libertine O", size: 11pt, lang: "en", hyphenate: false)
#set smartquote(enabled: false)
""" + BODY_PAR + r"""
#show quote.where(block: true): it => block(
  above: 12pt,
  below: 12pt,
  inset: (left: 22pt, right: 22pt),
)[
  #set text(size: 10.5pt, fill: black)
  #set par(justify: true, leading: 9pt, first-line-indent: 0pt, hanging-indent: 0pt, spacing: 10pt)
  #it.body
]
#set heading(numbering: none, hanging-indent: 0pt)
#show footnote: it => super(text(size: 14pt)[#it])
#set footnote.entry(
  separator: line(length: 30%, stroke: 0.5pt + luma(90)),
  clearance: 5.1pt,
  gap: 5.525pt,
)
#show footnote.entry: it => context {
  let values = counter(footnote).at(it.note.location())
  let number = numbering(it.note.numbering, ..values)
  grid(
    columns: (11.9pt, 1fr),
    gutter: 2.55pt,
    align: (right, top),
    [#text(size: 8.5pt)[#number.]],
    [
      #set text(size: 8.5pt, number-type: "lining")
      #set par(
        justify: false,
        first-line-indent: 0pt,
        hanging-indent: 0pt,
        leading: 5.5pt,
        spacing: 5.5pt,
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
    set text(size: 8pt, fill: luma(45))
    let header-title = if calc.even(current-page) {
      [ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    } else if current-chapter != none {
      if current-chapter.body == [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue] {
        [The Living Hindu Popular Religious Consciousness]
      } else {
        current-chapter.body
      }
    } else {
      [ESSAYS ON DALITS, RELIGION AND LIBERATION II]
    }
    // Use a compact stack so the title sits close to the rule while the
    // rule remains at its existing position in the top margin.
    stack(
      dir: ttb,
      spacing: 3pt,
      align(center)[#header-title],
      line(length: 100%, stroke: 0.5pt + luma(170)),
    )
  }
}
#set page(
  paper: "a5",
  binding: left,
  margin: (inside: 18mm, outside: 14mm, top: 18mm, bottom: 17mm),
  header: running-header,
  footer: context [
    #set text(size: 8.5pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
// Centre every essay chapter title (H1), including wrapped lines, across the full text width.
#show heading.where(level: 1): it => block(width: 100%, above: 0pt, below: 7pt, breakable: false)[
  #set text(font: "Linux Libertine O", size: 18pt, weight: "bold", hyphenate: false)
  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 11.7pt, spacing: 0pt)
  #align(center)[#it]
]
#show heading.where(level: 2): set heading(hanging-indent: 0pt)
#show heading.where(level: 2): it => block(above: 18pt, below: 16pt, breakable: false)[
  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 10.4pt, spacing: 0pt)
  #text(size: 16pt, weight: "bold", hyphenate: false)[#it.body]
]
#show heading.where(level: 3): it => block(above: 16pt, below: 14pt, breakable: false)[
  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 9.1pt, spacing: 0pt)
  #text(size: 14pt, weight: "bold", hyphenate: false)[#it.body]
]
#show heading.where(level: 4): it => block(above: 14pt, below: 14pt, breakable: false)[
  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 7.8pt, spacing: 0pt)
  #align(left)[
    #text(size: 12pt, weight: "bold", hyphenate: false)[#it.body]
  ]
]
#show heading.where(level: 5): it => block(above: 14pt, below: 14pt, breakable: false)[
  #set par(justify: false, first-line-indent: 0pt, hanging-indent: 0pt, leading: 8.8pt, spacing: 0pt)
  #text(size: 11pt, weight: "bold", hyphenate: false)[#it.body]
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
    #set par(justify: false, first-line-indent: 0pt, leading: 8.25pt, spacing: 0pt)
    #text(size: 10.5pt, weight: "bold")[Dr. Y. T. Vinayaraj]
    #linebreak()
    #text(size: 9pt)[Director]
    #linebreak()
    #text(size: 8.5pt)[Christian Institute for the Study of Religion and Society]
    #linebreak()
    #text(size: 8.5pt)[9 November 2026]
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
  #v(30mm)
  #move(dy: -5mm)[
    #text(size: 10pt, weight: "bold", tracking: 2pt)[ESSAYS ON]
    #v(2.5mm)
    #text(size: 25pt, weight: "bold")[Dalits, Religion]
    #linebreak()
    #text(size: 25pt, weight: "bold")[and Liberation II]
  ]
  #v(12mm)
  #image("half-title-ornament.svg", width: 22mm)
  #v(10mm)
  #text(size: 13pt, tracking: 0.7pt)[A. M. Abraham Ayrookuzhiel]
]
#pagebreak()
#set page(header: none, footer: none, numbering: none)
#v(1fr)
#align(left)[
  #move(dy: -6mm)[
  #align(left)[
  #block(width: 112mm)[
      #set par(justify: false, first-line-indent: 0pt, leading: 12.65pt, spacing: 0pt)
      #align(left)[
        #set par(justify: false, first-line-indent: 0pt, leading: 13pt, spacing: 0pt)
        #text(size: 11.5pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
        #linebreak()
        #text(size: 10pt)[A. M. Abraham Ayrookuzhiel]
      ]
      #v(16pt)

      #grid(
        columns: (32mm, 1fr),
        column-gutter: 4mm,
        row-gutter: 8.25pt,
        align: (left, left),
        [#text(size: 8pt, weight: "bold", fill: luma(85))[CONTACT]],
        [#text(size: 9.5pt)[publications\@sunilabraham.in]],
        [#text(size: 8pt, weight: "bold", fill: luma(85))[EDITOR]],
        [#text(size: 9.5pt)[Tito Dutta]],
        [#text(size: 8pt, weight: "bold", fill: luma(85))[TYPESETTING]],
        [#text(size: 9.5pt)[Tito Dutta]],
        [#text(size: 8pt, weight: "bold", fill: luma(85))[PRINT COORDINATION]],
        [#text(size: 9.5pt)[Herbert Paul]],
        [#text(size: 8pt, weight: "bold", fill: luma(85))[PRINTED BY]],
        [#text(size: 9.5pt)[National Printing Press, Bengaluru, India]],
      )

      #v(18pt)
      #align(left)[
        #text(size: 9.5pt)[First paperback edition]
        #linebreak()
        #text(size: 9.5pt)[Published on 29 November 2026 by The Sunil Abraham Project]
        #linebreak()
        #text(size: 8pt)[On the occasion of the thirtieth death anniversary of A. M. Abraham Ayrookuzhiel]
      ]

      #v(18pt)
      #align(left)[
        #block(width: 100%)[
          #set par(justify: false, first-line-indent: 0pt, leading: 6.6pt, spacing: 0pt)
          #text(size: 8pt, weight: "bold", fill: luma(85))[SOURCE ATTRIBUTION]
          #v(5.5pt)
          #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
          #text(size: 8.5pt)[The essays in this volume were originally published in various journals and other publications. Details of the original publication of each essay are provided on its opening page.]
        ]
      ]

      #v(18pt)
      #align(left)[
        #block(width: 100%)[
          #set par(justify: false, first-line-indent: 0pt, leading: 6.6pt, spacing: 0pt)
          #text(size: 8pt, weight: "bold", fill: luma(85))[PRODUCTION AND TYPESETTING]
          #v(5.5pt)
          #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
          #text(size: 8.5pt)[Typesetting and preparation of the book's print-production files were carried out using Python, Pandoc and Typst. Source files and production code are managed on GitHub, with automated builds run through GitHub Actions.]
        ]
      ]

      #v(18pt)
      #grid(
        columns: (27mm, 1fr),
        column-gutter: 4mm,
        row-gutter: 6.05pt,
        align: (left, left),
        [#text(size: 8pt, weight: "bold", fill: luma(85))[ISBN-13 (Paperback)]],
        [#text(size: 9.5pt)[978-93-345-8524-7]],
        [#text(size: 8pt, weight: "bold", fill: luma(85))[PRINTED PRICE]],
        [#text(size: 9.5pt)[₹120 (Rupees One Hundred and Twenty Only)]],
      )

      #v(18pt)
      #align(left)[
        #block(width: 100%)[
          #set par(justify: false, first-line-indent: 0pt, leading: 12pt, spacing: 0pt)
          #text(size: 8.5pt)[For e-book download options, visit: #link("https://sunilabraham.in/edrl-ii")[sunilabraham.in/edrl-ii]]
        ]
      ]
    ]
  ]
  ]
]
#v(1fr)
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
    #set par(justify: false, first-line-indent: 0pt, leading: 12.65pt, spacing: 0pt)
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
    #v(16pt)
    #align(right)[
      #set par(justify: false, first-line-indent: 0pt, leading: 12.65pt, spacing: 0pt)
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
      set text(size: 8.5pt, fill: luma(65))
      align(center)[#counter(page).display("i")]
    }
  }
)
#counter(page).update(1)
""" + '#set par(justify: true, leading: 9pt, first-line-indent: 12.1pt, hanging-indent: 0pt, spacing: 14pt)' + r"""
#set heading(outlined: true)
#align(center)[= Foreword]
#v(5pt)
#image("frontmatter-divider.svg", width: 100%)
#v(8pt)
@@FOREWORD_BODY@@
#pagebreak()
#set heading(outlined: true)
#align(center)[= Editor's Note]
#v(5pt)
#image("frontmatter-divider.svg", width: 100%)
#v(8pt)
_Essays on Dalits, Religion and Liberation II_#h(3.85pt)by A. M. Abraham Ayrookuzhiel is being published on the occasion of the thirtieth death anniversary of the author. This volume continues the work begun with the publication of _Essays on Dalits, Religion and Liberation_ in 2006, marking the tenth anniversary of his death. The first volume was published by the Asian Trading Corporation, Bangalore, for the Christian Institute for the Study of Religion and Society (CISRS), with a foreword by Dr. Godwin Shiri and an introduction by Dr. K. C. Abraham.

The present volume brings together nine essays that were not included in the earlier collected volume. These essays first appeared in different journals and publications over several decades, from the 1970s to the 1990s. Most were published in _Religion and Society_, the journal of the Christian Institute for the Study of Religion and Society. One appeared in the _Indian Journal of Theology_, while "Dalit Theology: A Movement of Counter-Culture" was published in _Towards a Dalit Theology_ in 1988. Their republication in one volume makes writings that were previously dispersed across publications and decades available together.

The essays reflect A. M. Abraham Ayrookuzhiel's sustained engagement with Dalit experience, religion, theology and liberation. Bringing them together is part of the continuing effort to preserve his intellectual contribution and make it accessible to readers, researchers and future generations.

The work of collecting and documenting his writings remains ongoing. Further essays and related materials may be identified as the archival work proceeds. Any errors or inaccuracies brought to my attention will be examined and, where necessary, addressed in a subsequent edition.

=== Acknowledgement

We would like to express our sincere gratitude to everyone who generously shared their valuable inputs and extended their kind cooperation during the production of this book. The names mentioned below represent only a few among the many people whose contributions and support we gratefully acknowledge.

We are grateful to Dr. Y. T. Vinayaraj, Director of the Christian Institute for the Study of Religion and Society (CISRS), and the staff of the Institute for their cooperation, advice and valuable contributions. We thank Dr. Vinayaraj for graciously contributing the Foreword to this volume.

We are thankful to the Principal, faculty members and Prabu P., Librarian, of the United Theological College, Bengaluru, for their cooperation and support.

We are grateful to Pranesh Prakash, a distinguished researcher and former colleague, for his valuable suggestions and practical guidance throughout the production of this book.

We also thank Rajiv Gautam for his thoughtful suggestions on the book's design and layout, several of which helped us improve the presentation of this volume.

Our heartfelt thanks go to M. Kunhikrishnan, Vice President of the Swami Anandatirtha Trust, for his enthusiasm, valuable inputs and active participation in the production of this book.

We wish to acknowledge Sangram Keshari Senapati for his initial guidance during the ISBN registration process with the Raja Rammohun Roy National Agency for ISBN (RRRNA).

And,

I personally take this opportunity to express my gratitude to the family of A. M. Abraham Ayrookuzhiel for giving me the opportunity to be a part of this initiative. I am deeply grateful for their trust, cooperation and support throughout the preparation of this book. My sincere thanks to Ponnamma Abraham, Sunil Abraham, Matthew Abraham, Jacob Abraham and their family.

#v(10pt)
#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 8.25pt, spacing: 0pt)
  #text(size: 11pt, weight: "bold")[Tito Dutta]
  #linebreak()
  #text(size: 9.5pt)[Editor]
  #linebreak()
  #text(size: 8.5pt)[13 November 2026]
]
#pagebreak()
#set heading(outlined: true)
#align(center)[= About the Author]
#v(5pt)
#image("frontmatter-divider.svg", width: 100%)
#v(6pt)
A. M. Abraham Ayrookuzhiel (18 September 1933 – 29 November 1996) was an Indian theologian, scholar and researcher whose work brought questions of religion into close conversation with the social and cultural realities of marginalised communities. Born in Chengannur, Kerala, he grew up in a region with a deep Christian heritage. His early schooling was in the villages around Puthenkavu. He later entered seminary formation in Thiruvananthapuram and pursued higher studies in philosophy and theology in Pune. He continued his academic formation in Rome and the United Kingdom, and was ordained in 1963.

Abraham Ayrookuzhiel's academic and professional journey took him across different church traditions and cultural settings. After his studies abroad, he joined the Anglican Church and served as a curate at St. Paul High Anglican Church in Wokingham, Berkshire, from 1970 to 1973. His time in the United Kingdom brought him into contact with wider ecumenical conversations and debates about the place of religion and the church in a changing society. He married Ponnamma Thekedath during this period. They returned to India in 1973.

In 1974, Abraham Ayrookuzhiel joined the Christian Institute for the Study of Religion and Society (CISRS) in Bangalore. He later became Associate Director, contributing to the institute's research, seminars and wider theological engagement. At CISRS, he turned sustained attention to the religious and cultural lives of Dalit communities and to the ways caste and social hierarchy shape religious identity. His research brought field studies into conversation with theological and social analysis, taking the experiences and cultural expressions of marginalised people seriously as sources for understanding religion.

A central concern in Abraham Ayrookuzhiel's writing was the relationship between faith and social emancipation. He questioned accounts of religion that obscured caste oppression or treated inherited social arrangements as natural. His studies explored Dalit identity, popular religious traditions, oral culture and forms of resistance expressed through stories, songs, myths and festivals. He argued that theology must engage with the lives and struggles of the oppressed, rather than remain confined to doctrine and institutional practice. His work therefore crossed the boundaries of theology, sociology and cultural study.

His publications include _The Sacred in Popular Hinduism: An Empirical Study in Chirakkal, North Malabar_ (1983) and _Swami Anand Thirth: Untouchability, Gandhian Solution on Trial_ (1987). He edited _The Dalit Desiyata: The Kerala Experience in Development and Class Struggle_ (1990), and later co-edited and co-authored works on Dalit poetry and literature. His essays addressed Dalit theology, religious identity and interfaith dialogue.

At the time of his death on 29 November 1996, Abraham Ayrookuzhiel was working on a study of Dalit and Hindu religious identity that remained incomplete. His writings brought together academic research, theological reflection and close attention to the social realities of his time. This volume makes a further part of his work available to readers.
#pagebreak()
#set heading(outlined: false)
= Contents
#show outline.entry: it => {
  set par(leading: 11pt)
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
  } else if title == [Dalit Liberation—Some Reflections on Their Ideological Predicament] {
    [8.]
  } else if title == [The Ideological Nature of the Emerging Dalit Consciousness] {
    [9.]
  } else {
    it.prefix()
  }
  let entry = link(it.element.location(), it.indented(prefix, it.inner()))
  if title == [The State of Hinduism in 2000 A.D.—Some Emerging Trends] {
    v(4pt) + entry
  } else {
    entry
  }
}

#outline(
  title: none,
  depth: 1,
  target: heading.where(level: 1),
)
#set heading(outlined: true)
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
    #set text(size: 8.5pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
""")
        parts.append("#counter(page).update(1)\n")
    parts.append("#counter(footnote).update(0)\n")
    parts.append(
        f'#align(center)[#text(font: "Linux Libertine O", size: 18pt, weight: "bold", fill: luma(50))[{essay["order"]}]]\n#v(8.25pt)\n'
    )
    parts.append(f"= {title}\n")
    parts.append(f"""#block[
  #set par(justify: false, first-line-indent: 0pt, leading: 11pt, spacing: 0pt)
  #v(7pt)
  #image("essay-divider.svg", width: 100%)
  #v(5pt)
  #align(center)[
    #text(size: 7.5pt, weight: "bold", tracking: 0.65pt, fill: luma(85))[ORIGINAL PUBLICATION: ]
    #text(size: 9.5pt, style: "italic", fill: luma(65))[{essay['publication_note']}]
  ]
  #v(5pt)
  #image("essay-divider.svg", width: 100%)
  #v(7pt)
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
    if essay["order"] == 1:
        target = re.compile(r"(?m)^\*\*6\. Will the sacred cow return\?\*\*$")
        pagebreak_and_indented_heading = (
            "```{=typst}\n"
            "#pagebreak(weak: true)\n"
            "#h(12.1pt) *6. Will the sacred cow return?*\n"
            "```\n\n"
        )
        body, count = target.subn(
            lambda match: pagebreak_and_indented_heading, body, count=1
        )
        if count != 1:
            raise SystemExit("Could not locate the exact Essay 1 subsection 6 bold paragraph.")
    converted = md_to_typst(body, f"essay-{essay['order']}")
    parts.append(converted + "\n")

if len(parts) < 2 or "@@FOREWORD_BODY@@" not in parts[1]:
    raise SystemExit("Foreword insertion point missing from print template.")
parts[1] = parts[1].replace("@@FOREWORD_BODY@@", foreword_typst)

write_heading_dividers()
interior_text = "\n".join(parts)
# Enforce straight quotation marks and apostrophes throughout the printed book.
interior_text = interior_text.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"'}))
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
cover_source.write_text(r'''#set page(width: 160mm, height: 222mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-cover.png", width: 160mm, height: 222mm, fit: "cover")
''', encoding="utf-8")
cover_pdf = OUT / "edrl-ii-front-cover-proof.pdf"
run([typst, "compile", str(cover_source), str(cover_pdf)])

back_cover_source = OUT / "edrl-ii-back-cover.typ"
back_cover_source.write_text(r'''#set page(width: 160mm, height: 222mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-back-cover.png", width: 160mm, height: 222mm, fit: "cover")
''', encoding="utf-8")
back_cover_pdf = OUT / "edrl-ii-back-cover-proof.pdf"
run([typst, "compile", str(back_cover_source), str(back_cover_pdf)])

full_wrap_cover_source = OUT / "edrl-ii-full-wrap-cover.typ"
full_wrap_cover_source.write_text(r'''#set page(width: 332mm, height: 222mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-full-wrap-cover.png", width: 332mm, height: 222mm, fit: "contain")
''', encoding="utf-8")
full_wrap_cover_pdf = OUT / "edrl-ii-full-wrap-cover-proof.pdf"
run([typst, "compile", str(full_wrap_cover_source), str(full_wrap_cover_pdf)])

# A5-sized blank page immediately after the front cover in the combined review PDF.
# The interior itself remains unchanged.
blank_page_source = OUT / "edrl-ii-blank-page.typ"
blank_page_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm)
''', encoding="utf-8")
blank_page_pdf = OUT / "edrl-ii-blank-page.pdf"
run([typst, "compile", str(blank_page_source), str(blank_page_pdf)])

# A5-sized cover pages in the combined review PDF match the interior page dimensions.
review_cover_source = OUT / "edrl-ii-review-cover.typ"
review_cover_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-cover.png", width: 148mm, height: 210mm, fit: "cover")
''', encoding="utf-8")
review_cover_pdf = OUT / "edrl-ii-review-cover.pdf"
run([typst, "compile", str(review_cover_source), str(review_cover_pdf)])

review_back_cover_source = OUT / "edrl-ii-review-back-cover.typ"
review_back_cover_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-back-cover.png", width: 148mm, height: 210mm, fit: "cover")
''', encoding="utf-8")
review_back_cover_pdf = OUT / "edrl-ii-review-back-cover.pdf"
run([typst, "compile", str(review_back_cover_source), str(review_back_cover_pdf)])

run(["pdfunite", str(review_cover_pdf), str(blank_page_pdf), str(interior), str(blank_page_pdf), str(blank_page_pdf), str(review_back_cover_pdf), str(OUT / "edrl-ii-combined-review.pdf")])
# Extract combined-review page 5 alone for focused half-title review.
run(["pdfseparate", "-f", "5", "-l", "5", str(OUT / "edrl-ii-combined-review.pdf"), str(OUT / "edrl-ii-page-%d.pdf")])
for path in (interior, cover_pdf, back_cover_pdf, full_wrap_cover_pdf, review_cover_pdf, review_back_cover_pdf, OUT / "edrl-ii-combined-review.pdf", OUT / "edrl-ii-page-5.pdf"):
    if not path.is_file() or path.stat().st_size < 10000:
        raise SystemExit(f"Expected PDF missing or unexpectedly small: {path}")
# A valid one-page blank PDF is naturally much smaller than the 10 KB threshold.
if not blank_page_pdf.is_file() or blank_page_pdf.stat().st_size < 500:
    raise SystemExit(f"Blank-page PDF missing or invalid: {blank_page_pdf}")
print(f"Interior: {interior} ({interior.stat().st_size:,} bytes)")
print(f"Front cover proof: {cover_pdf} ({cover_pdf.stat().st_size:,} bytes)")
print(f"Back cover proof: {back_cover_pdf} ({back_cover_pdf.stat().st_size:,} bytes)")
print(f"Full-wrap cover proof: {full_wrap_cover_pdf} ({full_wrap_cover_pdf.stat().st_size:,} bytes)")
print("Combined review PDF created with front cover, one blank page after the cover, unchanged interior, two blank pages before the back cover, and back cover.")
