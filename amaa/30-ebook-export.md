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


### Typography and font selection

Typography must be selected deliberately for sustained reading, rather than left to default export settings. The aim is a calm, professional and accessible reading experience across devices, with a consistent visual hierarchy and no unnecessary decoration.

- **Body typeface:** Choose a highly readable text face with well-differentiated characters and good support for punctuation, italics, bold text, symbols and the languages used in the publication. A restrained serif face is a suitable starting point for long-form essays; a clean sans-serif face is also acceptable where testing shows it reads well. Evaluate options such as Source Serif, Literata or Noto Serif for body text, and a compatible sans-serif face for headings only if a second family is genuinely useful. These are candidates to test, not mandatory choices.
- **Limit the number of typefaces:** Prefer one family with suitable weights and styles, or at most two complementary families. Avoid decorative display fonts for body text and avoid changing fonts without a clear purpose.
- **EPUB font behaviour:** Let readers adjust font size, line spacing, margins and, where the reading system permits, the typeface. Do not force fixed body font sizes or a rigid page layout in a reflowable EPUB. Embedded fonts should be used only when necessary, with appropriate licence permissions and a reliable fallback stack.
- **PDF body size:** Begin testing around 11–12 pt for body text, then judge the complete pages at normal reading size and in a test print. The correct size depends on the chosen typeface, page dimensions, line length and intended audience; do not treat one number as a universal rule.
- **Line spacing and paragraph rhythm:** For the fixed-layout PDF, begin around 1.3–1.5 times the body type size and adjust after page review. Use consistent paragraph spacing or a deliberate first-line indent system; do not combine both heavily. Avoid dense blocks of text and excessive blank space.
- **Line length and margins:** Keep PDF text lines comfortable to follow. Adjust the page size, margins and type size together rather than shrinking type to force content onto fewer pages. Check the result at typical screen magnification and in print.
- **Heading hierarchy:** Establish distinct, consistent styles for the book title, article titles, section headings and lower-level headings. Use semantic heading levels in the EPUB, not just visual formatting. Avoid skipping levels or using heading styles merely to make text larger.
- **Emphasis and special material:** Use bold and italics consistently. Give block quotations, footnotes, captions, tables, lists and references a clear but restrained treatment. Preserve the meaning of emphasis from the source material and do not use underlining as ordinary emphasis, since readers may mistake it for a link.
- **Hyphenation and justification:** Check word spacing and rivers of white space in justified PDF text. Test hyphenation carefully, especially for names and technical terms. Left-aligned text is a valid choice when it produces a more comfortable reading experience. EPUB text should remain adaptable to reader preferences.
- **Character and language support:** Verify curly-free or source-prescribed punctuation as appropriate, quotation marks, dashes, accented characters, symbols and any non-Latin scripts present. Prevent missing glyphs, substituted characters and incorrect line breaks.
- **Contrast and accessibility:** Use strong text/background contrast. Do not communicate structure through font appearance or colour alone. Keep links identifiable, provide meaningful alternative text for informative images and ensure the EPUB structure supports navigation and assistive technology.
- **Consistency across formats:** The EPUB and PDF may use different layout rules, but titles, hierarchy, emphasis, references, captions and publication details should remain consistent. Do not force the EPUB to mimic the PDF's fixed pages.
- **Proofing:** Review representative pages and sections, including long paragraphs, headings, quotations, lists, footnotes, tables, images and references. Inspect the EPUB at several font sizes and screen widths, and inspect the PDF both at normal screen size and in a test print where practicable.

Final font and size choices should be recorded in the export stylesheet or build configuration so that future editions can reproduce them. They must be confirmed by reviewing the actual exported files; this plan does not claim that any particular typeface or setting has already passed testing.


### Editorial design and book-production conventions

The finished publication should feel considered, coherent and appropriate to its subject. Design decisions should serve the author's text and the reader, not compete with them. The following checks apply to the cover, interior layout and treatment of scholarly material.

