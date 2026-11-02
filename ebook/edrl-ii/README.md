# E-book production: Essays on Dalits, Religion and Liberation II

This directory contains a separate production workflow for the nine full-text essays. It does not alter the original TSAP article pages.

## Scope

- Include the nine full-text sources listed in `manifest.yml`.
- Arrange them by original publication date, oldest first.
- Exclude each website page's YAML front matter, introductory page description, website-generated contents list, navigation and Jekyll interface elements.
- Preserve the essay text, substantive headings, quotations, lists, notes, references, meaningful links and source images where technically possible.
- Generate one consolidated Markdown manuscript, then EPUB 3 and PDF from that manuscript.
- Do not add the cover, half-title, full title page, foreword or other preliminary matter in this first pass.

## Current ordering decisions

The manifest records the bibliographic dates currently documented on TSAP. Some sources give only a year rather than a month or day. Where the original publication date cannot be established more precisely from the available records, the order within that year is provisional and is marked in the manifest. Do not interpret a website page's `created` date as the essay's original publication date.

The proposed chronological order is:
1. Indian Religious Heritage and Social Transformation: Change of Perspective within the CISRS (March–June 1993)
2. Christian Dalits in Revolt (July 1993)
3. Religious Legitimation and Delegitimations of Social Relations of Power (of Caste): The Case of the Dalits in Historical Perspective (December 1993)
4. The Dalits, Religions and Inter-faith Dialogue (1994; month not stated)
5. The Role of Religion in Dalit Liberation: Some Reflections (1994; month not stated)
6. A Proposal for the Study of the Religious Heritage of the Dalits: Some Methodological Considerations (March 1995)
7. Chinna Pulayan: The Dalit Teacher of Sankaracharya (1996; exact publication date not stated)
8. The Religious Factor in Dalit Liberation: Some Reflections (1996; exact publication date not stated)
9. The Dalit Church's Mission — A Dalit Response (September 1996)

The ordering of the two 1994 essays and the first two 1996 essays should be revisited if reliable evidence establishes their exact publication dates. The September 1996 date for the final essay is explicit; the exact order of the two other 1996 essays is not yet established.

## Requirements

Use Python 3, Pandoc and a PDF engine supported by the installed Pandoc version. The first PDF build uses Typst if available. If Typst is not installed, the script will still produce the manuscript and EPUB, then report that PDF generation was skipped.

Install Pandoc and (for PDF) Typst on Ubuntu using the official package instructions for the versions available on your system. Do not install or run software as root unless you understand the command and trust the source.

## Build

From the root of the cloned TSAP repository:

```bash
python3 ebook/edrl-ii/build.py
```

Or:

```bash
bash ebook/edrl-ii/build.sh
```

The build writes files to `ebook/edrl-ii/output/`. The generated manuscript is saved as `ebook/edrl-ii/manuscript.md`.

## Review before publication

A successful build is not proof that the book is publication-ready. Check the generated files for:
- all nine essays, in the intended order, with no missing or duplicated text;
- removal of website introductions and duplicate contents lists;
- preserved notes and references, and working note links;
- correct handling of headings, tables, quotations, images and special characters;
- EPUB navigation and reflow at multiple font sizes;
- PDF page breaks, margins, running text, headings, page numbers and any widows/orphans;
- bibliographic details against original publication records.

The output directory is a build product, not a substitute for review. Keep the original article pages unchanged.
