---
layout: default
title: "Print Book Production: Essays on Dalits, Religion and Liberation II"
permalink: /amaa/30-print-book-production/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Documentation for producing the A5 paperback edition of Essays on Dalits, Religion and Liberation II, including Typst typesetting, the print-ready interior PDF and full-wrap cover."
page_id: TSAP-1373
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

## International publishing standards and typographic principles

The print design will be reviewed against established international book-production guidance and recognised principles of book typography. These references are intended to inform decisions during design and proofing; they are not a claim that every publisher follows one universal layout or that every recommendation must be applied mechanically. Some or all of the points below may be adopted where they suit this book, its content, its A5 format and the printer's requirements.

The purpose of recording these principles is to preserve them as a reference for the remaining design, typesetting and proofreading work. They should be considered alongside the existing production specifications and the findings in the PDF audit.

### Page architecture and pagination

- Important opening sections, including the contents and the beginning of the main text, should be considered for right-hand (recto, odd-numbered) page openings, where appropriate to the book's structure.
- Blank pages required to maintain recto openings should remain intentional and should not carry running heads or folios.
- Preliminary matter and the main text may follow different numbering conventions. The chosen sequence must be deliberate, consistent and reflected correctly in the contents.
- Page numbers (folios) should be placed consistently and unobtrusively, normally towards the outside edge or in another established position that works with the running heads.
- Running heads should help readers navigate the book. Their wording and placement must remain consistent, and they should not collide with folios or other page elements.
- Facing pages should be assessed as spreads as well as individually. Inner margins must allow for binding, and the text block should look balanced across the spread.
- Essay or chapter openings should follow a consistent pattern, with appropriate space above the title and enough room for the opening paragraph.

### Body typography and measure

- Typeface, type size, line spacing and text-block width should be judged together. A nominal point size alone does not establish readability.
- Line length should support sustained reading. Bringhurst's commonly cited guidance is approximately 45–75 characters per line, with around 66 as a useful working target; this is a guide to evaluate against the actual typeface and page, not an inflexible rule.
- Line spacing should be sufficient to distinguish lines clearly without making the page look loose. Values such as 11/13 pt or 10/12 pt can serve as starting points for evaluation, not predetermined specifications.
- Paragraph treatment should be consistent. The first paragraph after a heading or section break is commonly set without a first-line indent; subsequent paragraphs may use a consistent indent or another clearly defined system.
- Avoid excessive consecutive hyphenated lines, awkward breaks, and hyphenation of proper names or display titles.
- Check for widows, orphans, short isolated lines and uneven page texture. Correct these through considered composition rather than arbitrary spacing changes.
- Heading levels should be distinct and consistent without unnecessary decoration or oversized display treatment.

### Tables, illustrations and captions

- Tables should be placed close to their first discussion where practical and should remain legible at the final trim size.
- Column widths should reflect the content. Text headings and labels should be easy to scan; numerical columns should be aligned consistently.
- Avoid splitting a table across pages where practical. If a table continues, repeat its number or title as appropriate and repeat the column headings so that the continued material remains understandable.
- Tables should be positioned without awkwardly interrupting the reading flow. If a table cannot fit legibly, consider a redesigned or divided presentation, or another treatment appropriate to the content, rather than merely reducing the type size.
- Illustrations and captions should remain together where possible. Images must reproduce clearly at the intended print size.

### Footnotes, references and other matter

- Footnotes should be readable, consistently numbered and clearly associated with their references. Their spacing and separation from the main text should be restrained and consistent.
- References, URLs, quotations, lists and other supporting matter should remain understandable in print and should not depend on active hyperlinks.
- Proper names, titles, punctuation, symbols and special characters require careful proofing. Fonts must contain the required glyphs and be embedded in the final PDF.
- The final PDF should be checked for clipping, collisions, missing glyphs, unexpected blank pages and other composition faults.

### Printer and PDF production checks

- The printer's own specifications take precedence for technical matters such as trim, binding allowance, bleed, crop marks, colour requirements and PDF standards.
- Confirm the required inner margin and binding allowance with the printer; do not infer them from a generic book-design recommendation.
- Confirm whether crop marks, bleed or other production marks are required before adding them.
- Check embedded fonts, page dimensions, image resolution and the final PDF against the printer's requirements.
- Inspect the PDF on screen and, where practicable, as a physical test print. A successful automated build is not proof of a satisfactory printed book.

