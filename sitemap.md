---
layout: default
title: Sitemap
categories: [Project pages]
description: "Complete list of all public pages and posts on sunilabraham.in, organised and linked for easy navigation and reference."
---

Here's a list of all public pages and posts on this site.

## Pages
<ul>
{% assign sorted_pages = site.pages | sort: "title" %}
{% for page in sorted_pages %}
  {% if page.title and page.url != '/' and page.categories == nil %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
      {% if page.description %}
        <br><small>{{ page.description }}</small>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

## Categories
<ul>
{% assign all_categories = site.categories | sort %}
{% for category in all_categories %}
  <li>
    <strong>Category: {{ category[0] }}</strong>
    <ul>
      {% for post in category[1] %}
        <li>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          {% if post.description %}
            <br><small>{{ post.description }}</small>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  </li>
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