- **Cover design:** Use a clear visual idea related to the book's subject and context. Establish an obvious order of importance between title, subtitle and author name. Check the title at thumbnail size as well as full size. Use a limited, deliberate colour palette, legible type and imagery that is relevant and properly sourced. Avoid unnecessary effects, ornamental elements and visual details that do not contribute to the book's identity.
- **Typography on the cover:** Choose typefaces suited to the subject and the period or character of the work. Use a restrained combination of typefaces and weights, carefully adjust line breaks and spacing, and ensure that the author's name and title remain readable at small sizes. Check spelling and punctuation directly against the approved title and publication details.
- **Page design:** Establish a consistent page grid, margins and text area for the PDF. Align headings, paragraphs, quotations, images, captions and notes with a clear underlying system. Use white space to separate meaningful parts of the text; avoid both cramped pages and arbitrary gaps.
- **Opening pages:** Keep the half-title and title pages simple. Give the title, author and publisher appropriate visual prominence. Present copyright, ISBN, edition, publication date and credits in a consistent, unobtrusive form. Include only front matter that has a clear purpose and verified content.
- **Article and chapter openings:** Start each major article or chapter consistently. Give its title sufficient space, but avoid oversized headings or large empty areas that waste pages. Use a drop cap only if it suits the book and remains legible and accessible; it is not required.
- **Paragraphs and indentation:** Choose one main paragraph system and apply it consistently. For continuous prose, first-line indentation can distinguish paragraphs without adding gaps between every paragraph; alternatively, modest paragraph spacing may be used where it improves readability. Avoid an unintended mixture of indentation and large paragraph gaps.
- **Running heads and page numbers:** For PDF, use restrained running heads only where they help readers navigate, such as the book title on one side and the current article or section title on the other. Keep folios consistently positioned and ensure that they do not appear on pages where they would be inappropriate, such as a deliberately unnumbered title page. Do not add fixed page numbers to the reflowable EPUB body.
- **Footnotes and endnotes:** Preserve every note and its connection to the relevant passage. Use sequential numbering consistently and distinguish note markers clearly from the surrounding text. In PDF, set notes in a readable, slightly smaller type size than the body text, with adequate line spacing and a clear separation from the main text. Keep each note close to its reference where practical; prevent notes from being clipped or separated confusingly across pages. In EPUB, make note references and note text navigable in both directions where the format and tooling permit. If endnotes are chosen instead, organise them consistently and provide links back to the cited passages where possible.
- **References and citations:** Follow one consistent citation system appropriate to the material. Preserve complete bibliographic details and the original author's citation intent. Apply consistent punctuation, italics, quotation marks, dates, page ranges and treatment of web sources. Distinguish source notes from explanatory notes and do not silently convert one citation style into another.
- **Block quotations:** Set long quotations apart from the main text using consistent indentation and spacing. Do not rely on quotation marks alone to signal a long extract if the design can make its status clearer. Preserve attribution and verify the wording against the source.
- **Tables, lists and illustrations:** Keep tables readable and prevent columns from being squeezed or cut off. Repeat table headings when a table continues across PDF pages where the layout system supports it. Keep lists aligned and consistently spaced. Place figures near the relevant discussion where possible, use captions consistently, and check that images remain clear at normal viewing size.
- **Colour and ornament:** Use colour sparingly and for a defined purpose. Ensure sufficient contrast in text, links and labels, and check the design in greyscale where relevant. Avoid gradients, shadows, decorative borders, badges or other effects unless they have a clear editorial function. A restrained design is not a substitute for careful typesetting.
- **Consistency of detail:** Standardise quotation marks, apostrophes, dashes, ellipses, spacing around punctuation, number ranges, abbreviations, capitalisation, dates and spelling variants. Use non-breaking spaces or other typographic controls only where needed to prevent awkward breaks, and check that they do not create problems in EPUB reflow.
- **Cover and interior as one publication:** The cover, title page, metadata, running heads, notes and publication hub should agree on the exact title, subtitle, author credit, publisher and edition. The cover can have its own visual character, but the publication should not look like unrelated pieces assembled together.
- **Final visual proof:** Review the cover at thumbnail size; inspect the title and copyright pages; review ordinary text pages, article openings, pages with notes, references, tables and images; and inspect the last pages. Check the PDF at normal size and in a test print where possible. Review the EPUB on different screen sizes and with enlarged text. Correct specific problems rather than applying decorative styling to every page.

