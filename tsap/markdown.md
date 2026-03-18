---
layout: default
title: "Markdown"
description: "Guide to Markdown syntax used across The Sunil Abraham Project (TSAP), including a practical cheatsheet."
categories: [TSAP Documentation]
permalink: /tsap/markdown/
created: 2026-03-18
---

**Markdown** is a lightweight markup language used to format text using simple and readable syntax. It allows content to be written in plain text while supporting headings, links, lists, and other structural elements.

Most pages in The Sunil Abraham Project (TSAP) are written in Markdown, typically using the `.md` file format. This ensures that content remains clean, version-controlled, and easy to maintain within the GitHub-based workflow.

**Note:** This page is a practical reference and may be expanded over time.

## Markdown Cheatsheet

<table class="markdown-cheatsheet">
<tr>
<th>You write</th>
<th>You get</th>
</tr>

<tr class="section-header">
<td colspan="2">Emphasis</td>
</tr>
<tr>
<td><code>*italics*</code></td>
<td><em>italics</em></td>
</tr>
<tr>
<td><code>**bold**</code></td>
<td><strong>bold</strong></td>
</tr>
<tr>
<td><code>***bold and italics***</code></td>
<td><strong><em>bold and italics</em></strong></td>
</tr>
<tr>
<td><code>~~strikethrough~~</code></td>
<td><del>strikethrough</del></td>
</tr>

<tr class="section-header">
<td colspan="2">Headings</td>
</tr>
<tr>
<td><code># Heading 1</code></td>
<td><h1 style="margin:0;font-size:1.4em;">Heading 1</h1></td>
</tr>
<tr>
<td><code>## Heading 2</code></td>
<td><h2 style="margin:0;font-size:1.2em;">Heading 2</h2></td>
</tr>
<tr>
<td><code>### Heading 3</code></td>
<td><h3 style="margin:0;font-size:1.05em;">Heading 3</h3></td>
</tr>
<tr>
<td><code>#### Heading 4</code></td>
<td><h4 style="margin:0;font-size:0.95em;">Heading 4</h4></td>
</tr>

