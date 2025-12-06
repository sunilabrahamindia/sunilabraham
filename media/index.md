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

## Media Mentions (Alphabetical List)

Below is an automatically generated list of all media mention pages located in the `/media/` directory. The list is alphabetically sorted by title.

<ul>
{% assign media_list = site.pages 
     | where_exp: "p", "p.path contains 'media/'" 
     | sort: 'title' %}

{% for page in media_list %}
  {% unless page.path == 'media/index.md' %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
      <br>
      <span style="font-size: 0.9rem; color: #555;">
        {{ page.source }} • {{ page.date | date: "%Y" }}
      </span>
    </li>
  {% endunless %}
{% endfor %}
</ul>
