---
layout: default
title: "Maintenance"
description: "Internal maintenance and quality checks for the Sunil Abraham Project."
categories: [Project pages]
permalink: /maintenance/
created: 2026-01-19
---

This page is an **internal maintenance dashboard** for the Sunil Abraham Project. It tracks metadata quality, editorial consistency, and structural hygiene across the site.

Nothing on this page is intended for public consumption.

## YAML Description Health

Search engines typically rewrite or ignore descriptions that are too short, too long, missing, or duplicated.

**Guiding ranges used here:**
- Ideal: 120–160 characters
- Acceptable: 70–170 characters
- Flagged: < 50 or > 200 characters

### Too short (less than 50 characters)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.description %}
      {% assign len = page.description | size %}
      {% if len < 50 %}
        <li>
          <a href="{{ page.url }}">{{ page.title | default: page.url }}</a><br>
          <small>{{ len }} characters — "{{ page.description }}"</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

### Too long (more than 200 characters)

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% if page.description %}
      {% assign len = page.description | size %}
      {% if len > 200 %}
        <li>
          <a href="{{ page.url }}">{{ page.title | default: page.url }}</a><br>
          <small>{{ len }} characters</small>
        </li>
      {% endif %}
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

### Missing description

<ul>
{% for page in site.pages %}
  {% unless page.published == false or page.url contains '/sandbox/' or page.url contains '/maintenance/' %}
    {% unless page.description %}
      <li>
        <a href="{{ page.url }}">{{ page.title | default: page.url }}</a>
      </li>
    {% endunless %}
  {% endunless %}
{% endfor %}
</ul>

## Notes

- Pages marked `published: false` are excluded by design.
- `/sandbox/` paths are excluded to reduce noise.
- This page is meant to be extended gradually (titles, dates, categories, authors, etc.).
- Fixes should prioritise clarity and accuracy over keyword optimisation.

