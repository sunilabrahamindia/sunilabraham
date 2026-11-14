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

## Subject index

A subject index will be prepared for the paperback edition. It will help readers locate people, places, concepts, movements, institutions and other significant subjects discussed across the essays. The index is an editorial component of the book, not simply a list of frequently occurring words. Entries must be selected for their significance and usefulness to readers, and page references must be checked against the final printed pagination.

### Tools and division of work

The subject-index workflow will use the Ubuntu laptop for PDF text extraction and the Windows 7 second-hand desktop for Cindex 4.4:

- **Ubuntu - PDF extraction:** Use Python with PyMuPDF to extract text page by page from the paginated book PDF. Retain the PDF page position and the printed folio/page number as separate pieces of information wherever they differ.
- **Ubuntu - candidate discovery:** Search and review the extracted text to identify possible names, places, concepts, organisations, events and recurring themes. Automated word counts and searches may help discover candidates, but they must not determine the final index automatically.
- **Editorial review:** Decide which subjects merit entries, choose consistent preferred terms, group related concepts, and identify useful subentries and cross-references. Check the context of each occurrence so that a word is not indexed merely because it appears.
- **Windows - Cindex 4.4:** Use Cindex to create and manage the index records, organise main entries and subentries, consolidate duplicate terms, add cross-references such as "See" and "See also", sort entries and prepare the index for export.
- **Final integration:** Transfer the reviewed index output back into the print-production project and compose it as the book's index section using the established Typst workflow.

PyMuPDF is a text-extraction tool, not an automatic subject-indexing system. It can extract searchable text and identify PDF pages, but editorial judgement is required to select and structure index entries. If the source PDF consists of scanned page images rather than selectable text, OCR will be required before text extraction. OCR output must be checked against the page images, particularly for names and specialised terminology.

### Page references and pagination control

The index must refer to the page numbers printed in the book, not blindly to the PDF viewer's page count. Preliminary pages, unnumbered pages, Roman-numbered pages, blank pages and the main-text sequence can make these values different. The extraction process must therefore record the relationship between each PDF page and its printed folio.

The body text and its pagination should be treated as stable before the index is finalised. The preferred sequence is to generate and proof the complete paginated interior without the index, extract and verify page references from that version, prepare the index in Cindex, and then append the index to the book. Because the index is placed at the end, adding it should not change the page references in the preceding text. Any later change that affects the main text's pagination must trigger a fresh page-reference check.

### Indexing principles

- Index meaningful subjects rather than every repeated word.
- Include significant people, places, communities, institutions, organisations, texts, events, movements and concepts where they are substantively discussed.
- Use consistent names and preferred terms; account for variant spellings and alternative names through cross-references where useful.
- Create subentries when they make a broad subject easier to navigate. Avoid long, undifferentiated strings of page numbers where more specific subentries would help.
- Distinguish substantive discussion from passing mentions. A page reference should take readers to a useful treatment of the subject.
- Use "See" references to direct readers from an unused or alternative term to the preferred entry, and "See also" references to connect related entries.
- Avoid duplicate entries, inconsistent singular/plural forms and unnecessary synonym entries.
- Verify every final page reference against the paginated PDF. Sampling alone is not sufficient for the final index.
- Keep the index concise enough to be useful while representing the full range of the book's arguments and subjects.

### Subject-index deliverables

The indexing stage should produce:

1. A page-by-page extracted text file or structured dataset from the paginated PDF.
2. A working list of candidate subjects with their occurrence locations.
3. A reviewed Cindex database containing the selected entries, subentries and cross-references.
4. An exported index suitable for integration into the Typst print source.
5. A final proofed index checked against the completed interior PDF.

The Cindex database and the extracted text should be retained as production files so that corrections can be made and the index can be regenerated if the manuscript or pagination changes.

## Draft book production plan

The following is a working plan for completing the paperback edition of *Essays on Dalits, Religion and Liberation II*. It is a proposed sequence, not a statement that every stage has already been completed. The existing source essays and front matter remain the authoritative manuscript; production work must not silently rewrite them.

### Stage 1 - Confirm and freeze the publication manuscript

- Confirm the title, author attribution, publication details and final contents.
- Confirm the front matter and the order of all nine essays.
- Check that each essay is complete and that no text, notes, references, tables or illustrations are missing.
- Record any editorial corrections separately and obtain approval before applying them to the publication text.
- Establish a dated, version-controlled manuscript baseline for print production.

### Stage 2 - Complete the interior design and typesetting

- Confirm the printer's trim size, binding method, inner margin, bleed and PDF requirements.
- Finalise the A5 page design, typefaces, type sizes, line spacing, paragraph treatment, heading hierarchy and folio conventions.
- Complete the Typst source and maintain the existing separation between the EPUB and print workflows.
- Typeset the front matter and all nine essays, including notes, references, tables, illustrations and captions.
- Review page openings, running heads, folios, blank pages, widows, orphans and overall page balance.

### Stage 3 - Generate and proof the paginated book

- Generate a complete interior PDF without the subject index.
- Check the PDF for missing text, missing glyphs, font embedding, image resolution, clipping, overlapping elements, footnote placement and unexpected blank pages.
- Confirm the relationship between PDF page positions and the printed page numbers.
- Treat the main text's pagination as provisionally locked before preparing index references.
- Preserve this paginated PDF as the reference copy for indexing.

### Stage 4 - Prepare the subject index

- On Ubuntu, install and use PyMuPDF to extract the text page by page from the reference PDF.
- Use OCR where pages are image-only, and verify OCR text against the original pages.
- Generate candidate names, places, concepts and themes with their occurrence locations.
- Review candidates in context and decide which subjects deserve entries.
- Transfer the selected terms and page references into Cindex 4.4 on the Windows desktop.
- Edit the index structure, consolidate entries, create subentries and add "See" and "See also" references.
- Export the reviewed index and integrate it at the end of the Typst book source.

### Stage 5 - Produce and proof the complete interior

- Generate a fresh PDF containing the complete book and the subject index.
- Verify every index entry and page reference against the final PDF.
- Check alphabetical order, indents, entry hierarchy, cross-references, line breaks and index-page typography.
- Recheck the main text's pagination to ensure that index integration has not altered it.
- Make corrections in the appropriate source and regenerate the PDF.

### Stage 6 - Prepare the cover

- Confirm the final interior page count and the printer's paper specification before calculating spine width.
- Prepare the full-wrap cover with back cover, spine and front cover.
- Apply the printer's required dimensions, bleed, colour settings and production marks.
- Proof the cover separately for text, alignment, spine placement, safe areas and image quality.

### Stage 7 - Technical validation and final proof

- Validate the interior and cover PDFs against the printer's current specifications.
- Check page dimensions, embedded fonts, image resolution, colour handling and PDF integrity.
- Inspect the complete interior both on screen and, where practicable, as a physical test print.
- Complete a final editorial and production checklist; record unresolved issues rather than treating them as approved.
- Retain the final source files, build logs and proof PDFs with the project.

### Stage 8 - Printer handover and publication archive

- Supply the approved print-ready interior PDF and full-wrap cover PDF to Pranesh.
- Obtain confirmation that the printer can use the supplied files and that no further technical changes are required.
- Review the printer's proof before authorising the print run.
- Archive the approved PDFs, Typst source, Cindex database, extracted indexing data and final production notes in the repository.
- Record the final edition details and publication status on the relevant TSAP publication page.

### Working completion criteria

The paperback should be considered ready for printer handover only when the complete interior and cover have passed their respective checks, the subject index has been verified against the final printed pagination, and the printer's technical requirements have been confirmed. A successful automated build or an uploaded PDF artifact is necessary evidence of production, but it is not by itself proof of editorial or print readiness.

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

- **8 November 2026** - Made the agreed pagination-only change in `ebook/edrl-ii/print/build.py`: reset the page counter immediately before the first essay so that *The State of Hinduism in 2000 A.D.—Some Emerging Trends* begins at printed page 1. The draft Foreword and Editor's Note remain unnumbered for now. No other print-layout or manuscript changes were included in this pass. GitHub Actions print proof [#65](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42488083862) completed successfully at commit `14b93b4ab3de6e633311e54609c986e220444684`. Artifact `edrl-ii-print-preview-65` (ID `13620047392`) contains the generated PDFs. The successful build confirms PDF generation and upload; visual verification of the numbering in the artifact remains to be recorded separately.
- **9 November 2026** - Continued preparation of the paperback front matter after learning that Y. T. Vinayaraj's foreword had arrived as a Word document attached to an email. Established the handling plan: obtain the original attachment, inspect its text and paragraph structure, flag any apparent typographical issues for confirmation, and then incorporate the approved text in place of the existing Foreword placeholder in `ebook/edrl-ii/print/build.py`. The foreword is to retain the author's original wording and paragraph structure and appear before the Editor's Note and Contents. The preparation checklist was added to this page. No foreword text was inserted and no print build was run as part of this planning work.
- **10 November 2026** - Received the foreword by Y. T. Vinayaraj as a Word document attached to an email. Added a **Foreword preparation** checklist to this documentation page. The original document still needs to be obtained and inspected before the foreword is incorporated into `ebook/edrl-ii/print/build.py`; the checklist records the remaining review, inclusion and PDF-proofing steps.

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

The foreword by Y. T. Vinayaraj was received as a Word document and inspected on 11 November 2026. The original wording has been transcribed into the shared source file `ebook/edrl-ii/foreword.md`. No copy-editing or rewriting has been undertaken.

- [x] Receive the foreword from the author.
- [x] Obtain and inspect the original Word document.
- [x] Transcribe the foreword, retaining its paragraph sequence, poem, signature and two references.
- [x] Use the shared foreword source in the e-book and paperback print workflows.
- [x] Include the foreword before the Editor's Note and Contents.
- [x] Set the preliminary folios from the foreword onwards in Roman numerals; restart the essays at Arabic page 1.
- [x] Run the paperback print workflow. GitHub Actions run 70 completed successfully and uploaded the `edrl-ii-print-preview-70` proof artifact.
- [x] Run the e-book workflow. GitHub Actions run 146 completed successfully; the manuscript, EPUB package and PDF were generated and the automated package checks passed.
- [ ] Visually inspect the print and e-book proofs for text fidelity, poem layout, reference rendering, Roman-numeral folios and pagination. Automated build success is not a substitute for visual proofreading.

## Front-matter spacing and preliminary folios — 11 November 2026

The paperback proof showed two front-matter spacing defects: the Foreword heading sat too close to its opening paragraph, and the Editor's Note heading overlapped or crowded the draft-status notice. The preliminary page numbers were also set in uppercase Roman numerals, whereas the required style is lowercase Roman numerals.

The print builder is being adjusted as follows:

1. Add deliberate vertical space between the Foreword heading and its first paragraph.
2. Separate the Editor's Note heading, its "DRAFT VERSION — NOT YET FINALISED" notice and the opening paragraph with consistent vertical spacing.
3. Change preliminary folios to lowercase Roman numerals (i, ii, iii, iv, v, vi, and so on), retaining the restart at Arabic page 1 for the first essay.
4. Keep the foreword wording, poem, references, essay text, table treatment, cover and other page furniture unchanged.

The documentation update is committed separately from the print-builder change so that only the builder commit triggers a new paperback workflow run. The visual result must still be checked in the resulting PDF; the source change alone does not establish that the spacing is correct.

## Running heads, signatures and minimum type size — 11 November 2026

Paperback proof #71 was inspected visually. The revised Foreword heading-to-body spacing is satisfactory, the Editor's Note draft notice no longer overlaps its heading, and the preliminary folios appear in lowercase Roman numerals. These corrections are retained.

The next consolidated paperback update implements the agreed production direction from Herbert Paul's review and the subsequent clarification:

- First essay remains printed as page 1; this pagination change was already implemented on 8 November and is not being repeated.
- Even-numbered (left-hand) pages carry the book title in the running head.
- Odd-numbered (right-hand) pages carry the current essay title in the running head, except on a page where a chapter begins.
- Chapter-opening pages have no running head.
- Foreword attribution is right-aligned and expanded to Dr. Y. T. Vinayaraj, Director, Christian Institute for the Study of Religion and Society (CISRS), with the institute website.
- Editor's Note attribution is right-aligned as Tito Dutta, followed by 29 November 2026; the place name Kolkata is removed.
- Small text is not set below 8 pt. Existing larger sizes are retained where appropriate; undersized running heads, table text and small labels are raised rather than forcing every element to exactly 8 pt.

The global hyphenation proposal is not included in this update. It remains a separate decision because disabling hyphenation throughout may materially change justification and page texture. The existing Foreword and Editor's Note spacing corrections, lowercase Roman folios and first-essay Arabic pagination must remain intact.

