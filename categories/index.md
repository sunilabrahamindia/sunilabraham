---
layout: default
title: "Categories"
description: "Index of all content categories on sunilabraham.in, including Videos, Books, Biographies, and more."
permalink: /categories/
---

<h2>All Categories</h2>
<ul>
  {% for category in site.categories %}
    <li>
      <a href="{{ '/categories/' | append: category[0] | slugify | append: '/' | relative_url }}">
        {{ category[0] | capitalize }}
      </a>
      ({{ category[1].size }} items)
    </li>
  {% endfor %}
</ul>
