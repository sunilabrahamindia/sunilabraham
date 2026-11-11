#!/usr/bin/env python3
"""Build the EDRL II print interior and cover review PDFs with Typst.
Independent Scholarly Redesign Edition: Classical Book Architecture & Typography.
"""
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
FONTS_DIR = OUT / "fonts"
FONTS_DIR.mkdir(parents=True, exist_ok=True)

AUTHOR_PHOTO_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/a-m-a-ayrookuzhiel-print-book-photo-01.png"
AUTHOR_PHOTO = OUT / "author-portrait.png"
COVER_URL = "https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-v0.2.jpg"
COVER = OUT / "edrl-ii-cover.jpg"

# Continuous scholarly book prose: 10.5pt on 14.5pt leading (~0.62em inter-line gap in Typst),
# 1.4em classical paragraph indent, zero inter-paragraph gap for unified text blocks.
BODY_PAR = "#set par(justify: true, leading: 0.62em, first-line-indent: 1.4em, spacing: 0.62em)"


def run(args):
    subprocess.run(args, cwd=ROOT, check=True)


def download(url, dest, label, validator):
    if dest.is_file() and dest.stat().st_size >= 10000:
        data = dest.read_bytes()
        if validator(data):
            return
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


def resolve_font_path():
    """Return a valid font path containing Linux Libertine O, downloading if apt mirror failed."""
    system_candidates = [
        Path("/usr/share/fonts/truetype/linux-libertine"),
        Path("/usr/share/fonts/opentype/linux-libertine"),
        Path("/usr/share/fonts/truetype"),
        Path("/usr/share/fonts"),
        Path.home() / ".local" / "share" / "fonts",
    ]
    for candidate in system_candidates:
        if candidate.is_dir() and (
            list(candidate.rglob("LinLibertine_R*"))
            or list(candidate.rglob("*Libertine*"))
        ):
            return str(candidate)

    # Fallback: fetch Linux Libertine O TTF files directly if apt mirror was down
    mirror_base = "https://raw.githubusercontent.com/oslugr/fim-plantilla-tfg/master/fonts/"
    font_files = [
        "LinLibertine_R.ttf",
        "LinLibertine_RI.ttf",
        "LinLibertine_RB.ttf",
        "LinLibertine_RBI.ttf",
        "LinLibertine_RZ.ttf",
        "LinLibertine_RZI.ttf",
    ]
    for fname in font_files:
        target = FONTS_DIR / fname
        if not target.is_file() or target.stat().st_size < 10000:
            try:
                req = urllib.request.Request(
                    mirror_base + fname, headers={"User-Agent": "EDRL-II-print-build"}
                )
                with urllib.request.urlopen(req, timeout=20) as resp:
                    target.write_bytes(resp.read())
            except Exception:
                pass
    if list(FONTS_DIR.glob("LinLibertine*")):
        return str(FONTS_DIR)
    return "/usr/share/fonts/truetype"


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
    """Create booktabs-style academic Typst tables with repeatable headers."""
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
        ratios = [2.15] + [0.85] * 5
        font_size = "8pt"
    elif width == 5:
        ratios = [2.25] + [0.85] * 4
        font_size = "8pt"
    elif width == 4:
        ratios = [1.85, 1.05, 1.05, 1.05]
        font_size = "8.2pt"
    elif width == 3:
        ratios = [2.0, 0.95, 1.05]
        font_size = "8.5pt"
    else:
        ratios = [2.0] + [1.0] * (width - 1)
        font_size = "8pt"

    total_rows = 1 + len(data_rows)
    last_y = total_rows - 1

    def cell_content(value, header_cell=False, row_label=False):
        value = typst_escape(value)
        if header_cell:
            return f"table.cell(align: bottom, breakable: false)[*{value}*]"
        if row_label:
            return f"table.cell(align: left + horizon, breakable: false)[*{value}*]"
        return f"table.cell(align: horizon, breakable: false)[{value}]"

    header_cells = ",\n    ".join(
        cell_content(value, header_cell=True)
        for value, _ in header
    )
    body_cells = []
    for row in data_rows:
        for col_idx, (value, is_row_label) in enumerate(row):
            body_cells.append(cell_content(value, row_label=(is_row_label or col_idx == 0)))

    cells = ",\n    ".join(body_cells)
    fence = chr(96) * 3
    return (
        fence + "{=typst}\n"
        f"#block(above: 1.35em, below: 1.35em, width: 100%)[\n"
        f"  #set text(size: {font_size}, number-type: \"lining\", number-width: \"tabular\", hyphenate: false)\n"
        "  #set par(justify: false, first-line-indent: 0pt, leading: 0.45em, spacing: 0pt)\n"
        "  #table(\n"
        f"    columns: ({', '.join(f'{ratio}fr' for ratio in ratios)}),\n"
        "    align: (left, " + ", ".join(["right"] * (width - 1)) + "),\n"
        "    inset: (x: 4pt, y: 4.5pt),\n"
        "    stroke: (x, y) => (\n"
        "      top: if y == 0 { 0.75pt + luma(30) } else { none },\n"
        f"      bottom: if y == 0 {{ 0.45pt + luma(60) }} else if y == {last_y} {{ 0.75pt + luma(30) }} else {{ 0.25pt + luma(210) }},\n"
        "    ),\n"
        "    fill: none,\n"
        "    table.header(\n"
        f"      {header_cells},\n"
        "    ),\n"
        f"    {cells},\n"
        "  )\n"
        "]\n"
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
            "#block(width: 100%, above: 1.35em, below: 1.35em, inset: (left: 1.8em, right: 1.2em))[\n"
            "  #set text(size: 9.5pt)\n"
            "  #set par(justify: false, first-line-indent: 0pt, leading: 0.58em, spacing: 0.58em)\n"
            "  " + poem + "\n]"
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
    if not shutil.which("pdftotext"):
        print("WARNING: pdftotext not found; skipping bbox overlap check.")
        return

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
            a_height = a[3] - a[1]
            for b in lines[i + 1:]:
                b_height = b[3] - b[1]
                # Ignore tiny superscript footnote marker boxes that share a parent line
                if min(a_height, b_height) < 6.0:
                    continue
                horizontal_overlap = min(a[2], b[2]) - max(a[0], b[0])
                vertical_overlap = min(a[3], b[3]) - max(a[1], b[1])

                if horizontal_overlap > 2.0 and vertical_overlap > 2.5:
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


def merge_pdfs(cover_pdf, interior_pdf, combined_pdf):
    """Merge cover and interior PDFs via pdfunite or pypdf fallback."""
    if shutil.which("pdfunite"):
        run(["pdfunite", str(cover_pdf), str(interior_pdf), str(combined_pdf)])
        return
    try:
        from pypdf import PdfWriter
        writer = PdfWriter()
        writer.append(str(cover_pdf))
        writer.append(str(interior_pdf))
        with open(combined_pdf, "wb") as out_f:
            writer.write(out_f)
    except Exception as exc:
        raise SystemExit(f"Failed to merge PDFs (neither pdfunite nor pypdf succeeded): {exc}")


manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

fetch_cover()
fetch_author_photo()
font_path = resolve_font_path()

common = r"""
#set document(
  title: "Essays on Dalits, Religion and Liberation II",
  author: "A. M. Abraham Ayrookuzhiel",
  keywords: ("Dalits", "religion", "liberation", "A. M. Abraham Ayrookuzhiel"),
)
#set text(
  font: "Linux Libertine O",
  size: 10.5pt,
  lang: "en",
  ligatures: true,
  number-type: "old-style",
  overhang: true,
)
""" + BODY_PAR + r"""
#set heading(numbering: none)

#set quote(block: true)
#show quote.where(block: true): it => block(
  above: 1.15em,
  below: 1.15em,
  inset: (left: 1.6em, right: 1.2em),
)[
  #set text(size: 9.5pt)
  #set par(justify: true, first-line-indent: 0pt, leading: 0.56em, spacing: 0.56em)
  #it.body
]

#set list(indent: 0.8em, body-indent: 0.5em, spacing: 0.55em)
#set enum(indent: 0.8em, body-indent: 0.5em, spacing: 0.55em)

#set footnote.entry(
  separator: line(length: 24%, stroke: 0.4pt + luma(110)),
  clearance: 0.85em,
  gap: 0.4em,
  indent: 0pt,
)
#show footnote.entry: it => {
  set text(size: 8.5pt, number-type: "lining")
  set par(justify: true, first-line-indent: 0pt, leading: 0.48em, spacing: 0.45em)
  it
}

#let prelim-titles = (
  [Foreword],
  [Editor's Note],
  [About the Author],
  [Contents],
)

#let running-header = context {
  let current-page = here().page()
  let all-h1 = query(heading.where(level: 1))
  let chapters = all-h1.filter(item => not prelim-titles.contains(item.body))
  let prelims = all-h1.filter(item => prelim-titles.contains(item.body))

  let first-chapter = if chapters.len() > 0 { chapters.first() } else { none }
  let intentional-blank = first-chapter != none and first-chapter.location().page() == current-page + 1
  let h1-starts-here = all-h1.any(item => item.location().page() == current-page)

  if intentional-blank or h1-starts-here {
    []
  } else {
    let before-first-chapter = first-chapter != none and first-chapter.location().page() > current-page
    let page-num-str = if before-first-chapter {
      counter(page).display("i")
    } else {
      counter(page).display("1")
    }

    set text(size: 8.5pt, fill: luma(55), number-type: "old-style")
    if before-first-chapter {
      let prev-prelims = prelims.filter(item => item.location().page() < current-page)
      let current-prelim = if prev-prelims.len() > 0 { prev-prelims.last() } else { none }
      let label = if current-prelim != none { current-prelim.body } else { [] }
      if calc.even(current-page) {
        grid(
          columns: (auto, 1fr),
          align: (left + bottom, right + bottom),
          [#page-num-str],
          [#smallcaps(text(size: 7.8pt, tracking: 0.8pt)[#label])],
        )
      } else {
        grid(
          columns: (1fr, auto),
          align: (left + bottom, right + bottom),
          [#smallcaps(text(size: 7.8pt, tracking: 0.8pt)[#label])],
          [#page-num-str],
        )
      }
    } else {
      let prev-chapters = chapters.filter(item => item.location().page() < current-page)
      let current-chapter = if prev-chapters.len() > 0 { prev-chapters.last() } else { none }
      if calc.even(current-page) {
        grid(
          columns: (auto, 1fr),
          align: (left + bottom, right + bottom),
          [#page-num-str],
          [#smallcaps(text(size: 7.6pt, tracking: 0.7pt)[Essays on Dalits, Religion and Liberation II])],
        )
      } else if current-chapter != none {
        grid(
          columns: (1fr, auto),
          align: (left + bottom, right + bottom),
          [#text(size: 8.2pt, style: "italic")[#current-chapter.body]],
          [#page-num-str],
        )
      } else {
        grid(
          columns: (1fr, auto),
          align: (left + bottom, right + bottom),
          [#smallcaps(text(size: 7.6pt, tracking: 0.7pt)[Essays on Dalits, Religion and Liberation II])],
          [#page-num-str],
        )
      }
    }
  }
}

#let running-footer = context {
  let current-page = here().page()
  let all-h1 = query(heading.where(level: 1))
  let chapters = all-h1.filter(item => not prelim-titles.contains(item.body))
  let first-chapter = if chapters.len() > 0 { chapters.first() } else { none }
  let intentional-blank = first-chapter != none and first-chapter.location().page() == current-page + 1
  let h1-starts-here = all-h1.any(item => item.location().page() == current-page)

  if intentional-blank {
    []
  } else if h1-starts-here {
    let before-first-chapter = first-chapter != none and first-chapter.location().page() > current-page
    set text(size: 8.5pt, fill: luma(65), number-type: "old-style")
    if before-first-chapter {
      align(center)[#counter(page).display("i")]
    } else {
      align(center)[#counter(page).display("1")]
    }
  } else {
    []
  }
}

#set page(
  paper: "a5",
  binding: left,
  margin: (inside: 19mm, outside: 16mm, top: 20mm, bottom: 21mm),
  header-ascent: 32%,
  footer-descent: 32%,
  header: running-header,
  footer: running-footer,
)

#show heading.where(level: 1): it => {
  let is-prelim = prelim-titles.contains(it.body)
  block(
    above: if is-prelim { 16mm } else { 0pt },
    below: if is-prelim { 10mm } else { 8pt },
    breakable: false,
    width: 100%,
  )[
    #set text(
      font: "Linux Libertine O",
      size: if is-prelim { 15pt } else { 15.5pt },
      weight: "regular",
      hyphenate: false,
    )
    #set par(justify: false, first-line-indent: 0pt, leading: 0.42em, spacing: 0pt)
    #if is-prelim [
      #align(left)[
        #text(tracking: 0.4pt)[#it.body]
        #v(6pt)
        #line(length: 22mm, stroke: 0.45pt + luma(110))
      ]
    ] else [
      #align(left)[
        #block(width: 92%)[
          #text(weight: "semibold")[#it.body]
        ]
      ]
    ]
  ]
}

#show heading.where(level: 2): it => block(above: 1.75em, below: 0.75em, breakable: false)[
  #set text(size: 11.5pt, weight: "bold", hyphenate: false)
  #set par(justify: false, first-line-indent: 0pt, leading: 0.45em, spacing: 0pt)
  #it.body
]

#show heading.where(level: 3): it => block(above: 1.35em, below: 0.55em, breakable: false)[
  #set text(size: 10.5pt, weight: "regular", style: "italic", hyphenate: false)
  #set par(justify: false, first-line-indent: 0pt, leading: 0.45em, spacing: 0pt)
  #it.body
]

#show outline.entry.where(level: 1): it => {
  let is-prelim = prelim-titles.contains(it.element.body)
  block(
    above: if is-prelim { 0.55em } else { 0.85em },
    below: 0pt,
    breakable: false,
  )[
    #set par(justify: false, first-line-indent: 0pt, leading: 0.45em)
    #grid(
      columns: (1fr, 24pt),
      column-gutter: 8pt,
      align: (left + top, right + bottom),
      [
        #if is-prelim [
          #text(size: 9.8pt, style: "italic")[#it.element.body]
        ] else [
          #text(size: 10pt)[#it.element.body]
        ]
      ],
      [
        #text(size: 9.5pt, number-type: "old-style", fill: luma(40))[#it.page()]
      ],
    )
  ]
}
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
signature_typst = r"""#v(14pt)
#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.52em, spacing: 0pt)
  #text(size: 10pt, weight: "bold")[Dr. Y. T. Vinayaraj]
  #linebreak()
  #text(size: 9pt, style: "italic")[Director,]
  #linebreak()
  #text(size: 9pt, style: "italic")[Christian Institute for the Study of]
  #linebreak()
  #text(size: 9pt, style: "italic")[Religion and Society]
]"""
if "TSAPFOREWORDSIGNATURETOKEN" not in foreword_typst:
    raise SystemExit("Foreword signature marker did not survive conversion")
foreword_typst = foreword_typst.replace("TSAPFOREWORDSIGNATURETOKEN", signature_typst)

parts = [common]
parts.append(r"""
#set heading(outlined: false)
#set page(header: none, footer: none)