The builder update is intended to trigger one paperback proof build. The generated PDF must be checked for running-head parity, blank chapter-opening headers, signature alignment, table fit after type enlargement, footnote legibility and preservation of the earlier front-matter corrections.
 
## Front-matter editorial copy and attribution — 11 November 2026

The print builder has been updated to prepare the Foreword and Editor's Note as finished front matter rather than provisional copy.

### Foreword attribution

The foreword signature is right-aligned and set as a separate line for each part of the author's name and institutional designation:

- Dr. Y. T. Vinayaraj
- Director,
- Christian Institute for the Study of Religion and
- Society (CISRS)

The institute's website address has been omitted from the print signature. The shared source file `ebook/edrl-ii/foreword.md` remains unchanged so that the e-book can apply its own digital treatment. The print builder replaces the source signature during print composition.

### Editor's Note and attribution

The draft-status notice, "DRAFT VERSION — NOT YET FINALISED", has been removed. The Editor's Note has been recast as finished editorial prose, retaining the documented publication history of the 2006 volume, the origins and archival purpose of The Sunil Abraham Project, the composition and publication history of the nine essays, and the continuing nature of the collection and preservation work.

The Editor's attribution is right-aligned and line-broken as follows:

- Tito Dutta
- Co-founder and Administrator
- The Sunil Abraham Project

The planned publication date, 29 November 2026, is retained above the attribution. The place name Kolkata is not included.

### Print-specific hyperlink treatment

The Foreword and Editor's Note are composed for a physical book. No active hyperlinks or clickable website labels are used in these signature blocks, and the CISRS website address has been removed from the foreword attribution. The e-book is a separate digital edition and may retain useful hyperlinks where appropriate; these print decisions must not be copied automatically into its output.

### Implementation and verification

The changes are confined to `ebook/edrl-ii/print/build.py`. The shared foreword source and original essay source pages have not been rewritten. The next paperback proof must be inspected to verify the line breaks, right alignment, paragraph spacing, front-matter pagination and the complete Editor's Note. A successful Typst build alone does not establish that the printed pages are correct.

### Correction: explicit signature line breaks — 11 November 2026

The first print proof showed that separate Typst text elements remained in the same paragraph and therefore flowed together on one long line. The signature blocks have now been corrected with explicit Typst line breaks; separate text elements alone are not sufficient.

The final intended print layout is:

**Foreword attribution (right-aligned):**

Dr. Y. T. Vinayaraj  
Director,  
Christian Institute for the Study of  
Religion and Society

The abbreviation "(CISRS)" and the institute's website address are omitted.

**Editor's attribution (right-aligned):**

Tito Dutta  
Co-founder and Administrator  
The Sunil Abraham Project

Each item is forced onto its own line in the print builder. This correction supersedes the earlier attribution description in this log. The generated paperback proof must still be visually checked to confirm the final rendered line breaks and spacing.

## Author biography for the paperback — plan and editorial scope — 11 November 2026

Sunil Abraham suggested including two biographies of A. M. A. Ayrookuzhiel in the book: a short biographical note on the back cover and a fuller biography within the preliminary pages. This entry records the plan for the longer, inside biography. The back-cover note is a separate piece of copy and will be prepared independently.

### Purpose and placement

The inside biography will introduce the author to readers before they begin the collected essays. It will appear after the Editor's Note and before the Contents. This creates a deliberate sequence: the Foreword introduces the intellectual significance of the work; the Editor's Note explains the history and purpose of the collection; the biography introduces the author; and the Contents lead into the essays.

### Length and format

- Target length: approximately 400–500 words.
- Heading: **About the Author**.
- Form: continuous, readable prose in a small number of paragraphs.
- No tables, publication grids, bullet-point chronology, references list or external links within the biography.
- The biography is an editorial narrative, not a compressed copy of the website's archival page and not an obituary.

### Content to retain

The narrative will draw on the existing author biography at `/amaa/index.md` and prioritise information relevant to understanding the author and his work:

1. His identity, dates and origins in Kerala.
2. His early formation and theological education in India and abroad.
3. His ministry in the United Kingdom and return to India.
4. His work at the Christian Institute for the Study of Religion and Society (CISRS), including his research and role as Associate Director.
5. His intellectual engagement with Dalit experience, caste, religious identity, popular religion, contextual theology and liberation.
6. Selected publications and the unfinished work on Dalit and Hindu religious identity, followed by his death in 1996.

### Material to omit or handle cautiously

The inside biography will not reproduce the website's family genealogy, detailed family chronology, tabular bibliography, article-by-article inventory, references or external links. It will avoid claims about influence, institutional history or intellectual priority that are not established by the source biography. Where the source gives only broad information, the book will retain that level of generality rather than supply guessed dates, institutions, qualifications or explanations.

### Relationship to the back-cover note

The back-cover biography will be approximately 70–100 words and will serve a different purpose: a concise introduction for prospective readers. It should not simply be a truncated version of the inside biography. The two texts should be consistent in facts and emphasis, but independently edited for their respective locations.

### Production status and verification

The longer biography is to be added to the print interior after the Editor's Note and before the Contents. Its final word count, paragraph flow, heading treatment and pagination must be checked in the generated A5 proof. The biography should be checked against `/amaa/index.md` for factual fidelity. The back-cover note remains a separate pending task.

### Inside biography added to print builder — 11 November 2026

The first draft of the longer biography has now been added to `ebook/edrl-ii/print/build.py` under the heading **About the Author**. It follows the Editor's Note and precedes the Contents, as specified in the plan above. A page break separates the Editor's Note from the biography and another separates the biography from the Contents; the biography itself may flow naturally across pages if required.

The draft is written as continuous prose in six paragraphs, without tables, bullet lists, references or hyperlinks. It follows the existing `/amaa/index.md` biography and covers Ayrookuzhiel's origins and education, ministry in the United Kingdom, work at CISRS, intellectual concerns, selected publications and unfinished manuscript. Family genealogy and detailed personal chronology have been left out. The text keeps broad source descriptions broad and does not add unsupported dates or qualifications.

The back-cover biography remains a separate, pending item. It is not included in this change.

**Verification still required:** inspect the generated A5 paperback proof for the biography's word flow, page count, heading and paragraph spacing, page breaks, and its transition to the Contents. Check every biographical statement against `/amaa/index.md`. This draft should not be treated as final until that proofread is complete.

### Approved author biography inserted — 11 November 2026

The editor-approved version of **About the Author**, supplied in the conversation on 11 November 2026, has replaced the earlier working draft in `ebook/edrl-ii/print/build.py`. The text is reproduced as approved, including the full-name usage, the description "theologian, scholar and researcher", the date range with spaces around the en dash, and the six-paragraph structure. No further stylistic rewriting was made during implementation.

The biography remains positioned after the Editor's Note and before the Contents. It is composed as continuous prose, with no table, list, references or hyperlinks. The separate short back-cover biography remains pending.

#### Pagination and proof requirements

The biography has been inserted into the existing preliminary matter; no folio numbers have been manually assigned or hard-coded for it. The existing preliminary-page numbering system is expected to continue in lowercase Roman numerals (i, ii, iii, iv, and so on), with Arabic numbering restarting at page 1 for the first essay. The added biography may increase the number of preliminary pages, so the next generated proof must be checked to confirm that Roman folios advance automatically, that the first essay still begins at Arabic page 1, and that the Contents page references and all subsequent pagination are correct.

The new A5 proof must also be visually inspected for the biography heading, paragraph spacing, page flow, blank-page behaviour and transition to the Contents. This implementation is not considered print-approved until the PDF itself has been reviewed.


## Critical incident: paragraph and text overlap in the paperback interior — 11 November 2026

### Summary

A serious composition defect appeared in the generated paperback PDF on 11 November 2026. Text from consecutive paragraphs overlaps vertically: the final line of one paragraph and the opening line of the next are printed at nearly the same vertical position. The defect is visible in the Foreword and is reported to affect the interior more broadly, including many pages across the book. It makes affected pages difficult or impossible to read and is a release-blocking production defect.

The problem was not present in the earlier series of paperback builds. More than 70 earlier workflow runs had been used during production without this particular paragraph-collision defect being reported. It appeared after changes were made to the print builder during the publication-details-page revision. The user's laptop restart occurred after the defect had appeared; there is no evidence that the laptop or a local machine restart caused it. The relevant changes were made in the repository's GitHub Actions build source.

**The current cause has not yet been conclusively isolated.** The incident must remain open until the exact source-level cause is demonstrated and a complete regenerated PDF has been inspected. A successful build status is not evidence that the layout is fixed.

### What the defect looks like

The supplied screenshots show the following symptoms:

- The end of a paragraph and the start of the next paragraph occupy overlapping vertical space.
- The problem occurs repeatedly at paragraph boundaries, rather than being limited to one isolated page or one particular paragraph.
- In the Foreword, the first paragraph ends with the sentence about studying religion in Rome and Oxford; the next paragraph begins with "His dedication to the study of religion..." at almost the same vertical position.
- A similar collision occurs later where a paragraph ending in "interfaith dialogue in India" is followed immediately by "The essays gathered in this volume...".
- The user reports that the problem affects the wider interior, with many pages showing the same behaviour.

The visible symptom is paragraph-to-paragraph collision. It must not be described merely as tight line spacing: lines within individual paragraphs may remain legible while separate paragraphs are placed on top of one another.

### Timeline of changes and investigation

1. **Earlier working state.** The paperback had gone through more than 70 earlier GitHub Actions builds. The user had not reported this repeated paragraph-overlap defect in those proofs.

2. **Publication-details revision.** During the revision of the publication and credits page, the print builder's global paragraph settings were changed from the previous body-text configuration to `leading: 1.2em` and `spacing: 8pt`. The publication page was also changed to remove the project-name heading and horizontal rules after the user objected to them. These changes were committed as part of the work leading to print build 88.

3. **Build 88.** The dedicated paperback workflow completed, but the PDF still showed the same paragraph collisions. This demonstrated that increasing the global line leading had not corrected the defect.

4. **Global block-spacing hypothesis.** The builder contained a global `#set block(spacing: 0.55em)` rule. It was removed as a possible contributor to block separation. The resulting proof still showed collisions. Removing this setting was therefore not a demonstrated fix.

5. **Paragraph show-rule experiment.** A global `#show par` rule wrapping paragraphs in blocks with a `below` spacing value was added as another attempted correction. The following proof still showed the defect. This experiment was subsequently removed. It must not be reintroduced without a clear, isolated test.

6. **Paragraph-spacing adjustment.** The global paragraph spacing was increased again, to 16 pt. This also did not establish a fix.

7. **Inspection of generated Typst content.** A temporary diagnostic print was added to the GitHub Actions build so that the Pandoc-generated Typst content for the Foreword could be inspected in the job log. The diagnostic output showed that ordinary paragraphs were separated by blank lines in the generated Typst text. The output did not show `#parbreak()` markers between those ordinary paragraphs. This matters because the earlier attempted replacement of `#parbreak()` did not target the paragraph separators actually present in the generated Foreword content.

8. **Explicit paragraph-gap experiment.** A post-processing step was then added to the Pandoc-generated Typst text. It uses a regular expression to find blank-line paragraph boundaries and insert an explicit `#v(10pt)` between paragraphs. This is an experimental intervention, not yet a verified solution. Its effect must be checked in the PDF, and its behaviour around headings, lists, quotations, footnotes, poems and other structured content must be examined before it is accepted.

9. **Latest diagnostic/build state.** The temporary diagnostic output and subsequent paragraph-boundary changes were committed during the investigation. The latest dedicated paperback workflow at the time of this entry is run **42966996529**. Its final PDF and visual result must be checked before the status of the experiment can be determined.

### What is known, and what is not yet known

**Established from the source and build logs:**

- The defect is in the generated print composition, not in the wording of the Foreword source.
- The Markdown source file `ebook/edrl-ii/foreword.md` contains normal paragraph breaks between the relevant paragraphs.
- The Pandoc-generated Typst content inspected in the workflow log represents those paragraphs as separate text paragraphs divided by blank lines.
- The earlier search-and-replace for `#parbreak()` did not match the ordinary paragraph separators shown in the diagnostic output.
- Increasing line leading, removing the global block-spacing setting and adding the tested global paragraph show rule did not, by themselves, resolve the visible collision.

**Not yet established:**

- The exact Typst layout mechanism responsible for the collision.
- Whether the fault is caused by the interaction of paragraph settings, a custom show rule, block layout, the Pandoc-generated Typst, or another surrounding layout construct.
- Whether the latest explicit `#v(10pt)` insertion fully fixes ordinary paragraphs.
- Whether that insertion has unwanted effects on non-paragraph structures or changes pagination elsewhere in the book.

