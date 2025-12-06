---
layout: default
title: "Clusters"
categories: [Clusters, Project pages]
description: "A directory of thematic clusters used across the Sunil Abraham Project to organise related articles, media mentions, and archival material."
permalink: /clusters/
created: 2025-12-06
---

The Sunil Abraham Project contains material that spans people, organisations, debates, policies, and historical moments. Some subjects attract sustained attention across multiple articles and media mentions. To keep this work coherent and readable, the project uses **clusters** — thematic groupings that bring together related pieces of writing or coverage under a single, navigable heading.

Each cluster functions as a small curated archive. Instead of scattering related items across the site, a cluster page pulls them together, provides background context, and offers a structured way to move between them. Clusters are especially useful when several publications, media reports, or editorial notes speak to the same event, appointment, controversy, or long-running policy theme.

This page lists all clusters stored inside the **`/clusters/`** directory. As research expands and more thematic collections are created, new entries will appear here automatically.

## How Clusters Differ from Portals

While `portals` and `clusters` both organise content, they serve different purposes. 
- **Portals** are broad, permanent sections of the site — for example, portals dedicated to a person, an organisation, or a major theme. They contain multiple subpages, biographical notes, timelines, galleries and other structured material.
- **Clusters**, by contrast, are smaller and more focused. A cluster is created when a set of articles or media mentions relates to a very specific topic or moment, such as a particular appointment, campaign, policy proposal or debate. Clusters do not aim to cover an entire subject area; they simply gather related items in one place for easier reading and reference.

In short:  
- `Portals` are long-term, comprehensive spaces.  
- `Clusters` are short-form, thematic collections. 

## Clusters

<ul>
{% assign cluster_pages = site.pages 
     | where_exp: "p", "p.path contains 'clusters/'" 
     | sort: 'title' %}

{% for page in cluster_pages %}
  {% unless page.path == 'clusters/index.md' %}
    <li><a href="{{ page.url | relative_url }}">{{ page.title }}</a></li>
  {% endunless %}
{% endfor %}
</ul>
