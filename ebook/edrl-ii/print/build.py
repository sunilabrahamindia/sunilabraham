#!/usr/bin/env python3
"""Build the EDRL II print interior and cover review PDFs with Typst."""
from pathlib import Path
import re
import shutil
import subprocess
import urllib.request
import yaml
from bs4 import BeautifulSoup, NavigableString

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
        return "\\n"
    return content

def extract_footnotes_and_clean(markdown):
    """Convert website HTML footnote anchors to native Pandoc Markdown footnotes."""
    soup = BeautifulSoup(markdown, "html.parser")
    notes = []
    for item in soup.select('li[id^="note-"]'):
        match = re.search(r"note-(\d+)", item.get("id", ""))
        if not match:
            continue
        number = match.group(1)
        for backlink in item.select('a[href^="#ref-"]'):
            backlink.decompose()
        note_text = inline_markdown(item).strip()
        if note_text:
            notes.append((int(number), note_text))
        item.decompose()
    for listing in soup.find_all("ol"):
        if not listing.get_text(" ", strip=True):
            listing.decompose()

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
        cleaned += "\n\n" + "\n".join(f"[^{n}]: {text}" for n, text in sorted(notes))
    return cleaned

def clean_source(path):
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.S)
    raw = re.sub(r"(?m)^\s*\{%.*?%\}\s*$", "", raw)
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
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
    references = set(re.findall(r"""<sup\s+id=["']ref-(\d+)["']""", raw, re.I))
    note_ids = set(re.findall(r"""<li\s+id=["']note-(\d+)["']""", raw, re.I))
    missing = sorted(references - note_ids, key=int)
    if missing:
        raise SystemExit(f"Footnote targets missing in {path.name}: {', '.join(missing)}")
    return extract_footnotes_and_clean(body)

def md_to_typst(markdown, stem):
    md = OUT / f"{stem}.md"
    typ = OUT / f"{stem}.typ"
    md.write_text(markdown, encoding="utf-8")
    run(["pandoc", str(md), "--from=markdown+smart", "--to=typst", "--output", str(typ)])
    content = typ.read_text(encoding="utf-8")
    if re.search(r"</?[A-Za-z][^>]*>", content):
        raise SystemExit(f"Raw HTML survived conversion in {stem}; refusing to publish a malformed proof.")
    return content

manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

fetch_cover()
common = r"""
#set text(font: "Linux Libertine O", size: 10.5pt, lang: "en")
#set par(justify: true, leading: 0.72em, first-line-indent: 1.1em, spacing: 0.45em)
#set heading(numbering: none)
#set block(spacing: 0.55em)
#set page(
  paper: "a5",
  binding: left,
  margin: (inside: 18mm, outside: 14mm, top: 18mm, bottom: 17mm),
  header: context [
    #set text(size: 7.5pt, fill: luma(85))
    #align(center)[THE SUNIL ABRAHAM PROJECT · ESSAYS ON DALITS, RELIGION AND LIBERATION II]
  ],
  footer: context [
    #set text(size: 8pt, fill: luma(65))
    #align(center)[#counter(page).display("1")]
  ],
)
#show heading.where(level: 1): it => block(above: 0pt, below: 15pt, breakable: false)[
  #set text(font: "Libertinus Serif", size: 18pt, weight: "bold")
  #align(center)[#it]
]
#show heading.where(level: 2): it => block(above: 13pt, below: 5pt, breakable: false)[
  #set text(size: 13pt, weight: "bold")
  #it
]
#show heading.where(level: 3): it => block(above: 9pt, below: 4pt, breakable: false)[
  #set text(size: 11.5pt, weight: "bold")
  #it
]
"""
parts = [common]
parts.append(r"""
#set heading(outlined: false)
#align(center)[
  #v(45mm)
  #text(size: 22pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
]
#pagebreak()
#pagebreak()
#align(center)[
  #v(30mm)
  #text(size: 9pt, weight: "bold", tracking: 1.4pt)[THE SUNIL ABRAHAM PROJECT]
  #v(22mm)
  #text(size: 22pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
  #v(12mm)
  #text(size: 14pt)[A. M. Abraham Ayrookuzhiel]
  #v(18mm)
  #text(size: 10.5pt)[Edited by Tito Dutta]
  #v(3mm)
  #text(size: 10.5pt)[The Sunil Abraham Project]
]
#pagebreak()
= Publication information
*Author:* A. M. Abraham Ayrookuzhiel \
*Editor:* Tito Dutta \
*Publisher:* The Sunil Abraham Project \
*Website:* https://sunilabraham.in \
*Language:* English \
*Publication date:* 29 November 2026 \
*Paperback ISBN:* 978-93-345-8524-7 \
*E-book ISBN:* 978-93-345-1180-2

This is a provisional editorial print proof. It is not approved for printing or distribution. Final rights, copyright wording and publication credits remain subject to approval.
#pagebreak()
= Foreword
#text(style: "italic", fill: luma(90))[Placeholder: Foreword text to be added after it is received and approved.]
#pagebreak()
= Editor's Note
#text(style: "italic", fill: luma(90))[Placeholder: Editor's Note text to be prepared and approved.]
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
    parts.append(f"= {title}\n")
    parts.append(f"#text(size: 8.5pt, style: \"italic\", fill: luma(80))[Original publication: {essay['publication_note']}]\n#v(7pt)\n")
    if "under-construction.html" in raw or re.search(r"full text.*being transcribed|transcription.*being prepared", raw, re.I):
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