Do not record any one of the attempted explanations as the confirmed root cause until a controlled test demonstrates it.

### Required recovery and verification procedure

The priority is to restore reliable paragraph flow without changing the approved wording or introducing new design changes.

1. Preserve the current source and diagnostic evidence so that the investigation can be reconstructed.
2. Compare the current print builder with the last known working version from before the publication-details revision. Use Git history to identify the exact changes introduced after that working state; do not guess at a rollback point.
3. Reproduce the defect with a minimal test containing two ordinary paragraphs, then compare the generated Typst source and PDF output with the last known working implementation.
4. Identify the specific rule or transformation that causes the second paragraph to begin at the wrong vertical position. Change one variable at a time.
5. Do not apply blanket regular-expression spacing changes to all generated Typst content unless tests demonstrate that headings, lists, block quotations, poems, footnotes, tables and other structures remain correct.
6. Once a correction is identified, generate the complete A5 interior through the dedicated paperback workflow. Do not use the editorial preview workflow as a substitute.
7. Inspect multiple pages from the Foreword and every essay, especially pages with consecutive paragraphs, headings, quotations, footnotes, lists, tables and page breaks. Check both the beginning and end of the book.
8. Compare the regenerated PDF with the supplied defective proof. Confirm that no paragraph collisions remain and that the correction has not introduced excessive gaps, missing text, new overlaps, blank pages or pagination errors.
9. Only after this inspection should the production log mark the incident resolved. A green GitHub Actions status alone is insufficient.

### Scope control and safeguards

Until this incident is resolved:

- Do not make further cosmetic changes to the publication-details page, running heads, title typography or other front-matter design unless required to diagnose the defect.
- Do not alter the original essay or Foreword wording to compensate for a layout problem.
- Do not change the EPUB source or e-book styling as part of this print-only investigation.
- Keep diagnostic logging temporary and remove it after the cause has been identified.
- Record each experimental source change, commit and workflow run in this section, including whether the generated PDF passed or failed visual inspection.
- Do not ask the user to re-upload the same PDF or screenshots when the existing files and repository build artefacts are available.

**Current status: OPEN — critical, unresolved.** The paperback interior must not be approved or sent for printing until the paragraph-overlap defect has been conclusively corrected and the complete PDF has passed visual inspection.

### PDF overlap-check false positives corrected — 11 November 2026

The dedicated EDRL II print workflow was failing after PDF generation because the automated `check_pdf_overlaps()` function reported six possible line collisions on pages 176 and 178. The build log showed that the failure came from the validation check, which compared the vertical starting positions (`yMin`) of text lines and flagged pairs whose starts were closer than 0.8 times the line height.

That test was too broad: two normally spaced consecutive lines can have nearby starting positions without their text bounding boxes actually intersecting. The six detections were therefore possible false positives, not proof that the PDF contained six actual text collisions. The workflow stopped with exit code 1 at this check.

**Correction made:** `check_pdf_overlaps()` in `ebook/edrl-ii/print/build.py` now compares the horizontal and vertical intersection of the two line bounding boxes. It reports a collision only when the boxes overlap horizontally by more than 1 point and vertically by more than 1 point. The previous proximity-based comparison of `yMin` values has been removed.

The change is limited to the automated PDF validation logic. No manuscript text, footnotes, typography, paragraph spacing, page dimensions, margins or layout settings were changed as part of this correction.

**Implementation:** commit `728eb658e872364f78c7e77031cf1a0f851638c4` in `ebook/edrl-ii/print/build.py`.

**Build result:** the dedicated **EDRL II print proof** workflow completed successfully on this commit: [GitHub Actions run 42970201063](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42970201063).

**Status and distinction:** the false-positive failure in the automated overlap checker is corrected, and the workflow is green. This does not by itself establish that every visual text or paragraph overlap in the generated book has been resolved. The earlier critical incident concerning visible paragraph collisions remains a separate visual-proofing issue and must not be marked resolved solely because this automated check now passes. The generated PDF still requires visual inspection before print approval.


## Stable recovery checkpoint — 11 November 2026

The current print-production source is being recorded as a **stable recovery checkpoint**. This is a deliberate preservation point, not a declaration that the paperback is finished, fully proofread or ready for printing.

**Checkpoint commit:** `11b45f870dab5c5ef25e826b00fcd270e851b4f7`  
**Print builder:** `ebook/edrl-ii/print/build.py`

This checkpoint preserves the current implementation as a known point to which the project can return if subsequent editing reintroduces paragraph collisions, overlapping text, pagination faults or other layout regressions. Further editorial corrections and formatting improvements may continue on the working branch. They must not overwrite or replace this recovery point.

The checkpoint is intentionally distinct from final publication approval:

- It is a source-code recovery point, not a claim that every editorial or formatting issue has been resolved.
- The known paragraph-overlap investigation remains open. The automated overlap check and a visual inspection are separate checks; passing one does not establish that the other has passed.
- The latest footer correction changes the preliminary-page footer from Typst content-block syntax to executable context code. Its generated PDF still requires a fresh build and visual inspection.
- Future changes should be compared with this checkpoint when a regression is suspected. If necessary, the relevant source files can be restored from this exact commit without discarding later editorial work wholesale.

**Status: STABLE RECOVERY CHECKPOINT — further editing permitted; final proof and print approval pending.**


## Editorial and production suggestions from Sunil — 11 November 2026

The following suggestions were communicated by Sunil on 11 November 2026. They are recorded here as a checklist for consideration and follow-up.

- [x] **No images inside the book.** Images would make print production more complicated.
- [x] **No glossary.** Definitions are not available.
- [ ] **Subject index.** Consider an alphabetical index of names, subjects and important terms, with references to the pages on which they appear.
- [ ] **Automated subject indexing.** Ideally, AI should help build dedicated software to generate the index. The index should not be compiled manually by an LLM.
- [ ] **Future editions.** The subject index may be considered for a future edition; it should not require manual effort for the current production.
- [ ] **Book-production auditing software.** Develop software to audit the book and identify production problems.
- [ ] **Graphic design review.** Review pages from a graphic designer's perspective. Vision-capable LLMs may assist with this review.
- [ ] **Title line break.** Consider arranging the title as:  
  `Essays on`  
  `Dalits, Religion and Liberation - II`
- [x] **Author's name.** Removed "Dr." from references to A. M. Abraham Ayrookuzhiel in the Foreword, as requested. The honorific for Dr. M. M. Thomas is retained.
- [ ] **Cover credit.** Add "Cover Design: Tito Dutta".
- [ ] **Copyright notice.** Include a copyright notice consistent with the original publication.


## Signature spacing and editor date placement — 11 November 2026

The next paperback proof showed that both front-matter signature blocks had excessive vertical separation between their lines, making the attributions look disconnected.

The print builder has been corrected:

- The date has been removed from above Tito Dutta's name. It now appears as the final, smaller line after "The Sunil Abraham Project".
- The editor's name, designation, project name and date are arranged as one compact, right-aligned stack with controlled 2 pt spacing.
- Dr. Y. T. Vinayaraj's name, designation and two-line institutional name are also arranged as one compact, right-aligned stack with controlled 2 pt spacing. His name is set slightly larger and bold.
- The wording and institutional attribution have not otherwise been changed.

Implementation: commit `b173ac3a88a57b03b50adc96fb01bb573643e9e0` in `ebook/edrl-ii/print/build.py`.

The next generated A5 proof must be checked to confirm that the stack spacing renders as intended and that neither signature is split across pages. The source change is committed; visual verification remains pending.


## Pambatti Cittar epigraph page — 11 November 2026

A dedicated, unnumbered epigraph page has been added to the paperback interior, after the publication-details page and before the Foreword. It contains only the four-line passage reproduced in A. M. Abraham Ayrookuzhiel's deposited essay `amaa/dalits-challenges-religious-systems-full-text.md`, with its source attribution.

The wording is retained exactly:

> We'll set fire to divisions of caste,  
> We'll debate philosophical questions in the market place;  
> We'll have dealings with despised households,  
> We'll go around in different paths.

Attribution: *Cittar Gnanakkovai*, Pambatti Cittar, verse 123. Only the collection title is italicised. The page has no heading, running header, footer or printed folio. It precedes the Roman-numbered preliminary matter; the Foreword's Roman folio sequence must be checked in the next proof.

Implementation: commit `66b69ed0366c64191c854e5974b1f25c197c2c99` in `ebook/edrl-ii/print/build.py`.

Visual verification is pending the next dedicated print build. Confirm that the four lines retain their line breaks, the attribution is correctly aligned, the page has balanced white space, and Roman preliminary numbering begins as intended.


## Epigraph refrain restored — 11 November 2026

The epigraph has been revised to reproduce the full selection shown in the memorial document. The opening refrain, "So dance snake, dance!", was inadvertently omitted in the first implementation. It has now been restored as the opening line, followed by the four lines on caste divisions, philosophical debate, dealings with despised households and different paths.

The source essay presents this refrain in the preceding Pambatti Cittar verse sequence (footnote 19) and cites the final four lines separately to *Cittar Gnanakkovai*, verse 123 (footnote 20). The print epigraph follows the memorial document's combined presentation. Retain this distinction when checking the final source note and do not imply that the entire five-line selection is independently verified as a single verse without checking the underlying edition.

Implementation: commit `d8266cd5a597df7d10913b3880c4592ee23ecbc7` in `ebook/edrl-ii/print/build.py`. The dedicated print workflow is triggered by the source change. Visual verification remains pending.


## Author portrait plate — 11 November 2026

A full-page portrait of A. M. Abraham Ayrookuzhiel has been added to the paperback interior. The image is maintained in the companion media repository at `amaa/a-m-a-ayrookuzhiel-print-book-photo-01.png` and is fetched by the print builder at build time; it is not duplicated in the TSAP repository.

The portrait is placed immediately after the publication-details page and before the Pambatti Cittar epigraph. It is a standalone photographic plate, centred and scaled proportionally to fit the A5 text area. It has no caption at this stage because the year and occasion have not yet been confirmed by the family.

The photographic plate is intentionally unnumbered: it has no running head, footer or Roman-numeral folio. Roman preliminary pagination begins with the Foreword after the epigraph, and the main text retains its existing Arabic page 1 restart.

Implementation: print builder commit ec86da5cd7062906b31ffe15da59a05b38238bf8. The dedicated paperback print workflow must be checked for image retrieval, successful compilation, page sequence and visual fit. The original source photograph remains in the media repository; no separate compressed copy is stored in the print repository.


## Epigraph and biography typography corrections — 11 November 2026

The paperback builder has been corrected after review of the generated proof:

- The five epigraph lines now use explicit Typst `#linebreak()` commands rather than backslash-based line-break notation. This prevents backslashes from appearing in the printed poem and preserves each intended line as a separate line.
- The epigraph attribution now begins with an em dash. The collection title is italicised, followed on the next line by "Pambatti Cittar, verse 123."
- The three book titles in **About the Author** are now marked with Typst italic syntax (underscores), not asterisks, which Typst interprets as bold. The titles should therefore appear in italics rather than bold.

Implementation: commit `67cc1623f7b3ff1d067246a2937e7c870f2df1e5` in `ebook/edrl-ii/print/build.py`. The dedicated paperback workflow must be checked to verify the rendered line breaks, attribution and italic book titles. No source essay wording has been changed.

## Initial paperback back-cover design — 11 November 2026

An initial visual design for the back cover of *Essays on Dalits, Religion and Liberation II* has been prepared. It follows the front cover's visual identity: a warm parchment-coloured background, dark serif typography, restrained maroon rules and a solid maroon footer.

The current concept contains these elements:

- The book title at the top, arranged over two lines in a consistent serif style.
- A short description of the volume's essays and their engagement with Dalit life, religion, caste, popular traditions and liberation.
- An **About the Author** section, combining a short biographical note with the supplied archival portrait of A. M. Abraham Ayrookuzhiel. The portrait is used without facial retouching or reconstruction.
- A white retail barcode label in the lower-right area. The hyphenated paperback ISBN, **978-93-345-8524-7**, is centred above the EAN-13 bars; the unhyphenated digits are printed below the bars.
- The printed price, **₹250**, immediately below the barcode label.
- A maroon footer band with **The Sunil Abraham Project** on the left and https://sunilabraham.in on the right.

The EAN-13 symbol in the current proof was decoded programmatically as **9789334585247**, matching the allotted paperback ISBN. This confirms that the encoded number is correct; it does not replace a physical scan test of the final, printer-sized barcode.

