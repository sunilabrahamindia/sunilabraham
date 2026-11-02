---
layout: default
title: "E-book Export: A. M. A. Ayrookuzhiel"
permalink: /amaa/30-ebook-export/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Documentation of the process for creating EPUB and PDF e-books from selected pages of The Sunil Abraham Project using Pandoc."
page_id: TSAP-1329
created: 2026-10-14
---

**E-book Export** is a project to create downloadable electronic publications from selected pages of The Sunil Abraham Project (TSAP) as part of the preparations for the [30th Death Anniversary Commemoration of A. M. A. Ayrookuzhiel](/amaa/30/). The initial objective is to compile approximately 8-10 pages into an e-book using Pandoc, producing EPUB and PDF editions while preserving the original source pages.

## Purpose

The purpose of this initiative is to establish a repeatable process for converting selected website content into well-formatted e-books suitable for offline reading, distribution and long-term preservation. The exported publications should contain the substantive article content rather than the surrounding website interface.

## Scope

The initial publication will include approximately 8-10 selected pages relating to A. M. A. Ayrookuzhiel. The pages will be arranged in a defined reading order. Where necessary, individual sections can be included or excluded without modifying the original Markdown files.

The export process will exclude website headers, footers, navigation menus, breadcrumbs, existing article contents lists, category labels and other website-specific elements.

## Workflow

1. **Select the source pages:** Identify the articles to be included and specify their reading order.
2. **Extract the content:** Read the original Markdown files, remove YAML front matter and exclude website-specific markup while preserving substantive text.
3. **Apply section-selection rules:** Include or exclude specific sections where required.
4. **Assemble the manuscript:** Combine the selected content into a single Markdown manuscript, preserving headings, paragraphs, quotations, lists, tables, citations, links and relevant images.
5. **Prepare publication metadata:** Store the publication title, author or editor details, language and other metadata separately.
6. **Generate the table of contents:** Use Pandoc to generate a new book-level table of contents from the selected headings.
7. **Export the formats:** Generate EPUB and PDF editions with appropriate typography, margins, heading styles and page breaks.
8. **Review the output:** Compare the exported content with the source articles and check links, images, reading order and layout.

## Proposed E-book Structure

The initial e-book will use a conventional book structure adapted specifically for electronic reading. This structure applies to the e-book export only; it does not require duplicate article pages or additional published articles on the website.

1. **Front cover:** A designed cover image featuring the book title and appropriate publication details. The same cover image can be embedded as the EPUB cover.
2. **Half-title page:** The book title only, kept simple.
3. **Full title page:** The full title and subtitle, where applicable, with the relevant author, editor or compiler credits and publisher/imprint.
4. **Copyright and publication details:** Copyright statement, publication year, edition, ISBN if obtained, and other confirmed publication credits. Do not invent or assume an ISBN.
5. **Foreword:** The foreword, with the foreword writer's name and any supplied date or other details. There will be no dedication page.
6. **Table of contents:** A new book-level contents list generated from the assembled manuscript. It should link to the foreword and the selected articles where supported by the format.
7. **Main text:** The selected full-text articles, in the confirmed reading order, preserving substantive content, references, citations, images and captions.
8. **Biographical note:** A short, verified note about A. M. A. Ayrookuzhiel may be included at the end if suitable material is available.

The structure is provisional until the article selection, foreword and publication details are confirmed. Optional sections should be omitted if they are not needed or if verified content is unavailable.

### E-book-specific layout decisions

- Do not add a dedication page.
- Do not insert artificial blank pages merely to imitate print pagination. EPUB pages reflow according to the reader's device, and blank pages are generally unnecessary.
- A separate back-cover page is not required for the e-book. The front cover image and publication metadata are sufficient; a short book description may be included in the metadata or introductory material if needed.
- Keep the half-title and full title pages simple and readable. The EPUB and PDF may use format-appropriate layouts while sharing the same content order.
- Generate the table of contents from the book manuscript, not from any article's website TOC.

## Content and Formatting

Each selected article will begin with its title, followed by the relevant article content. The process should preserve meaningful formatting, including emphasis, quotations, citations, footnotes where present, tables, hyperlinks and images with their captions.

The website's existing contents lists will not be reproduced. Instead, a new table of contents will be generated for the assembled publication. Website navigation and other interface elements will not be included.

## Technical Implementation

The original Markdown files in the TSAP repository will remain the source of truth. A separate manifest will specify the selected pages and their order, with additional configuration for section-level inclusion or exclusion where necessary.

A build script will process the source files, extract the selected content, assemble the manuscript and invoke Pandoc to generate the output files. Separate metadata and styling files will control publication information and formatting.

The initial implementation will be tested locally on Ubuntu. GitHub Actions automation may be introduced after the extraction and export process has been tested and verified. The website will continue to be served through GitHub Pages; Pandoc will run as a separate part of the publication workflow.

## Output Formats

