---
layout: default
title: "Print Book Production: Essays on Dalits, Religion and Liberation II"
permalink: /amaa/30-print-book-production/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Documentation for producing the A5 paperback edition of Essays on Dalits, Religion and Liberation II, including Typst typesetting, the print-ready interior PDF and full-wrap cover."
created: 2026-11-06
---

**Print Book Production** documents the preparation of the paperback edition of *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It records the production decisions, technical requirements and workflow for creating a complete print-ready PDF, which will be supplied to the printer through Pranesh.

This page is the print-production companion to [E-book Export: A. M. A. Ayrookuzhiel](/amaa/30-ebook-export/). The two editions belong to the same publication project, but their layout and production systems are different.

## Purpose

The objective is to produce a professionally typeset, print-ready interior PDF for the paperback edition. The Sunil Abraham Project will take responsibility for the book's editorial layout and typesetting decisions rather than sending an EPUB to the printer for the printer to redesign.

The finished PDF will be supplied to Pranesh. His role, as discussed, is to coordinate with the printer and arrange for the printing plates to be made from the supplied print-ready PDF. The printer's production specifications must therefore be confirmed before the final PDF is approved.

## Scope

This documentation covers the paperback interior and its production workflow, including:

- Page size, margins and binding allowance.
- Typography, paragraph treatment and heading hierarchy.
- Front matter, essay openings, pagination and running heads.
- Automatic interior page numbering (folios), including preliminary-page numbering conventions.
- Print-specific treatment of hyperlinks and references.
- A separate full-wrap paperback cover PDF containing the back cover, spine and front cover.
- Footnotes, references, tables, illustrations and captions.
- Typst source files and automated PDF generation.
- Printer requirements, technical validation and proofing.

The EPUB remains a separate digital edition. Its content and editorial structure should remain consistent with the print book, but its CSS and reflowable layout rules will not be reused as the print layout. The print design will reproduce the same editorial identity through Typst's own typesetting and styling system.

## Production direction and responsibilities

The following direction was given by Sunil:

- The work should focus on producing the complete print-ready PDF.
- The project will make the decisions about fonts, typography, page layout and design.
- Typst will be used for typesetting the print edition.
- The completed PDF will be sent to Pranesh.
- Pranesh will coordinate with the printer and arrange for printing plates to be made from the print-ready PDF.

The printer is not being asked to make the book's design decisions. The project must supply a finished interior PDF that meets the printer's technical requirements.

## Proposed production workflow

1. **Confirm the printer's requirements:** Obtain any printer-specific PDF instructions, templates, bleed and crop-mark requirements, and the required binding allowance.
2. **Prepare the manuscript:** Use the approved essay sequence and front matter from the e-book project, checking the complete text and publication details before print composition.
3. **Set up the Typst project:** Create a separate print-production directory containing the Typst source, reusable layout rules, required fonts and images.
4. **Establish the page design:** Configure A5 pages, margins, typography, paragraph rhythm, heading styles, page numbering and other book conventions.
5. **Define pagination:** Configure automatic page numbering (folios), decide how preliminary pages are numbered or left unnumbered, establish the main-text numbering sequence, and set consistent folio placement and running-head rules.
6. **Prepare print-specific links:** Remove active hyperlink behaviour and styling from the print interior. Retain references and URLs as readable printed text wherever they form part of the approved content.
7. **Typeset the complete book:** Compose the front matter and all nine essays, preserving notes, references, tables, illustrations and captions.
8. **Generate the interior PDF:** Run Typst in GitHub Actions so that the PDF can be built from the repository without requiring Typst to be installed on the Ubuntu laptop.
9. **Prepare the cover separately:** Create a full-wrap cover layout containing the back cover, spine and front cover in the printer's required dimensions and order. Calculate the spine width only after the final interior page count and printer's paper specification are known. Add bleed, crop marks and other production marks only as required by the printer.
10. **Proof both outputs:** Inspect the interior for missing text, pagination errors, widows and orphans, footnotes, references and image quality. Inspect the cover separately for dimensions, alignment, spine placement and bleed.
11. **Validate for the printer:** Check both PDFs against the printer's supplied specifications. A successful build alone does not establish printer approval.
12. **Supply the approved PDFs:** Send the print-ready interior PDF and separate full-wrap cover PDF to Pranesh for coordination with the printer and plate preparation.

## Page size and initial layout specifications

Herbert suggested the following specifications, which we intend to use as the starting point for the design:

