---
layout: default
title: "Maintenance"
description: "Internal maintenance and quality checks for the Sunil Abraham Project."
categories: [Project pages]
permalink: /maintenance/
created: 2026-01-19
---

This page functions as an **internal maintenance dashboard** for the Sunil Abraham Project. It is used to review metadata quality, editorial consistency, and structural hygiene across the site.

While the page is publicly accessible, it is not designed for general reading. Most of the content consists of routine checks, lists, and diagnostic outputs that are primarily useful for ongoing maintenance rather than public consumption.

**Some sections on this page may appear empty at times — or remain empty for long periods.** This is expected and simply indicates that no pages are currently affected by the specific issue being tracked in that section.

{% assign today = site.time | date: "%Y-%m-%d" %}

## 1. Title Health

### Overlong title (more than 70 characters)

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.title %}
      {% assign tlen = page.title | size %}
      {% if tlen > 70 %}
        <li>
          <a href="{{ page.url }}">{{ page.title }}</a><br>
          <small>{{ tlen }} characters</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>

## 2. Created Date Hygiene

### Missing `created` field

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.created %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ol>

### Suspicious `created` (future date)

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.created %}
      {% assign created_str = page.created | date: "%Y-%m-%d" %}
      {% if created_str > today %}
        <li>
          <a href="{{ page.url }}">{{ page.title | default: page.url }}</a><br>
          <small>created: {{ page.created }}</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>

## 3. Category Hygiene

### Missing categories

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.categories %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ol>

## 4. Permalink Hygiene

### Missing permalink

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.permalink %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ol>

### Suspicious permalink patterns

Flags:
- Uppercase letters
- `.html` or `.md`
- Double slashes (`//`)

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.permalink %}
      {% assign p = page.permalink %}
      {% assign lower = p | downcase %}
      {% if p != lower or p contains '.html' or p contains '.md' or p contains '//' %}
        <li>
          <a href="{{ page.url }}">{{ page.title | default: page.url }}</a><br>
          <small>{{ p }}</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>

## 5. Author Attribution Health

### Missing `authors` field

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.authors %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ol>

### Empty `authors` array

<ol>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.authors and page.authors.size == 0 %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>

## Notes

- Pages marked `published: false` are excluded by design.
- `/sandbox/` paths are excluded to reduce noise.
- This dashboard is intentionally descriptive, not prescriptive.
- Fixes should prioritise clarity, correctness, and long-term maintainability.
