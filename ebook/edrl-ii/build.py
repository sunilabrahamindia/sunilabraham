#!/usr/bin/env python3
"""Build the essay-only manuscript and, when installed, EPUB/PDF outputs."""
from pathlib import Path
import re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "ebook" / "edrl-ii"
OUT = BASE / "output"
OUT.mkdir(parents=True, exist_ok=True)

def parse_manifest(path):
    items=[]
    current=None
    for line in path.read_text(encoding="utf-8").splitlines():
        m=re.match(r"\s*-\s*order:\s*(\d+)", line)
        if m:
            if current: items.append(current)
            current={"order":int(m.group(1))}
            continue
        if current is not None:
            m=re.match(r'\s*(title|source|publication_date|publication_note):\s*"(.*)"\s*$', line)
            if m: current[m.group(1)]=m.group(2)
    if current: items.append(current)
    return sorted(items, key=lambda x:x["order"])

def clean_source(path):
    text=path.read_text(encoding="utf-8")
    text=re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    text=re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text=re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines=text.splitlines()
    # On summary pages, take the actual article body, not the overview or website TOC.
    full_idx=next((i for i,l in enumerate(lines) if re.match(r"^##\s+Full\s+[Tt]ext\b",l.strip())), None)
    if full_idx is not None:
        end_idx=next((i for i in range(full_idx+1,len(lines)) if re.match(r"^##\s+Publication\b",lines[i].strip())),len(lines))
        body=lines[full_idx+1:end_idx]
        # Preserve endnotes/notes that occur after the publication note.
        notes_idx=next((i for i,l in enumerate(lines) if i>end_idx and re.match(r"^##\s+Notes\b",l.strip())),None)
        if notes_idx is not None:
            body += [""] + lines[notes_idx:]
    else:
        # On dedicated full-text pages, remove only the website-generated TOC.
        body=[]
        skipping_toc=False
        for l in lines:
            if re.match(r"^##\s+Contents\b",l.strip()):
                skipping_toc=True
                continue
            if skipping_toc and re.match(r"^#{1,6}\s+",l.strip()):
                skipping_toc=False
            if not skipping_toc:
                body.append(l)
    text="\n".join(body)
    text=re.sub(r"^\s*\{%.*?%\}\s*$", "", text, flags=re.M)
    text=re.sub(r"^\s*\[\s*Back to contents\s*\].*$", "", text, flags=re.M|re.I)
    text=re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

items=parse_manifest(BASE/"manifest.yml")
if len(items)!=9:
    raise SystemExit(f"Expected 9 essays in manifest; found {len(items)}")
parts=["# Essays on Dalits, Religion and Liberation II",
       "",
       "A. M. Abraham Ayrookuzhiel",
       "",
       "The Sunil Abraham Project",
       ""]
for item in items:
    src=ROOT/item["source"]
    if not src.exists():
        raise SystemExit(f"Missing source file: {item['source']}")
    body=clean_source(src)
    if len(body)<500:
        raise SystemExit(f"Extraction looks incomplete for {item['title']} ({len(body)} characters)")
    parts += ["# "+item["title"], "", f"*Originally published: {item['publication_note']}*", "", body, ""]
manuscript="\n".join(parts).rstrip()+"\n"
manuscript_path=OUT/"manuscript.md"
manuscript_path.write_text(manuscript, encoding="utf-8")
print(f"Manuscript created: {manuscript_path} ({len(manuscript)} characters; {len(items)} essays)")
print("Essay body character counts:")
for item in items:
    body=clean_source(ROOT/item["source"])
    print(f"  {len(body):>6}  {item['title']}")
pandoc=shutil.which("pandoc")
if not pandoc:
    print("Pandoc not installed; EPUB/PDF export skipped. Manuscript is available.", file=sys.stderr)
    sys.exit(0)
meta=BASE/"metadata.yml"
css=BASE/"epub.css"
epub=OUT/"edrl-ii.epub"
subprocess.run([pandoc,str(manuscript_path),"-o",str(epub),"--from=markdown+smart","--to=epub3","--metadata-file",str(meta),"--css",str(css),"--toc","--split-level=1"],check=True)
print(f"EPUB created: {epub}")
pdf=OUT/"edrl-ii.pdf"
engine=next((x for x in ("xelatex","lualatex","pdflatex") if shutil.which(x)),None)
if engine:
    subprocess.run([pandoc,str(manuscript_path),"-o",str(pdf),"--from=markdown+smart","--pdf-engine="+engine,"--metadata-file",str(meta),"-V","geometry:margin=25mm","-V","fontsize=11pt","-V","linestretch=1.35","-V","indent: true","-V","parskip=0pt"],check=True)
    print(f"PDF created: {pdf}")
else:
    print("No LaTeX PDF engine installed; PDF export skipped.",file=sys.stderr)
