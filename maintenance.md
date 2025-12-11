---
layout: default
title: "Maintenance"
description: "Site-wide maintenance dashboard listing pages that use the under construction and notice templates."
permalink: /maintenance/
created: 2025-12-11
---

**Maintenance** page is meant to act as a quiet housekeeping zone for the website. It helps track sections that are still being worked on, parts that use special notice blocks, and other areas that may need occasional reviews during site development. The aim is simple: to keep things tidy, organised and easy to follow, without turning the site into a clutter of half-finished work. Nothing here is meant to draw attention from regular readers. It is simply a working record for maintenance, updates and quality checks carried out from time to time.

### Notes about templates
- Under construction include: https://github.com/sunilabrahamindia/sunilabraham/blob/main/_includes/under-construction.html  
- Notice include: https://github.com/sunilabrahamindia/sunilabraham/blob/main/_includes/notice.html

## Pages Using Under Construction Template

{% comment %}
Build a combined array of pages + collections used on the site.
This safely adds collections only if they exist on the site.
{% endcomment %}

{% assign all_pages = site.pages %}

{% if site.publications %}
  {% assign all_pages = all_pages | concat: site.publications %}
{% endif %}

{% if site.media %}
  {% assign all_pages = all_pages | concat: site.media %}
{% endif %}

{% if site.documents %}
  {% assign all_pages = all_pages | concat: site.documents %}
{% endif %}

{% comment %} Filter pages marked with under_construction: true and sort by title {% endcomment %}
{% assign uc_pages = all_pages | where: "under_construction", true | sort: "title" %}
<p><strong>Total:</strong> {{ uc_pages | size }}</p>

<ul aria-label="Pages under construction">
  {% for p in uc_pages %}
    <li><a href="{{ p.url }}">{{ p.title }}</a>{% if p.created %} — <small>created: {{ p.created }}</small>{% endif %}</li>
  {% endfor %}
</ul>

## Pages Using Notice Template

{% assign notice_pages = all_pages | where: "notice", true | sort: "title" %}
<p><strong>Total:</strong> {{ notice_pages | size }}</p>

<ul aria-label="Pages using notice include">
  {% for p in notice_pages %}
    <li><a href="{{ p.url }}">{{ p.title }}</a>{% if p.created %} — <small>created: {{ p.created }}</small>{% endif %}</li>
  {% endfor %}
</ul>

