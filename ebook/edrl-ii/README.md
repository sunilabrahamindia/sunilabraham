# E-book production: Essays on Dalits, Religion and Liberation II

This directory contains a direct-to-main production workflow for the EDRL II editorial preview. It does not change the original essay pages.

## Current preview scope

- Nine full-text essays selected exclusively from the TSAP category "Writings not in Essays on Dalits, Religion and Liberation".
- Essays arranged by original publication date, oldest first. The relative order of the two 1988 works remains provisional because one publication date is known only to the year.
- A traditional half-title (title only), full title page, publication details, credits, foreword placeholder and editor's-note placeholder are included. The fixed-layout PDF includes a blank verso after the half-title; the reflowable EPUB does not force an artificial blank page.
- Editor: Tito Dutta. Project website: https://sunilabraham.in. Planned publication date: 29 November 2026.
- The e-book ISBN is 978-93-345-1180-2. The paperback ISBN must not be used for the EPUB.
- The front matter is a preview, not a final rights/copyright page. Do not publish the preview as a final edition.
- Source Markdown pages remain the content source of truth.

## Files

- `manifest.yml`: ordered essay selection, source paths and original publication details.
- `front-matter.md`: typeset half-title and title page, publication details, credits, and explicit foreword/editor's-note placeholders.
- `metadata.yml`: EPUB/PDF bibliographic metadata.
- `epub.css`: reflowable EPUB styling and front-matter composition rules.
- `build.py`: extraction, manuscript assembly, note-integrity checks and export validation.
- `build.sh`: local launcher.
- `output/`: generated manuscript and preview files; build products are not committed by default.

## Build locally

From the repository root:

```bash
python3 ebook/edrl-ii/build.py
```

Or:

```bash
bash ebook/edrl-ii/build.sh
```

Requires Python 3, Pandoc and (for PDF) a working LaTeX engine such as XeLaTeX.

## Automated build

The GitHub Actions workflow at `.github/workflows/build-edrl-ii.yml` runs on relevant pushes and can also be started manually from the Actions tab. The downloadable artifact contains the manuscript and generated preview files. Artifacts expire after 30 days, so download and retain a reviewed copy.

## Quality assurance

The script checks that all nine manifest sources exist, each extraction is substantial, footnote reference/note counts are not reduced, the EPUB ZIP/package is readable, its title metadata is present, and it contains enough XHTML chapters. These are automated safeguards, not a substitute for editorial proofing or a full EPUBCheck validation.

Before publication, inspect all essays against the source, check note links and all references, test EPUB navigation and reflow in actual reading applications, validate with EPUBCheck, and proof the PDF page-by-page. Confirm cover, foreword, editor's note, final rights/copyright statement and bibliographic details. Never claim the book is ready for publication based only on a successful build.
