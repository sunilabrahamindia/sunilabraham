---
layout: default
title: "Maintenance"
description: "Internal maintenance and quality checks for the Sunil Abraham Project."
categories: [Project pages]
permalink: /maintenance/
created: 2026-01-19
---

This page is an **internal maintenance dashboard** for the **Sunil Abraham Project**. It tracks metadata quality, editorial consistency, and structural hygiene across the site.

{% assign today = site.time | date: "%Y-%m-%d" %}

## 1. Title Health

### Missing title (1a)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.title %}
      <li>
        <a href="{{ page.url }}">{{ page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

### Overlong title (more than 70 characters) (1b)

<ul>
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
</ul>

## 2. Created Date Hygiene

### Missing `created` field (2a)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.created %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

### Suspicious `created` (future date) (2b)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.created %}
      {% if page.created > today %}
        <li>
          <a href="{{ page.url }}">{{ page.title | default: page.url }}</a><br>
          <small>created: {{ page.created }}</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

## 3. Category Hygiene

### Missing categories (3a)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.categories %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

## 4. Permalink Hygiene

### Missing permalink (4a)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.permalink %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

### Suspicious permalink patterns (4b)

Flags:
- Uppercase letters
- `.html` or `.md`
- Double slashes (`//`)

<ul>
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
</ul>

## 5. Author Attribution Health

### Missing `authors` field (5a)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.authors %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

### Empty `authors` array (5b)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.authors and page.authors.size == 0 %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

## Notes

- Pages marked `published: false` are excluded by design.
- `/sandbox/` paths are excluded to reduce noise.
- This dashboard is intentionally descriptive, not prescriptive.
- Fixes should prioritise clarity, correctness, and long-term maintainability.
