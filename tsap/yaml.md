---
layout: default
title: "YAML Front Matter"
description: "Guide to YAML front matter used across The Sunil Abraham Project (TSAP), including all supported parameters."
categories: [TSAP Documentation]
permalink: /tsap/yaml/
created: 2026-03-18
---

**YAML** (YAML Ain't Markup Language) is a human-readable data format used to store structured information. In Jekyll-based sites like TSAP, YAML appears as **front matter** — a block of key-value pairs at the very top of every `.md` file, fenced by triple dashes (`---`).

Jekyll reads the front matter before processing the page, using it to set the layout, generate URLs, build navigation, and pass metadata to templates. Without front matter, Jekyll will not process the file as a page and it will not be rendered with a layout.

**Note:** Front matter must appear at the very top of the file, with no content before the opening `---`.

## TSAP YAML Parameters

Every TSAP page begins with a front matter block. Below is a real example, followed by an explanation of each parameter.

```yaml
---
layout: default
title: Athanasius Mathen Abraham Ayrookuzhiel
permalink: /amaa/
categories: [A. M. A. Ayrookuzhiel, Biographies]
description: Biography of Rev. Athanasius Mathen Abraham Ayrookuzhiel (A. M. A. Ayrookuzhiel) (1933–1996), Indian theologian and scholar who advanced Dalit theology and contextual Christian thought through his work at the Christian Institute for the Study of Religion and Society.
created: 2025-10-27
---
```

### `layout`

**Required.** Tells Jekyll which HTML template to wrap the page content in.

- All TSAP pages use `layout: default`.
- Do not change this unless a different layout template exists and is intentionally required.

```yaml
layout: default
```

### `title`

**Required.** The title of the page. Used in the browser tab, page heading, and site navigation.

- Write the full name or title without quotation marks unless it contains a colon.
- For biographical pages, use the subject's full formal name.
- If the title contains a colon, wrap the entire value in double quotes.

```yaml
title: Athanasius Mathen Abraham Ayrookuzhiel
```

```yaml
title: "Faith and Society: A Study"
```

### `description`

**Required.** A plain-text summary of the page shown in search engine results and site previews.

- Write in one sentence where possible; two sentences are acceptable for complex subjects.
- For biographical pages, include full name, birth–death years, nationality, and primary significance.
- Do not use Markdown formatting inside the description value.
- Keep it concise; around 150–160 characters is ideal for search results, but longer descriptions are acceptable when necessary.

```yaml
description: Biography of Rev. Athanasius Mathen Abraham Ayrookuzhiel (A. M. A. Ayrookuzhiel) (1933–1996), Indian theologian and scholar who advanced Dalit theology and contextual Christian thought through his work at the Christian Institute for the Study of Religion and Society.
```

### `permalink`

**Required.** Sets the URL path for the page on the site.

- Always begin and end with a forward slash (`/`).
- Use lowercase letters and hyphens only; no spaces or special characters.
- Keep it short and stable — changing a permalink after publication breaks existing links.

```yaml
permalink: /amaa/
```

### `categories`

**Required.** A list of category tags used to group and organise pages across the site.

- Written as a YAML list inside square brackets, separated by commas.
- Each TSAP page should include at least one subject category and one type category (e.g., `Biographies`, `Articles`).
- Use title case for all category names.
- Multi-word names with initials (e.g., `A. M. A. Ayrookuzhiel`) are valid and must match exactly across all pages that share the category.

```yaml
categories: [A. M. A. Ayrookuzhiel, Biographies]
```

### `created`

**Required.** The date the page was first created, in `YYYY-MM-DD` format.

- This is the creation date of the file, not the date of publication or the subject's birth.
- Do not update this value when editing the page later.
- Note that while TSAP uses DMY format (e.g., 18 March 2026) in visible page content, the `created` field uses `YYYY-MM-DD` as required by Jekyll and YAML conventions.

```yaml
created: 2025-10-27
```

## Notes for TSAP Usage

- All six parameters above are required on every TSAP page. Do not omit any.
- Front matter is case-sensitive. `Layout: default` will not work; it must be `layout: default`.
- Values containing colons, quotation marks, or leading special characters must be wrapped in double quotes.
- Do not add extra parameters not listed here without checking the TSAP Manual of Style first.
- Follow the [TSAP Manual of Style](/tsap/manual-of-style/) for naming conventions, date formats, and category standards.

<style>
article pre, .content pre, main pre {
  overflow-x: auto;
  white-space: pre;
  max-width: 100%;
}

@media (max-width: 600px) {
  article pre, .content pre, main pre {
    font-size: 0.9rem;
  }
}
</style>