### Reference sources

The following sources inform this review. Publisher instructions are production guidance for their own workflows; typographic principles are reference points to evaluate, not universal rules.

1. [Oxford University Press - Preparing print-ready files](https://academic.oup.com/pages/for-authors/books/the-book-publishing-process/writing-and-content-preparation/preparing-print-ready-files)
2. [Oxford University Press - Tables and boxes](https://academic.oup.com/pages/for-authors/books/the-book-publishing-process/writing-and-content-preparation/tables-and-boxes)
3. [Wiley - Preparing print-ready PDFs](https://authorservices-ppd.wiley.com/author-resources/book-authors/prepare-your-manuscript/preparing-print-ready-pdfs.html)
4. [The Chicago Manual of Style - Production technologies](https://www.chicagomanualofstyle.org/help-tools/production-technologies.html)
5. Robert Bringhurst, [The Elements of Typographic Style](https://s3.amazonaws.com/arena-attachments/2584673/e36028a1643a616ec4be1e8d0e859fbb.pdf).
6. [University of Alabama Press - Illustration guidelines](https://www.uapress.ua.edu/illustration-guidelines/).

These references should be revisited when the page design, tables and final PDF are reviewed. Any adopted change should be recorded in the production log, and should not silently alter the source essays or previously approved page elements.

## Typst and technical implementation

Typst will be the typesetting system for the paperback interior. It will generate the PDF from source files maintained in the TSAP GitHub repository.

The planned approach is to run Typst through GitHub Actions, just as the e-book build uses tools installed in a GitHub-hosted runner. Typst does not need to be installed on the Ubuntu laptop for this workflow. Local installation may be useful for optional experimentation, but it is not a requirement.

The print project should remain separate from the EPUB build. A likely location for its source files is `ebook/edrl-ii/print/`. The exact file structure and workflow will be recorded when implementation begins. The print workflow should generate a PDF artifact that can be inspected and supplied to the printer; it should not change the EPUB output or its CSS.

The source manuscript should remain traceable to the approved essays and front matter. Any publication-only corrections must be deliberate and recorded. The original website articles should not be silently rewritten as part of print composition.

## Typst versus Markdown

Markdown and Typst are both text-based markup systems, but their formatting symbols are not interchangeable. Markdown is used for the TSAP source pages and the reflowable e-book content. Typst is used to compose the fixed-page print PDF. When text is transferred from a Markdown source into a Typst document, its emphasis markers must be converted to Typst syntax rather than copied unchanged.

The TSAP [Markdown cheatsheet](/tsap/markdown/) documents the Markdown conventions used across the project. The comparisons below focus on the formatting features that matter directly to this print workflow.

### Inline formatting

<div class="typst-markdown-table-wrap" role="region" aria-label="Comparison of Markdown and Typst inline formatting" tabindex="0">
<table class="typst-markdown-table">
<thead>
<tr><th scope="col">Formatting</th><th scope="col">Markdown (TSAP source)</th><th scope="col">Typst (print source)</th><th scope="col">Important difference</th></tr>
</thead>
<tbody>
<tr><th scope="row">Bold</th><td><code>**bold text**</code></td><td><code>*bold text*</code> or <code>#strong[bold text]</code></td><td>In Typst, asterisks indicate bold.</td></tr>
<tr><th scope="row">Italic</th><td><code>*italic text*</code> or <code>_italic text_</code></td><td><code>_italic text_</code> or <code>#emph[italic text]</code></td><td>In Typst, underscores indicate italic.</td></tr>
<tr><th scope="row">Underline</th><td>Not part of standard Markdown. HTML <code>&lt;u&gt;underlined text&lt;/u&gt;</code> may work where raw HTML is permitted.</td><td><code>#underline[underlined text]</code></td><td>Typst has a native underline function; Markdown does not have a standard underline marker.</td></tr>
</tbody>
</table>
</div>

### Headings and tables

<div class="typst-markdown-table-wrap" role="region" aria-label="Comparison of Markdown and Typst headings and tables" tabindex="0">
<table class="typst-markdown-table">
<thead>
<tr><th scope="col">Element</th><th scope="col">Markdown (TSAP source)</th><th scope="col">Typst (print source)</th><th scope="col">Important difference</th></tr>
</thead>
<tbody>
<tr><th scope="row">Level 1 heading</th><td><code># Heading</code></td><td><code>= Heading</code></td><td>Markdown uses hash signs; Typst uses equals signs.</td></tr>
<tr><th scope="row">Level 2 heading</th><td><code>## Heading</code></td><td><code>== Heading</code></td><td>Each additional marker indicates a lower heading level.</td></tr>
<tr><th scope="row">Level 3 heading</th><td><code>### Heading</code></td><td><code>=== Heading</code></td><td>The marker sequence is different even though the heading hierarchy is comparable.</td></tr>
<tr><th scope="row">Table</th><td>Pipe table, with a header separator row: <code>| Name | Year |</code> followed by <code>|---|---|</code></td><td><code>#table(columns: 2, [Name], [Year], [Example], [2026])</code></td><td>Markdown uses pipe-delimited rows; Typst uses the <code>#table()</code> function and explicit column definitions.</td></tr>
</tbody>
</table>
</div>

The distinction between bold and italic is especially important in this project. The Markdown cheatsheet uses `*italics*` and `**bold**`. In Typst, the meanings are different: `*bold*` and `_italics_`. Copying Markdown emphasis markers directly into a Typst source can therefore change the intended appearance. The Editor's Note uses Typst's underscore syntax for book and journal titles; all other text in that note is plain, without bold styling.

The two comparison tables are placed in horizontally scrollable containers on narrow screens. This keeps the table columns readable on mobile rather than forcing the page layout to compress the contents.

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
| Body size | 11 pt |
| Paragraph alignment | Justified |
| Line leading | 0.85 em |
| First-line indent | 1.1 em |
| Paragraph spacing | 12 pt |
| Level-one headings | 18 pt, bold, centred |
| Level-two headings | 16 pt, bold |
| Level-three headings | 14 pt, bold |
| Running head | Book title only: ESSAYS ON DALITS, RELIGION AND LIBERATION II; centred, 7.5 pt, light grey, with a thin rule below |
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

- **6 November 2026** - Continued the interior typography review. The body text was set to 11 pt Linux Libertine O, with 0.85 em leading, 1.1 em first-line indentation and 12 pt paragraph spacing. Heading sizes were set to 18 pt for level one, 16 pt for level two and 14 pt for level three. The A5 margins remained 18 mm inside, 14 mm outside, 18 mm top and 17 mm bottom. These are the current proof settings, not final printer-approved specifications.
- **6 November 2026** - Added a thin rule below the centred book-title running head. The publication-details heading replaced the earlier "Publication and copyright" heading, and the copyright notice and all-rights-reserved reproduction restriction were removed from the print front matter as instructed. This records a change to the print composition; it does not alter the source essays.
- **6 November 2026** - Corrected the source treatment of *Religion: A Way of Salvation or an Ideology of Oppression?* so the print build takes the complete essay text rather than the website's transcription-introduction material. The placeholder detection was also narrowed to the explicit under-construction marker, avoiding a false transcription-pending result caused by ordinary wording in an essay. These were print-extraction changes; the original article source remains the source of the essay text.
- **7 November 2026** - Added print-specific handling for explicitly marked poem blocks in *Dalit Theology: A Movement of Counter-Culture* and *The Ideological Nature of the Emerging Dalit Consciousness*. The build preserves these blocks through HTML cleanup and converts them as centred text with no first-line indentation, no justification and no paragraph spacing. The source poem wording and stanza structure were not edited in this change. GitHub Actions print-preview run [#42335828680](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42335828680) completed successfully; its artifact is `edrl-ii-print-preview-35` (ID `13558688901`). The successful build confirms generation, not visual approval of the poem pages.
- **7 November 2026** - Removed redundant standalone "Notes" headings from the print conversion when the corresponding HTML note entries have been extracted and converted to page-bottom footnotes. This is conditional: note text is retained, and the heading is removed only when note entries were successfully extracted. The source essay pages are unchanged. GitHub Actions print-preview run [#42336320507](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42336320507) completed successfully at commit `cbf5bcde75224e7a4c32770e07c0aadad572ff1c`. Artifact `edrl-ii-print-preview-36` (ID `13559537201`, approximately 1.97 MB) contains the three PDFs and is retained until 7 December 2026. The PDF still needs visual checking to confirm that the redundant headings have disappeared and that all note text appears correctly at the foot of the relevant pages.
- **7 November 2026** - Added a source reference section listing all nine essays in the print edition, each linked to its full-text page and accompanied by its original publication details.
- **7 November 2026** - Updated the print conversion to preserve the five HTML tables in *Religion: A Way of Salvation or an Ideology of Oppression?* as structured tables in the generated manuscript, rather than flattening their contents during HTML cleanup. GitHub Actions print-preview run #37 was triggered to test the change.
- **7 November 2026** - Added a draft Editor's Note to the print front matter. The note records the occasion for the volume, the publication history of the first volume, the Sunil Abraham Project's preservation work, the nine essays and their original publication history, and the possibility of a future revised edition. A draft notice and the editor's place, date and name were included. The styling instruction is that only book titles and journal titles are italic; institutional names, the draft notice and all other text remain plain, with no bold styling.
- **7 November 2026** - Corrected the Editor's Note emphasis syntax after identifying a difference between Markdown and Typst. Markdown-style asterisks had been used for titles in the Typst source; in Typst, asterisks produce bold text, while underscores produce italics. Replaced the five book and journal title markers with Typst underscore emphasis. The rest of the note was left plain. Print workflow run [#40](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42341967515) completed successfully at commit `54aa0a2f9afb09563f6cd03286f720210fc22c60`.
- **7 November 2026** - Added this **Typst versus Markdown** reference section, based on the TSAP [Markdown cheatsheet](/tsap/markdown/). It compares bold, italic, underline, heading and table syntax, and records the specific asterisk/underscore distinction that affected the Editor's Note. Both comparison tables use horizontally scrollable wrappers on mobile screens.

## Essay sources and original publication details

The following list identifies each essay in the print edition, links to its full text on the TSAP website, records its original publication details and gives the total number of footnote citation markers in the source text. Repeated citations are counted each time they appear, rather than counting only distinct note entries. These figures provide a checklist for checking the footnotes in the generated PDF.

| Essay | Full text | Citations (footnote markers) | Original publication |
|---|---|---:|---|
| The State of Hinduism in 2000 A.D.—Some Emerging Trends | [Full text](/amaa/state-of-hinduism-in-2000-ad-full-text/) | 0 | *Indian Journal of Theology*, Vol. 26, No. 2, April–June 1977. |
| Religion, Spirituality and Aspirations of the People | [Full text](/amaa/religion-spirituality-and-aspirations-of-the-people-full-text/) | 6 | *Religion and Society*, Vol. XXV, No. 1, March 1978. |
| The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue | [Full text](/amaa/living-hindu-popular-religious-consciousness-full-text/) | 8 | *Religion and Society*, Vol. XXVI, No. 1, March 1979, pp. 5–25. |
| The Church and the Study of Religion | [Full text](/amaa/the-church-and-the-study-of-religion/) | 6 | *Religion and Society*, Vol. XXVIII, No. 3, September 1981, pp. 36–41. |
| Religions and the Aspirations of the People | [Full text](/amaa/religions-and-the-aspirations-of-the-people/) | 3 | *Religion and Society*, Vol. XXX, Nos. 3 & 4, September–December 1983, pp. 102–108. |
| Religion: A Way of Salvation or an Ideology of Oppression? | [Full text](/amaa/religion-way-salvation-ideology-oppression-full-text/) | 4 | *Religion and Society*, Vol. XXXII, No. 1, March 1985. |
| Dalit Theology: A Movement of Counter-Culture | [Full text](/amaa/dalit-theology-movement-counter-culture-full-text/) | 42 | Paper No. 7, pp. 83–103, in *Towards a Dalit Theology* (1988). |
| Dalit Liberation — Some Reflections on Their Ideological Predicament | [Full text](/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament/) | 0 | *Religion and Society*, Vol. XXXV, No. 2, June 1988, pp. 47–52. |
| The Ideological Nature of the Emerging Dalit Consciousness | [Full text](/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness/) | 22 | *Religion and Society*, Vol. XXXVII, No. 3, September 1990, pp. 14–23. |
| **Total** | | **91** | |


## Footnote tally snapshot — 7 November 2026, 12:20 p.m.

This is the baseline PDF audit recorded before the next round of corrections. The tally was checked against the **combined review PDF, artifact version 46** (`edrl-ii-combined-review-46.pdf`, 142 pages). It records what was actually visible in that PDF at the time of the audit; it is not a statement about the current or final build.

<div class="footnote-tally-wrap" role="region" aria-label="Footnote tally for combined review PDF artifact version 46, audited on 7 November 2026 at 12:20 pm" tabindex="0">
<table class="footnote-tally">
<thead>
<tr>
<th scope="col">Essay</th>
<th scope="col">Source citation markers</th>
<th scope="col">Rendered as page-bottom footnotes</th>
<th scope="col">Visible as raw markers</th>
</tr>
</thead>
<tbody>
<tr><th scope="row">1. The State of Hinduism in 2000 A.D.</th><td>0</td><td>0</td><td>0</td></tr>
<tr><th scope="row">2. Religion, Spirituality and Aspirations of the People</th><td>6</td><td>6</td><td>0</td></tr>
<tr><th scope="row">3. The Living Hindu Popular Religious Consciousness</th><td>8</td><td>8</td><td>0</td></tr>
<tr><th scope="row">4. The Church and the Study of Religion</th><td>6</td><td>6</td><td>0</td></tr>
<tr><th scope="row">5. Religions and the Aspirations of the People</th><td>3</td><td>3</td><td>0</td></tr>
<tr><th scope="row">6. Religion: A Way of Salvation or an Ideology of Oppression?</th><td>4</td><td>4</td><td>0</td></tr>
<tr><th scope="row">7. Dalit Theology: A Movement of Counter-Culture</th><td>42</td><td>0</td><td>42</td></tr>
<tr><th scope="row">8. Dalit Liberation — Some Reflections on Their Ideological Predicament</th><td>0</td><td>0</td><td>0</td></tr>
<tr><th scope="row">9. The Ideological Nature of the Emerging Dalit Consciousness</th><td>22</td><td>0</td><td>22</td></tr>
<tr class="tally-total"><th scope="row">Total linked citation markers</th><td>91</td><td>27</td><td>64</td></tr>
</tbody>
</table>
</div>

The PDF also contains **two additional manually numbered footnotes** that are not included in the 91 linked source-marker tally: one in essay 7 (PDF page 120; printed page 119) and one in essay 9 (PDF page 142; printed page 141). These must be reconciled separately with the source articles before a final footnote total is declared.

**Audit result:** 27 of the 91 linked citation markers were correctly rendered as page-bottom footnotes. The remaining 64 appeared literally as Markdown markers (`[^1]`, `[^2]`, and so on) in the body text, without their corresponding page-bottom notes. The raw markers also caused a serious collision with the poetry layout on PDF page 142. This is the baseline against which the next corrected artifact must be checked.



## Full PDF audit snapshot — 7 November 2026, 12:20 p.m.

This section preserves the other findings from the same inspection of **combined review PDF artifact version 46**. It is a historical audit record, not a claim that every item remains unresolved in a later artifact. The Foreword, Editor's Note and production-credit wording were known working material at the time and are recorded here for completeness, not classified as errors requiring immediate correction.

### Tables and boxed material

The tables are the most substantial non-footnote layout problem identified in the version 46 PDF.

| PDF page | Printed page | Finding recorded |
|---|---:|---|
| 79 | 78 | Table 1 is cramped; words break awkwardly across narrow columns. |
| 80 | 79 | Table 2 column headings collide with borders or overlap; narrow columns cause excessive word breaks. |
| 80–81 | 79–80 | Tables cross page boundaries without sufficiently clear continuation treatment. Table 3 continues without repeating its headings, making the context of continued rows difficult to follow. |
| 81 | 80 | Table 4 has narrow columns and awkward line breaks. |

**Required review when the tables are addressed:**
- Redesign column widths around the content rather than forcing all columns to equal widths.
- Keep headings legible and clearly separated from rules and cell content.
- Avoid splitting individual rows across pages.
- Where a table must continue, repeat its column headings and make the continuation unmistakable.
- Consider landscape treatment or a redesigned multi-part table where the information cannot fit legibly at A5 size.
- Do not solve the problem simply by shrinking the type until it becomes difficult to read.
- Keep tables compact but independently understandable. Use clear headings, align numeric material consistently, and use rules sparingly.

### Headings and hierarchy

- The general heading hierarchy is restrained and consistent, but display essay titles need a specific check for undesirable line-end hyphenation.
- Example: on PDF page 77, the word "Ideology" is broken as "Ideol-ogy" in the essay display title. Display titles should not be hyphenated; adjust the title measure, line breaks or local typography instead.
- Keep the heading hierarchy consistent and descriptive. Avoid introducing unnecessary levels or decorative treatments.
- Review heading placement at page bottoms so that a heading is not stranded without enough following text.

### Footnotes, poetry and source notes

The detailed marker count and version 46 footnote findings are recorded in the preceding **Footnote tally snapshot**. The additional observations from the visual audit were:

- Where footnotes did render correctly, the thin separator and spacing at the foot of the page looked appropriate. Retain this restrained treatment.
- The two additional manually numbered legacy notes were visible separately from the 91 linked source-marker tally. They require reconciliation with the source articles before the definitive total is stated.
- On PDF page 142 (printed page 141), raw citation markers in the poetry area disrupted the lines and caused visible collisions/overlap. The poetry layout must be checked again after citation conversion.
- Preserve the distinction between prose and poetry: poetry should not inherit justified prose spacing or first-line indentation.

### General typography and page composition

- The A5 trim size is consistent throughout the proof.
- Linux Libertine O is an appropriate scholarly serif for this collection. The 11 pt body size is readable; the audit did not recommend replacing the typeface or undertaking a wholesale redesign.
- Running headers and centred page numbers are restrained and consistent. Retain them unless a later page-specific issue is found.
- Justified body text contains frequent hyphenation in places. This was not judged uniformly defective, but it should be reviewed after the footnote and table corrections, with particular attention to awkward breaks and uneven page texture.
- Review widows and orphans, short final lines, isolated headings and page turns during final pagination.
- The blank pages observed in the proof appear to support intentional recto/verso or section-opening layout. Do not remove them automatically; confirm their purpose against the print pagination plan.
- The contents page (PDF page 9) appeared to show the correct starting page numbers for all nine essays in version 46. Recheck it after pagination changes.

### Front matter and production material — status at the time of audit

These items were visible in version 46 but were identified as work in progress, not as defects to fix in the citation-only pass:

- PDF page 6 (printed page 5): the Foreword contained the placeholder text indicating that the approved Foreword was still awaited.
- PDF pages 7–8 (printed pages 6–7): the Editor's Note carried the notice "DRAFT VERSION — NOT YET FINALISED".
- PDF page 5 (printed page 4): the publication details said that typesetting and printing credits would be added when production details were confirmed.

The Foreword and Editor's Note are being worked on separately. These passages must remain untouched during a citation-only correction.

### Cover proof

- PDF page 1 is a front-cover proof only. It is not a complete printer's wrap.
- The cover concept itself was judged coherent and professionally restrained: cream ground, dark serif title, muted red accent, and the ochre sun/tree and silhouettes.
- Final print production still requires the full-wrap cover, including back cover and spine. The spine width must be calculated from the printer's final paper, binding and page-count specifications, using the printer's template.

### PDF accessibility and archival preparation

The version 46 file was selectable/searchable as text, but the PDF inspection reported:

- no tagged PDF structure;
- no custom document metadata;
- no confirmed bookmarks/outlines;
- no declared document language.

For the final digital/archival PDF, investigate adding accurate title, author, subject, keywords and language metadata; useful bookmarks/outlines for the front matter and nine essays; and tagged structure where the production toolchain permits it. These are quality and accessibility improvements, not part of the citation-only correction.

### Stray notes and web material

- No separate, stray "Notes" section heading was found in the extracted version 46 PDF.
- No unrelated or accidentally scraped web content was identified.
- The site addresses visible in the book were in relevant publication/editorial contexts: the project website and the AMAA portal.
- The legitimate page-bottom notes in essays 2–6 and the two manually numbered legacy notes were not classified as stray material.

### Scope and order of subsequent work

This audit record is intended to prevent findings from being lost between successive proof versions. The order agreed for the next checks is:

1. Correct and verify citations/footnotes against the source articles and the version 46 baseline.
2. Inspect the next artifact specifically for citation correctness before changing anything else.
3. Address the four table-layout cases and their page continuations as a separate task.
4. Review display-title hyphenation and page composition.
5. Complete front matter and production credits when the relevant text/details are ready.
6. Prepare the final full-wrap cover and improve PDF metadata/accessibility as part of final production.

No table, heading, front-matter, cover, metadata or general typography changes were made as part of the citation-only correction recorded after this audit.


## Production log — publication page and final layout review — 7 November 2026

The following changes were made in the print builder after the version 46 audit and the subsequent table and heading-layout work.

1. **Publication details page composition:** Replaced the previous centred "Publication details" heading and loosely stacked text with a restrained colophon-style layout. The existing publication information and wording were retained. The page now uses a compact imprint line, a clear title-and-author hierarchy, a ruled separation and a two-column label/value arrangement for the publisher, website, edition, ISBN, printed price and language.
2. **Page furniture:** Suppressed the running header, footer and folio on the publication details page so that it reads as a deliberate preliminary page rather than an ordinary essay page.
3. **Typography and spacing:** Used the book's existing Linux Libertine O family, restrained sizes and greyscale rules. The composition is left-aligned within a narrower measure and avoids boxes or decorative graphics.
4. **Scope:** No essay source text, publication facts, ISBN, price, date, author/editor attribution or existing production-credit wording was changed. The change is confined to the Typst builder.
5. **Existing layout work retained for verification:** The builder also contains the earlier HTML-table-to-Typst conversion, content-weighted column proportions, repeating table-header treatment, non-breakable table cells, local table typography and non-hyphenated heading styles. These are to be checked in the generated PDF rather than assumed correct from source code alone.
6. **Build and proof checks:** The GitHub Actions build is the validation step. The resulting combined review PDF must be inspected for table readability and continuation, caption placement, heading breaks and page-bottom placement, footnote rendering (including poetry), publication-page composition and contents pagination. A successful automated build is not by itself proof of visual correctness.

Builder change: `0eb937ed5fd93f39266038fddd7a1d3a11aa4ab1` (`Redesign EDRL II publication details page`). The workflow run number, artifact identifier, PDF page count and visual inspection findings should be appended here after the build completes and the generated files have been examined.

## Table readability correction — 7 November 2026

The combined review PDF from workflow run 54 (artifact `edrl-ii-print-preview-54`, 143 pages) showed that the table headings remained difficult to read at A5 size. In particular, Table 4's long column labels were broken into narrow fragments and justified spacing stretched the words across the header cells.

The print builder has now been adjusted, without changing the essay source or its data:

1. **Concise print-only column labels:** Long headings are replaced in the printed tables with shorter labels that retain their meaning. Examples include "Families with land", "Land held (acres)", "Borewells and pumpsets", "Amount (Rs.)", "Fully employed: own farm / other work", and "Agriculture + wage labour". The original full wording remains in the source article.
2. **Natural header spacing:** Table content now uses non-justified paragraph layout with no first-line indent or extra paragraph spacing. This prevents the large, uneven gaps between words visible in the previous proof.
3. **Clear header alignment:** Header cells are explicitly left-aligned, while the numeric data columns retain their centred alignment.
4. **Scope:** The change is confined to the print builder. No essay text, figures, row labels, credits-page content or other front matter has been changed.

The next proof must be visually checked at A5 size, especially Tables 1–5, including header wrapping, row integrity, page continuation and repeated headings. This correction is not considered complete until the generated PDF has been inspected.


## Foreword preparation

The foreword by Y. T. Vinayaraj has been received as a Word document attached to an email.

- [x] Receive the foreword from the author.
- [ ] Obtain and inspect the original Word document.
- [ ] Identify any apparent typographical issues for confirmation.
- [ ] Incorporate the approved foreword into `ebook/edrl-ii/print/build.py`, replacing the existing placeholder.
- [ ] Retain the author's original wording and paragraph structure.
- [ ] Include the foreword before the Editor's Note and Contents in the paperback interior.
- [ ] Run the print production workflow and inspect the resulting PDF for pagination, layout and formatting.

## See also

- [E-book Export: A. M. A. Ayrookuzhiel](/amaa/30-ebook-export/) - documentation for the EPUB edition, its metadata, build process and digital quality checks.

{% include navbox-amaa.html %}


<!-- NOTE DO NOT ADD ANYTHING EXCEPT STYLE AND SCRIPT BELOW, DO NOT READ TITO'S EDIT -->
<style>
.typst-markdown-table-wrap {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  overscroll-behaviour-x: contain;
  margin: 1rem 0 1.5rem;
  -webkit-overflow-scrolling: touch;
  border: 1px solid #767676;
}

.typst-markdown-table-wrap:focus-visible {
  outline: 3px solid #1f5fbf;
  outline-offset: 3px;
}

.typst-markdown-table-wrap table.typst-markdown-table {
  display: table !important;
  width: max-content !important;
  min-width: 760px;
  max-width: none;
  margin: 0 !important;
  border-collapse: collapse;
  border-spacing: 0;
  box-shadow: none !important;
  border-radius: 0 !important;
  background: #fff;
  font-size: 0.92rem;
}

.typst-markdown-table-wrap .typst-markdown-table th,
.typst-markdown-table-wrap .typst-markdown-table td {
  min-width: 9rem;
  border: 1px solid #767676;
  padding: 0.65rem 0.75rem;
  text-align: left;
  vertical-align: top;
  white-space: normal;
  overflow-wrap: anywhere;
}

.typst-markdown-table-wrap .typst-markdown-table thead th {
  background: #e8edf3;
  color: #20252b;
  font-weight: 700;
}

.typst-markdown-table-wrap .typst-markdown-table tbody th {
  background: #f3f5f7;
  color: #20252b;
  font-weight: 600;
}

.typst-markdown-table-wrap .typst-markdown-table code {
  white-space: normal;
  overflow-wrap: anywhere;
}

body.tsap-dark-mode .typst-markdown-table-wrap {
  border-color: #64748b;
}

body.tsap-dark-mode .typst-markdown-table-wrap .typst-markdown-table {
  background: #111827;
  color: #f3f4f6;
}

body.tsap-dark-mode .typst-markdown-table-wrap .typst-markdown-table th,
body.tsap-dark-mode .typst-markdown-table-wrap .typst-markdown-table td {
  border-color: #64748b;
}

body.tsap-dark-mode .typst-markdown-table-wrap .typst-markdown-table thead th,
body.tsap-dark-mode .typst-markdown-table-wrap .typst-markdown-table tbody th {
  background: #1b2636;
  color: #f3f4f6;
}

/* Footnote tally: keep the wide audit table within the page on small screens. */
.footnote-tally-wrap {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  overscroll-behaviour-x: contain;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0 1.5rem;
  border: 1px solid #767676;
}
.footnote-tally-wrap:focus-visible {
  outline: 3px solid #1f5fbf;
  outline-offset: 3px;
}
.footnote-tally {
  display: table !important;
  width: max-content !important;
  min-width: 760px;
  max-width: none;
  margin: 0 !important;
  border-collapse: collapse;
  border-spacing: 0;
  box-shadow: none !important;
  border-radius: 0 !important;
  background: #fff;
  font-size: 0.92rem;
}
.footnote-tally th,
.footnote-tally td {
  min-width: 8rem;
  padding: 0.6rem 0.7rem;
  border: 1px solid #767676;
  text-align: left;
  vertical-align: top;
  white-space: normal;
  overflow-wrap: anywhere;
}
.footnote-tally thead th {
  background: #e8edf3;
  color: #20252b;
}
.footnote-tally tbody th {
  background: #f3f5f7;
  color: #20252b;
}
.footnote-tally td {
  text-align: center;
}
.footnote-tally .tally-total th,
.footnote-tally .tally-total td {
  font-weight: 700;
  border-top: 2px solid #444;
}
body.tsap-dark-mode .footnote-tally-wrap {
  border-color: #64748b;
}
body.tsap-dark-mode .footnote-tally {
  background: #111827;
  color: #f3f4f6;
}
body.tsap-dark-mode .footnote-tally th,
body.tsap-dark-mode .footnote-tally td {
  border-color: #64748b;
}
body.tsap-dark-mode .footnote-tally thead th,
body.tsap-dark-mode .footnote-tally tbody th {
  background: #1b2636;
  color: #f3f4f6;
}

</style>
