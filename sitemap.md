---
layout: default
title: Sitemap
categories: [Project pages]
description: "Complete list of all pages and posts on sunilabraham.in, organised and linked for easy navigation and reference."
---

Here's a list of all public pages and posts on this site.

## Pages
<ul>
{% assign sorted_pages = site.pages | sort: "title" %}
{% for page in sorted_pages %}
  {% comment %}
    Skip pages that:
      - have no title, or
      - are the home page '/', or
      - are category index pages (either by layout or by URL path)
  {% endcomment %}
  {% if page.title and page.url != '/' and page.title != "" %}
    {% assign is_category_page = false %}
    {% if page.layout == "category" %}{% assign is_category_page = true %}{% endif %}
    {% if page.url contains '/categories/' %}{% assign is_category_page = true %}{% endif %}

    {% unless is_category_page %}
      <li>
        <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
        {% if page.description %}
          <br><small>{{ page.description }}</small>
        {% endif %}
      </li>
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>

## Posts
<ul>
{% assign sorted_posts = site.posts | sort: "title" %}
{% for post in sorted_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%B %Y" }}
    {% if post.description %}
      <br><small>{{ post.description }}</small>
    {% endif %}
  </li>
{% endfor %}
</ul>

## Categories
<ul>
{% comment %}
  Collect pages that are category index pages. Two approaches for safety:
    - layout == "category"
    - URL path contains /categories/
  We combine both and deduplicate by URL.
{% endcomment %}

{% assign cat_pages = site.pages | where_exp: "p", "p.layout == 'category' or p.url contains '/categories/'" %}
{% assign cat_pages = cat_pages | sort: "title" %}
{% for c in cat_pages %}
  {% if c.title and c.url != '/' %}
    <li>
      <a href="{{ c.url | relative_url }}">{{ c.title }}</a>
      {% if c.description %}
        <br><small>{{ c.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>
