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
  {% if page.title and page.url != '/' %}
    {% assign cats = page.categories | join: ',' %}
    {% if cats == "" or cats == "Project pages" %}
      <li>
        <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
        {% if page.description %}
          <br><small>{{ page.description }}</small>
        {% endif %}
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

## Categories
<ul>
{% assign category_pages = site.pages | sort: "title" %}
{% for page in category_pages %}
  {% assign cats = page.categories | join: ',' %}
  {% if cats != "" and cats != "Project pages" %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
      {% if page.description %}
        <br><small>{{ page.description }}</small>
      {% endif %}
      <br><small>Category: {{ page.categories | join: ', ' }}</small>
    </li>
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