// A. Half-title page (Recto, p. i unnumbered)
#v(38mm)
#align(left)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.45em)
  #text(size: 13.5pt, tracking: 0.3pt)[Essays on Dalits, Religion]
  #linebreak()
  #text(size: 13.5pt, tracking: 0.3pt)[and Liberation II]
]

#pagebreak()
// Blank Verso (p. ii)
#pagebreak()

// B. Full title page (Recto, p. iii unnumbered)
#block(height: 100%, width: 100%)[
  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt)
  #v(18mm)
  #align(center)[
    #text(size: 18.5pt, tracking: 0.25pt)[Essays on Dalits,]
    #v(4pt)
    #text(size: 18.5pt, tracking: 0.25pt)[Religion and Liberation II]
    #v(14mm)
    #line(length: 18mm, stroke: 0.4pt + luma(110))
    #v(14mm)
    #smallcaps(text(size: 11.5pt, tracking: 1.4pt)[A. M. Abraham Ayrookuzhiel])
    #v(16mm)
    #text(size: 9.5pt, style: "italic", fill: luma(60))[Edited by]
    #v(3.5pt)
    #text(size: 10.5pt, tracking: 0.4pt)[Tito Dutta]
    #v(1fr)
    #smallcaps(text(size: 8.5pt, tracking: 2.2pt, fill: luma(40))[The Sunil Abraham Project])
    #v(6mm)
  ]
]