These are editorial production criteria, not fixed templates. The appropriate choices depend on the book's subject, source material and format. Any final design should be judged by the actual pages and files, with readability, accuracy and consistency taking precedence over novelty.

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


## Work Log

- **14 October 2026** - Created the e-book export documentation page and recorded the initial aim of producing EPUB and PDF editions from selected TSAP articles while preserving the original website pages.
- **2 November 2026** - Expanded the production documentation with standards for manuscript consolidation, book structure and navigation, pagination, page breaks, editorial consistency, typography, font selection, cover and interior design, paragraph treatment, notes, references, illustrations, metadata, technical validation and ongoing maintenance.
- **2 November 2026** - Reviewed the nine full-text essay source files and identified their current source paths in the TSAP repository.
- **2 November 2026** - An initial production branch was created during preparation, but its pull request was closed without merging. The live website article pages were not changed by that pull request.
- **2 November 2026** - Added the nine-essay manifest directly to `main`, selecting the works in the specified TSAP category and arranging them chronologically. The manifest now points to dedicated full-text files where they exist; some within-year ordering remains provisional because exact publication dates have not yet been established.
- **2 November 2026** - The initial build script was found to be missing from `main`. A replacement `build.py` was committed directly to `main`. It assembles the nine source texts into a separate manuscript, removes website-generated contents lists and front matter, and invokes Pandoc for EPUB and PDF output when the required tools are installed. This script still requires a successful build and output review before release.
- **2 November 2026** - Added initial EPUB typography rules and provisional technical metadata. The cover, half-title, full title page, foreword and other preliminary matter remain outside the current build scope.
- **2 November 2026** - Pull request [#58](https://github.com/sunilabrahamindia/sunilabraham/pull/58) was closed without merging after it was created in error. The production files are now being committed directly to `main`, as originally intended.
- **2 November 2026** - Added a GitHub Actions workflow on `main` to build the manuscript, EPUB and PDF and publish them as a downloadable workflow artifact. The workflow has been added but has not yet been confirmed successful. The final files must still be checked against all nine sources, including notes, references, navigation, PDF layout and format-specific ISBN treatment. No ISBN has been inserted into the provisional metadata.


- **2 November 2026 - Entry 10: Production files and their purpose.** The following files are in the repository under `ebook/edrl-ii/`. They are production/configuration files, not new public TSAP article pages:
  - **Created `ebook/edrl-ii/README.md`:** records the working scope, build instructions and checks.
  - **Modified `ebook/edrl-ii/manifest.yml`:** corrected source paths for five essays to use dedicated full-text files where available. It lists the nine selected essays and their proposed chronological order. The relative order of the two 1988 essays remains provisional because one source has only a year-level date.
  - **Created `ebook/edrl-ii/metadata.yml`:** stores provisional title, author/imprint and language metadata. Cover and preliminary pages remain out of scope for the current essay-only build; no ISBN was inserted.
  - **Created `ebook/edrl-ii/epub.css`:** provides initial EPUB styling. It has not yet been validated in a finished EPUB.
  - **Created `ebook/edrl-ii/build.sh`:** launcher that runs `python3 ebook/edrl-ii/build.py`.
  - **Created `ebook/edrl-ii/build.py`:** reads the manifest, extracts and combines the nine essay texts into `ebook/edrl-ii/output/manuscript.md`, and calls Pandoc to attempt EPUB and PDF generation when the necessary tools are installed. Its extraction and output still need verification.
  - **Created `.github/workflows/build-edrl-ii.yml`:** configures GitHub Actions to install Pandoc and a PDF engine, run the builder, and upload the manuscript and generated files as a workflow artifact. A configured workflow is not proof of a successful build.
- **2 November 2026 - Entry 11: Misleading commit summaries in Recent Changes.** Several production-file commits used the same summary, `Add EDRL II e-book production file directly to main`. This was a mistake: the site's Recent Changes page treats summaries beginning with `Add` as page-creation activity, so these file operations appeared misleadingly as "Created" entries with "0 changed files". The repository changes concerned the seven paths documented above, not seven new public pages, and did not intentionally edit the nine original essay pages. For future commits, summaries must describe the specific action and file or purpose, and must not start with `Add` where that causes the Recent Changes page to misclassify the activity.
- **2 November 2026 - Entry 12: Build status and next checks.** The manifest, builder and workflow are present in the repository, but the final EPUB/PDF are not confirmed as complete or approved. Check the GitHub Actions result, verify that all nine essays and their notes/references were extracted correctly, inspect the manuscript, validate EPUB navigation and accessibility, review PDF pagination and typography, and confirm the correct ISBN treatment for each format. Do not announce or describe the e-books as ready until these checks are complete.


- **2 November 2026 - Entry 13: Front matter and professional preview edition.** The user authorised direct changes on `main` and explicitly instructed that no new pull request be created. Created `ebook/edrl-ii/front-matter.md` with a half-title, full title page, publication-details page, foreword placeholder and editor's-note placeholder. The placeholder copy is clearly labelled and does not invent the missing foreword or editorial note. The EPUB ISBN `978-93-345-1180-2` is recorded as the e-book identifier; the paperback ISBN is not substituted. The publication date is marked as the planned date, 29 November 2026. Final copyright/rights language remains pending confirmation.
- **2 November 2026 - Entry 14: Manuscript extraction and note preservation safeguards.** Reworked `ebook/edrl-ii/build.py` to remove website introductions and generated contents lists, extract the actual essay body, retain notes that appear before or after publication metadata, strip site navigation and style blocks, and check that the number of HTML footnote references and note bodies is not reduced during extraction. Added EPUB package/ZIP, metadata and chapter checks. These automated checks are safeguards; they do not replace reading every essay and checking every note link in the generated files.
- **2 November 2026 - Entry 15: Preview metadata and reflowable styling.** Updated `ebook/edrl-ii/metadata.yml` with the confirmed e-book ISBN, planned publication date and provisional preview rights wording. Revised `ebook/edrl-ii/epub.css` to use readable line spacing, consistent headings and links, and reflow-friendly image/table rules while leaving typeface and text-size control to the reader. Updated `ebook/edrl-ii/README.md` with the new scope, files, build instructions and quality gates.
- **2 November 2026 - Entry 16: Workflow correction.** Revised `.github/workflows/build-edrl-ii.yml` so the build listens to changes on `main` in the e-book directory, the source essays and the workflow itself, and names the output as an editorial preview rather than a finished publication. The workflow is triggered by relevant pushes or manually from Actions; it is not scheduled. Its next run must complete successfully before the new preview artifact can be considered available.
- **2 November 2026 - Entry 17: Production quality and remaining limits.** The current build pipeline aims to create a readable preview with front matter and all nine essays, but a successful automated run alone cannot establish trade-publisher quality. The generated EPUB still requires human inspection in reading applications, and full EPUBCheck validation and page-by-page PDF proofing remain required. Cover artwork has intentionally not been invented; cover design, the final foreword, the final editor's note, final rights statement, and confirmation of the provisional 1988 ordering remain outstanding. No pull request was created for these direct-to-main edits.


- **2 November 2026 - Entry 18: First successful editorial-preview build and artifact retrieval.** GitHub Actions run [Build EDRL II editorial preview #9](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/41497619659) completed with **Success** on `main`, at commit `375472e14dcb6ea54d417eebd3315d27142c03e5` (commit summary: `Document EDRL II front matter and quality-control revisions`). The build job completed in approximately 1 minute 46 seconds; the workflow run took approximately 1 minute 50 seconds. GitHub reported one artifact, `edrl-ii-editorial-preview`, artifact ID `13167820610`, with a ZIP size of 543,117 bytes and expiry on 2 December 2026. The artifact was retrieved and its contents were made available for review: `edrl-ii-preview.epub`, `edrl-ii-preview.pdf`, and `manuscript.md`. This confirms that the configured workflow completed and produced the preview package; it does not confirm that the book is publication-ready or that all editorial and note links have passed human proofing.
- **2 November 2026 - Entry 19: Mobile download friction and delivery distinction.** The user was unable to obtain the artifact reliably through the Android/GitHub mobile flow. An unauthenticated direct GitHub API URL displayed a `401 Requires authentication` response; this was an unsuitable link to give the user. The artifact is currently a GitHub Actions ZIP artifact, not a standalone EPUB file committed to the repository or attached to a GitHub Release. The EPUB was separately retrieved from the artifact and provided in the ChatGPT conversation for review, but this is a workaround rather than the ideal GitHub-native delivery route. Future delivery should make the intended download route explicit and, if requested, consider a stable GitHub Release asset or another clearly documented distribution method. Do not imply that a successful workflow automatically places the EPUB in the repository's `ebook/edrl-ii/` directory.
- **2 November 2026 - Entry 20: Current review status after successful build.** The next stage is to inspect the actual EPUB, PDF and assembled manuscript, compare essay extraction against the source pages, and verify footnote references and note bodies, EPUB navigation, reading-system rendering, accessibility/reflow, and PDF pagination. The automated checks currently in `build.py` are useful safeguards but are not a full EPUBCheck report or a substitute for human proofing. Cover design, approved foreword, approved editor's note, final rights statement and confirmation of the relative order of the two 1988 essays remain outstanding. No new pull request was created for the direct-to-`main` changes.


- **3 November 2026 - Entry 21: Front-matter typography and book credits revision.** Following the user's review in Readera and Foliate, revised `ebook/edrl-ii/front-matter.md` and `ebook/edrl-ii/epub.css` to replace the plain sequence of headings and paragraphs with deliberately structured half-title, full title page, copyright/publication details, credits, foreword placeholder and editor's-note placeholder. The title and author are centred, the imprint is positioned separately towards the foot of the title-page composition, and a restrained typographic rule separates title and author. Publication details and production credits are distinct sections; unconfirmed contributors, cover design and rights wording are explicitly marked pending rather than invented. The CSS uses relative sizing and reflow-oriented rules and leaves font family, font size and colour controls to the reading application. Updated `ebook/edrl-ii/build.py` to enable Pandoc's `fenced_divs` Markdown extension so the front-matter classes are retained during EPUB/PDF conversion, and updated the production README. This is an editorial design revision based on established book-design conventions, not an attempt to copy a publisher's proprietary identity.
- **3 November 2026 - Entry 22: Front-matter rendering verification pending.** The revised source files have been committed directly to `main`; the workflow should generate a new preview from this push. The prior EPUB does not include these latest changes. Inspect the new EPUB in Readera and Foliate before deciding whether the title-page layout behaves consistently: EPUB reading systems may interpret CSS flex layout and viewport-height units differently. If either app collapses the vertical composition or ignores page breaks, simplify the layout to robust block styling and retest. Confirm the new build result and artefact before sharing a new download. No pull request was created.

{% include navbox-amaa.html %}


- **3 November 2026 - Entry 23: Publication details and half-title revision.** Added the confirmed editor credit, the project website and the planned publication date in DMY display format to the publication-details page. Reworked the half-title to follow the traditional convention of showing the book title alone, without author or imprint decoration. Removed the CSS flex and viewport-height composition that could behave inconsistently across EPUB readers. For the fixed-layout PDF, added a print-specific blank verso after the half-title using a LaTeX-only block; this block is ignored by EPUB, where artificial blank pages are not appropriate because pagination is controlled by the reading system. The full title page remains a separate page with the author and imprint. Rebuild and inspect the new EPUB in Readera and Foliate, and proof the PDF page sequence before treating the layout as approved.
