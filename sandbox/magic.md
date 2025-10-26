---
layout: default
title: Magic
date: 2025-10-26
last_modified_at: 2025-10-26
author: Sunil Abraham
categories: [sandbox, test]
tags: [jekyll, liquid, variables]
---

# Jekyll Liquid Sandbox

This page demonstrates **all common page and site variables**, filters, and usage.

---

## Page Variables (`page`)

| Variable | Output | Description |
|----------|--------|-------------|
| `page.title` | {{ page.title }} | Title from front matter |
| `page.date` | {{ page.date | date: "%d %B %Y" }} | Creation date |
| `page.last_modified_at` | {{ page.last_modified_at | date: "%d %B %Y" }} | Last modification date |
| `page.url` | {{ page.url }} | Relative URL |
| `page.path` | {{ page.path }} | Path to source file |
| `page.layout` | {{ page.layout }} | Layout used |
| `page.categories` | {{ page.categories }} | Categories array |
| `page.tags` | {{ page.tags }} | Tags array |
| `page.author` | {{ page.author }} | Author from front matter |
| `page.content` | {{ page.content | strip_html | truncate:50 }} | Page HTML content, stripped & truncated |
| `page.excerpt` | {{ page.excerpt | strip_html | truncate:50 }} | First paragraph/excerpt |

---

## Site Variables (`site`)

| Variable | Output | Description |
|----------|--------|-------------|
| `site.title` | {{ site.title }} | Site title from `_config.yml` |
| `site.description` | {{ site.description }} | Site description |
| `site.url` | {{ site.url }} | Base URL |
| `site.baseurl` | {{ site.baseurl }} | Base path if hosted in subfolder |
| `site.time` | {{ site.time | date: "%d %B %Y %H:%M:%S" }} | Build time |
| `site.posts` | {% for post in site.posts %}{{ post.title }} {% endfor %} | List all posts |
| `site.pages` | {% for p in site.pages %}{{ p.title }} {% endfor %} | List all pages |
| `site.categories` | {% for c in site.categories %}{{ c[0] }} {% endfor %} | Categories dictionary |
| `site.tags` | {% for t in site.tags %}{{ t[0] }} {% endfor %} | Tags dictionary |
| `site.author` | {{ site.author }} | Global author info |
| `site.data` | {% for d in site.data %}{{ d[0] }} {% endfor %} | Custom data from `_data/*.yml` |

---

## Common Filters

| Filter | Example | Output |
|--------|---------|--------|
| `date` | `{{ page.date | date: "%A, %d %B %Y" }}` | {{ page.date | date: "%A, %d %B %Y" }} |
| `upcase` | `{{ page.title | upcase }}` | {{ page.title | upcase }} |
| `downcase` | `{{ page.title | downcase }}` | {{ page.title | downcase }} |
| `capitalize` | `{{ page.title | capitalize }}` | {{ page.title | capitalize }} |
| `strip_html` | `{{ page.content | strip_html | truncate:50 }}` | {{ page.content | strip_html | truncate:50 }} |
| `replace` | `{{ page.title | replace: " ", "-" }}` | {{ page.title | replace: " ", "-" }} |
| `truncate` | `{{ page.content | truncate:30 }}` | {{ page.content | truncate:30 }} |
| `default` | `{{ page.author | default: "Unknown" }}` | {{ page.author | default: "Unknown" }} |

---

## Example Usage

```liquid
<p>Title: {{ page.title }}</p>
<p>URL: {{ page.url }}</p>
<p>Published: {{ page.date | date: "%d %B %Y" }}</p>
<p>Last updated: {{ page.last_modified_at | date: "%d %B %Y" }}</p>
<p>Site: {{ site.title }} ({{ site.url }})</p>
<p>Author: {{ page.author | default: "Unknown" }}</p>
<p>Categories: {{ page.categories | join: ", " }}</p>
<p>Tags: {{ page.tags | join: ", " }}</p>
