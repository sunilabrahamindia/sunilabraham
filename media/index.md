---
layout: default
title: "Media Mentions"
categories: [Media mentions]
description: "Index of media coverage featuring Sunil Abraham, including interviews, quotations, profiles, and reporting across newspapers, magazines, and digital platforms."
permalink: /media/
created: 2025-12-06
---

Over the years, Sunil Abraham's work in technology policy, digital rights, internet governance, and institutional leadership has been covered by a wide range of media outlets. These pieces — whether they are interviews, quotations, profiles, or news reports — form a valuable part of the public record. They help trace how ideas have travelled, how debates have shifted, and how organisations, policymakers and journalists have engaged with questions of openness, privacy, platforms and technology governance.

To keep the site organised, all media-related material is stored inside the **`/media/`** directory. This includes coverage from newspapers, magazines, online newsrooms, and specialist technology publications. Each article reproduced here follows a consistent archival format: contextual introduction, publication details, and the full text from the original source, whenever available.

## Media Mentions (Sorted by Year – Newest First)

Sort by:  
[Year (Newest First)](/media/?sort=year_desc) · 
[Year (Oldest First)](/media/?sort=year_asc) · 
[Alphabetical](/media/?sort=alpha)

{% assign sort_param = page.sort | default: site.params.sort | default: 'year_desc' %}

{% comment %}
Collect media pages
{% endcomment %}
{% assign media_list = site.pages 
     | where_exp: "p", "p.path contains 'media/'" 
%}

{% comment %}
Remove index.md
{% endcomment %}
{% assign media_list = media_list | where_exp: "p", "p.path != 'media/index.md'" %}

{% if sort_param == 'alpha' %}
  {% assign media_list = media_list | sort: 'title' %}
{% elsif sort_param == 'year_asc' %}
  {% assign media_list = media_list | sort: 'date' %}
{% else %}
  {%- assign media_list = media_list | sort: 'date' | reverse -%}
{% endif %}

<ul>
{% for page in media_list %}
  <li>
    <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    <br>
    <span style="font-size: 0.9rem; color: #555;">
      {{ page.source }} • {{ page.date | date: "%Y" }}
    </span>
  </li>
{% endfor %}
</ul>
