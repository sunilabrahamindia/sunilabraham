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
/* Informational note box */

/* Cluster list reset */
.cluster-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Individual cluster item (structure only) */
.cluster-item {
  margin-bottom: 0.9rem;
  border: 1px solid #e2e6ea;
  border-radius: 8px;
}

/* Accessible colours – repeat every 5 */
.cluster-item:nth-child(5n + 1) {
  background-color: #fffdf8; /* warm paper */
}

.cluster-item:nth-child(5n + 2) {
  background-color: #f2f8ff; /* pale scholarly blue */
}

.cluster-item:nth-child(5n + 3) {
  background-color: #fff7f1; /* soft parchment */
}

.cluster-item:nth-child(5n + 4) {
  background-color: #f4fbf7; /* archival mint */
}

.cluster-item:nth-child(5n + 5) {
  background-color: #f7f3ff; /* lavender tint */
}

/* Cluster link */
.cluster-link {
  display: block;
  padding: 1.05rem 1.15rem;
  text-decoration: none;
  color: inherit;
  transition: background-color 0.15s ease;
}

/* Hover and focus states */
.cluster-link:hover,
.cluster-link:focus {
  background-color: #f1f6fb;
  outline: none;
}

/* Keyboard focus visibility */
.cluster-link:focus-visible {
  outline: 2px solid #0a4a7a;
  outline-offset: 2px;
}

/* Cluster title */
.cluster-title {
  display: block;
  font-weight: 600;
  font-size: 1.08rem;
  color: #1a1a1a;
}

/* Optional cluster description */
.cluster-description {
  display: block;
  margin-top: 0.35rem;
  font-size: 0.96rem;
  color: #555;
  line-height: 1.5;
}
</style>