| Element | Suggested specification |
|---|---:|
| Page size | A5 |
| Page width | 14.8 cm |
| Page height | 21 cm |
| Left margin | 1 cm |
| Right margin | 1 cm |
| Top margin | 1.7 cm |
| Bottom margin to text | 1 cm |
| Body text | 10-12 pt |
| Main headings | 16-18 pt |
| Subheadings | 14-16 pt |

A5 (148 × 210 mm) is the specified page size and will be retained. The type sizes are ranges for design and proofing, not a claim that one final size has already been selected. A body size around 11 pt can be tested as an initial setting, with the final choice judged on actual pages and a printed proof.

The stated 1 cm left and right margins are an initial proposal. The inner margin may need to be increased to provide sufficient binding allowance. The final gutter should be settled after the printer's requirements and the likely page extent are understood. The bottom measurement also needs to be applied consistently to the text area and any footer or page number.

## Typography and visual design

The print edition will have its own fixed-page typographic system. The design should be calm, scholarly, readable and appropriate for a collection of essays. It should prioritise sustained reading over decorative effects.

The design work will establish:

- A readable body typeface and suitable weights for regular, italic and bold text.
- A clear hierarchy for the book title, essay titles, section headings and subheadings.
- Consistent line spacing, paragraph indentation or paragraph spacing.
- Readable treatment of quotations, footnotes, references, lists and tables.
- Restrained running heads and consistently placed page numbers, where useful.
- Appropriate spacing around essay openings and front matter.
- Sufficient contrast and legibility, including in a greyscale print.
- Reliable support for punctuation, symbols and all characters used in the essays.

The e-book and print editions should share the same editorial identity, including consistent titles, heading hierarchy, emphasis, references and publication details. However, the EPUB stylesheet is not a print stylesheet: EPUB CSS controls the reflowable digital edition, while Typst controls the fixed-page PDF.

## Typst and technical implementation

Typst will be the typesetting system for the paperback interior. It will generate the PDF from source files maintained in the TSAP GitHub repository.

The planned approach is to run Typst through GitHub Actions, just as the e-book build uses tools installed in a GitHub-hosted runner. Typst does not need to be installed on the Ubuntu laptop for this workflow. Local installation may be useful for optional experimentation, but it is not a requirement.

The print project should remain separate from the EPUB build. A likely location for its source files is `ebook/edrl-ii/print/`. The exact file structure and workflow will be recorded when implementation begins. The print workflow should generate a PDF artifact that can be inspected and supplied to the printer; it should not change the EPUB output or its CSS.

The source manuscript should remain traceable to the approved essays and front matter. Any publication-only corrections must be deliberate and recorded. The original website articles should not be silently rewritten as part of print composition.

## Pagination and print treatment

Page numbers will be generated automatically by Typst as part of the interior layout; they will not be typed manually into the manuscript. The design will establish their position, type style and whether running heads are used.

The pagination plan will distinguish preliminary matter from the main text. Preliminary pages may use a separate numbering convention or remain unnumbered where appropriate; the main text will begin with the agreed numbering sequence. The exact convention and first displayed page number will be settled during layout. Pagination must be checked again after the complete book has been composed, because changes to text, images or page breaks can alter the final sequence.

The print edition is not an interactive digital document. Active hyperlinks, link colours and underlining used only to signal clickable links will be removed. References, citations and URLs that belong to the content will remain as readable printed text. No reference should depend on being clicked to make sense on paper.

## Paperback cover: back, spine and front

The cover is a separate production item from the interior PDF. It will be designed as one full-wrap spread, arranged in the printer's required order and dimensions: back cover panel, spine panel and front cover panel.

The cover PDF will be supplied separately from the A5 interior PDF. Spine width cannot be finalised from page size alone: it depends on the final interior page count, paper stock and binding method. The printer must confirm the cover template or exact spine calculation, overall spread dimensions, bleed, crop marks and any other required production marks before final export.

Cover artwork and text can be prepared while the interior is being typeset, but the final spine width and complete wrap dimensions must wait until the interior pagination and printer specifications are confirmed.

## Printer requirements: questions to confirm

Before final PDF export, the following details need confirmation from Herbert or the printer:

1. Does the printer have specific PDF requirements or a template that the project must follow?
2. What inner binding margin (gutter) should be allowed for the A5 pages?
3. Does the printer require bleed and crop marks, or any other specific printing marks in the PDF?

These are the outstanding questions identified so far. Paper type and GSM do not need to be fixed in order to begin the Typst layout. They may be relevant to the printer's production choices and spine calculation, but they are not prerequisites for designing the interior pages.

## PDF proofing and quality assurance

