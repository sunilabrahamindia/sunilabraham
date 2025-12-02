---
layout: default
title: "Articles"
categories: [Project pages]
description: "Index of articles published under the Sunil Abraham Project, including biographical notes, research essays, organisational histories, and topical writings."
permalink: /articles/
created: 2025-12-02
---

The Sunil Abraham Project includes a growing collection of articles that document people, organisations, history, technology, public policy and personal narratives. To keep the site organised, articles are placed inside different directories and portals. When a piece of writing logically belongs within a specific area — such as a portal dedicated to a person, a theme or an institution — it is stored inside that folder. Articles that do not fall under any specialised portal, or those intended to stand alone, are placed here in the main **Articles** directory.

This page brings together all articles stored directly under `/articles/`, providing a single place to browse and access them. As with the rest of the project, new material will continue to be added as research progresses and archival work expands.

## Articles (Alphabetical List)

Below is an automatically generated list of all articles located in the `/articles/` directory. The list is alphabetically sorted by title.

<ul>
{% assign articles_list = site.pages 
     | where_exp: "p", "p.path contains 'articles/'" 
     | where_exp: "p", "p.path ends_with '.md'" 
     | sort: "title" %}
{% for page in articles_list %}
  {% unless page.path == 'articles/index.md' %}
    <li><a href="{{ page.url | relative_url }}">{{ page.title }}</a></li>
  {% endunless %}
{% endfor %}
</ul>
