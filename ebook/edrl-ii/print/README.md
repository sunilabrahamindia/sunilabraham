# EDRL II print production proofs

This directory contains the Typst source and automated workflow for producing the paperback interior and cover review PDFs for *Essays on Dalits, Religion and Liberation II*.

## Build outputs

The GitHub Actions workflow `.github/workflows/build-edrl-ii-print.yml` creates three files:

- `edrl-ii-interior.pdf`: the A5 interior only. This is the file to proofread as a book interior; it does not contain the cover.
- `edrl-ii-front-cover-proof.pdf`: the supplied front-cover artwork placed on an A5 page. It is a front-cover proof only, not a full-wrap cover.
- `edrl-ii-combined-review.pdf`: the front-cover proof followed by the interior, for convenient reading and review. Do not send this combined file to the printer as an interior PDF.

The front-cover artwork is fetched from the dedicated TSAP media repository at build time. The build validates that it is a JPEG before typesetting.

## Interior design system

- A5, 148 × 210 mm.
- Mirrored inside/outside margins: 18 mm inside, 14 mm outside, 18 mm top and 17 mm bottom. These are provisional until the printer confirms the binding allowance.
- Linux Libertine O, 10.5 pt body text, justified, with first-line paragraph indentation.
- Restrained running head and centred folios.
- Separate half-title, blank verso, title page, publication information, foreword, Editor's Note and contents. Preliminary pages beginning with the foreword use Roman-numeral folios; the essays restart at Arabic page 1.
- Essays begin on new pages.
- Native Typst footnotes generated from the essay sources and the two references in the foreword. The foreword poem is centred and retains its line breaks.
- Website navigation and active web links are not part of the print edition; the visible wording is retained.
- The 1979 essay remains an explicit transcription-pending placeholder. The 1985 essay also remains a placeholder until its complete text is available.

## Build requirements

GitHub Actions installs Python, PyYAML, Beautiful Soup, Pandoc, Typst, Linux Libertine fonts and Poppler utilities. Run the workflow manually from the Actions tab or let a relevant source change trigger it.

## Important limitations

These are editorial review proofs, not printer-approved files. The front-cover proof is not a full-wrap paperback cover. The printer must provide the final cover template or confirm the spine width, binding method, paper stock, bleed, crop marks, colour requirements and PDF standard. Do not calculate or invent the spine width before final pagination and printer confirmation.

The interior still requires page-by-page visual proofreading, comparison against the source essays, editorial approval of front matter, completion of missing essays, and a physical test print. A successful GitHub Actions build does not establish that the book is ready for printing.