The generated PDF must be inspected as a complete book, not judged solely by whether Typst exits successfully. Checks should include:

- Correct A5 page dimensions and consistent margins.
- Correct sequence of front matter and all nine essays.
- No missing, duplicated or unexpectedly altered text.
- Correct heading hierarchy and consistent typography.
- No headings stranded at the foot of a page.
- No widows, orphans, awkward page breaks or excessive blank space.
- Footnotes and their references correctly connected and readable.
- References, tables, lists, images and captions complete and legible.
- Page numbers (folios) automatically generated, correctly sequenced and consistently positioned; running heads checked for correctness.
- No active hyperlink styling or behaviour in the print interior; printed references and URLs remain readable.
- Separate full-wrap cover PDF checked for back-cover, spine and front-cover order, final spine width, dimensions and printer-required marks.
- No clipped text, overflow, missing glyphs or low-resolution images.
- Any required bleed, crop marks, embedded fonts or PDF standard verified against the printer's instructions.

The PDF should be checked on screen and, where practicable, through a physical test print. Final approval should follow visual proofing and confirmation that the printer can accept the file.

## Current decisions and pending items

### Decisions and directions recorded

- The print edition will be a paperback.
- A5 (14.8 × 21 cm) is the required page size.
- Typst will be used for typesetting.
- The project will make the layout and typography decisions and produce the complete print-ready PDF.
- Pranesh will coordinate with the printer and arrange plate preparation from the supplied PDF.
- The PDF build can run through GitHub Actions; installing Typst on the Ubuntu laptop is optional.
- The EPUB and print PDF will have separate format-specific styling systems while maintaining editorial consistency.

### Pending confirmation or implementation

- Printer-specific PDF requirements or a production template.
- Final inner binding margin.
- Whether bleed, crop marks or other printing marks are required.
- Final font family, body size, line spacing and heading sizes after page proofing.
- Final running-head, folio, preliminary-page numbering and essay-opening conventions.
- Full-wrap cover design and printer-confirmed spine width, bleed and crop-mark requirements.
- Removal of active hyperlinks while retaining readable reference text in the print interior.
- Typst source structure and GitHub Actions workflow.
- Complete PDF proofing and printer acceptance.

## Print-build configuration and variables

The print builder is maintained separately from the EPUB builder. The current implementation is in `ebook/edrl-ii/print/build.py`, with automation in `.github/workflows/build-edrl-ii-print.yml`. The values below record the current implementation; they are configuration facts, not all final design approvals.

### Paths and source configuration

| Variable or setting | Current value or purpose |
|---|---|
| `ROOT` | Repository root, derived from the location of `build.py` |
| `BASE` | `ebook/edrl-ii/` |
| `PRINT` | `ebook/edrl-ii/print/` |
| `OUT` | `ebook/edrl-ii/print/output/` |
| `COVER_URL` | `https://raw.githubusercontent.com/sunilabrahamindia/sunilabrahammedia/main/amaa/edrl-ii-v0.2.jpg` |
| `COVER` | Downloaded cover image at `output/edrl-ii-cover.jpg` |
| Manifest | `ebook/edrl-ii/manifest.yml`; the builder expects nine essay entries and sorts them by `order` |
| Source text | Original TSAP Markdown pages named in the manifest; these remain the source of truth |

The cover download is checked for a minimum file size and JPEG signature before the build continues. The supplied artwork is currently treated as a front-cover image only; it is not a printer's full-wrap cover.

### Current interior typesetting values

| Setting | Current implementation |
|---|---|
| Page size | A5, 148 × 210 mm |
| Binding model | Mirrored pages, binding on the left |
| Inside margin | 18 mm |
| Outside margin | 14 mm |
| Top margin | 18 mm |
| Bottom margin | 17 mm |
| Body typeface | Linux Libertine O |
| Body size | 10.5 pt |
| Paragraph alignment | Justified |
| Line leading | 0.72 em |
| First-line indent | 1.1 em |
| Paragraph spacing | 0.45 em |
| Level-one headings | 18 pt, bold, centred |
| Level-two headings | 13 pt, bold |
| Level-three headings | 11.5 pt, bold |
| Running head | Book title only: ESSAYS ON DALITS, RELIGION AND LIBERATION II; centred, 7.5 pt, light grey |
| Folio | Centred, 8 pt, light grey |

These are the current proof settings, not final approved specifications. They must be compared with the EDRL I printed-book references when supplied. The final gutter and page design remain subject to printer requirements and physical proofing.

### Build tools and workflow settings