#pagebreak()

// C. Copyright and publication-details page (Verso, p. iv unnumbered)
#set page(header: none, footer: none, numbering: none)
#block(height: 100%, width: 100%)[
  #set par(justify: false, first-line-indent: 0pt, spacing: 0pt, leading: 0.55em)
  #set text(size: 8.5pt, fill: luma(45), number-type: "lining")
  #v(1fr)
  #text(size: 9.5pt, style: "italic", fill: luma(20))[Essays on Dalits, Religion and Liberation II]
  #v(3pt)
  #text(size: 9pt, fill: luma(30))[A. M. Abraham Ayrookuzhiel]
  #v(8mm)
  #text[First paperback edition published on 29 November 2026 by The Sunil Abraham Project.]
  #v(3pt)
  #text[Website: https://sunilabraham.in]
  #v(2pt)
  #text[Email: sunilabrahamindia\@gmail.com]
  #v(2pt)
  #text[Mobile: +91 96111 00817]
  #v(6mm)
  #text(style: "italic")[Edited by Tito Dutta]
  #v(2.5pt)
  #text(style: "italic")[Design and Print Production Advisor: Herbert Paul]
  #v(6mm)
  #text[ISBN: 978-93-345-8524-7]
  #v(2.5pt)
  #text[Printed price: ₹250]
  #v(6mm)
  #text(size: 8pt, style: "italic", fill: luma(80))[Published in India]
  #v(4mm)
]