- **EPUB:** A reflowable format suitable for e-readers, reading applications and mobile devices.
- **PDF:** A fixed-layout format suitable for printing and reading on larger screens.

Both formats should be reviewed for accessibility, including logical heading levels, readable typography, meaningful link text and appropriate alternative text for images.

## Initial Milestone

The first milestone is to produce and review an EPUB and a PDF from a confirmed selection of 8–10 pages. The extraction rules must be verified against the original articles before the process is extended to additional publications.


## Production Standards and Maintenance

The aim is to produce e-books that meet high standards of editorial consistency, usability, accessibility and technical reliability. Each publication will be prepared through a documented workflow and reviewed as a complete book, rather than treated as a simple export of website pages. The process will preserve the original source material while making the finished publication coherent and comfortable to read across devices.

### Manuscript consolidation

- Confirm the final list of source articles, their titles and their order before generating the book.
- Consolidate the selected material into one continuous manuscript, checking for missing sections, accidental duplication, inconsistent headings and broken transitions.
- Preserve the wording and meaning of the source texts. Editorial corrections must be deliberate and checked against the original pages.
- Remove website-only elements, including navigation, breadcrumbs, category labels, duplicate article contents lists and other interface material.
- Check references, quotations, footnotes, tables, captions and image placement after consolidation.

### Book structure and navigation

- Maintain a clear front matter, main text and end matter structure appropriate to the publication.
- Provide a consistent half-title page, title page, copyright and publication details, foreword where supplied, and other confirmed preliminary matter.
- Generate one book-level table of contents from the final manuscript. Check that its entries and links point to the correct sections.
- Create or maintain a dedicated publication hub page on the TSAP website. It should identify the publication, provide accurate bibliographic information, describe the available formats and link to the current authorised files. The hub page should also provide a clear route back to the relevant project material.
- Keep the hub page and the files in sync whenever a publication is revised or replaced.

### Pagination, page breaks and blank pages

- Treat pagination according to the format. The PDF has fixed pages and should have orderly page breaks, consistent margins, readable page numbers and a logical relationship between headings and the text that follows them.
- The EPUB is reflowable. Do not rely on fixed page numbers or insert artificial blank pages into it; readers' devices determine pagination.
- Do not insert blank pages merely to imitate a printed book. In a PDF intended for duplex printing, use a blank page only where a genuine production requirement calls for one, and ensure that it does not disrupt reading.
- Check chapter and article openings, heading placement, widows and orphans, tables, footnotes, images and captions in the PDF. Avoid headings stranded at the bottom of a page or content clipped at page boundaries.

### Editorial and visual consistency

- Use a consistent hierarchy of title, section and subsection headings, with predictable spacing and typography.
- Apply consistent treatment to quotations, notes, references, hyperlinks, lists, tables and captions.
- Check spelling, punctuation, names, dates, titles and bibliographic details throughout the complete manuscript.
- Use readable type sizes, sufficient contrast and layouts that remain usable on different screen sizes. Avoid relying on colour alone to convey meaning.
- Ensure that images have appropriate resolution and that meaningful images have useful alternative text where the format supports it.

### Metadata and publication details

- Verify the title, subtitle, author/editor/compiler credits, publisher or imprint, language, publication date, edition and other bibliographic fields before release.
- Include only confirmed identifiers and claims. ISBNs must match the correct format and edition; do not reuse an identifier across different formats.
- Set and verify EPUB metadata, including the language and publication identifier, and check the PDF's document properties where applicable.
- Keep the publication details in the file consistent with the hub page and the publication record.

### Technical validation and quality assurance

- Validate the generated EPUB with an appropriate EPUB validation tool and correct errors before release.
- Open and inspect the EPUB in more than one compatible reading application or device where practicable. Check navigation, links, images, text flow and display at different font sizes.
- Inspect the complete PDF on screen and, where practical, review a test print. Check page order, page numbering, margins, links, image quality and the absence of clipped or missing content.
- Compare both outputs against the source articles to confirm that no text, references, images or other substantive material has been lost or duplicated.
- Check internal and external links, table-of-contents navigation, accessibility features and document metadata.
- Retain a final quality-assurance checklist and record any known limitations that cannot be resolved before publication.

### Versioning and ongoing maintenance

- Keep the original TSAP Markdown pages as the source of truth. Do not make publication-specific changes by silently altering the source articles.
- Record the source pages and their order, the publication metadata, the build settings and the date of each release.
- Retain the exact files released and identify revisions clearly. When a correction is necessary, document the change and update the hub page and downloadable files together.
- Rebuild and recheck the EPUB and PDF after any change to the manuscript, metadata, styling or export process that could affect the output.
- Before announcing a release, perform a final review of the actual downloadable files, not only the source manuscript or build log.

These standards are a maintenance framework and quality target. Each item should be checked against the actual output; describing a step here does not mean it has already been completed. The workflow may be refined as testing identifies improvements.

{% include navbox-amaa.html %}