This is an initial back-cover design, not the final full-wrap cover PDF. The title scale, barcode-label margins and overall spacing remain subject to final proofing. The spine width, bleed, trim and full-wrap dimensions must be set only after the printer supplies the cover template and the final interior page count and paper specification are confirmed. The barcode must be scan-tested at final print size before the cover is approved.



## Preliminary running heads and Roman-numeral blank page — 11 November 2026

The running-head treatment has been revised in response to the latest proof review.

- From the Foreword through the Editor's Note, every page of **About the Author**, the Contents and the intervening blank page, the book title and chapter title are removed from the top running head.
- The horizontal rule is retained on these preliminary pages.
- The existing running-head treatment for the essays is retained. Chapter-opening pages continue to follow their existing design; subsequent essay pages retain the established alternating book-title and chapter-title headers.
- **About the Author** is explicitly excluded from the list of essay chapters used to determine running heads. This prevents its heading from being mistaken for a chapter title.

The blank page immediately before the first essay remains intentional. The transition to Arabic main-text pagination has been moved until after that blank page, so it remains part of the Roman-numbered preliminary matter. Its folio should therefore display as a Roman numeral (for example, XIII), not Arabic "13". The first essay's Arabic pagination is still reset to 1.

**Implementation:** commit `fcda4ea5362af6c45b35f47f448e44181ea41d33` in `ebook/edrl-ii/print/build.py`.

**Verification pending:** the dedicated EDRL II print proof workflow has been queued for this commit. Inspect the Foreword, Editor's Note, both pages of About the Author, Contents, the blank page and the first essay opening. Confirm that the preliminary pages show the horizontal rule without a running title, that the blank page carries the correct Roman folio XIII, and that the essay running heads and Arabic page 1 restart remain unchanged. Do not treat the source change as visually verified until the generated PDF has been inspected.

## Indexing and PDF production-auditing software — 11 November 2026

This section records the software investigation arising from Sunil's editorial and production suggestions. It distinguishes two separate requirements: software for preparing a subject index, and software for auditing the finished paperback PDF. These tools have different purposes and should not be treated as interchangeable.

The preferred working environment is **Ubuntu/Linux**. Native Linux applications and command-line tools should be preferred. A Windows-only application should not be selected merely because it is established or widely used. **OpenCindex/Cindex is not being considered for this project.**

### 1. Subject-indexing software

Sunil's suggestion is to consider an alphabetical subject index of names, subjects and important terms, with references to the pages on which they appear. He also suggested that AI could assist in developing dedicated software, but that the index should not be compiled manually by an LLM. The index may be considered for a future edition; it should not create manual indexing work for the current production.

Indexing software generally helps an indexer compose, arrange, alphabetise, format and edit index entries. It does not necessarily identify the important subjects in a book automatically. The editorial decision about what deserves an entry, which terms should be grouped, and which cross-references are meaningful remains a separate task.

#### Picardy — first Ubuntu candidate

**Cost:** Free of charge (freeware).  
**Platform:** Windows, macOS and Linux, according to the American Society for Indexing's software directory.  
**Purpose:** Editing and formatting back-of-the-book indexes.

Picardy allows an indexer to record indexable terms, names and concepts together with page references and cross-references. It then alphabetises, collates and formats those entries for incorporation into a published book.

It does **not** ingest the text of a book and independently produce a subject index. Its role is to manage and format entries that have been selected during the indexing process.

**Why it is relevant:** It is the first candidate to test on Ubuntu because it is free, is listed as supporting Linux, and is specifically intended for back-of-the-book indexes.

**Proposed action:** Obtain the software from its publisher, test it on Ubuntu, and check whether its output can be incorporated into the Typst print workflow.