The GitHub Actions workflow currently:

- Runs on pushes to `main` when the manifest, front matter, print directory, AMAA source pages or workflow file changes; it can also be started manually with `workflow_dispatch`.
- Uses `ubuntu-latest` and Python `3.x`.
- Installs Python packages `PyYAML` and `beautifulsoup4`.
- Installs Pandoc, `fonts-linuxlibertine` and `poppler-utils` from Ubuntu packages.
- Downloads the latest Linux x86_64 musl Typst release and installs the `typst` executable.
- Runs `python ebook/edrl-ii/print/build.py`.
- Uploads the three PDFs as the `edrl-ii-print-preview` artifact, retained for 30 days.

### Extraction and conversion safeguards

The builder removes YAML front matter, website introductions and generated contents lists where identified, strips website navigation and Liquid include lines, and converts source HTML footnote references and note-list entries into Pandoc Markdown footnotes before Typst conversion. It checks that each detected footnote reference has a corresponding note target, checks that essay extraction is not suspiciously short, and checks the converted Typst text for common raw HTML elements. These checks are useful safeguards, not proof that every source feature has been preserved correctly. In particular, every essay, footnote and reference still requires visual comparison with the original source.

### Output files

The current successful workflow produces:

- `output/edrl-ii-interior.pdf` - the A5 interior proof, without a cover.
- `output/edrl-ii-front-cover-proof.pdf` - the supplied front-cover image placed on an A5 page.
- `output/edrl-ii-combined-review.pdf` - the cover proof followed by the interior for convenient reading.

The combined review is not the printer's interior file. The front-cover proof is not a full-wrap cover. The full-wrap cover still requires the printer's dimensions, bleed and crop-mark instructions, binding method, final page count and confirmed spine width.

## Work log

