---
layout: default
title: Sitemap
categories: [Project pages]
permalink: /sitemap/
description: "Complete list of all public pages, categories, and posts on sunilabraham.in, organised and linked for easy navigation and reference."
---

<p>Below is the complete sitemap of <strong>sunilabraham.in</strong>, divided into <em>Pages</em>, <em>Categories</em>, and <em>Posts</em> for easy browsing.</p>

<!-- =========================================================
     Pages (excluding categories)
     ========================================================= -->
<h2>Pages</h2>
<ol class="sitemap-list">
{% assign sorted_pages = site.pages | sort: "title" %}
{% for page in sorted_pages %}
  {% if page.title and page.url != '/' and page.path contains 'categories' == false %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
      {% if page.description %}
        <br><small>{{ page.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>

<!-- =========================================================
     Categories (only category pages)
     ========================================================= -->
<h2>Categories</h2>
<ol class="sitemap-list">
{% assign category_pages = site.pages | where_exp: "p", "p.path contains 'categories/'" | sort: "title" %}
{% for page in category_pages %}
  {% if page.title %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
      {% if page.description %}
        <br><small>{{ page.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ol>

<!-- =========================================================
     Posts (with date)
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
  counter-reset: section;
}

.sitemap-list li {
  margin: 0.4em 0;
  line-height: 1.5;
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

.date {
  color: #666;
  font-size: 0.9em;
}
</style>