References:
- [American Society for Indexing — Software directory](https://asindexing.org/reference-shelf/software/)
- [Picardy — Help and description](https://picardy-indexing.ca/online-help/)

#### Index Manager — commercial alternative

**Cost:** Commercial product; a 14-day trial is advertised.  
**Platform:** Windows and macOS; Linux support is listed as available on request.  
**Purpose:** Professional index management, including embedded-index workflows.

Index Manager supports the management of index entries and provides add-ons for transferring entries between document versions and importing an existing index into a document. These facilities may be useful where an index must be embedded in a publishing file or transferred after layout changes.

**Why it may be relevant:** It is a possible advanced alternative if Picardy does not provide the required workflow.

**Important limitation:** "Linux on request" does not establish that a standard Ubuntu installer is publicly available. Before considering purchase, contact the vendor to confirm the Linux package, compatibility with the Ubuntu version in use, supported features, licence terms and total cost.

References:
- [Index Manager — Download and system requirements](https://index-manager.net/en/download-en/)
- [Index Manager — Pricing and requirements](https://index-manager.net/en/prices/)

#### xindy — free index processor

**Cost:** Free software.  
**Platform:** Linux and other systems supported by the TeX ecosystem.  
**Purpose:** Sorting, merging and formatting index entries supplied to it.

xindy processes index entries that have already been marked or supplied. It can apply sorting and language rules and produce formatted index output.

It does not read a book and decide which names, subjects or concepts should be indexed. It is a technical index processor rather than a full graphical indexing environment.

**Why it may be relevant:** It could be useful if indexing is integrated into a source-marked or TeX-oriented typesetting workflow. It is not the first choice for a standalone index-editing interface.

References:
- [Ubuntu man page — xindy](https://manpages.ubuntu.com/manpages/focal/man1/texindy.1.html)
- [CTAN — xindy package](https://ctan.org/pkg/xindy)

#### MakeIndex — free index processor

**Cost:** Free software.  
**Platform:** Linux and other systems supported by TeX distributions.  
**Purpose:** Sorting and formatting supplied index entries.

MakeIndex processes entries supplied in an index file. It can arrange entries and subentries according to a style definition and produce index output.

It does not automatically discover subjects in a manuscript and does not replace editorial selection of index terms.

**Why it may be relevant:** It is an established option for a LaTeX-style source and typesetting workflow. It is a technical processor, not the preferred standalone interface for this project.

Reference:
- [MakeIndex manual](https://man.archlinux.org/man/makeindex.1.en)

#### Subject-indexing recommendation

1. Test Picardy on Ubuntu first.
2. Assess whether its output can be incorporated cleanly into the Typst book.
3. If Picardy is insufficient, contact Index Manager about an actual Ubuntu/Linux version and its price.
4. Consider xindy or MakeIndex only if the project adopts a source-integrated indexing workflow.
5. Do not use OpenCindex/Cindex.

No decision has yet been made to produce a subject index for the current paperback. The existing direction from Sunil is that it may be considered for a future edition and should not create manual work for the current production.

### 2. PDF production-auditing and inspection software

The paperback is a fixed-page A5 PDF. A successful Typst build confirms that the source compiled; it does not establish that the PDF is visually correct or technically acceptable to the printer. The following tools inspect different aspects of the generated PDF.

#### callas pdfToolbox CLI — professional print preflight

**Cost:** Commercial; a 14-day trial is advertised.  
**Platform:** Linux, Windows and macOS for the CLI/server product. The desktop graphical application has different platform availability.  
**Purpose:** Automated PDF analysis, correction and print-production preflight.

The CLI can analyse PDF objects, apply preflight profiles, and identify technical issues involving such matters as fonts, colour, images, transparency and page geometry. Depending on the operation and profile, it can also correct or enhance PDF files and can be integrated into automated workflows.

**Why it is relevant:** It is the professional-grade candidate for checking whether the final PDF meets defined print-production requirements before it is sent to the printer.

**Important qualification:** The printer's own specifications must determine the preflight checks. Do not assume that a generic profile is sufficient. The relevant Linux product is the CLI/server, not the Windows/macOS desktop interface.

**Proposed action:** Evaluate the Linux CLI during the trial after the printer's specifications are available. Purchase only if it provides useful checks beyond the free tools and the cost is justified.

References:
- [callas — pdfToolbox CLI installation and activation](https://hilfe.callassoftware.com/m/59504/l/665202-installation-and-activation-of-pdftoolbox-server-cli)
- [callas — pdfToolbox system requirements](https://callassoftware.com/products/pdftoolbox/system-requirements/)
- [callas — pdfToolbox product information](https://callassoftware.com/products/pdftoolbox/)

#### veraPDF — PDF standards validation

**Cost:** Free and open source.  
**Platform:** Java application; usable on Linux/Unix, Windows and macOS with a suitable Java installation.  
**Purpose:** Validation against PDF/A archival and PDF/UA accessibility standards.

veraPDF checks whether a PDF conforms to defined requirements in the supported PDF/A and PDF/UA specifications. It produces validation reports identifying rules that pass or fail. For PDF/UA, the software can perform machine-verifiable checks; it cannot replace human accessibility evaluation.

**Why it is relevant:** It can provide a separate standards-based validation report and reveal certain structural, metadata and accessibility-conformance problems.

**Important limitation:** PDF/A and PDF/UA validation is not the same as commercial print preflight. Passing veraPDF does not establish that the book is ready for the printer. Use it when the relevant archival or accessibility conformance target is intended; do not treat every profile as a mandatory print requirement.

References:
- [veraPDF — Validation](https://docs.verapdf.org/validation/)
- [veraPDF — Installation](https://docs.verapdf.org/install/)
- [Open Preservation Foundation — veraPDF overview](https://openpreservation.org/tools/verapdf/)

#### qpdf — PDF structural integrity

**Cost:** Free and open source.  
**Platform:** Linux/Ubuntu and other major operating systems.  
**Purpose:** Checking the internal structure and syntax of a PDF.

qpdf can check PDF structure and report problems involving syntax, encryption, linearisation and encoded streams. Its command-line exit status can be used in automated scripts.

**Why it is relevant:** It is a basic first-stage check to establish that the generated PDF is structurally readable and syntactically sound.

**Important limitation:** qpdf explicitly does not validate the actual visual page content or its semantic correctness. A PDF can pass qpdf and still contain overlapping paragraphs, clipped text, misplaced headings or other visual defects.

Reference:
- [qpdf — Command-line manual](https://github.com/qpdf/qpdf/blob/main/manual/cli.rst)

#### Poppler — PDF inspection and rendering utilities

**Cost:** Free and open source.  
**Platform:** Linux/Ubuntu and other major operating systems.  
**Purpose:** Inspecting PDF properties, extracting text and fonts, and rendering pages.

The Poppler utilities are useful for different checks:

- `pdfinfo` reports page count, page dimensions, metadata and other document properties.
- `pdffonts` lists fonts used in the PDF and indicates whether they are embedded.
- `pdftotext` extracts text for content and page-by-page checks.
- `pdftoppm` and `pdftocairo` render PDF pages into images for visual inspection.
- `pdfimages` extracts images embedded in the PDF.

**Why it is relevant:** These utilities allow us to inspect the actual output: page dimensions, font embedding, extracted text and rendered pages. Rendered pages can be examined individually or assembled into contact sheets for a visual review.

**Important limitation:** Poppler is an inspection and rendering toolkit, not a complete automated print-production auditor. It does not decide whether the book's typography and page design are professionally satisfactory.

References:
- [Poppler project](https://poppler.freedesktop.org/)
- [Poppler utilities — package overview](https://packages.debian.org/stable/poppler-utils)

#### Python and PyMuPDF — foundation for our own book-production auditor

**Cost:** PyMuPDF is available under open-source and commercial licensing terms; the applicable licence must be checked for the intended use.  
**Platform:** Python on Linux/Ubuntu and other supported platforms.  
**Purpose:** Programmatic inspection of PDF text, coordinates, fonts, images and page geometry.

PyMuPDF exposes text blocks, words, their bounding boxes and font information. It can also inspect page dimensions, embedded images and image locations, vector drawings and other page elements.

We could develop a project-specific auditing programme around it. Proposed checks include:

- Text extending outside the intended page area.
- Potential overlaps between text blocks or line bounding boxes.
- Text or paragraphs that appear clipped.
- Unexpectedly empty pages.
- Inconsistent page dimensions.
- Expected page sequence and pagination.
- Running-head and footer regions.
- Expected text appearing on expected pages.
- Missing, unexpected or poorly placed images.
- A report identifying the page number and coordinates of each suspected issue.
- Rendered page images or contact sheets for visual review.

**Why it is relevant:** The production has already encountered paragraph-overlap and layout problems. A generic PDF validator cannot understand every book-specific rule. We can build checks around the actual A5 page design, folios, running heads, footers, page sequence and Typst output.

**Important limitations:** This is a development project, not an already completed auditing application. Geometric checks can produce false positives and must be reviewed. PyMuPDF cannot replace human proofreading or visual design judgement.

**Proposed action:** Begin with a small, read-only audit programme. It should inspect and report problems without modifying the production PDF. Add checks incrementally and test each one against known-good and known-defective pages.

References:
- [PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/)
- [PyMuPDF text extraction and bounding-box FAQ](https://pymupdf.readthedocs.io/en/latest/faq/index.html)
- [PyMuPDF page and image inspection](https://pymupdf.readthedocs.io/en/latest/page.html)

### 3. What the PDF tools do — and do not do

| Tool | Main purpose | What it does not establish |
|---|---|---|
| callas pdfToolbox CLI | Professional print preflight against configured requirements | Does not replace visual/editorial approval |
| veraPDF | PDF/A and PDF/UA standards validation | Is not a complete commercial print preflight |
| qpdf | PDF structural and syntax integrity | Does not inspect visual layout |
| Poppler | Page information, fonts, text extraction and rendering | Is not a complete automated quality auditor |
| Python + PyMuPDF | Custom book-specific text, geometry and layout checks | Does not replace human visual judgement |

These tools are complementary. We do not need to purchase or deploy all of them.

### 4. Why these checks are needed at this production stage

The project is preparing a fixed-page A5 paperback PDF that will eventually be supplied to the printer. A defect discovered after printing may be expensive to correct. The checks should therefore be organised in layers:

1. **Structural integrity:** Is the PDF internally sound? Use qpdf.
2. **Document properties:** Are page count, dimensions, metadata and fonts correct? Use Poppler.
3. **Standards validation:** Does the PDF meet a relevant archival or accessibility standard, if one is required? Use veraPDF.
4. **Print preflight:** Does the PDF meet the printer's technical specifications? Evaluate callas pdfToolbox CLI.
5. **Book-specific layout audit:** Are there overlaps, clipped text, unexpected blank pages, pagination errors or other defects? Develop the PyMuPDF-based auditor.
6. **Visual design review:** Does the book look professionally typeset when pages and spreads are inspected? Human review remains essential. A vision-capable LLM may assist by flagging suspicious pages, but it must not replace human approval.

A successful Typst build alone is not proof of a satisfactory printed book.

### 5. Recommended Ubuntu-first evaluation sequence

1. Obtain the printer's PDF, trim, bleed, binding, colour and other production specifications.
2. Test Picardy on Ubuntu for the possible subject-index workflow.
3. Use the free PDF inspection tools: qpdf, Poppler and veraPDF where its standards checks are relevant.
4. Begin a read-only, book-specific PDF audit programme using Python and PyMuPDF.
5. Evaluate callas pdfToolbox CLI on its trial only after the printer's requirements are available.
6. Generate a fresh paperback proof.
7. Run the automated checks and retain their reports with the proof.
8. Render and inspect the pages and facing-page spreads.
9. Correct defects in the Typst source and rebuild.
10. Obtain human approval before supplying the PDFs for printing.

### 6. Current decisions and status

- Ubuntu/Linux is the preferred environment for this work.
- OpenCindex/Cindex is excluded from consideration.
- Picardy is the first subject-indexing candidate to test on Ubuntu; it has not yet been installed or tested in this project.
- Index Manager is a possible commercial alternative, but its Linux availability must be confirmed with the vendor.
- xindy and MakeIndex are free technical index processors, not automatic subject-discovery tools.
- qpdf, Poppler and veraPDF are candidates for complementary PDF checks; installation and testing in this production workflow remain pending.
- callas pdfToolbox CLI is a commercial Linux preflight candidate; no purchase decision has been made.
- Python + PyMuPDF is the proposed foundation for a custom book-specific auditor; development has not yet begun.
- Human visual proofing remains mandatory.
- No subject index has been committed to the current paperback. The recorded direction is to consider it for a future edition without creating manual work for this production.
- No software listed in this section should be described as installed, tested or approved until that work has actually been completed.

## Incident report: disruption of the EDRL II automated print build — 11 November 2026

### Summary

On 11 November 2026, the previously working automated PDF production process for *Essays on Dalits, Religion and Liberation II* was disrupted during a series of substantial changes to the print builder and its GitHub Actions workflow.

The Python builder (`ebook/edrl-ii/print/build.py`) underwent extensive revisions, affecting significant parts of the document-generation and PDF-production process. The workflow was also revised to accommodate the changed builder and its installation and dependency requirements. Subsequent attempts moved between different versions of the builder and workflow, including attempts to return to an earlier working implementation.

This sequence did not restore a consistently working production process. Several builds failed, and the project temporarily lost its dependable ability to generate fresh, downloadable PDF proofs after manuscript or layout changes.

The last confirmed successful build in this sequence was **GitHub Actions run #109**, which generated the interior PDF, front-cover proof and combined review PDF. Later attempts did not consistently reproduce that result.

### What happened

1. **Previously working production process.** The EDRL II print workflow had completed more than 100 runs during development. Run #109, on 11 November 2026, completed successfully. It installed the required tools and dependencies, executed the Python builder, generated all three PDF outputs and uploaded them as a downloadable GitHub Actions artifact.

2. **Extensive builder revisions.** Significant portions of `build.py` were subsequently rewritten. These revisions changed parts of the build process and introduced or altered the technical requirements of the builder. The workflow consequently needed corresponding changes to its setup, installation and dependency-management steps.

3. **Workflow and dependency changes.** Different approaches were tried for installing Typst, setting up Python, managing Python packages and installing system-level packages. The workflow was no longer simply executing the same established sequence used by the last successful build. It had become dependent on a revised set of setup and installation steps.

4. **Movement between builder versions.** After the revised implementation failed to produce a dependable result, attempts were made to return to an earlier builder and workflow. Further changes were then made to the workflow during recovery. As a result, the source files on the working branch did not consistently match the last known successful production configuration.

5. **The significance of a GitHub-hosted runner.** GitHub Actions uses temporary, newly provisioned Ubuntu runners. Software installed during one workflow run is not permanently retained for the next run. Therefore, even when the source code is restored to an earlier version, the packages installed during a previous successful run are not automatically available. The workflow must install its required tools and dependencies again, unless an explicitly configured cache or another persistent distribution mechanism supplies them.

6. **Ubuntu package-server DNS failure.** In run #115, the workflow reached the system-dependency installation step but could not download the required Ubuntu packages. The runner repeatedly reported:

   `Temporary failure resolving 'azure.archive.ubuntu.com'`

   The affected packages included Pandoc, Pandoc data, Linux Libertine fonts and Poppler utilities. The installation ended with exit code 100. The Python builder was never executed, and no PDF artifact was generated in that run.

   This was a package-server DNS/network resolution failure on the GitHub-hosted Ubuntu runner. It was not evidence of a defect in the manuscript or in the Linux Libertine font.

7. **A separate workflow-configuration failure.** Run #116 failed at the Python setup stage for a different reason. The workflow attempted to enable pip dependency caching, but GitHub Actions could not find a `requirements.txt` or `pyproject.toml` file in the repository. The setup step therefore failed before the system-package installation and PDF build steps could run. The later steps, including PDF generation and artifact upload, were skipped.

### Why restoring the older builder did not automatically restore the working process

Restoring an earlier Python file does not, by itself, restore the entire production environment.

The successful build depended on a combination of:

- The correct version of `build.py`.
- The matching GitHub Actions workflow.
- A compatible Python environment and its required packages.
- Pandoc and its supporting data.
- Typst.
- Linux Libertine fonts.
- Poppler utilities used by the PDF-production process.
- Successful access to the external package repositories and download sources.

These components must work together. A builder restored from an earlier commit can still fail if the workflow surrounding it has changed, if the dependency setup is different, or if the newly provisioned runner cannot reach the package repositories.

The previous successful installation was not stored permanently on GitHub's runners. Every new run had to provision its environment again. Consequently, the fact that run #109 installed the required packages successfully did not guarantee that a later run would be able to download the same packages.

### Build history and confirmed outcomes

| Run | Date, 11 November 2026 | Outcome | Significance |
|---|---|---|---|
| #109 | 13:18 UTC | Successful | Last confirmed successful build in this sequence. All three PDFs were generated and uploaded. |
| #110 | 15:01 UTC | Failed | Build attempt after the builder and workflow revisions. |
| #111 | 15:23 UTC | Failed | Build attempt using the revised workflow. |
| #112 | 15:26 UTC | Cancelled | Build attempt cancelled during the recovery sequence. |
| #113 | 15:38 UTC | Failed | Subsequent recovery attempt. |
| #114 | 15:38 UTC | Failed | Subsequent recovery attempt. |
| #115 | 15:52 UTC | Failed | Ubuntu package installation failed because the runner could not resolve `azure.archive.ubuntu.com`. |
| #116 | 15:54 UTC | Failed | Python pip caching setup failed because no dependency manifest (`requirements.txt` or `pyproject.toml`) was found. The PDF build and upload steps were skipped. |

The successful artifact from run #109 was retained and downloaded as a fallback. It contains the three PDFs generated by that successful build, but it does not include any editorial or layout changes committed after that run.

### Current impact

The principal impact is a disruption to the editorial production cycle. The book requires further corrections and layout revisions, and each revision must be followed by a fresh PDF build so that the resulting pages can be inspected.

At present, a source-file edit can be committed to the repository, but the project cannot treat the automated build as dependable until the complete builder and workflow combination has been verified again. A failed workflow means that no fresh downloadable artifact is available for that revision.

The last successful PDF remains useful as a reference and fallback, but it cannot substitute for a newly generated proof containing subsequent changes.

### Recovery requirements

The recovery should prioritise restoring a reproducible build rather than introducing another redesign of the print system.

1. Establish the exact builder and workflow versions associated with the last confirmed successful build.
2. Compare the current files with those versions and identify all differences before making further changes.
3. Restore a matching builder-workflow combination, preserving the established book layout and production logic.
4. Ensure that the workflow can install its required dependencies on a newly provisioned Ubuntu runner.
5. Avoid dependency-caching configuration that assumes a `requirements.txt` or `pyproject.toml` file unless the corresponding manifest is deliberately added and maintained.
6. Address temporary package-server failures without changing the manuscript or typesetting logic.
7. Execute a complete build and confirm that the interior, front-cover proof and combined review PDF are all generated.
8. Confirm that the artifact-upload step succeeds and that the files can actually be downloaded.
9. Only after this end-to-end test should further editorial and layout revisions resume through the automated production workflow.

### Status

**Production disruption: OPEN.**

Run #109 remains the last confirmed successful build and its PDFs have been preserved as a fallback. Runs #115 and #116 demonstrate two separate infrastructure and workflow-configuration failures. The project must re-establish a verified, repeatable build-and-download process before relying on GitHub Actions for the remaining paperback corrections.

The recovery is not complete merely because the source files have been reverted or a workflow reports that it has started. Completion requires a successful build of the current manuscript, successful upload of the resulting PDFs, and confirmation that the new artifacts are downloadable.


### Historical baseline: first complete successful build on 6 November 2026

The first complete successful run of this Typst-based EDRL II print workflow was **GitHub Actions run #4 on 6 November 2026**. It completed all stages, including Python dependency installation, installation of Pandoc, Typst and fonts, PDF generation and artifact upload.

**Successful run:** [EDRL II print workflow — run #4, 6 November 2026](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/42189828557)

The run is an important reference because it demonstrates that the repository's print-production approach and its required tools were capable of producing and uploading the PDF successfully. The later successful run #109 on 11 November was another confirmed success, and remains the last successful build immediately before the failures recorded in this incident.

### Why subsequent builds have not consistently succeeded

The available run logs do not establish one single cause. They show at least two distinct failures in the recovery attempts:

- **Runner network/DNS failure (run #115):** the Ubuntu runner could not resolve `azure.archive.ubuntu.com` while installing system packages. The installation stopped before the Python builder ran. This points to a runner-side package-server connectivity problem during that attempt; it does not show that the builder or manuscript is defective.
- **Python setup configuration error (run #116):** `actions/setup-python@v5` was configured with pip caching enabled. The action searched the checked-out repository for `requirements.txt` or `pyproject.toml`, found neither, and stopped. The builder and system-package installation steps were skipped. This is a workflow configuration error; pip caching should not be enabled unless a suitable dependency manifest is present.

These are different failure points and should not be conflated. Run #115 failed while reaching the Ubuntu package repository; run #116 failed before attempting that installation. Neither run reached PDF generation, so neither provides evidence that the Python builder itself failed. The reason the process is not currently dependable is that the workflow setup has changed and the recent attempts have encountered separate setup failures. The exact current builder/workflow combination still needs an end-to-end successful run before it can be treated as restored.

The 6 November run is a historical proof of a successful installation and build, not a guarantee that a later GitHub-hosted runner will have identical network conditions. GitHub-hosted runners are newly provisioned for each run, so required packages must be installed again; successful installation in one run does not make those packages persist for subsequent runs.

## Recovery record: successful restoration of the EDRL II print artifact — 11 November 2026

### Outcome

The production build was recovered on 11 November 2026. GitHub Actions **run #117** completed successfully on its second attempt and uploaded a new artifact containing the three expected PDF files:

- `edrl-ii-interior.pdf`
- `edrl-ii-front-cover-proof.pdf`
- `edrl-ii-combined-review.pdf`

**Successful run:** [EDRL II print proof — run #117](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43061265800)  
**Run ID:** `43061265800`  
**Successful job ID:** `130672873198`  
**Commit:** `a4cfcba453eddb548226a8a854498adaa64b7955`  
**Commit message:** `Tito VSCode fix attempt #109 based`  
**Artifact:** `edrl-ii-print-preview-117`  
**Artifact size:** 7,405,501 bytes (approximately 7.4 MB)  
**Artifact retention:** 30 days; GitHub reported an expiry date of 11 December 2026.

The artifact was downloaded and opened. The user confirmed that the expected earlier version of the book was present. This confirms that the workflow generated and uploaded usable PDFs; it does not, by itself, certify every page or establish printer approval.

### Important correction to the earlier incident status

The earlier incident report above described the production disruption as open because no later successful build had yet been confirmed. That status is now superseded: run #117 succeeded, and a downloadable artifact was obtained. The production workflow is therefore **recovered to a working state**, although the output still requires the normal editorial and visual proofing before it can be approved for printing.

Run #109 remains the last successful reference build before the disruption. Its exact commit was:

`b20ffc15b3f238465b0e3ccbe7897525f497f0c5`

It completed at 13:18:38 UTC on 11 November 2026. The recovery commit used for run #117 was different:

`a4cfcba453eddb548226a8a854498adaa64b7955`

The recovery commit message described the work as based on Run #109. This record does **not** claim that every file in the recovery commit is byte-for-byte identical to Run #109. The important operational result is that the current committed combination successfully produced the artifact that was downloaded and inspected.

### Chronology of the disruption and recovery

The following chronology records the known events and distinguishes confirmed log evidence from conclusions that cannot be established.

1. **Run #109 — last known successful reference.** The workflow installed its dependencies, ran the print builder, generated the interior, front-cover proof and combined review PDFs, and uploaded the artifact. This became the reference point for recovery.

2. **Builder and workflow experimentation.** The print builder, `ebook/edrl-ii/print/build.py`, and the workflow, `.github/workflows/build-edrl-ii-print.yml`, were changed during attempts to revise the production process. The changes affected both the document-generation code and the environment setup. The experimental changes were not kept isolated from the production path as originally intended. This made it harder to identify which exact pair of files was responsible for a given result.

3. **Gemini-related production changes and attempted rollback.** Changes associated with the experimental builder were committed to the production branch. The subsequent rollback attempts did not initially restore the exact Run #109 versions. An earlier version was mistakenly described as the Run #109 baseline. That assurance was incorrect. The distinction matters: restoring a file from an earlier point in the repository is not the same as restoring the file from the exact commit used by a known successful run.

4. **Repeated failed workflow attempts.** Runs #110–#116 included failed and cancelled attempts while the builder and workflow were being changed and recovery was being attempted. The run records and logs show more than one failure point; they should not all be described as the same error.

5. **Run #115 — Ubuntu package repository resolution failure.** The runner could not resolve `azure.archive.ubuntu.com` while APT was installing system packages. The log included `Temporary failure resolving 'azure.archive.ubuntu.com'` and APT ended with exit code 100. The affected packages included Pandoc, Pandoc data, Linux Libertine fonts and Poppler utilities. The builder did not run in this attempt. This is direct evidence of a runner-side DNS/network failure during dependency installation, not evidence of a manuscript or PDF-layout defect.

6. **Run #116 — Python setup configuration failure.** The workflow attempted to use pip caching without a repository dependency manifest recognised by `actions/setup-python`. The action could not find `requirements.txt` or `pyproject.toml` and failed before the PDF build. This was a separate workflow configuration problem, not an Azure DNS failure and not a builder error.

7. **Local VS Code recovery.** The repository was pulled into the local working copy. During the file replacement, the wrong path, `ebook/edrl-ii/build.py`, was briefly modified instead of the print builder at `ebook/edrl-ii/print/build.py`. That unrelated edit was restored. The final local status showed the intended workflow and print-builder files as the modified files. The user then committed the work with the message `Tito VSCode fix attempt`; the resulting commit on the successful run was `a4cfcba453eddb548226a8a854498adaa64b7955`.

8. **Run #117 — successful second attempt.** The first attempt of run #117 did not provide the required successful artifact. The existing failed job was rerun. The second attempt completed successfully: dependency installation, PDF generation and artifact upload all completed. GitHub recorded run attempt 2 as successful. The artifact was then downloaded and opened by the user.

### What the logs establish — and what they do not

The failed attempts do not support one single explanation for every failure:

- The Azure Ubuntu mirror/DNS error is confirmed for run #115. That attempt stopped during APT installation, before the builder ran.
- The missing dependency-manifest error is confirmed for run #116. That attempt stopped during Python setup, before APT installation and before the builder ran.
- The successful second attempt of run #117 establishes that the workflow could again install its environment, execute the builder and upload the PDFs.
- The available evidence does not establish why the rerun succeeded when the preceding attempt did not. It is not appropriate to claim that a particular code change fixed the DNS issue, or that the Azure mirror was permanently repaired. A transient runner or network condition is possible, but the logs available here do not prove that explanation.
- A successful artifact build confirms execution and upload. It does not establish that all typography, pagination, tables, footnotes, references, images or printer specifications are correct. Those require inspection of the downloaded PDFs.

### Why a small formatting edit can still encounter the installation stage

The current workflow runs on `ubuntu-latest` and has explicit setup steps before it invokes the Python builder. The workflow currently:

1. Checks out the repository.
2. Sets up Python.
3. Installs `PyYAML` and `beautifulsoup4` with pip.
4. Runs `apt-get update`.
5. Installs `pandoc`, `fonts-linuxlibertine` and `poppler-utils`.
6. Downloads the Typst Linux release archive and installs the `typst` executable.
7. Runs `python ebook/edrl-ii/print/build.py`.
8. Uploads the three PDF outputs as an artifact.

The workflow does not currently use a dependency cache. GitHub-hosted runners are temporary environments, so software installed during one run should not be assumed to remain installed for the next run. A formatting-only edit inside `build.py` does not inherently introduce a new package requirement, but if that edit triggers this workflow, the existing installation steps will still run. This is a property of the current workflow configuration, not a requirement created by the formatting edit itself.

The workflow is triggered by a push to `main` when a listed manuscript, print-production or workflow path changes, and it can also be started manually. The exact trigger paths are recorded in `.github/workflows/build-edrl-ii-print.yml`.

### Production freeze and next editing approach

The immediate priority is to preserve the working production state. No dependency is to be added or removed, and no further redesign of the build environment is planned as part of routine formatting work.

Future visual refinements will be made manually in the existing Python builder, `ebook/edrl-ii/print/build.py`, by changing its existing Typst layout and styling instructions in small, deliberate steps. These are formatting adjustments, not a reason to introduce another typesetting system or a new package. The manuscript content must remain unchanged unless a separately approved editorial correction is requested.

The current successful commit and downloaded artifact should be retained as a recovery reference. Before any future production change, preserve the current working files and identify the exact lines or formatting rule being changed. Do not describe a future build as tested until a new artifact has actually been generated and checked.

### Lessons recorded for future maintenance

- Keep experimental builders separate from production files. Do not replace the working production builder merely to test a new approach.
- Treat a successful workflow run as a reproducible configuration consisting of the builder, workflow and dependency setup together, not as a Python file alone.
- Record the exact commit SHA for every known-good artifact.
- When restoring a known-good build, retrieve files from the exact successful commit and compare them before claiming that the restoration is exact.
- Read the failing step before diagnosing a failed workflow. A DNS error during APT installation, a Python action configuration error and a builder exception are different failures.
- Do not infer that a builder is defective when the workflow never reached the builder.
- A successful retry proves that the retry worked; it does not automatically explain why an earlier attempt failed.
- Preserve downloaded artifacts. They provide a usable fallback and a concrete reference for visual comparison.
- Keep formatting changes small and local, and avoid unnecessary dependency or workflow changes during the final book-proofing stage.

**Current status: RECOVERED WORKING BUILD.** Run #117, attempt 2, successfully generated and uploaded the three PDF outputs. The user downloaded the artifact and confirmed that the expected earlier book file was present. The environment and dependency setup are to be left unchanged while the remaining formatting is considered.



## Production log: credit-page redesign and opening-page audit — 12 November 2026

### Credit/publication page redesign

The credit/publication page in the paperback interior was redesigned on 12 November 2026. The change was deliberately confined to the credit-page layout block in `ebook/edrl-ii/print/build.py`; no manuscript text, other front-matter pages, essay layouts, pagination rules or build-workflow configuration were changed.

The existing publication information was retained. This includes the book title and author, the website and contact details, the editor and design/print-production advisor credits, the first paperback edition date, publisher, paperback ISBN, printed price and place of publication. No permissions statement or other new publication claim was introduced.

The layout now organises the information into three visually separated groups: the book title and author near the top, contact and production credits in the middle, and edition, publisher and ISBN/price information towards the bottom. Flexible vertical spacing provides the separation while preserving the existing content.

- **Commit:** `bfdf991151f2aa348da2acbd0d2c1037c88adbed`
- **Commit message:** `Redesign EDRL II credit page layout`
- **Changed file:** `ebook/edrl-ii/print/build.py` (credit-page block only)
- **Print workflow run:** [Run #142 — EDRL II print proof](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43168627879)
- **Run ID:** `43168627879`
- **Result:** Successful; the workflow generated and uploaded the print-preview artifact `edrl-ii-print-preview-142`.

### Opening-page sequence checked

The combined review PDF generated by run #142 was inspected to identify the actual contents of its opening pages. The PDF page positions are:

| PDF page | Content |
|---:|---|
| 1 | Front cover |
| 2 | Half-title page, carrying the book title |
| 3 | Blank page |
| 4 | Full title page, carrying the book title and author's name |
| 5 | Credit/publication page |
| 6 | Blank page |
| 7 | Author photograph |
| 8 | Epigraph |

This inspection distinguishes the half-title page from the full title page. Although both display the book title, they have different functions in the opening sequence. The page-2/page-4 comparison was therefore recorded on the basis of the actual PDF contents, not an assumption that page 2 was blank or duplicated. No page was deleted as part of this work.

The page sequence is an inspection record, not a final approval of the complete book's front matter or a printer sign-off. Any decision to alter or remove a page must be made separately and must be followed by a fresh proof.



## Print layout refinements and verified production builds — 12 November 2026

The essay-opening layout and preliminary-page running-head treatment were refined in the existing Typst print builder, `ebook/edrl-ii/print/build.py`. These are print-only layout changes; the original essay wording, publication details, manifest, page dimensions, margins, footnotes, tables and cover content were not changed.

### Essay chapter openings

The essay-opening block now follows this sequence:

1. The essay title remains left-aligned in the existing serif heading style.
2. A 9 pt vertical gap follows the title.
3. A thin horizontal rule spans the text measure.
4. The label `ORIGINAL PUBLICATION:` and the original publication citation are set inline on the same line where space permits. The citation can wrap naturally if it is too long; the label is not split onto a separate line.
5. A second thin horizontal rule follows the publication citation.
6. A 9 pt gap follows the second rule before the essay's first section heading.

The publication label and citation are set without first-line indentation. The ordinary essay body paragraph style and its established first-line indentation remain unchanged. The first section heading and essay text retain their existing styles.

### Preliminary-page running heads

The preliminary pages before the first essay, numbered with Roman numerals (i–xii in the proof under review), no longer display the top horizontal running-head rule. The running-head function returns an empty header for this preliminary-page range. This change does not remove the running heads or their rules from the essay section. Existing chapter-opening pages continue to suppress running heads according to the established behaviour.

### Dependency and workflow safeguards

The existing GitHub Actions print workflow was adjusted to reduce unnecessary repeated setup without introducing new dependencies:

- The pip download cache is retained between compatible workflow runs.
- The Typst executable is cached and reused when present; the download is used only when the cached executable is absent.
- Python dependencies are checked before pip installation.
- Pandoc, Poppler utilities and Linux Libertine fonts are checked before APT installation; APT runs only when a required tool or font is missing.
- The cached Typst directory is explicitly added to the PATH for the build step.

No new Python package, system package or typesetting engine was introduced. GitHub-hosted runners remain temporary; caching reduces repeated downloads but does not guarantee that every dependency will always be available without a fallback installation.

### Build failures and correction

Two intermediate builds failed because paragraph-formatting directives were inserted repeatedly into the generated Typst document. The builder's existing lint check correctly rejected those unscoped paragraph rules. Those injected directives were removed; the paragraph indentation of the essay body was left intact. The corrected build then completed successfully.

- Failed intermediate run after the first paragraph override: [run 43171678736](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43171678736).
- Failed intermediate run after the escaped newline was corrected but the repeated overrides remained: [run 43171708143](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43171708143).
- Successful build after restoring the two-rule essay opening and removing the injected paragraph overrides: [run 43171910391](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43171910391).
- Successful build after adding the 9 pt gap above the first rule and putting the publication label and citation on one line: [run 43172368394](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43172368394).
- Successful build after removing the top rule from the Roman-numbered preliminary pages only: [run 43173001495](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43173001495).

The successful runs generated the A5 interior, front-cover proof and combined review PDF. Their logs report that the PDF overlap check passed with no colliding lines. The latest verified run is [EDRL II print proof — run 43173001495](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43173001495), associated with commit `158fa055c9a3a8ed236c4ecb180c7987c608382e`.

### Current status and limits of verification

**Build status: successful.** The latest recorded production build completed and uploaded its preview artifact. Automated overlap validation also passed. These results confirm that the current source and workflow generated the PDFs; they do not constitute final visual approval or printer approval. The latest PDF should still be checked page by page, including the Roman-numbered preliminary pages, essay openings, running heads, paragraph indents and page transitions.

The production workflow and its dependency setup should now be treated as established. Further design changes should be limited to the specific requested formatting, made in the existing builder, and checked with a fresh build. Do not change the manuscript or add dependencies as part of routine layout refinements.


## Further corrections, failed attempts and production notes — 12 November 2026

This log records the additional work carried out after the earlier 12 November entries. It includes both successful corrections and failed approaches because the build history is useful when continuing the work in another session. The failures below were not all caused by the same problem: some were incorrect source-matching assumptions, some were conversion-order problems, and some were visual layout defects.

### Title page and preliminary matter

The text `THE SUNIL ABRAHAM PROJECT` was removed from the full title page (PDF page 4). This was a targeted change to the title-page content. The separate page-5 line-break issue was identified but deliberately left for a later pass; it was not silently changed as part of the page-4 correction.

The four-line Vinayaraj signature also required attention. It was splitting across pages, so the intended treatment was to keep the signature block together rather than allow individual lines to be separated by pagination. An earlier negative vertical offset (`above: -24pt`) had caused the signature to overlap the final paragraph. That offset was removed, restoring the original positioning; the signature must be judged in the generated PDF, not assumed correct from the source change alone.

### Footnotes: hanging indents and repeated markers

The paperback footnote treatment was changed to use hanging indents so that wrapped lines align with the footnote text rather than with the note number. This was a print-layout change in the existing builder, not an alteration to the wording of the notes.

A later inspection exposed a separate repeated-footnote problem. The correction was committed as `5f391dc` and triggered print build #180. The purpose of this change was to prevent a repeated footnote reference from being treated as a fresh numbered note. The hanging-indent change and the repeated-reference correction address different aspects of footnote rendering and should not be conflated.

### Orphaned "Notes" heading: conversion-order and matching failures

An unwanted standalone "Notes" heading remained in the output after the notes themselves had been converted into footnotes. The source essay contained two genuine notes; the problem was not that the notes were absent or that the source contained an extra set of notes.

The cause was the order of transformations in the builder. The HTML heading was converted into raw Typst before the later Markdown-heading cleanup ran. The cleanup therefore no longer saw a Markdown heading to remove, leaving the heading in the generated document even though the notes had already become footnotes.

Two attempted corrections then failed for separate reasons:

- The first removal attempt (`a432011`) did not take effect because the heading was protected as a token before the cleanup could remove it. Protecting the token preserved the very heading that needed to be removed; build #182 still showed the problem.
- The next attempt used an incorrectly escaped regular expression (`e94364e`). The expression did not match the actual Markdown heading, so the intended removal did not occur.
- The matching expression was corrected in commit `42c23f1`. Build #183 was queued after that change. At the time this entry was written, its resulting PDF had not yet been visually verified; the source correction must not be treated as a confirmed PDF fix until that proof is inspected.

The durable lesson is to account for the builder's actual conversion order and inspect the generated intermediate representation before writing a cleanup rule. A regular expression that looks plausible in Python source may still fail to match if its escaping does not represent the intended newline or heading syntax.

### Heading conversion: failed assumptions and successful correction

A separate heading-formatting experiment failed because the code searched for a heading pattern that was not present in the Pandoc-generated content. Runs #158 and #159 failed during that speculative heading-3 matching attempt; run #160 failed for the same underlying reason, reporting: `The complete section 3 heading was not found...` and exiting with status 1. The failure was in the assumed source pattern, not in Typst's ability to typeset the heading. The builder was returned to the last successful version before a later, narrower correction was made.

A subsequent build (#173) completed technically and generated 175-page PDFs, but inspection showed that the heading was still split. A successful build alone had therefore not proved that the visual defect was fixed. The cause was identified and corrected in the next iteration: build #174 (run ID `43179950408`, commit `75ba5efa`) produced the complete four-line heading together. That result was visually checked. This is an important distinction for future work: build success and visual correctness are separate checks.

### Table-header contrast

The PDF review identified table headings on pages 102–105 with dark grey backgrounds and black text. The text was difficult to read because the header fill was too dark for the default black lettering. The fix was limited to the table-header fill in `ebook/edrl-ii/print/build.py`: the Typst fill changed from `luma(94)` to `luma(235)`. The existing bold black header text, table contents, column widths and other table layout rules were retained.

- **Commit:** `44efdd885638bc9d578878d6011cef3691faea22`
- **Commit message:** `Improve print table header contrast`
- **Verification status:** The source change is committed. The separate print-PDF workflow and visual inspection of the regenerated pages are still required before calling the correction verified. The site-index workflow is not evidence that the print PDF was rebuilt.

### Production safeguards for the next session

- Work only in the existing print builder, `ebook/edrl-ii/print/build.py`, unless a specific, demonstrated need requires otherwise.
- Inspect the current source and the relevant generated PDF page before changing a layout rule. Make one change at a time.
- Do not repeat dependency or runner-environment troubleshooting. The recovered production environment is to be preserved; no speculative dependency changes, reinstallations or workflow redesigns are part of these formatting fixes.
- When a build fails, identify the failing step first. A pattern-not-found exception is a builder/source-matching failure; an installation or DNS failure occurs before typesetting and is not evidence of a layout defect.
- After a successful build, inspect the affected PDF pages. Record a fix as visually verified only after the generated PDF demonstrates the intended result.
- Keep the page-5 line-break issue separate from the completed page-4 title-page edit. Do not bundle unrelated front-matter changes.


## Running-title correction and poem stanza audit — 12 November 2026

### Essay 3 running title

The running title for the third essay, *The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue*, was too long for the available running-head space. In the generated PDF it wrapped onto a second line and the first line was clipped at the top of the page. The first two essays checked at the same time did not show this problem, so a global running-head change was not justified.

The print builder now uses the shorter running title **The Living Hindu Popular Religious Consciousness** for this essay only. The full essay title remains unchanged in the essay opening, contents and source manuscript. No other essay's running title was changed.

- **Commit:** `d64e0f4ce3f564ccf16e6dc159d80c66dcc5dda4`
- **Commit message:** `Shorten EDRL II essay 3 running title only`
- **Print workflow:** [Run #191 — EDRL II print proof](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43194151925)
- **Verification:** The workflow completed successfully and generated the print-preview artifact. The source change was confirmed; visual verification of the revised running title remains part of the full proof review.

### Poem line and stanza audit: final essay

A reverse-order comparison was begun using the source essay, *The Ideological Nature of the Emerging Dalit Consciousness*, and the generated print PDF. The purpose was to check whether the print conversion preserved explicit line breaks and blank-line stanza divisions.

The first three poems/verse passages checked were:

1. **Pambatti Cittar's final poem:** The source contains three stanzas. The individual line breaks were preserved, but the first and second stanzas did not have a sufficiently clear visual separation in the print PDF. The third stanza begins on the following page.
2. **Siddhalingiah's *Dalitaru Barvaru*:** The source has several distinct verse sections, separated by blank lines and dotted separators. The print presentation made some of these sections appear too continuous; the stanza gaps were not sufficiently distinct.
3. **Buddha's four-line verse:** The four lines appeared as one stanza, consistent with the source. No correction was identified for this verse.

The audit identified a poem-layout issue rather than a need to rewrite the poems. The source wording, punctuation, line order and explicit line breaks were not changed.

### Poem stanza rendering: builder correction and iterations

The issue was traced to the poem conversion in `ebook/edrl-ii/print/build.py`. The earlier conversion passed an entire poem to Pandoc as one segment and relied on paragraph spacing to make stanza boundaries visible. That did not provide sufficiently reliable control over the distinction between lines within a stanza and the separation between stanzas.

The builder was changed to split each poem at its source blank lines, convert each stanza separately, and place the stanza blocks in sequence with explicit vertical space between them. The line spacing within each stanza remains separately controlled. Stanza boundaries are therefore an explicit part of the print layout rather than relying only on generic paragraph spacing.

Several proof iterations were needed:

- An initial increase in paragraph spacing improved the gap but was not a satisfactory final solution on its own.
- Treating each stanza as a non-breakable block caused an undesirable pagination result, including an almost empty page. That approach was not retained.
- The stanza blocks were then allowed to paginate naturally while keeping explicit space between them. The stanza gap and outer poem-block spacing were reduced to balance visual separation with page flow.

The final implementation keeps stanza divisions visible without forcing every stanza to remain on a single page. A stanza may continue across a page boundary where the available space requires it; the source stanza division remains represented in the layout.

- **Final builder commit:** `41070d71342933f07ab33a435b8811b7c2cb6e05`
- **Commit message:** `Keep poem stanzas distinct without forcing page breaks`
- **Final print workflow:** [Run #197 — EDRL II print proof](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43196640862)
- **Result:** Successful build; preview artifact `edrl-ii-print-preview-197` was generated.
- **Visual check:** The final essay's Pambatti Cittar poem was inspected in the generated proof (PDF pages 174–175). The three stanza divisions are visibly distinct. The poem wording and line order remain unchanged. The proof remained 176 pages; the nearly empty page caused by the earlier non-breakable-block experiment was not present in the final version.

### Scope and remaining audit

The stanza-rendering correction is a general print-builder change for poem blocks, not an editorial change to one poem. It should benefit other poems in the book wherever blank lines in the source mark stanza boundaries. The final proof confirms the visual result for the inspected poem, but it does not establish that every poem in all nine essays has been checked.

Continue the source-to-PDF poem audit in reverse order, in batches of two or three poems. For each passage, compare the source's exact line breaks, stanza boundaries, dotted separators and page transitions with the generated PDF. Record any exceptions before making further layout changes. Do not alter poem wording or lineation without separate editorial approval.


## Print proof corrections — 13 November 2026

This entry records the three narrowly scoped print-layout corrections made or initiated on 13 November. Each change was limited to the existing print builder, `ebook/edrl-ii/print/build.py`. The manuscript wording was not edited.

### Running-header position

The running-header text was moved further down from the top trim edge to improve its safety distance from the page edge and bring it closer to the horizontal rule. The existing running-head content and the rule were retained.

- **Commit:** `ccecd01e28091c4c7e1d837da59457bbbce2bf06`
- **Print build:** #201
- **Result:** The print workflow completed successfully. This change was carried forward into subsequent proofs.

### Heading and following-paragraph separation

A formatting defect was identified in which the final line of a long Markdown heading was being rendered as ordinary body text and continued on the same line as the following paragraph. The affected PDF pages identified in the audit were 34, 45 and 72.

The heading conversion in the print builder was changed so that preserved Markdown headings are emitted as separate Typst heading blocks. An initial commit contained incorrect regular-expression escaping; that attempt was superseded by the corrected conversion.

- **Initial attempt:** `731c203e30f44e0b804ee8ad3f940738ab1befca`
- **Corrected commit:** `9be75e5b94b12c12079975fdfff99d4b92755a6d`
- **Print build:** #203
- **Result:** The build completed successfully. PDF pages 34, 45 and 72 were inspected in the generated proof, and the affected headings were visibly separated from their following paragraphs. The proof remained 176 pages.

### Footnote markers: superscript correction

The audit found that footnote reference markers in the body text were being displayed at the normal body-text size and baseline rather than as superscripts. The print builder was changed to render the markers at 7 pt in superscript. The footnote text and the existing footnote-entry layout were not intentionally changed.

- **Commit:** `fa876a1eb6525641917ba7c8dbe5a6fce5de38fa`
- **Commit message:** `Superscript EDRL II footnote markers`
- **Print workflow:** [Run #43289732456 — EDRL II print proof](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/43289732456)
- **Status at the time of this entry:** The workflow had been triggered and was queued. The generated PDF and the visual result had not yet been verified.

Only the footnote-marker correction is the active change in this final entry. No other audit item was included in that commit. The next step is to wait for this print build to complete and inspect the footnote markers in the resulting PDF before treating the correction as verified.

## See also

- [E-book Export: A. M. A. Ayrookuzhiel](/amaa/30-ebook-export/) - documentation for the EPUB edition, its metadata, build process and digital quality checks.

{% include navbox-amaa.html %}



## Design and typographic review of combined proof 204 — 13 November 2026

This section records the design, layout and typographic recommendations arising from the complete visual review of the 176-page combined review PDF (proof 204). It is a record of recommendations, not an instruction to make all changes together. Each item must be considered separately, and only the specifically authorised item may be changed. The present working scope is the visual redesign of the **page-5 credit page only**. No other book page is authorised for alteration by this entry.

### Page 5 — credit-page design (first and only current design task)

The page should be treated as a designed book credit/colophon page, not as a legal-status exercise or an administrative form. The review is concerned with visual hierarchy, typography, alignment, spacing and page composition. Do not invent missing printer, typesetter, designer or production details. If a detail has not yet been supplied, leave its wording and presence for the editor to decide; do not fill the gap with guessed information.

Design points to assess on page 5:

- Establish a clear typographic hierarchy between the book title, author, edition/publisher information and the smaller production or contact details.
- Arrange related information into visually distinct groups, with deliberate vertical spacing between groups.
- Use a consistent alignment system. Labels and their corresponding details should align cleanly; avoid irregular spacing created by manually positioning individual words.
- Set a comfortable text measure suitable for the A5 page. Avoid long lines stretching across the full page where a narrower colophon measure would improve balance.
- Use restrained type-size differences and weight. Secondary information may be smaller, but must remain comfortably legible in print.
- Use the existing book typeface and typographic identity unless a specific defect justifies a change. Do not introduce decorative fonts.
- Use rules, if any, sparingly and consistently. Do not add boxes, ornamental borders, icons, colour panels or decorative graphics merely to fill space.
- Balance the page vertically. Avoid both a crowded block at the top and an excessively scattered arrangement with unexplained empty gaps.
- Check the page as a single page and as part of the opening spread. Confirm that the page furniture (running head and folio) follows the deliberate preliminary-page treatment.
- Check that the page remains clear in a monochrome print and that small text has adequate contrast and weight.
- Preserve the exact approved wording and factual details. This is a layout and style pass, not permission to rewrite the credits or add unconfirmed production information.

The page-5 redesign must be made and reviewed as one isolated change. Do not combine it with changes to the title page, portrait, Foreword, Editor's Note, Contents or essay pages. Do not start a print build until the user explicitly authorises it.

### Other design and composition findings from proof 204 — recorded for later, not authorised now

These observations are retained so they are not lost. They are not part of the current page-5 task.

**Front matter and page architecture**

- The overall front-matter sequence is coherent. Retain the established sequence unless a specific editorial decision requires otherwise.
- The Foreword currently begins on a left-hand (verso) page. Consider whether it should begin on a right-hand (recto) page, using an intentional blank page if the book's structure and printer's imposition permit it.
- The Contents begins on a right-hand (recto) page; retain that favourable placement.
- The Editor's Note and About the Author pages are also positioned on right-hand pages in proof 204. Avoid disturbing their pagination while addressing page 5.
- The author's portrait would benefit from a discreet caption identifying the person. Any source or image credit must be based on confirmed information, not guessed.
- Keep intentional blank pages free of running heads and folios.

**Essay openings and running heads**

- Six of the nine essays begin on left-hand (verso) pages in proof 204: essays 2, 3, 4, 5, 6 and 8. Consider a consistent right-hand opening convention for all essays, subject to the final pagination and printer's signature requirements.
- If recto openings are adopted, use deliberate blank versos rather than ad hoc spacing. Recheck the contents page and all subsequent folios after any pagination change.
- Preserve the restrained running-head system. Check each essay's running title for fit, clipping, collisions and consistent placement.
- Chapter-opening pages should retain the agreed absence of running heads.

**Essay-opening label and display typography**

- The label "ORIGINAL P UBLICATION" appears with an unwanted internal gap in the word "PUBLICATION" on all nine essay-opening pages. Inspect the source and correct the spacing/word treatment consistently.
- Consider a clearer and more natural label such as "Originally published in:" but do not change the wording without approval.
- Check essay display titles for balanced line breaks and adequate space above and below. Avoid hyphenating words in display titles.
- Maintain a consistent visual template for all nine essay openings: title, original-publication information and opening text should have predictable hierarchy and spacing.

**Text flow and punctuation**

- Proof 204 contains a one-line carryover at the top of PDF page 144. Review the preceding and following paragraphs and adjust composition to avoid an isolated line where practicable.
- Review paragraph endings, widows, orphans, short isolated lines and awkward page turns across the whole book. Do not correct them through arbitrary global spacing changes.
- Remove unintended spaces before question marks, exclamation marks and colons in the affected essay text, after checking against the approved source. This is a copy-proofing item, not a licence to rewrite the author's prose.
- The standalone heading "Sony !" on PDF page 154 appears to be an accidental editorial remnant. Verify it against the source manuscript before deciding whether it should be removed.
- Keep paragraph spacing, first-line indentation, line leading and justification consistent. Any global change must be assessed across prose, poetry, tables, footnotes and headings rather than judged from one page.

**Tables**

- Tables on PDF pages 101–105 are generally readable but their composition can be improved.
- Reassess column widths in relation to the content. Avoid narrow columns that force headings into awkward multi-line fragments.
- Keep table headings concise, clear and aligned consistently. Do not stretch word spacing through justification in table cells.
- Align numerical columns consistently and keep descriptive text left-aligned where that improves scanning.
- Retain the repeated column header when a table continues onto another page.
- Avoid splitting individual rows across pages where possible.
- If a table cannot fit legibly at A5 size, consider a redesigned multi-part presentation rather than simply shrinking the type.
- Review the vertical spacing before and after each table so that it does not interrupt the reading flow.

**Scholarly apparatus and navigation**

- Prepare a subject/name index and verify every page reference against the final printed pagination. The index is a strong scholarly usability improvement; it must be prepared after the main text pagination is stable.
- Consider a list of tables because the volume contains several substantive tables. This is optional and should be judged against the book's overall front-matter design.
- Consider an editorial-method note explaining the preparation of this collected edition, including the treatment of original publication texts and any approved corrections. This is an editorial-content decision, not a layout correction.
- Check the consistency and legibility of footnotes, references, quotations, lists and cross-references. Retain the restrained footnote separator and hanging-indent treatment where it is working.

**Cover and final PDF presentation**

- Proof 204 contains a front-cover image only. The complete cover still needs a separately designed back-cover and spine layout using the printer's confirmed template and dimensions.
- Assess the back-cover text hierarchy, barcode area, publisher identification and spine typography when the full-wrap cover is prepared. Do not estimate the spine width before final page count, paper stock and binding method are confirmed.
- For the final digital/archival PDF, add accurate document title and author metadata, subject/keyword metadata and document language.
- Add useful PDF bookmarks for the Foreword, Editor's Note, About the Author, Contents and each essay.
- Investigate tagged PDF structure and logical reading order where the production toolchain permits. These are digital accessibility improvements and should not be confused with print-layout requirements.
- Continue to inspect the complete PDF visually and, where practicable, as a physical A5 proof. A successful automated build is not evidence of visual approval.

### Order of work and scope control

1. Page 5 credit-page visual redesign only.
2. Review that page in isolation and approve its composition before moving to another item.
3. Take the next design issue only after the page-5 task is complete and the user selects or authorises it.
4. Keep every later correction isolated, record the exact page or component affected, and inspect the resulting proof before calling it complete.

No book source, print-builder file, generated PDF or workflow was changed by adding this review record. This documentation entry itself does not trigger a print build.

## Editor's Note and acknowledgement drafting — 13 November 2026

Work began on the front matter for the print edition, including the drafting of the Editor's Note and an Acknowledgement subsection. The acknowledgement material is being assembled from contributions and support received during the preparation of the volume, including a personal acknowledgement of the author's family. The text is a working draft and has not yet been finalised. The individual acknowledgement wording is not reproduced in this production log.

The draft material was added to the print composition in `ebook/edrl-ii/print/build.py`. The wording was also adjusted during this work, including the removal of a term the editor did not wish to use. No essay text was changed.

- **Print source updated:** `ebook/edrl-ii/print/build.py`.
- **Print workflow:** EDRL II print proof #215.
- **Build result:** Successful; the proof artefacts were generated.
- **Remaining work:** Some spacing issues remain in the front matter. These will be reviewed and corrected shortly.
- **Editorial status:** The Editor's Note and acknowledgement material remain in draft. The successful build confirms that the source can be typeset; it does not mean the text or layout is final or approved.

## Front-matter editorial corrections — 14 November 2026

A further review of the Foreword, Editor's Note and Acknowledgement led to a set of small, specifically scoped corrections. These changes were made in the print source; the essays were not edited.

### Foreword

- Replaced the clerical title `Fr.` with `Rev.` in all occurrences referring to A. M. Abraham Ayrookuzhiel, following the instruction received from Sunil. This included the occurrence written as `Fr Abraham` without a full stop.
- Standardised the spacing between initials in human names throughout the Foreword, including its footnotes: for example, `P.D.` to `P. D.`, `M.M.` to `M. M.`, `B.R.` to `B. R.` and `A.M.A.` to `A. M. A.`.
- Retained the Foreword's existing American English spelling. No spelling conversion to British/Indian English was made.

- **Source:** `ebook/edrl-ii/foreword.md`.
- **Commit:** `5261afc5fea599fe1401f78329bda05a3b6e8ee3`.
- **Print proof:** #224 — successful.

### Editor's Note and Acknowledgement

The following wording and presentation corrections were made in the print composition:

- Changed the reference to errors or inaccuracies being brought to the "editors' attention" to "my attention", matching the individual editor's signature.
- Simplified the sentence thanking Dr. Y. T. Vinayaraj for contributing the Foreword. The final wording is: "We thank Dr. Vinayaraj for graciously contributing the Foreword to this volume." The word "also" and evaluative wording were avoided.
- Changed the United Theological College acknowledgement to begin "We are thankful to the Principal..." rather than "We also thank the Principal...".
- Introduced a separate transition, "And,", before the personal acknowledgement of the Ayrookuzhiel family. The following sentence now begins "I personally take this opportunity to express my gratitude..." This marks the deliberate shift from the collective "we" to the editor's personal "I". Normal paragraph line spacing is retained.
- Removed the possessive "our" from the description of Pranesh Prakash as a former colleague, leaving "a distinguished researcher and former colleague".
- Simplified the ISBN acknowledgement to refer to the "ISBN registration process", without the phrase "our efforts".
- Corrected the name of the contributor who provided initial ISBN guidance from "Sangram Kesari Senapati" to **Sangram Keshari Senapati**, as confirmed by him.

The collective voice in the acknowledgement is retained where it represents the production effort; the personal family acknowledgement remains in the first person. No other acknowledgement contributions or names were changed.

- **Print source:** `ebook/edrl-ii/print/build.py`.
- **Relevant commits:** `c5fdc2f6`, `5cd237ae`, `3924ed12` and `e9adcf21`.
- **Print proofs:** #217, #218, #219 and #225 — successful.

### Signature preparation

A fresh scan of the editor's handwritten blue-ink signature was prepared from the supplied A4 scan. The paper background was removed and the signature retained as a transparent PNG for possible placement above the editor's typed name. This is a prepared image asset; its placement in the book remains a separate design decision.

The corrections recorded above are limited to the front matter. The successful print builds confirm that the source typesets; they do not by themselves constitute final editorial approval of the book.

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
  vertical-align: top;  white-space: normal;
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
