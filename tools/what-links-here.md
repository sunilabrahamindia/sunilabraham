---
layout: default
title: What Links Here
permalink: /tools/what-links-here/
description: Explore internal backlinks across The Sunil Abraham Project.
sitemap: false
created: 2026-05-29
exclude_from_backlinks: true
---

<p>This tool is being tested.</p>


<ul>
{% assign all_content = site.pages | concat: site.documents %}

{% for target in site.data.backlinks %}

  {% assign target_page = all_content | where: "url", target[0] | first %}

  <li>

    <strong>
      {% if target_page %}
        <a href="{{ target[0] }}">{{ target_page.title }}</a>
      {% else %}
        {{ target[0] }}
      {% endif %}
    </strong>

    <ul>

      {% for source in target[1] %}

        {% assign source_page = all_content | where: "url", source | first %}

        <li>
          {% if source_page %}
            <a href="{{ source }}">{{ source_page.title }}</a>
          {% else %}
            <a href="{{ source }}">{{ source }}</a>
          {% endif %}
        </li>

      {% endfor %}

    </ul>

  </li>

{% endfor %}
</ul>

