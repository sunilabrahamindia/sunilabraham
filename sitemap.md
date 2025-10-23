---
layout: default
title: Sitemap
permalink: /sitemap/
---

# Sitemap

Here’s a list of all public pages and posts on this site.

## Pages
<ul>
{% for page in site.pages %}
  {% if page.title and page.url != '/' %}
    <li><a href="{{ page.url | relative_url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

## Posts
<ul>
{% for post in site.posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%B %Y" }}</li>
{% endfor %}
</ul>