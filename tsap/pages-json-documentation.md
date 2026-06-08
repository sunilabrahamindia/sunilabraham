---
layout: default
title: "Pages Index (pages.json) Documentation"
description: "Documentation for the pages.json content index used by The Sunil Abraham Project (TSAP)."
categories: [TSAP Documentation]
permalink: /tsap/pages-json-documentation/
created: 2026-06-08
---

{% include documentation-notice.html %}

The **Pages Index** is a machine-readable catalogue of content published on The Sunil Abraham Project (TSAP). It is generated automatically from page front matter and exported as a JSON file named `pages.json`.

The purpose of the Pages Index is to provide a structured representation of TSAP content that can be consumed by external tools, bots, scripts, search systems, and future applications without requiring direct access to Jekyll internals or repository source files.

The implementation was developed with support from ChatGPT. All design decisions, testing, debugging, editorial judgement, and final implementation choices were made by the project maintainer.

## Background

As TSAP grew beyond one thousand pages, it became increasingly desirable to expose a structured list of published content.

Human readers can navigate the website through categories, internal links, search engines, and navigation menus. Software tools, however, require a structured source of information.

Several future use cases were identified:

* Telegram bot integration.
* Search and discovery tools.
* Research utilities.
* Content analysis.
* Statistics and reporting.
* External applications consuming TSAP metadata.

A machine-readable index became increasingly useful as the project expanded.

## Why Earlier Approaches Were Limited

The first instinct was to allow tools to examine repository files directly.

Although possible, this approach has several disadvantages.

A tool would need to:

* Read Markdown files.
* Parse front matter.
* Understand Jekyll conventions.
* Reconstruct URLs.
* Determine which pages should be included.
* Handle future structural changes.

This creates unnecessary complexity and tightly couples external tools to repository internals.

A simpler approach is to generate a dedicated content index once and allow tools to consume that index.

The Pages Index was created to solve this problem.

## Architecture

The Pages Index is generated from page front matter.

The script scans Markdown files throughout the repository and extracts selected metadata fields.

Only pages containing a `created` field are included.

This rule was chosen because:

* TSAP pages are expected to contain a `created` field.
* Utility pages and temporary files can be excluded naturally.
* The resulting index focuses on published content.

The process is:

```text
Markdown Files
        ↓
Front Matter Extraction
        ↓
Metadata Selection
        ↓
pages.json Generation
        ↓
Publication
```

The generated file becomes a structured catalogue of TSAP content.

## Script Location

The generator script is located at:

```text
scripts/generate_pages_json.py
```

The script is intended to be run manually whenever the content index requires regeneration.

## Generated File

The output file is:

```text
pages.json
```

It is written to the repository root and published automatically by GitHub Pages.

Published URL:

```text
https://sunilabraham.in/pages.json
```

## Included Metadata

Each indexed page may contain:

```json
{
  "title": "Example Page",
  "description": "Example description",
  "created": "2026-06-08",
  "date": "2026-05-01",
  "source": "Example Source",
  "authors": ["Example Author"],
  "categories": ["Example Category"],
  "permalink": "https://sunilabraham.in/example-page/"
}
```

The following fields are exported when available:

* title
* description
* created
* date
* source
* authors
* categories
* permalink

## Generator Script

The current implementation is:

```python
import os
import json
import yaml

SITE_URL = "https://sunilabraham.in"

pages = []

for root, dirs, files in os.walk("."):
    if ".git" in root:
        continue

    for file in files:
        if not file.endswith((".md", ".markdown")):
            continue

        path = os.path.join(root, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.startswith("---"):
                continue

            parts = content.split("---", 2)

            if len(parts) < 3:
                continue

            front_matter = yaml.safe_load(parts[1])

            if not isinstance(front_matter, dict):
                continue

            created = front_matter.get("created")

            if not created:
                continue

            title = front_matter.get("title")
            description = front_matter.get("description")
            date = front_matter.get("date")
            source = front_matter.get("source")
            authors = front_matter.get("authors")
            categories = front_matter.get("categories")
            permalink = front_matter.get("permalink")

            if permalink:
                permalink = SITE_URL.rstrip("/") + permalink
            else:
                permalink = None

            page = {
                "title": title,
                "description": description,
                "created": str(created),
                "date": str(date) if date else None,
                "source": source,
                "authors": authors,
                "categories": categories,
                "permalink": permalink
            }

            pages.append(page)

        except Exception as e:
            print(f"Skipping {path}: {e}")

pages.sort(
    key=lambda x: x.get("created") or "",
    reverse=True
)

with open("pages.json", "w", encoding="utf-8") as f:
    json.dump(
        pages,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Created pages.json with {len(pages)} pages.")
```

## Installation Requirements

The script was designed to remain lightweight and portable.

Requirements:

* Python 3
* PyYAML

On Ubuntu:

```bash
sudo apt install python3-yaml
```

or within a Python virtual environment:

```bash
pip install pyyaml
```

No database is required.

No Jekyll plugin is required.

No GitHub Actions workflow is required.

## Running the Generator

Navigate to the repository root:

```bash
cd ~/Projects/sunilabraham
```

Run:

```bash
python scripts/generate_pages_json.py
```

Typical output:

```text
Created pages.json with 1048 pages.
```

## First Successful Build

The first successful generation occurred on 8 June 2026.

Results:

```text
Created pages.json with 1048 pages.
```

Generated file size:

```text
576 KB
```

This demonstrated that a machine-readable index of the entire project could be generated efficiently while remaining small enough for rapid download.

## Maintenance Workflow

Recommended workflow:

```bash
python scripts/generate_pages_json.py

git add pages.json

git commit -m "Update pages index"

git push
```

This ensures that the published index remains synchronised with site content.

## Current Uses

The Pages Index was originally created to support project retrieval systems.

Current use cases include:

* content discovery
* metadata retrieval
* project statistics
* external tooling
* bot integration

Future tools may consume the same index without requiring access to repository source files.

## Advantages and Limitations

Advantages:

* Simple architecture.
* Human-readable output.
* Machine-readable output.
* No database required.
* No build plugins required.
* Compatible with GitHub Pages.
* Lightweight and portable.

Limitations:

* Requires manual regeneration.
* Newly created pages will not appear until the index is regenerated.
* Only pages containing a `created` field are included.
* Metadata quality depends upon front matter quality.

These limitations are considered acceptable given the project's emphasis on simplicity and maintainability.

## Future Improvements

Potential future enhancements include:

* automatic generation during deployment
* additional metadata fields
* filtering options
* specialised indexes
* category-specific exports
* author-specific exports
* change tracking

Any future development should continue to prioritise transparency, portability, and compatibility with GitHub Pages.

## Lessons Learned

The development of the Pages Index reinforced an important architectural lesson.

The most valuable improvement was not adding another AI model or another search interface.

The most valuable improvement was creating a structured representation of TSAP's own content.

By transforming page metadata into a machine-readable index, TSAP content becomes accessible to future tools, bots, reports, and retrieval systems while remaining entirely within the project's existing static-site architecture.

Future development should continue to favour structured project data and retrieval mechanisms wherever practical.
