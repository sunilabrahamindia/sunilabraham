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

  {% assign sorted_categories = all_categories | sort %}

  {% for cat in sorted_categories %}
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