- **27 October 2026** - The late-October planning established that the paperback edition would require its own ISBN, separate from the EPUB ISBN, while retaining 29 November 2026 as the publication date.
- **29 October 2026** - Submitted the paperback ISBN application to the Raja Rammohun Roy National Agency (RRRNA), Ministry of Education, under application reference 55408|ISBN|2026|A. The title, publisher (The Sunil Abraham Project), paperback format and publication date were recorded.
- **30 October 2026** - The paperback ISBN was allotted: **978-93-345-8524-7**. This is separate from the EPUB ISBN.
- **2 November 2026** - Initial production work began in a separate EDRL II production workspace and branch. Draft pull request #58 was created with the book manifest, the nine-source chronological essay sequence, build scripts, metadata, EPUB CSS and README. The source selection was restricted to the repository's "works not in EDRL" category pages; material from the 2006 volume was excluded. This was the start of the digital-edition production workflow, not yet the Typst print-layout implementation.
- **6 November 2026** - Created this separate print-production documentation page to record the paperback workflow independently of the EPUB documentation.
- **6 November 2026** - Recorded Sunil's instruction to focus on producing the complete print-ready PDF using Typst. The project will make the design and typesetting decisions; Pranesh will coordinate with the printer and arrange plate preparation from the supplied PDF.
- **6 November 2026** - Recorded Herbert's proposed A5 page dimensions, margins and type-size ranges. A5 is the specified page size; the margin and typography details remain subject to printer requirements and visual proofing.
- **6 November 2026** - Recorded the plan to run Typst through GitHub Actions. Local Typst installation on Ubuntu is optional, not required for the automated build.
- **6 November 2026** - Identified three outstanding printer questions: PDF requirements or template, inner binding margin, and bleed/crop-mark requirements. Paper GSM is not a prerequisite for beginning the page layout.
- **6 November 2026** - Expanded the print specification to record automatic Typst pagination, preliminary-page and main-text folio conventions, removal of active hyperlink behaviour from the print interior, and a separate full-wrap cover PDF for the back cover, spine and front cover. Final spine width remains dependent on final page count and printer specifications.
- **6 November 2026** - Reworked the first Typst proof after inspecting the 73-page PDF. The revised workflow removes website navigation and raw HTML from the print text, converts the source pages' HTML footnote anchors and note lists into native Pandoc/Typst footnotes, uses mirrored inside/outside margins, adds a half-title and blank verso, and builds a separate A5 front-cover proof from the existing artwork. GitHub Actions now produces an interior PDF, a front-cover proof and a combined review PDF. These are editorial proofs, not printer-ready files; the 1979 and 1985 essays remain incomplete placeholders.
- **6 November 2026** - Added a configuration record for the print builder, including repository paths, cover-image source, current Typst variables, page and margin settings, typography, paragraph rhythm, heading sizes, running head, folios, workflow dependencies, triggers, extraction safeguards and output filenames. This section is intended to make future changes traceable and to distinguish current implementation values from final design decisions.
- **6 November 2026** - First print-workflow attempts failed before producing an artifact. The initial run encountered missing Typst footnote labels after the earlier Markdown-to-HTML-to-Typst conversion path had produced dangling note links. The conversion was changed to Markdown-to-Typst directly so Pandoc could handle footnotes natively.
- **6 November 2026** - The next run failed at the raw-HTML safeguard in `md_to_typst()`. The check was too broad: Typst's own generated syntax could be mistaken for an HTML tag. The source validation was narrowed to look for common HTML element names rather than every angle-bracketed expression. This was a validation-rule correction, not a change to the source essays.
- **6 November 2026** - GitHub Actions run [#42191742269](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42191742269) failed during the print build because raw HTML was still detected in essay 1. Run [#42192742064](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42192742064) failed at the same safeguard after the first attempted correction. In both runs, dependency installation completed; PDF generation and artifact upload did not.
- **6 November 2026** - Corrected the raw-HTML detection rule and aligned the heading typeface with the installed Linux Libertine O font. The change was committed as `27be101143f10d94aca451bc172cb76c95c8205c`.
- **6 November 2026** - First successful Typst print-preview workflow: GitHub Actions run [#42193427267](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42193427267) completed successfully on `main` at commit `27be101143f10d94aca451bc172cb76c95c8205c`. All build steps, including PDF generation and artifact upload, passed. GitHub created artifact `edrl-ii-print-preview` (artifact ID `13491585063`), approximately 1.60 MB, with expiry on 6 December 2026. The artifact contains the interior proof, front-cover proof and combined review PDF. This confirms that the workflow generated and uploaded the files; it does not mean that the PDFs have passed visual, editorial or printer QA.

- **6 November 2026** - First focused typography revision after review of the EDRL I printed-book page references and the initial EDRL II preview. Changed only three paragraph/heading rhythm values in `ebook/edrl-ii/print/build.py`: body leading from `0.72em` to `0.85em`; paragraph spacing from `0.45em` to `0.7em`; level-two heading spacing from 13/5 pt to 16/8 pt; and level-three heading spacing from 9/4 pt to 11/6 pt (above/below). No source essay text, cover, front matter, footnote extraction, margins, type sizes or other layout rules were changed in this pass. Code commit: `1f1fe81da9dd33e6f96622ed0380c9361c7fc522`.
- **6 November 2026** - The focused spacing revision was built successfully by GitHub Actions in run [#42195272876](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42195272876), on `main` at documentation commit `28da5dcae985d43b5ad2cbd26639acf8647bcaf3`. Dependency installation, Typst/Pandoc setup, PDF generation and artifact upload all completed successfully. Artifact `edrl-ii-print-preview` (ID `13492325987`, approximately 1.60 MB) contains the three preview PDFs and expires on 6 December 2026. This verifies the build and artifact, not yet the visual acceptability of the revised spacing.
- **6 November 2026** - Updated the running head to remove the project name entirely; the only running-head text is now the book title, `ESSAYS ON DALITS, RELIGION AND LIBERATION II`. The intentionally blank verso after the half-title now has both header and footer disabled, so it carries no running head or folio. The normal book-title running head and folio are restored for following pages.
- **6 November 2026** - Changed the GitHub Actions run title to include its run number (`EDRL II print proof #N`) and made each uploaded artifact unique using `edrl-ii-print-preview-N`. This prevents successive mobile downloads from sharing the same artifact name. The workflow path filters now list the nine manifest essay source files explicitly rather than triggering on every file under `amaa/**`; documentation-only changes to this production page therefore do not start another PDF build.
- **6 November 2026** - The book-title running head, completely blank verso and numbered artifact changes were built successfully in GitHub Actions run [#42197772258](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42197772258), workflow run number 21, commit `a003041fe4f56ab4d071712ae07900b7ef5ae9b0`. All seven build steps completed successfully, including PDF generation and artifact upload. Artifact `edrl-ii-print-preview-21` (ID `13493515685`, approximately 1.60 MB) contains the three PDFs and expires on 6 December 2026. This confirms successful generation and upload; visual inspection of the blank page and running head remains necessary.
## See also

- [E-book Export: A. M. A. Ayrookuzhiel](/amaa/30-ebook-export/) - documentation for the EPUB edition, its metadata, build process and digital quality checks.

{% include navbox-amaa.html %}
