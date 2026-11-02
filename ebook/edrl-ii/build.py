#!/usr/bin/env python3
"""Build and validate the EDRL II preview manuscript, EPUB 3 and PDF."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "ebook" / "edrl-ii"
OUT = BASE / "output"
MANIFEST = BASE / "manifest.yml"
FRONT_MATTER = BASE / "front-matter.md"
OUT.mkdir(parents=True, exist_ok=True)

def parse_manifest(path):
    items = []
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*-\s*order:\s*(\d+)", line)
        if match:
            if current:
                items.append(current)
            current = {"order": int(match.group(1))}
            continue
        if current is not None:
            match = re.match(r'^\s*(title|source|publication_date|publication_note|date_precision):\s*"((?:[^"\\]|\\.)*)"\s*$', line)
            if match:
                current[match.group(1)] = match.group(2).replace(r'\"', '"').replace(r'\\', '\\')
    if current:
        items.append(current)
    items.sort(key=lambda item: item["order"])
    if [item["order"] for item in items] != list(range(1, len(items) + 1)):
        raise SystemExit("Manifest order values must be consecutive, starting at 1.")
    return items

def remove_section(lines, heading_pattern):
    """Return (remaining lines, removed section lines) for a level 2+ heading."""
    start = next((i for i, line in enumerate(lines) if re.match(heading_pattern, line.strip(), re.I)), None)
    if start is None:
        return lines, []
    end = next((i for i in range(start + 1, len(lines)) if re.match(r"^#{1,6}\s+", lines[i].strip())), len(lines))
    return lines[:start] + lines[end:], lines[start:end]

def tidy_markdown(text):
    text = re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style\s*>", "", text, flags=re.I | re.S)
    text = re.sub(r'<div\s+class=["\']full-text["\']\s+markdown=["\']1["\']\s*>', "", text, flags=re.I)
    text = re.sub(r"</div\s*>", "", text, flags=re.I)
    # Internal TSAP page links are not useful navigation in a standalone book.
    text = re.sub(r"\[([^\]]+)\]\((?:https?://sunilabraham\.in)?/(?!#)[^)]*\)", r"\1", text)
    text = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", text)
    return text.strip()

def clean_source(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    text = re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = text.splitlines()

    # Dedicated full-text pages have a web introduction before their Contents list.
    # Summary pages use a Full text section, with publication metadata outside it.
    full_index = next((i for i, line in enumerate(lines)
                       if re.match(r"^##\s+Full\s+[Tt]ext\b", line.strip())), None)
    notes_section = []
    if full_index is not None:
        main = lines[full_index + 1:]
        publication_index = next((i for i, line in enumerate(main)
                                  if re.match(r"^##\s+Publication\b", line.strip())), len(main))
        main = main[:publication_index]
        # Notes are sometimes placed after Publication; always collect them separately.
        _, notes_section = remove_section(lines, r"^#{1,6}\s+Notes\b")
        main, embedded_notes = remove_section(main, r"^#{1,6}\s+Notes\b")
        if not notes_section:
            notes_section = embedded_notes
    else:
        # Drop the introductory web description and generated contents list.
        contents_index = next((i for i, line in enumerate(lines)
                               if re.match(r"^##\s+Contents\b", line.strip())), None)
        if contents_index is not None:
            next_heading = next((i for i in range(contents_index + 1, len(lines))
                                 if re.match(r"^#{1,6}\s+", lines[i].strip())), len(lines))
            lines = lines[next_heading:]
        main = lines
        main, _publication_section = remove_section(main, r"^#{1,6}\s+Publication\b")
        main, notes_section = remove_section(main, r"^#{1,6}\s+Notes\b")

    body = tidy_markdown("\n".join(main))
    notes = tidy_markdown("\n".join(notes_section))
    if notes:
        body += "\n\n" + notes
    return body

items = parse_manifest(MANIFEST)
if len(items) != 9:
    raise SystemExit(f"Expected exactly 9 essays in manifest; found {len(items)}.")
if not FRONT_MATTER.is_file():
    raise SystemExit(f"Missing front-matter source: {FRONT_MATTER}")

front_matter = FRONT_MATTER.read_text(encoding="utf-8").strip()
parts = [front_matter, ""]
checks = []
for item in items:
    source = ROOT / item["source"]
    if not source.is_file():
        raise SystemExit(f"Missing source file: {item['source']}")
    body = clean_source(source)
    if len(body) < 500:
        raise SystemExit(f"Extraction looks incomplete for {item['title']} ({len(body)} characters).")
    source_text = source.read_text(encoding="utf-8")
    ref_count = len(re.findall(r'<sup\s+id=["\']ref-', source_text, re.I))
    note_count = len(re.findall(r'<li\s+id=["\']note-', source_text, re.I))
    out_ref_count = len(re.findall(r'<sup\s+id=["\']ref-', body, re.I))
    out_note_count = len(re.findall(r'<li\s+id=["\']note-', body, re.I))
    if ref_count and out_ref_count < ref_count:
        raise SystemExit(f"Footnote references missing from {item['title']}: source {ref_count}, manuscript {out_ref_count}.")
    if note_count and out_note_count < note_count:
        raise SystemExit(f"Footnote notes missing from {item['title']}: source {note_count}, manuscript {out_note_count}.")
    parts.extend(["# " + item["title"], "", f"*Original publication: {item['publication_note']}*", "", body, ""])
    checks.append((item["title"], len(body), ref_count, note_count, out_ref_count, out_note_count))

manuscript = "\n".join(parts).rstrip() + "\n"
manuscript_path = OUT / "manuscript.md"
manuscript_path.write_text(manuscript, encoding="utf-8")
print(f"Manuscript created: {manuscript_path} ({len(manuscript):,} characters; {len(items)} essays).")
print("Extraction and note-integrity checks:")
for title, chars, src_refs, src_notes, out_refs, out_notes in checks:
    print(f"  OK | {title} | {chars:,} characters | note refs {out_refs}/{src_refs} | note bodies {out_notes}/{src_notes}")

pandoc = shutil.which("pandoc")
if not pandoc:
    raise SystemExit("Pandoc is required. Manuscript was written, but no EPUB/PDF was generated.")

meta = BASE / "metadata.yml"
css = BASE / "epub.css"
epub = OUT / "edrl-ii-preview.epub"
pdf = OUT / "edrl-ii-preview.pdf"
subprocess.run([
    pandoc, str(manuscript_path), "--from=markdown+raw_html+smart",
    "--to=epub3", "--output", str(epub), "--metadata-file", str(meta),
    "--css", str(css), "--toc", "--toc-depth=2", "--split-level=1",
    "--epub-chapter-level=1"
], check=True)

with zipfile.ZipFile(epub) as archive:
    bad_member = archive.testzip()
    if bad_member:
        raise SystemExit(f"EPUB ZIP integrity failure in {bad_member}")
    names = archive.namelist()
    if not names or names[0] != "mimetype":
        raise SystemExit("EPUB package check failed: mimetype must be the first archive member.")
    container = ET.fromstring(archive.read("META-INF/container.xml"))
    ns = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
    rootfile = container.find("c:rootfiles/c:rootfile", ns)
    if rootfile is None:
        raise SystemExit("EPUB package check failed: package document not found.")
    opf = ET.fromstring(archive.read(rootfile.attrib["full-path"]))
    opf_ns = {"dc": "http://purl.org/dc/elements/1.1/"}
    epub_titles = [node.text for node in opf.findall(".//dc:title", opf_ns) if node.text]
    if not epub_titles or "Essays on Dalits, Religion and Liberation II" not in epub_titles[0]:
        raise SystemExit("EPUB metadata check failed: book title is missing.")
    if len([name for name in names if name.endswith(".xhtml")]) < len(items):
        raise SystemExit("EPUB chapter check failed: fewer XHTML files than expected essays.")
print(f"EPUB created and package checks passed: {epub} ({epub.stat().st_size:,} bytes).")

engine = next((name for name in ("xelatex", "lualatex", "pdflatex") if shutil.which(name)), None)
if engine:
    subprocess.run([
        pandoc, str(manuscript_path), "--output", str(pdf),
        "--from=markdown+raw_html+smart", "--pdf-engine=" + engine,
        "--metadata-file", str(meta), "-V", "geometry:margin=25mm",
        "-V", "fontsize=11pt", "-V", "linestretch=1.3",
        "-V", "indent: true", "-V", "parskip=0pt"
    ], check=True)
    if not pdf.is_file() or pdf.stat().st_size < 10000:
        raise SystemExit("PDF output check failed: output is missing or unexpectedly small.")
    print(f"PDF created: {pdf} ({pdf.stat().st_size:,} bytes).")
else:
    print("No LaTeX PDF engine installed; PDF export skipped.", file=sys.stderr)

print("PREVIEW BUILD COMPLETE. This is a review proof, not a publication-approved edition.")
