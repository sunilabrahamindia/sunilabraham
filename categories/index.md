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
  {% assign all_categories = "" | split: "" %}

  {% for page in site.pages %}
    {% if page.categories %}
      {% for cat in page.categories %}
        {% unless all_categories contains cat %}
          {% assign all_categories = all_categories | push: cat %}
        {% endunless %}
      {% endfor %}
    {% endif %}
  {% endfor %}

  {% for cat in all_categories %}
    <li>
      <a href="{{ '/categories/' | append: cat | slugify | append: '/' | relative_url }}">
        {{ cat | capitalize }}
      </a>
      ({{ site.pages | where_exp: "p", "p.categories contains cat" | size }} items)
    </li>
  {% endfor %}
</ul>
