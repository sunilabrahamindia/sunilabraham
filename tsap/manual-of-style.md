---
layout: default
title: "Manual of Style"
description: "Writing and formatting standards for The Sunil Abraham Project (TSAP)."
categories: [TSAP Documentation]
permalink: /tsap/manual-of-style/
created: 2026-03-18
---

The **Manual of Style** page defines the writing and formatting standards followed across The Sunil Abraham Project (TSAP). The aim is to ensure consistency, readability, and long-term maintainability across all pages.

**Note:** This documentation is evolving and may change as the project develops.

## Language and Spelling

- Use Indian English / British English spelling (e.g. "centre", not "center"; "colour", not "color"; "organisation", not "organization").
- Avoid American spellings unless part of a quoted source (e.g. retain "color", "program", "defense" if present in original text).
- Maintain consistent spelling across the site.
- Do not change language variants in direct quotes, full text reproductions, or source material. Always preserve original spelling in such cases.

## Punctuation

- Always use straight apostrophes (') and straight quotation marks (").
- Do not use curly or typographic quotation marks (e.g. ‘ ’ “ ”).

## Tone and Style

- Write in a clear, natural, and human-readable manner.
- Avoid overly formal, academic, or mechanical phrasing.
- Ensure writing is not easily identifiable as machine-generated.
- Keep sentences direct and precise.

## Capitalisation

- Use Title Case for page titles.
- Use sentence case within paragraphs unless grammatically required.
- Maintain consistency in headings.

## Bold Usage

- Use bold sparingly.
- Allowed uses:
  - First sentence lead format (e.g. **Sunil Abraham** is an Indian internet researcher...).
  - Page titles (where needed)
  - Section headers
  - Key terms (e.g. legislation, policy names)
- Do not bold full sentences or use bold for emphasis.

## Markdown Structure

- Avoid unnecessary horizontal rules (`---`).
- Use them only where they serve a structural purpose (e.g. separating YAML front matter from content).
- Prefer clean heading hierarchy:
  - `##` for major sections
  - `###` for subsections
- Do not mix heading levels inconsistently.

## YAML Front Matter

{% include main-article.html link="/tsap/yaml/" title="YAML Front Matter" %}

All pages must include:

- `layout: default`
- `title:` in Title Case
- `description:` (clear and concise)
- `categories:` (appropriate classification)
- `permalink:` (clean, structured URL)
- `created:` (must reflect actual IST date of creation)

The `created:` field must:
- Always be present
- Always match the actual creation date (Indian Standard time)
- Be placed as the last parameter in the YAML block

## Authors

- Use `authors` as an array.
- Example: authors: ["Name"]
