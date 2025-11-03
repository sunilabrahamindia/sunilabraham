---
layout: default
title: "Categories"
categories: [Project pages]
description: "Index of all content categories on sunilabraham.in, including Videos, Books, Biographies, and more."
permalink: /categories/
---

<p>This section serves as a directory of all content categories published on <strong>sunilabraham.in</strong>. Browse through collections of videos, books, biographies, and project pages to explore related material and archived work.</p>

<h2>All Categories</h2>

<ul>
  {% comment %}
    Collect all categories from pages
  {% endcomment %}
  {% assign all_cats = site.pages | map: "categories" | compact | join: "," | split: "," | uniq | sort %}

  {% for cat in all_cats %}
    {% assign cat_slug = cat | slugify %}
    {% assign formatted_name = cat | split: " " | map: "capitalize" | join: " " %}
    <li>
      <a href="{{ '/categories/' | append: cat_slug | append: '/' | relative_url }}">
        {{ formatted_name }}
      </a>
      ({{ site.pages | where_exp: "p", "p.categories contains cat" | size }} items)
    </li>
  {% endfor %}
</ul>
