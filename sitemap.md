---
layout: default
title: Sitemap
categories: [Project pages]
permalink: /sitemap/
description: "Complete list of all public pages, categories, and posts on sunilabraham.in, organised and linked for easy navigation and reference."
---

Below is the complete sitemap of <strong>sunilabraham.in</strong>, divided into <em>Pages</em>, <em>Categories</em>, and <em>Posts</em> for easy browsing.

As of {{ site.time | date: "%-d %B %Y" }}, the site contains {{ site.pages | size }} pages and {{ site.posts | size }} blog posts. This does not include support files such as PDFs, images, scripts.

<!-- =========================================================
     Pages (excluding categories and system pages) 
     ========================================================= -->
<h2>Pages</h2>
<ol class="sitemap-list">
{% assign sorted_pages = site.pages | sort: "title" %}
{% for page in sorted_pages %}
  {% unless page.url == '/' or page.path contains 'categories/' or page.path contains '_layouts' or page.path contains '_includes' or page.path contains '_templates' or page.path contains '404' or page.path contains 'sitemap' %}
    {% if page.title %}
      <li>
        <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
        {% if page.description %}
          <br><small>{{ page.description }}</small>
        {% endif %}
      </li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ol>

<!-- =========================================================
     Categories (only category pages, with page counts)
     ========================================================= -->
<h2>Categories</h2>
<ol class="sitemap-list">
{% assign category_pages = site.pages | where_exp: "p", "p.path contains 'categories/'" | sort: "title" %}
{% for cat in category_pages %}
  {% if cat.title %}
    {% assign cat_name = cat.title | remove: 'Category:' | strip %}
    {% assign cat_count = site.pages | where_exp: "p", "p.categories contains cat_name" | size %}

    {%- comment -%}
      Fix: The main Categories index.md page (/categories/) should show 
      the total number of category pages, not zero.
    {%- endcomment -%}
    {% if cat_count == 0 and cat.url == '/categories/' %}
      {% assign cat_count = category_pages.size %}
    {% endif %}

    <li>
      <a href="{{ cat.url | relative_url }}">{{ cat_name }}</a>
      <span class="count">({{ cat_count }})</span>
      {% if cat.description %}
        <br><small>{{ cat.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>


<!-- =========================================================
     Posts (with publication date)
     ========================================================= -->
<h2>Posts</h2>
<ol class="sitemap-list">
{% assign sorted_posts = site.posts | sort: "title" %}
{% for post in sorted_posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="date"> — {{ post.date | date: "%B %Y" }}</span>
    {% if post.description %}
      <br><small>{{ post.description }}</small>
    {% endif %}
  </li>
{% endfor %}
</ol>

<style>
.sitemap-list {
  padding-left: 1.5em;
  margin-top: 0.8em;
  margin-bottom: 1.5em;
}

.sitemap-list li {
  margin: 0.4em 0;
  line-height: 1.6;
}

.sitemap-list a {
  color: #0645ad;
  text-decoration: none;
}

.sitemap-list a:hover {
  text-decoration: underline;
}

.sitemap-list small {
  color: #555;
  font-size: 0.9em;
}

.count {
  color: #444;
  font-weight: normal;
  font-size: 0.9em;
  margin-left: 0.3em;
}

.date {
  color: #666;
  font-size: 0.9em;
}
</style>
