---
layout: default
title: "Clusters"
categories: [Clusters, Project pages]
description: "A directory of thematic clusters used across the Sunil Abraham Project to organise related articles, media mentions, and archival material."
permalink: /clusters/
created: 2025-12-06
---

The Sunil Abraham Project contains material that spans people, organisations, debates, policies, and historical moments. Some subjects attract sustained attention across multiple articles and media mentions.

To keep this work coherent and readable, the project uses **clusters** — focused thematic groupings that bring together related pieces of writing or coverage under a single, navigable heading.

Each cluster functions as a small curated archive. Rather than scattering related items across the site, a cluster page pulls them together, provides background context, and offers a structured way to move between them.

<div class="clusters-note">
This page lists all clusters stored inside the <code>/clusters/</code> directory. As research expands and more thematic collections are created, new entries will appear here automatically.
</div>

## How Clusters Differ from Portals

While **portals** and **clusters** both organise content, they serve different purposes.

- **Portals** are broad, long-term sections of the site — often dedicated to a person, organisation, or major theme. They may include timelines, biographies, galleries, and multiple subpages.
- **Clusters** are smaller and more focused. They bring together related articles or media mentions around a specific event, appointment, controversy, campaign, or policy moment.

In short:  
**Portals** are comprehensive spaces.  
**Clusters** are concise thematic collections.

## All Clusters

<ul class="cluster-list">
{% assign cluster_pages = site.pages 
     | where_exp: "p", "p.path contains 'clusters/'" 
     | sort: 'title' %}

{% for page in cluster_pages %}
  {% unless page.path == 'clusters/index.md' %}
    <li class="cluster-item">
      <a href="{{ page.url | relative_url }}" class="cluster-link">
        <span class="cluster-title">{{ page.title }}</span>
        {% if page.description %}
        <span class="cluster-description">{{ page.description }}</span>
        {% endif %}
      </a>
    </li>
  {% endunless %}
{% endfor %}
</ul>

<style>
/* =========================================================
   Clusters Index – Scoped Styles
   ========================================================= */

/* Subtle note box */
.clusters-note {
  margin: 1.25rem 0 2rem 0;
  padding: 0.9rem 1rem;
  background: #f6f8fa;
  border-left: 4px solid #0a4a7a;
  color: #333;
  font-size: 0.95rem;
}

/* Cluster list */
.cluster-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Individual cluster item */
.cluster-item {
  margin-bottom: 0.9rem;
  border: 1px solid #e3e3e3;
  border-radius: 8px;
  background-color: #fafafa;
}

/* Cluster link */
.cluster-link {
  display: block;
  padding: 1.05rem 1.15rem;
  text-decoration: none;
  color: inherit;
  transition: background-color 0.15s ease;
}

.cluster-link:hover,
.cluster-link:focus {
  background-color: #f1f6fb;
  outline: none;
}

/* Cluster title */
.cluster-title {
  display: block;
  font-weight: 600;
  font-size: 1.08rem;
  color: #1a1a1a;
}

/* Optional description */
.cluster-description {
  display: block;
  margin-top: 0.35rem;
  font-size: 0.96rem;
  color: #555;
}
</style>
