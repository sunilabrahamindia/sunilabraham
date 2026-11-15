# E-book production: Essays on Dalits, Religion and Liberation II

This directory contains a direct-to-main production workflow for the EDRL II editorial preview. It does not change the original essay pages.

## Current preview scope

- Nine full-text essays selected exclusively from the TSAP category "Writings not in Essays on Dalits, Religion and Liberation".
- Essays arranged by original publication date, oldest first. The relative order of the two 1988 works remains provisional because one publication date is known only to the year.
- The cover is sourced from `sunilabrahammedia/amaa/edrl-ii-v0.2.jpg` at build time. The book sequence is cover, title-only half-title, full title page (title, author and centred imprint; no subtitle), publication details, foreword, Editor's Note, contents and nine essays. The fixed-layout PDF includes a blank verso after the half-title; the reflowable EPUB does not force an artificial blank page. The foreword by Y. T. Vinayaraj is included from the shared source file `foreword.md`, preserving the received wording, poem and two references. The Editor's Note remains draft material.
- Editor: Tito Dutta. Project website: https://sunilabraham.in. Planned publication date: 29 November 2026.
- The e-book ISBN is 978-93-345-1180-2. The paperback ISBN must not be used for the EPUB.
- The front matter is a preview, not a final rights/copyright page. Do not publish the preview as a final edition.
- Source Markdown pages remain the content source of truth.

## Files

- `manifest.yml`: ordered essay selection, source paths and original publication details.
- `front-matter.md`: cover insertion, half-title, full title page, publication details, foreword, Editor's Note and linked contents.
- `foreword.md`: the received foreword text, shared by the e-book and paperback print builders.
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

The GitHub Actions workflow at `.github/workflows/build-edrl-ii.yml` runs on relevant pushes to `main` and can also be started manually from the Actions tab. It builds and validates the editorial EPUB preview, then uploads `edrl-ii-preview.epub` as the `edrl-ii-editorial-preview` artifact. The artifact expires after 30 days, so download and retain a reviewed copy.

### Workflow trigger scope (15 November 2026)

The push trigger is deliberately restricted to files that can affect this editorial preview:

- All files under `ebook/edrl-ii/**`.
- The nine essay Markdown source files listed in `manifest.yml`.
- The workflow file itself, `.github/workflows/build-edrl-ii.yml`.

The previous broad path rule, `amaa/**`, has been removed. It caused unrelated AMAA changes - including the commemoration invitation SVG and other pages - to launch a full EDRL II build, which installs Pandoc and a LaTeX PDF engine and takes around two minutes. Replacing that wildcard with the nine explicit essay paths prevents unrelated AMAA work from triggering the editorial preview.

This change affects only the editorial-preview workflow. The separate `.github/workflows/build-edrl-ii-print.yml` print-preview workflow was not changed by this adjustment and retains its own, narrower path filters. Both workflows can still be started manually using `workflow_dispatch`.

## Quality assurance

The script checks that all nine manifest sources exist, each extraction is substantial, footnote reference/note counts are not reduced, the EPUB ZIP/package is readable, its title metadata is present, and it contains enough XHTML chapters. These are automated safeguards, not a substitute for editorial proofing or a full EPUBCheck validation.

Before publication, inspect all essays against the source, check note links and all references, test the cover, contents and return links plus EPUB navigation and reflow in actual reading applications, validate with EPUBCheck, and proof the PDF page-by-page. Confirm whether a foreword or editor's note will be included, and approve the final rights/copyright statement and bibliographic details. Never claim the book is ready for publication based only on a successful build.
