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

{% include navbox-amaa.html %}
