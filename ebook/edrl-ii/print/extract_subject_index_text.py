#!/usr/bin/env python3
"""Extract page-separated text from the EDRL II print interior for subject indexing."""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
PDF = ROOT / "ebook" / "edrl-ii" / "print" / "output" / "edrl-ii-interior.pdf"
OUTPUT = ROOT / "ebook" / "edrl-ii" / "print" / "output" / "edrl-ii-page-text.txt"

if not PDF.is_file():
    raise SystemExit(f"Print interior PDF not found: {PDF}")

document = pymupdf.open(PDF)
if document.page_count == 0:
    raise SystemExit("Print interior PDF contains no pages.")

sections = []
empty_pages = []
for page_number, page in enumerate(document, start=1):
    text = page.get_text("text", sort=True).strip()
    if not text:
        empty_pages.append(page_number)
    sections.append(
        f"\n{'=' * 24} PDF PAGE {page_number} {'=' * 24}\n\n{text}\n"
    )

if empty_pages:
    raise SystemExit(
        "Text extraction found pages with no selectable text: "
        + ", ".join(map(str, empty_pages))
        + ". Check whether these pages contain scanned images or artwork."
    )

OUTPUT.write_text(
    "EDRL II - page-separated text extraction for subject indexing\n"
    f"Source: {PDF.name}\n"
    f"PDF pages: {document.page_count}\n"
    + "".join(sections),
    encoding="utf-8",
)

print(f"Extracted {document.page_count} PDF pages to {OUTPUT}")
print(f"Output size: {OUTPUT.stat().st_size:,} bytes")
