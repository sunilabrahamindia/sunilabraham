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

FRONT_MATTER = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
LIQUID_LINE = re.compile(r"^\s*\{%.*?%\}\s*$", re.M)
WEBSITE_UI = re.compile(
    r"^\s*(?:\{%\s*(?:include|if|unless|endif|else|for|endfor).*?%\}|"
    r"\{:\s*[^}]+\}|\{%.*?%\})\s*$", re.M
)

def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True)

def load_manifest() -> list[tuple[str, str]]:
    """Read the simple, deliberately flat essay entries without a YAML dependency."""
    text = MANIFEST.read_text(encoding="utf-8")
    entries = re.split(r"(?m)^  - order:\s*\d+\s*$", text)[1:]
    essays: list[tuple[str, str]] = []
    for entry in entries:
        title_match = re.search(r'(?m)^    title:\s*"([^"]+)"\s*$', entry)
        source_match = re.search(r'(?m)^    source:\s*"([^"]+)"\s*$', entry)
        if not title_match or not source_match:
            raise ValueError("Manifest entry is missing a quoted title or source path.")
        essays.append((title_match.group(1), source_match.group(1)))
    if len(essays) != 9:
        raise ValueError(f"Expected exactly 8 manifest entries; found {len(essays)}.")
    return essays

def remove_intro_and_contents(text: str, source: str) -> str:
    """Remove page-specific introduction and website TOC, keeping the essay body."""
    lines = text.splitlines()
    contents_index = next(
        (i for i, line in enumerate(lines)
         if re.match(r"^#{1,6}\s+contents\s*$", line.strip(), re.I)),
        None,
    )
    if contents_index is None:
        raise ValueError(f"No 'Contents' heading found in {source}; manual review is required.")

    # The source page's introductory description and generated contents list precede
    # the first substantive essay heading. Do not treat list items as essay content.
    next_heading = next(
        (i for i in range(contents_index + 1, len(lines))
         if re.match(r"^#{1,6}\s+", lines[i].strip())
         and not re.match(r"^#{1,6}\s+contents\s*$", lines[i].strip(), re.I)),
        None,
    )
    if next_heading is None:
        raise ValueError(f"Could not find essay body after Contents in {source}.")
    return "\n".join(lines[next_heading:]).strip()

def clean_source(raw: str, source: str) -> str:
    text = FRONT_MATTER.sub("", raw, count=1)
    text = HTML_COMMENT.sub("", text)
    text = remove_intro_and_contents(text, source)
    # Remove Jekyll/Liquid includes and conditional controls, not ordinary HTML
    # that may be part of the article's footnotes, tables or illustrations.
    text = LIQUID_LINE.sub("", text)
    text = WEBSITE_UI.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    # Normalise the essay's first substantive section to H2 if the source used
    # H3 because of its website template. Keep H2 end-matter headings (e.g. Notes).
    first_heading = re.search(r"(?m)^(#{1,6})\s+", text)
    if first_heading:
        first_level = len(first_heading.group(1))
        if first_level > 2:
            shift = first_level - 2
            def adjust_heading(match: re.Match[str]) -> str:
                hashes = match.group(1)
                if len(hashes) >= first_level:
                    return "#" * max(2, len(hashes) - shift) + match.group(2)
                return match.group(0)
            text = re.sub(r"(?m)^(#{1,6})(\s+)", adjust_heading, text)
    return text

def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    try:
        essays = load_manifest()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    pieces = [
        "<!-- Essay-only production manuscript. Front matter intentionally deferred. -->",
        "",
    ]
    for number, (title, relpath) in enumerate(essays, start=1):
        source_path = ROOT / relpath
        if not source_path.is_file():
            print(f"ERROR: Missing source file: {relpath}", file=sys.stderr)
            return 2
        try:
            body = clean_source(source_path.read_text(encoding="utf-8"), relpath)
        except (OSError, ValueError) as exc:
            print(f"ERROR processing {relpath}: {exc}", file=sys.stderr)
            return 2
        if not body.strip():
            print(f"ERROR: Extraction produced empty content: {relpath}", file=sys.stderr)
            return 2

        # A Typst-only raw block creates a PDF page break. Pandoc ignores this
        # block when creating EPUB, which remains reflowable.
        pieces.extend([
            "~~~{=typst}",
            "#pagebreak()",
            "~~~",
            "",
            f"# {number}. {title} {{#essay-{number}}}",
            "",
            body,
            "",
        ])

    manuscript = "\n".join(pieces).rstrip() + "\n"
    manuscript_path = BOOK / "manuscript.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")

    if manuscript.count("<!-- Essay-only production manuscript") != 1:
        print("ERROR: Manuscript marker check failed.", file=sys.stderr)
        return 3
    for number, (title, _) in enumerate(essays, start=1):
        if manuscript.count(f"# {number}. {title}") != 1:
            print(f"ERROR: Missing or duplicated essay heading: {title}", file=sys.stderr)
            return 3

    print(f"Created manuscript: {manuscript_path.relative_to(ROOT)}")
    print(f"Source essays included: {len(essays)}")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("Pandoc not found. Manuscript is ready; install Pandoc to build EPUB/PDF.")
        return 0

    epub = OUTPUT / "essays-on-dalits-religion-and-liberation-ii.epub"
    epub_cmd = [
        pandoc, str(manuscript_path), "--from=markdown+raw_html+fenced_divs",
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
        pandoc, str(manuscript_path), "--from=markdown+raw_html+fenced_divs",
        "--to=pdf", "--standalone", "--toc", "--toc-depth=3",
        "--metadata-file", str(BOOK / "metadata.yml"),
        "--resource-path", str(ROOT),
        "--pdf-engine=typst", "--output", str(pdf),
    ]
    result = run(pdf_cmd)
    if result.returncode:
        print("PDF build failed:\n" + result.stderr, file=sys.stderr)
        return result.returncode
    print(f"Created PDF: {pdf.relative_to(ROOT)}")
    print("Build complete. Review the files visually before publication.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