#pagebreak()

// Portrait page
#set page(header: none, footer: none, numbering: none)
#v(1fr)
#align(center)[
  #image("author-portrait.png", height: 156mm, fit: "contain")
]
#v(1fr)

#pagebreak()

// Epigraph page
#set page(header: none, footer: none, numbering: none)
#v(48mm)
#align(center)[
  #block(width: 78%)[
    #set text(size: 10pt, style: "italic")
    #set par(justify: false, first-line-indent: 0pt, leading: 0.65em, spacing: 0pt)
    #align(left)[
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
    #v(10pt)
    #align(right)[
      #set text(style: "normal", size: 8.8pt, fill: luma(50))
      #set par(justify: false, first-line-indent: 0pt, leading: 0.55em, spacing: 0pt)
      — #emph[Cittar Gnanakkovai]
      #linebreak()
      Pambatti Cittar, verse 123.
    ]
  ]
]

#pagebreak()
#set page(
  numbering: "i",
  header: running-header,
  footer: running-footer,
)
#counter(page).update(1)
""" + BODY_PAR + r"""
#set heading(outlined: true)
= Foreword
@@FOREWORD_BODY@@
#pagebreak()
#set heading(outlined: true)
= Editor's Note
_Essays on Dalits, Religion and Liberation II_ by A. M. Abraham Ayrookuzhiel is being published on the occasion of the thirtieth death anniversary of the author. This volume continues the work begun with the publication of _Essays on Dalits, Religion and Liberation_ in 2006, marking the tenth anniversary of his death. The first volume was published by the Asian Trading Corporation, Bangalore, for the Christian Institute for the Study of Religion and Society (CISRS), with a foreword by Dr. Godwin Shiri and an introduction by Dr. K. C. Abraham.