<tr class="section-header">
<td colspan="2">Links and Images</td>
</tr>
<tr>
<td><code>[Link text](https://example.com)</code></td>
<td><a href="#">Link text</a></td>
</tr>
<tr>
<td><code>[Link text](https://example.com "Title")</code></td>
<td><a href="#" title="Title">Link text</a> <em>(with tooltip)</em></td>
</tr>
<tr>
<td><code>![Alt text](image.png)</code></td>
<td><em>Displays an image</em></td>
</tr>
<tr>
<td><code>![Alt text](image.png "Caption")</code></td>
<td><em>Displays an image with caption tooltip</em></td>
</tr>

<tr class="section-header">
<td colspan="2">Lists</td>
</tr>
<tr>
<td><code>- Item</code><br><code>- Another item</code></td>
<td>
<ul style="margin:0;padding-left:1.2em;">
<li>Item</li>
<li>Another item</li>
</ul>
</td>
</tr>
<tr>
<td><code>1. First</code><br><code>2. Second</code></td>
<td>
<ol style="margin:0;padding-left:1.2em;">
<li>First</li>
<li>Second</li>
</ol>
</td>
</tr>
<tr>
<td><code>- Item</code><br><code>&nbsp;&nbsp;- Nested item</code></td>
<td>
<ul style="margin:0;padding-left:1.2em;">
<li>Item<ul><li>Nested item</li></ul></li>
</ul>
</td>
</tr>
<tr>
<td><code>- [ ] Unchecked task</code><br><code>- [x] Checked task</code></td>
<td>&#9744; Unchecked task<br>&#9745; Checked task</td>
</tr>

<tr class="section-header">
<td colspan="2">Blockquotes and Code</td>
</tr>
<tr>
<td><code>&gt; This is a quote.</code></td>
<td><blockquote style="margin:0 0 0 0.5em;border-left:3px solid #ccc;padding-left:0.5em;color:#333;">This is a quote.</blockquote></td>
</tr>
<tr>
<td><code>&gt; Line one.</code><br><code>&gt; Line two.</code></td>
<td><blockquote style="margin:0 0 0 0.5em;border-left:3px solid #ccc;padding-left:0.5em;color:#333;">Line one.<br>Line two.</blockquote></td>
</tr>
<tr>
<td><code>`inline code`</code></td>
<td><code>inline code</code></td>
</tr>
<tr>
<td><pre style="margin:0;font-size:0.9em;">```
code block
```</pre></td>
<td><pre style="margin:0;background:#f8f8f8;padding:4px 6px;border-radius:4px;font-size:0.9em;">code block</pre></td>
</tr>
<tr>
<td><pre style="margin:0;font-size:0.9em;">```python
print("Hello")
```</pre></td>
<td><em>Syntax-highlighted code block (Python)</em></td>
</tr>

<tr class="section-header">
<td colspan="2">Tables</td>
</tr>
<tr>
<td><pre style="margin:0;font-size:0.9em;">| Col 1 | Col 2 |
|-------|-------|
| A     | B     |</pre></td>
<td>
<table style="border-collapse:collapse;font-size:0.9em;">
<tr><th style="border:1px solid #ccc;padding:2px 6px;">Col 1</th><th style="border:1px solid #ccc;padding:2px 6px;">Col 2</th></tr>
<tr><td style="border:1px solid #ccc;padding:2px 6px;">A</td><td style="border:1px solid #ccc;padding:2px 6px;">B</td></tr>
</table>
</td>
</tr>
<tr>
<td><pre style="margin:0;font-size:0.9em;">| Left | Centre | Right |
|:-----|:------:|------:|</pre></td>
<td><em>Left, centre, and right column alignment</em></td>
</tr>

<tr class="section-header">
<td colspan="2">Other Elements</td>
</tr>
<tr>
<td><code>---</code></td>
<td><hr style="margin:4px 0;"></td>
</tr>
<tr>
<td><code>\*not italic\*</code></td>
<td>*not italic* <em>(escaped character)</em></td>
</tr>
<tr>
<td><code>Text&lt;br&gt;New line</code></td>
<td>Text<br>New line <em>(line break)</em></td>
</tr>
<tr>
<td><code>&amp;nbsp;</code></td>
<td>&nbsp; <em>(non-breaking space)</em></td>
</tr>
<tr>
<td><code>[^1]</code> and <code>[^1]: Footnote text</code></td>
<td><em>Footnote reference and definition</em></td>
</tr>

</table>

## Code Block Examples

The following five examples demonstrate common TSAP writing patterns.

**1. Article front matter and introduction**

```markdown
---
layout: default
title: "Example Article"
description: "A short description of the article."
categories: [Articles]
permalink: /tsap/example/
created: 2026-03-18
---

This is the opening paragraph of an article. It introduces the subject
clearly and concisely before moving into sections.
```

**2. Sections with headings and lists**

```markdown
## Background

This section provides context for the subject. Keep paragraphs short
and focused on a single idea.

## Key Points

- First important point about the subject
- Second point with additional context
- Third point, kept brief

### Sub-section

Further detail belonging to a sub-topic goes here.
```

**3. Links, images, and blockquotes**

```markdown
For further reading, see the [TSAP Manual of Style](/tsap/manual-of-style/).

![A descriptive caption for the image](assets/images/example.png "Optional tooltip")

> "A quote from a relevant source or person."
> — Attribution, *Source Title*, Year
```

**4. Tables and task lists**

```markdown
| Name       | Role       | Since |
|:-----------|:-----------|------:|
| Example A  | Editor     |  2024 |
| Example B  | Researcher |  2025 |

## To Do

- [x] Draft the article
- [x] Add citations
- [ ] Peer review
- [ ] Publish
```

**5. Code blocks with syntax highlighting and footnotes**

```markdown
The configuration file uses YAML front matter.[^1]

---
layout: default
title: "My Page"
date: 2026-03-18
---

Inline references use backticks, such as `permalink` or `layout: default`.

[^1]: YAML front matter is processed by Jekyll before the page is rendered.
```

## Notes for TSAP Usage

- Keep Markdown clean and minimal; avoid unnecessary HTML unless required for layout.
- Prefer readability over visual styling in raw source files.
- Use `---` primarily for front matter; avoid using it as a visual separator in content unless necessary.
- Footnotes (`[^1]`) are preferred over inline parenthetical asides for references.
- Follow the [TSAP Manual of Style](/tsap/manual-of-style/) for heading hierarchy, date format, and spelling conventions.
- All dates in TSAP pages use the DMY format (e.g., 18 March 2026), except in direct quotations.

<style>
.markdown-cheatsheet {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.markdown-cheatsheet th,
.markdown-cheatsheet td {
  border: 1px solid #ccc;
  padding: 0.5rem 0.75rem;
  vertical-align: top;
}

.markdown-cheatsheet th {
  background-color: #f2f2f2;
  text-align: left;
}

.markdown-cheatsheet td:first-child {
  width: 45%;
}

.markdown-cheatsheet code {
  background: #f8f8f8;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.9em;
}

.markdown-cheatsheet tr.section-header td {
  background-color: #e8e8e8;
  font-weight: bold;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  border-top: 2px solid #aaa;
}

@media (max-width: 600px) {
  .markdown-cheatsheet {
    font-size: 0.85rem;
  }

  .markdown-cheatsheet pre {
    overflow-x: auto;
    white-space: pre;
    max-width: 100%;
  }
}

article pre, .content pre, main pre {
  overflow-x: auto;
  white-space: pre;
  max-width: 100%;
}

</style>
