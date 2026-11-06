# EDRL II print preview

This directory contains the first Typst-based A5 paperback interior proof for *Essays on Dalits, Religion and Liberation II*.

## Build

The GitHub Actions workflow `.github/workflows/build-edrl-ii-print.yml` installs Typst and Pandoc, extracts the nine manifest entries from the repository's current source pages, converts the content and compiles an A5 PDF.

The PDF is an editorial layout proof, not a printer-approved file. The 1979 essay is currently represented by an explicit transcription placeholder because its source page is still under construction. Foreword and Editor's Note placeholders are retained from the current front matter.

## Current provisional design

- A5, 148 × 210 mm.
- 10 mm left and right margins, 17 mm top and 10 mm bottom.
- 11 pt Libertinus Serif body text, justified.
- Automatic page numbering.
- Separate essay openings and a book-level contents page.
- No full-wrap cover yet: spine, bleed and crop marks require printer specifications and final pagination.

The first proof is intended for visual review. Typography, margins, pagination, essay-opening pages, notes, images and the placeholder treatment will be revised after inspection.