In October 2025, work began on The Sunil Abraham Project. One of the project's objectives from its inception was to document, preserve and make the writings of A. M. Abraham Ayrookuzhiel more widely accessible. The work has since grown to include the collection of his writings, biographical documentation, publication records and related archival materials, brought together through the A. M. A. Ayrookuzhiel portal.

The present volume brings together nine essays that were not included in the earlier collected volume. These essays first appeared in different journals and publications over several decades, from the 1970s to the 1990s. Most were published in _Religion and Society_, the journal of the Christian Institute for the Study of Religion and Society. One appeared in the _Indian Journal of Theology_, while "Dalit Theology: A Movement of Counter-Culture" was published in _Towards a Dalit Theology_ in 1988. Their republication in one volume makes writings that were previously dispersed across publications and decades available together.

The essays reflect A. M. Abraham Ayrookuzhiel's sustained engagement with Dalit experience, religion, theology and liberation. Bringing them together is part of the continuing effort to preserve his intellectual contribution and make it accessible to readers, researchers and future generations.

The work of collecting and documenting his writings remains ongoing. Further essays and related materials may be identified as the archival work proceeds. Any errors or inaccuracies brought to the editors' attention will be examined and, where necessary, addressed in a subsequent edition.

#v(14pt)
#align(right)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.52em, spacing: 0pt)
  #text(size: 10pt, weight: "bold")[Tito Dutta]
  #linebreak()
  #text(size: 9pt, style: "italic")[Co-founder and Administrator]
  #linebreak()
  #text(size: 9pt, style: "italic")[The Sunil Abraham Project]
  #linebreak()
  #text(size: 8.5pt, number-type: "lining")[29 November 2026]
]
#pagebreak()
#set heading(outlined: true)
= About the Author
A. M. Abraham Ayrookuzhiel (18 September 1933 – 29 November 1996) was an Indian theologian, scholar and researcher whose work brought questions of religion into close conversation with the social and cultural realities of marginalised communities. Born in Chengannur, Kerala, he grew up in a region with a deep Christian heritage. His early schooling was in the villages around Puthenkavu. He later entered seminary formation in Thiruvananthapuram and pursued higher studies in philosophy and theology in Pune. He continued his academic formation in Rome and the United Kingdom, and was ordained in 1963.

