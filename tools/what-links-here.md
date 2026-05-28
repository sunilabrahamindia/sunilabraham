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
{% for target in site.data.backlinks %}
  <li>
    <strong>{{ target[0] }}</strong>

    <ul>
      {% for source in target[1] %}
        <li>
          <a href="{{ source }}">{{ source }}</a>
        </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>
