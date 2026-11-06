---
layout: default
title: "Print Book Production: EDRL II"
permalink: /amaa/31-print-production/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Planning and documentation for producing the A5 paperback edition of Essays on Dalits, Religion and Liberation II using Typst and a printer-ready PDF."
created: 2026-11-06
---

**Print Book Production** documents the preparation of the paperback edition of *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It records the production decisions, technical requirements and workflow for creating a complete print-ready PDF, which will be supplied to the printer through Pranesh.

This page is the print-production companion to [E-book Export](/amaa/30-ebook-export/). The two editions belong to the same publication project, but their layout and production systems are different.

## Purpose

The objective is to produce a professionally typeset, print-ready interior PDF for the paperback edition. The Sunil Abraham Project will take responsibility for the book's editorial layout and typesetting decisions rather than sending an EPUB to the printer for the printer to redesign.

The finished PDF will be supplied to Pranesh. His role, as discussed, is to coordinate with the printer and arrange for the printing plates to be made from the supplied print-ready PDF. The printer's production specifications must therefore be confirmed before the final PDF is approved.

## Scope

This documentation covers the paperback interior and its production workflow, including:

- Page size, margins and binding allowance.
- Typography, paragraph treatment and heading hierarchy.
- Front matter, essay openings, pagination and running heads.
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
5. **Typeset the complete book:** Compose the front matter and all nine essays, preserving notes, references, tables, illustrations and captions.
6. **Generate the PDF:** Run Typst in GitHub Actions so that the PDF can be built from the repository without requiring Typst to be installed on the Ubuntu laptop.
7. **Proof the output:** Inspect the complete PDF for missing text, incorrect page breaks, widows and orphans, heading placement, footnotes, references, image quality and other layout defects.
8. **Validate for the printer:** Check the final PDF against the printer's supplied specifications. A successful Typst build alone does not establish that the file is printer-approved.
9. **Supply the approved PDF:** Send the final print-ready file to Pranesh for coordination with the printer and plate preparation.

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
- Page numbers and running heads consistently positioned.
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
- Final running-head, folio and essay-opening conventions.
- Typst source structure and GitHub Actions workflow.
- Complete PDF proofing and printer acceptance.

## Work log

- **27 October 2026** - The late-October planning established that the paperback edition would require its own ISBN, separate from the EPUB ISBN, while retaining 29 November 2026 as the publication date.
- **29 October 2026** - Submitted the paperback ISBN application to the Raja Rammohun Roy National Agency (RRRNA), Ministry of Education, under application reference 55408|ISBN|2026|A. The title, publisher (The Sunil Abraham Project), paperback format and publication date were recorded.
- **30 October 2026** - The paperback ISBN was allotted: **978-93-345-8524-7**. This is separate from the EPUB ISBN.
- **2 November 2026** - Initial production work began in a separate EDRL II production workspace and branch. Draft pull request #58 was created with the book manifest, the nine-source chronological essay sequence, build scripts, metadata, EPUB CSS and README. The source selection was restricted to the repository's "works not in EDRL" category pages; material from the 2006 volume was excluded. This was the start of the digital-edition production workflow, not yet the Typst print-layout implementation.
- **6 November 2026** - Created this separate print-production documentation page to record the paperback workflow independently of the EPUB documentation.
- **6 November 2026** - Created this separate print-production documentation page to record the paperback workflow independently of the EPUB documentation.
- **6 November 2026** - Recorded Sunil's instruction to focus on producing the complete print-ready PDF using Typst. The project will make the design and typesetting decisions; Pranesh will coordinate with the printer and arrange plate preparation from the supplied PDF.
- **6 November 2026** - Recorded Herbert's proposed A5 page dimensions, margins and type-size ranges. A5 is the specified page size; the margin and typography details remain subject to printer requirements and visual proofing.
- **6 November 2026** - Recorded the plan to run Typst through GitHub Actions. Local Typst installation on Ubuntu is optional, not required for the automated build.
- **6 November 2026** - Identified three outstanding printer questions: PDF requirements or template, inner binding margin, and bleed/crop-mark requirements. Paper GSM is not a prerequisite for beginning the page layout.

## See also

- [E-book Export](/amaa/30-ebook-export/) - documentation for the EPUB edition, its CSS, metadata, build process and digital quality checks.

{% include navbox-amaa.html %}