A. M. Abraham Ayrookuzhiel's academic and professional journey took him across different church traditions and cultural settings. After his studies abroad, he joined the Anglican Church and served as a curate at St. Paul High Anglican Church in Wokingham, Berkshire, from 1970 to 1973. His time in the United Kingdom brought him into contact with wider ecumenical conversations and debates about the place of religion and the church in a changing society. He married Ponnamma Thekedath during this period. They returned to India in 1973.

In 1974, Abraham Ayrookuzhiel joined the Christian Institute for the Study of Religion and Society (CISRS) in Bangalore. He later became Associate Director, contributing to the institute's research, seminars and wider theological engagement. At CISRS, he turned sustained attention to the religious and cultural lives of Dalit communities and to the ways caste and social hierarchy shape religious identity. His research brought field studies into conversation with theological and social analysis, taking the experiences and cultural expressions of marginalised people seriously as sources for understanding religion.

A central concern in Abraham Ayrookuzhiel's writing was the relationship between faith and social emancipation. He questioned accounts of religion that obscured caste oppression or treated inherited social arrangements as natural. His studies explored Dalit identity, popular religious traditions, oral culture and forms of resistance expressed through stories, songs, myths and festivals. He argued that theology must engage with the lives and struggles of the oppressed, rather than remain confined to doctrine and institutional practice. His work therefore crossed the boundaries of theology, sociology and cultural study.

His publications include _The Sacred in Popular Hinduism: An Empirical Study in Chirakkal, North Malabar_ (1983) and _Swami Anand Thirth: Untouchability, Gandhian Solution on Trial_ (1987). He edited _The Dalit Desiyata: The Kerala Experience in Development and Class Struggle_ (1990), and later co-edited and co-authored works on Dalit poetry and literature. His essays addressed Dalit theology, religious identity and interfaith dialogue.

At the time of his death on 29 November 1996, A. M. Abraham Ayrookuzhiel was working on a study of Dalit and Hindu religious identity that remained incomplete. His writings brought together academic research, theological reflection and close attention to the social realities of his time. This volume makes a further part of his work available to readers.
#pagebreak()
= Contents
#v(2mm)
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
    if essay["order"] == 1:
        parts.append('#pagebreak(to: "odd")\n')
        parts.append(r"""#set heading(outlined: true)
#set page(
  numbering: "1",
  header: running-header,
  footer: running-footer,
)
""")
        parts.append("#counter(page).update(1)\n")
    else:
        parts.append("#pagebreak()\n")
    parts.append("#counter(footnote).update(0)\n")
    parts.append("#v(16mm)\n")
    parts.append(f"= {title}\n")
    parts.append(f"""#block(above: 6pt, below: 18pt, width: 100%, breakable: false)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.48em, spacing: 0pt)
  #line(length: 18mm, stroke: 0.4pt + luma(120))
  #v(6pt)
  #smallcaps(text(size: 7.5pt, tracking: 1pt, fill: luma(85))[Original Publication])
  #v(3pt)
  #text(size: 8.8pt, style: "italic", fill: luma(60))[{essay['publication_note']}]
]
""")
    if "under-construction.html" in raw:
        parts.append(r"""#block(inset: 12pt, stroke: 0.5pt + luma(175))[
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
run([typst, "compile", "--font-path", font_path, str(interior_source), str(interior)])
check_pdf_overlaps(interior)

cover_source = OUT / "edrl-ii-front-cover.typ"
cover_source.write_text(r'''#set page(width: 148mm, height: 210mm, margin: 0mm, fill: rgb("f5ead8"))
#image("edrl-ii-cover.jpg", width: 148mm, height: 210mm, fit: "contain")
''', encoding="utf-8")
cover_pdf = OUT / "edrl-ii-front-cover-proof.pdf"
run([typst, "compile", str(cover_source), str(cover_pdf)])

combined_pdf = OUT / "edrl-ii-combined-review.pdf"
merge_pdfs(cover_pdf, interior, combined_pdf)
for path in (interior, cover_pdf, combined_pdf):
    if not path.is_file() or path.stat().st_size < 10000:
        raise SystemExit(f"Expected PDF missing or unexpectedly small: {path}")
print(f"Interior: {interior} ({interior.stat().st_size:,} bytes)")
print(f"Front cover proof: {cover_pdf} ({cover_pdf.stat().st_size:,} bytes)")
print("Combined review PDF created. Cover and interior remain separate production files.")

