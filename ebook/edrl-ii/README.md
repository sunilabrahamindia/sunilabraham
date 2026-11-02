# E-book production: Essays on Dalits, Religion and Liberation II

This directory contains a separate production workflow for the proposed full-text essays. It does not alter the original TSAP article pages.

## Scope

- Include the full-text sources listed in `manifest.yml`.
- Arrange them by original publication date, oldest first.
- Exclude each website page's YAML front matter, introductory page description, website-generated contents list, navigation and Jekyll interface elements.
- Preserve the essay text, substantive headings, quotations, lists, notes, references, meaningful links and source images where technically possible.
- Generate one consolidated Markdown manuscript, then EPUB 3 and PDF from that manuscript.
- Do not add the cover, half-title, full title page, foreword or other preliminary matter in this first pass.

## Selection and chronological order

The selection is drawn exclusively from the TSAP category [Writings not in Essays on Dalits, Religion and Liberation](https://sunilabraham.in/categories/writings-not-in-essays-on-dalits-religion-and-liberation/). Do not add an essay unless its source page belongs to that category. The category excludes book reviews and other material.

The manifest currently contains these nine category members, ordered by original publication date, oldest first:

1. The State of Hinduism in 2000 A.D.—Some Emerging Trends (April–June 1977)
2. Religion, Spirituality and Aspirations of the People (March 1978)
3. The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue (March 1979)
4. The Church and the Study of Religion (September 1981)
5. Religions and the Aspirations of the People (September–December 1983)
6. Religion: A Way of Salvation or an Ideology of Oppression? (March 1985)
7. Dalit Theology: A Movement of Counter-Culture (1988; exact date not stated)
8. Dalit Liberation — Some Reflections on Their Ideological Predicament (June 1988)
9. The Ideological Nature of the Emerging Dalit Consciousness (September 1990)

The relative order of the two 1988 works is provisional because one source records only the year. Do not use a website page's `created` date as the essay's original publication date.

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
- all essays listed in the manifest, in the intended order, with no missing or duplicated text;
- removal of website introductions and duplicate contents lists;
- preserved notes and references, and working note links;
- correct handling of headings, tables, quotations, images and special characters;
- EPUB navigation and reflow at multiple font sizes;
- PDF page breaks, margins, running text, headings, page numbers and any widows/orphans;
- bibliographic details against original publication records.

The output directory is a build product, not a substitute for review. Keep the original article pages unchanged.
