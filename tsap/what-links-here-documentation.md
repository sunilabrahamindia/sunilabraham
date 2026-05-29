---

layout: default
title: "What Links Here (Documentation)"
description: "Documentation for the What Links Here tool on The Sunil Abraham Project (TSAP), including its purpose, architecture, workflow, and development history."
categories: [TSAP Documentation]
permalink: /tsap/what-links-here-documentation/
created: 2026-05-29
---

The **What Links Here** tool is a navigation and maintenance utility on The Sunil Abraham Project (TSAP). It allows readers and editors to select a page and view other pages across the site that link to it.

The tool serves several purposes. It helps readers discover related content, assists editors in understanding relationships between pages, identifies orphaned or poorly linked content, reveals broken internal links, and provides a practical way to audit the structure of the site. Although primarily designed as a reader-facing navigation aid, it has also proved useful as a quality-control mechanism, helping identify incorrect URLs, outdated links, duplicate targets, and other structural issues across the repository.

The tool forms part of a broader effort to create Wikipedia-inspired navigation and maintenance utilities for TSAP. As the site has expanded to include thousands of pages across articles, publications, media reports, portals, events, photographs, and documentation pages, understanding how content is interconnected has become increasingly important. The What Links Here tool provides a practical way to explore those relationships while supporting ongoing editorial and maintenance work.

The implementation was developed with support from ChatGPT and Claude. All design decisions, testing, editorial judgement, and final implementation choices were made by the project maintainer.

## Background

As The Sunil Abraham Project grew, manually determining which pages linked to a particular article or publication became increasingly difficult. Internal links existed across a wide range of content types, including articles, publications, media reports, events, portals, and documentation pages. While the links themselves were valuable, there was no easy way to view them from the perspective of the destination page.

The idea behind What Links Here was to create a dedicated tool that could automatically identify and display these relationships. Instead of manually searching through the repository, readers and editors could simply select a page and immediately view other pages that link to it.

The project also supports a broader long-term goal of developing a collection of navigation, maintenance, and editorial tools under the `/tools/` section of the site.

## Architecture

The What Links Here system consists of three components working together.

First, a Python script generates backlink data by scanning content across the repository and identifying internal links. This script is executed manually whenever backlink data needs to be refreshed:

```bash
python3 scripts/generate_backlinks.py
```

The script produces a structured backlink index stored in:

```text
_data/backlinks.yml
```

The generated file uses a target-to-sources structure:

```yaml
/target-page/:
  - /page-linking-to-it/
  - /another-page-linking-to-it/
```

Each key represents a destination page, while the associated list contains pages that link to that destination.

The third component is the user-facing interface located at:

```text
/tools/what-links-here/
```

The page reads data from `_data/backlinks.yml`, resolves page titles where possible, builds a page selector, and displays backlink relationships dynamically within the browser. The interface currently supports page selection, backlink counts, search filtering, sorting, mobile-responsive layouts, accessibility enhancements, and direct linking through URL hashes.

This architecture separates data generation from presentation. The backlink data is generated offline, committed to the repository, and then consumed by a lightweight client-side interface.

## Development History

### 29 May 2026

The first public version of the What Links Here tool was developed and deployed on 29 May 2026.

Development began with the creation of a dedicated backlink-generation workflow. A Python script (`scripts/generate_backlinks.py`) was developed to scan site content, identify internal links, and generate a structured backlink index. The generated data was written to `_data/backlinks.yml`, which became the primary data source for the project.

The initial prototype was intentionally simple and displayed backlinks for a single fixed page. Once the underlying data model had been validated, the implementation was expanded to support dynamic page selection, allowing readers to choose any indexed page from a dropdown list.

Subsequent development focused on title resolution, search filtering, sorting, backlink counts, accessibility improvements, and mobile responsiveness. Several interface approaches were explored before a working implementation was achieved.

An unexpected benefit of the project was its usefulness as a repository auditing tool. During testing, the system revealed a number of incorrect, outdated, duplicate, and malformed internal links that would otherwise have been difficult to locate manually. Examples included references to non-existent paths, incorrect assumptions about page locations, duplicate representations of the same target page, and legacy links that no longer reflected the site's structure.

As a result, the tool quickly proved valuable not only as a navigation aid but also as a maintenance and quality-control utility.

The initial public version remains a working draft. While the core functionality is operational, additional refinement and cleanup are expected as the site continues to evolve.

## Maintenance Workflow

Whenever pages are added, moved, renamed, or modified in ways that affect internal links, the backlink index should be regenerated.

The recommended workflow is:

1. Create or modify content.
2. Run:

   ```bash
   python3 scripts/generate_backlinks.py
   ```
3. Verify that `_data/backlinks.yml` has been regenerated successfully.
4. Review any unexpected additions or removals.
5. Commit the updated files.
6. Push changes to GitHub.

Once deployed, the What Links Here page automatically uses the updated backlink data.

## Known Limitations

As of the initial deployment, several limitations remain.

Some pages may occasionally appear as unresolved even when valid content exists. Duplicate target representations may also appear in certain situations where multiple URL forms refer to the same page. Historical content may contain malformed or outdated internal links that surface through the backlink index. The user interface also remains under active development and may continue to change as additional testing and refinement take place.

These limitations are expected to be addressed gradually as the tool matures and the site's internal link structure continues to improve.
