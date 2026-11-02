#!/usr/bin/env python3
"""Build the essay-only EDRL II manuscript and, where tools exist, EPUB/PDF.

Uses only Python's standard library. Source pages remain untouched.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "ebook" / "edrl-ii"
OUTPUT = BOOK / "output"
MANIFEST = BOOK / "manifest.yml"

# Kept in Python as well as manifest.yml so the first build does not require
# PyYAML. Change the order only after checking original publication evidence.
ESSAYS = [
    ("Indian Religious Heritage and Social Transformation: Change of Perspective within the CISRS",
     "amaa/indian-religious-heritage-social-transformation-full-text.md"),
    ("Christian Dalits in Revolt",
     "amaa/christian-dalits-in-revolt-full-text.md"),
    ("Religious Legitimation and Delegitimations of Social Relations of Power (of Caste): The Case of the Dalits in Historical Perspective",
     "amaa/religious-legitimation-delegitimations-social-relations-power-full-text.md"),
    ("The Dalits, Religions and Inter-faith Dialogue",
     "amaa/dalits-religions-inter-faith-dialogue-full-text.md"),
    ("The Role of Religion in Dalit Liberation: Some Reflections",
     "amaa/role-of-religion-dalit-liberation-full-text.md"),
    ("A Proposal for the Study of the Religious Heritage of the Dalits: Some Methodological Considerations",
     "amaa/proposal-study-religious-heritage-dalits-full-text.md"),
    ("Chinna Pulayan: The Dalit Teacher of Sankaracharya",
     "amaa/chinnapulayan-full-text.md"),
    ("The Religious Factor in Dalit Liberation: Some Reflections",
     "amaa/religious-factor-dalit-liberation-full-text.md"),
    ("The Dalit Church's Mission — A Dalit Response",
     "amaa/dalit-church-mission-dalit-response-full-text.md"),
]

FRONT_MATTER = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
LIQUID_LINE = re.compile(r"^\s*\{%.*?%\}\s*$", re.M)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
WEBSITE_UI = re.compile(
    r"^\s*(?:\{%\s*(?:include|if|unless|endif|else|for|endfor).*?%\}|"
    r"\{:\s*[^}]+\}|\{%.*?%\})\s*$", re.M
)

def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True)

def remove_intro_and_contents(text: str, source: str) -> str:
    """Remove page-specific intro and generated contents list, preserving essay text."""
    lines = text.splitlines()
    contents_index = next((i for i, line in enumerate(lines)
                           if re.match(r"^#{1,6}\s+contents\s*$", line.strip(), re.I)), None)
    if contents_index is None:
        # If no website contents list exists, do not guess which prose is original.
        # Report this for manual review and retain the body from its first heading.
        first_heading = next((i for i, line in enumerate(lines)
                              if re.match(r"^#{1,6}\s+", line)), None)
        if first_heading is None:
            raise ValueError(f"No contents heading or article heading found in {source}")
        return "\n".join(lines[first_heading:]).strip()

    # Start at the first substantive heading after the website contents list.
    # The TOC list is Markdown list content, while the essay body starts at a heading.
    next_heading = next((i for i in range(contents_index + 1, len(lines))
                         if re.match(r"^#{1,6}\s+", lines[i].strip())
                         and not re.match(r"^#{1,6}\s+contents\s*$", lines[i].strip(), re.I)), None)
    if next_heading is None:
        raise ValueError(f"Could not find the essay body after Contents in {source}")
    return "\n".join(lines[next_heading:]).strip()

def clean_source(raw: str, source: str) -> str:
    text = FRONT_MATTER.sub("", raw, count=1)
    text = HTML_COMMENT.sub("", text)
    text = remove_intro_and_contents(text, source)

    # Remove website-only include/control lines and navigation artefacts.
    text = LIQUID_LINE.sub("", text)
    text = WEBSITE_UI.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    # Source pages often link back to their own TSAP wrapper page in the intro;
    # that intro is already removed. Keep external citations and meaningful links.
    # Keep HTML footnote anchors, semantic emphasis and image markup.
    return text

def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pieces = [
        "# Essays on Dalits, Religion and Liberation II",
        "",
        "<!-- Essay-only production manuscript. Front matter intentionally deferred. -->",
        "",
    ]
    for number, (title, relpath) in enumerate(ESSAYS, start=1):
        source_path = ROOT / relpath
        if not source_path.is_file():
            print(f"ERROR: Missing source file: {relpath}", file=sys.stderr)
            return 2
        raw = source_path.read_text(encoding="utf-8")
        body = clean_source(raw, relpath)
        if not body.strip():
            print(f"ERROR: Extraction produced empty content: {relpath}", file=sys.stderr)
            return 2
        # Explicit top-level heading makes each essay a chapter in the EPUB TOC.
        # The original title and original heading hierarchy inside the text are preserved.
        pieces.extend([
            f"\\newpage",
            "",
            f"# {number}. {title} {{#essay-{number}}}",
            "",
            body,
            "",
        ])

    manuscript = "\n".join(pieces).rstrip() + "\n"
    manuscript_path = BOOK / "manuscript.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")

    # Basic safeguards against omissions and accidental duplication.
    if manuscript.count("<!-- Essay-only production manuscript") != 1:
        print("ERROR: Manuscript marker check failed.", file=sys.stderr)
        return 3
    if len(ESSAYS) != 9:
        print(f"ERROR: Expected 9 essays, found {len(ESSAYS)}.", file=sys.stderr)
        return 3
    for number, (title, _) in enumerate(ESSAYS, start=1):
        marker = f"# {number}. {title}"
        if manuscript.count(marker) != 1:
            print(f"ERROR: Missing or duplicated essay heading: {title}", file=sys.stderr)
            return 3

    print(f"Created manuscript: {manuscript_path.relative_to(ROOT)}")
    print(f"Source essays included: {len(ESSAYS)}")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("Pandoc not found. Manuscript is ready; install Pandoc to build EPUB/PDF.")
        return 0

    epub = OUTPUT / "essays-on-dalits-religion-and-liberation-ii.epub"
    epub_cmd = [
        pandoc, str(manuscript_path), "--from=markdown+raw_html",
        "--to=epub3", "--standalone", "--toc", "--toc-depth=3",
        "--css", str(BOOK / "epub.css"),
        "--metadata-file", str(BOOK / "metadata.yml"),
        "--resource-path", str(ROOT),
        "--output", str(epub),
    ]
    result = run(epub_cmd)
    if result.returncode:
        print("EPUB build failed:\n" + result.stderr, file=sys.stderr)
        return result.returncode
    print(f"Created EPUB: {epub.relative_to(ROOT)}")

    typst = shutil.which("typst")
    if not typst:
        print("Typst not found. EPUB created; PDF build skipped. Install Typst to build PDF.")
        return 0

    pdf = OUTPUT / "essays-on-dalits-religion-and-liberation-ii.pdf"
    pdf_cmd = [
        pandoc, str(manuscript_path), "--from=markdown+raw_html",
        "--to=typst", "--standalone", "--toc", "--toc-depth=3",
        "--metadata-file", str(BOOK / "metadata.yml"),
        "--resource-path", str(ROOT),
        "--pdf-engine=typst", "--output", str(pdf),
    ]
    result = run(pdf_cmd)
    if result.returncode:
        print("PDF build failed:\n" + result.stderr, file=sys.stderr)
        return result.returncode
    print(f"Created PDF: {pdf.relative_to(ROOT)}")
    print("Build complete. These files still require editorial and visual proofing.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
