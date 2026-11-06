#!/usr/bin/env python3
"""Build a provisional A5 Typst interior proof for EDRL II."""
from pathlib import Path
import re
import shutil
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "ebook" / "edrl-ii"
PRINT = BASE / "print"
OUT = PRINT / "output"
OUT.mkdir(parents=True, exist_ok=True)


def run(args):
    subprocess.run(args, cwd=ROOT, check=True)


def clean_source(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    text = re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = text.splitlines()
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
                if re.match(r"^\{%\s*include\s+navbox-amaa", line.strip())
                or re.match(r"^<style\b", line.strip())
                or re.match(r"^##\s+Publication\b", line.strip())), len(lines))
    lines = lines[:end]
    # Typst's Pandoc writer emits an unsupported #blockquote helper for
    # Markdown blockquotes. Preserve the quoted wording as ordinary paragraphs.
    lines = [re.sub(r"^\s*>\s?", "", line) for line in lines]
    text = "\n".join(lines)
    text = re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def md_to_typst(markdown, stem):
    md = OUT / f"{stem}.md"
    html = OUT / f"{stem}.html"
    typ = OUT / f"{stem}.typ"
    md.write_text(markdown, encoding="utf-8")
    run(["pandoc", str(md), "--from=markdown+raw_html+smart", "--to=html5", "--output", str(html)])
    run(["pandoc", str(html), "--from=html", "--to=typst", "--output", str(typ)])
    return typ.read_text(encoding="utf-8")


manifest = yaml.safe_load((BASE / "manifest.yml").read_text(encoding="utf-8"))
essays = sorted(manifest["essays"], key=lambda item: item["order"])
if len(essays) != 9:
    raise SystemExit(f"Expected 9 manifest entries, found {len(essays)}")

parts = []
parts.append(r"""
#set page(
  paper: "a5",
  margin: (left: 10mm, right: 10mm, top: 17mm, bottom: 10mm),
  footer: context [
    #set text(size: 8pt, fill: luma(90))
    #counter(page).display("1")
  ],
)
#set text(font: "Linux Libertine O", size: 11pt, lang: "en")
#set par(justify: true, leading: 0.68em, first-line-indent: 1em)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 0pt, below: 18pt)[
  #set text(font: "Linux Libertine O", size: 19pt, weight: "bold")
  #align(center)[#it]
]
#show heading.where(level: 2): it => block(above: 15pt, below: 7pt)[
  #set text(size: 14pt, weight: "bold")
  #it
]
#show heading.where(level: 3): it => block(above: 11pt, below: 5pt)[
  #set text(size: 12pt, weight: "bold")
  #it
]
#set block(spacing: 0.55em)
""")

parts.append(r"""
#v(28mm)
#align(center)[
  #text(size: 10pt, tracking: 1.5pt, weight: "bold")[THE SUNIL ABRAHAM PROJECT]
  #v(18mm)
  #text(size: 23pt, weight: "bold")[Essays on Dalits, Religion and Liberation II]
  #v(12mm)
  #text(size: 14pt)[A. M. Abraham Ayrookuzhiel]
  #v(20mm)
  #text(size: 11pt)[Edited by Tito Dutta]
  #v(3mm)
  #text(size: 11pt)[The Sunil Abraham Project]
  #v(30mm)
  #text(size: 9pt)[Editorial print proof · 6 November 2026]
]
#pagebreak()
#align(center)[#text(size: 16pt, weight: "bold")[Publication information]]
#v(12pt)
*Author:* A. M. Abraham Ayrookuzhiel

*Editor:* Tito Dutta

*Publisher:* The Sunil Abraham Project

*Website:* https://sunilabraham.in

*Language:* English

*Publication date:* 29 November 2026

*Paperback ISBN:* 978-93-345-8524-7

*E-book ISBN:* 978-93-345-1180-2

#v(8pt)
This is a provisional editorial print proof. It is not approved for printing or distribution. Final rights, copyright wording and publication credits remain subject to approval.
#pagebreak()
= Foreword
#text(fill: luma(90), style: "italic")[Placeholder: Foreword text to be added after it is received and approved.]
#pagebreak()
= Editor's Note
#text(fill: luma(90), style: "italic")[Placeholder: Editor's Note text to be prepared and approved.]
#pagebreak()
= Contents
#outline(title: none, depth: 1)
#pagebreak()
""")

for essay in essays:
    title = essay["title"]
    source = ROOT / essay["source"]
    if not source.is_file():
        raise SystemExit(f"Missing essay source: {essay['source']}")
    raw = source.read_text(encoding="utf-8")
    if "under-construction.html" in raw or re.search(r"full text.*being transcribed|transcription.*being prepared", raw, re.I):
        parts.append(f"""#pagebreak()
= {title}
#text(size: 9pt, style: "italic")[Original publication: {essay['publication_note']}]
#v(12pt)
#block(inset: 12pt, stroke: 0.6pt + luma(180), radius: 2pt)[
  #text(weight: "bold")[Transcription pending]
  The source page is currently under construction. The complete essay text has not yet been supplied to this print workflow. This placeholder is retained to preserve the planned book sequence; it is not a substitute for the essay.
]
""")
        continue
    body = clean_source(source)
    if len(body) < 500:
        raise SystemExit(f"Extraction looks incomplete for {title}: only {len(body)} characters.")
    converted = md_to_typst(body, f"essay-{essay['order']}")
    parts.append(f"""#pagebreak()
= {title}
#text(size: 9pt, style: "italic")[Original publication: {essay['publication_note']}]
#v(8pt)
{converted}
""")

typst_source = OUT / "edrl-ii-print-preview.typ"
typst_source.write_text("\n".join(parts), encoding="utf-8")
typst = shutil.which("typst")
if not typst:
    raise SystemExit("Typst CLI is not installed.")
pdf = OUT / "edrl-ii-print-preview.pdf"
run([typst, "compile", str(typst_source), str(pdf)])
if not pdf.is_file() or pdf.stat().st_size < 15000:
    raise SystemExit("PDF output missing or unexpectedly small.")
print(f"Created {pdf} ({pdf.stat().st_size:,} bytes).")
print("This is a layout proof only. It has not passed full visual proofing or printer validation.")
