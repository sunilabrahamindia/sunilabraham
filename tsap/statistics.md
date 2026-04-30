---
layout: default
title: "Statistics"
description: "A statistical overview of the Sunil Abraham Project (TSAP), including page counts, growth trends, content distribution, and structural indicators."
permalink: /statistics/
categories: [TSAP Documentation]
created: 2026-04-30
---

{% include under-construction.html %}

The **Statistics** page provides a quantitative overview of the Sunil Abraham Project (TSAP), presenting aggregated data about the site's content, structure, and growth. It functions as a central dashboard for understanding the scale and development of the project, including the number of published pages, distribution across categories and authors, and patterns of content creation over time.

This page is generated using build-time data and reflects the state of the site at the time of rendering. It is intended to support transparency, editorial analysis, and navigation by offering clear insights into how content is organised and how the project is evolving.

In addition to summary metrics, the page may include indicators of structural health, such as orphaned pages, highly linked pages, and category distribution, helping identify areas for further development and improvement.

## Core Metrics

{% assign created_pages = site.pages | where_exp: "p", "p.created" %}
{% assign catlist = "" | split: "," %}
{% for page in created_pages %}
  {% for c in page.categories %}
    {% unless catlist contains c %}
      {% assign catlist = catlist | push: c %}
    {% endunless %}
  {% endfor %}
{% endfor %}

- **Total Pages:** {{ created_pages | size }}
- **Total Categories:** {{ catlist | size }}

## Articles created by month

{% assign months = "" | split: "," %}
{% for page in created_pages %}
  {% assign m = page.created | date: "%Y-%m" %}
  {% unless months contains m %}
    {% assign months = months | push: m %}
  {% endunless %}
{% endfor %}

{% assign sorted_months = months | sort %}

<ul>
{% for m in sorted_months %}
  {% assign count = 0 %}
  {% for page in created_pages %}
    {% assign pm = page.created | date: "%Y-%m" %}
    {% if pm == m %}
      {% assign count = count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <li><strong>{{ m | date: "%B %Y" }}</strong>: {{ count }}</li>
{% endfor %}
</ul>
