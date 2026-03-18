---
layout: default
title: "Site Structure"
description: "Overview of the directory and file structure of The Sunil Abraham Project (TSAP) repository."
categories: [TSAP Documentation]
permalink: /tsap/structure/
created: 2026-03-18
---

The **site structure** documents the directory and file structure of the TSAP repository. Understanding the structure helps contributors find the right place for new content, assets, and configuration.

The repository is hosted on GitHub and built with Jekyll. Most directories map directly to sections of the live site; others are Jekyll-specific and do not appear as pages.

## Jekyll System Directories

These directories are used by Jekyll internally and are not published as pages directly.

### `_data`
Stores structured data files in YAML, JSON, or CSV format. Jekyll makes these available to templates via the `site.data` variable. Used for things like navigation menus, author lists, or reusable reference data. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/_data)

### `_includes`
Contains reusable HTML snippets inserted into layouts or pages via Jekyll's include tag. Common includes are headers, footers, and navigation components. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/_includes)

### `_layouts`
Contains HTML layout templates that wrap page content. TSAP pages use `layout: default`, which refers to `_layouts/default.html`. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/_layouts)

## Content Directories

These directories contain the main published content of the site.

### `ai`
Content related to artificial intelligence topics within TSAP's scope. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/ai)

### `amaa`
Pages related to Rev. Athanasius Mathen Abraham Ayrookuzhiel (A. M. A. Ayrookuzhiel). The primary biographical entry is at `/amaa/`. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/amaa)

### `articles`
Long-form articles written or curated for the project. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/articles)

### `categories`
Auto-generated or manually maintained category index pages. Each category listed in a page's `categories` front matter corresponds to a page here. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/categories)

### `clusters`
Thematic groupings of related pages or subjects that do not fit a single category. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/clusters)

### `events`
Pages documenting events connected to Sunil Abraham or TSAP's subject areas. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/events)

### `ideas-and-opinions`
Opinion pieces, commentary, and exploratory writing published under TSAP. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/ideas-and-opinions)

### `media`
Media coverage, press mentions, and related content. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/media)

### `mentions`
Pages tracking references to Sunil Abraham or TSAP in external sources. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/mentions)

### `projects`
Documentation of projects associated with Sunil Abraham or TSAP. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/projects)

### `publications`
Pages for books, papers, reports, and other formal publications. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/publications)

### `resources`
Reference material, reading lists, and external resources curated for the project. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/resources)

### `sandbox`
A working area for drafts, experiments, and pages under development. Content here is not considered final. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/sandbox)

### `sunil`
Pages specifically about Sunil Abraham — biography, profile, and related content. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/sunil)

### `tsap`
Documentation and meta-pages about the project itself, including this page. All help and style guide pages live here. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/tsap)

### `versions`
Archives or versioned snapshots of pages or documents. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/versions)

### `videos`
Pages for video content associated with TSAP or Sunil Abraham. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/videos)

## Asset Directory

### `assets`
Static files served directly to the browser. Typically organised into subdirectories: [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/assets)

- `assets/images/` — photographs, illustrations, and diagrams used across pages
- `assets/css/` — stylesheets
- `assets/js/` — JavaScript files, if any

## Short Links Directory

### `_short`
Used to manage short redirect URLs for the site. Pages here map a short path to a longer destination URL. [View on GitHub](https://github.com/sunilabrahamindia/sunilabraham/tree/main/_short)

## Root Files

These files sit at the root of the repository and serve specific functions.

| File | Purpose |
|:-----|:--------|
| [`index.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/index.md) | The site homepage |
| [`_config.yml`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/_config.yml) | Jekyll configuration — site title, URL, plugins, build settings |
| [`CNAME`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/CNAME) | Maps a custom domain to the GitHub Pages site |
| [`README.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/README.md) | Project description shown on the GitHub repository page; not published to the site |
| [`robots.txt`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/robots.txt) | Instructs search engine crawlers which pages to index or ignore |
| [`contact.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/contact.md) | Contact page |
| [`disclaimer.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/disclaimer.md) | Legal disclaimer |
| [`privacy.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/privacy.md) | Privacy policy |
| [`maintenance.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/maintenance.md) | Displayed when the site is under maintenance |
| [`sitemap.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/sitemap.md) | Human-readable sitemap of the site |
| [`newest.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/newest.md) | Lists the most recently added or updated pages |
| [`otd.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/otd.md) | On this day — date-based content feature |
| [`random.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/random.md) | Redirects or loads a random page from the site |
| [`shortcuts.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/shortcuts.md) | Lists available short URLs |
| [`tsapdays.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/tsapdays.md) | Content related to TSAP Days, a recurring feature or event series |

## Notes for TSAP Contributors

- New content pages should be placed in the most specific matching directory (e.g., a biography goes in `sunil/` or `amaa/`, not in `articles/`).
- Do not place draft content in published directories; use `sandbox/` instead.
- Asset files should always go into `assets/` with an appropriate subdirectory; never store images inside content directories.
- Changes to `_config.yml` affect the entire site build and should be made with care.
- Follow the [TSAP Manual of Style](/tsap/manual-of-style/) for all content pages.

<style>
article pre, .content pre, main pre {
  overflow-x: auto;
  white-space: pre;
  max-width: 100%;
}

@media (max-width: 600px) {
  article pre, .content pre, main pre {
    font-size: 0.85rem;
  }

  table {
    font-size: 0.875rem;
  }
}
</style>
