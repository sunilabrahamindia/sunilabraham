---
layout: default
title: "Clusters"
categories: [Clusters, Project pages]
description: "A directory of thematic clusters used across the Sunil Abraham Project to organise related articles, media mentions, and archival material."
permalink: /clusters/
created: 2025-12-06
---

<div class="clusters-intro">

The Sunil Abraham Project contains material that spans people, organisations, debates, policies, and historical moments. Some subjects attract sustained attention across multiple articles and media mentions.

To keep this work coherent and readable, the project uses **clusters** — focused thematic groupings that bring together related pieces of writing or coverage under a single, navigable heading.

Each cluster functions as a small curated archive. Rather than scattering related items across the site, a cluster page pulls them together, provides background context, and offers a structured way to move between them.

</div>

<details class="clusters-explainer">
  <summary>How clusters differ from portals</summary>

  <p>
  While <strong>portals</strong> and <strong>clusters</strong> both organise content, they serve different purposes.
  </p>

  <ul>
    <li>
      <strong>Portals</strong> are broad, long-term sections of the site — often dedicated to a person, organisation, or major theme. They may include timelines, biographies, galleries, and multiple subpages.
    </li>
    <li>
      <strong>Clusters</strong> are smaller and more focused. They bring together related articles or media mentions around a specific event, appointment, controversy, campaign, or policy moment.
    </li>
  </ul>

  <p>
  In short: portals are comprehensive spaces; clusters are concise thematic collections.
  </p>
</details>

<h2 class="clusters-heading">All Clusters</h2>

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

/* Intro text */
.clusters-intro {
  max-width: 65ch;
  margin-bottom: 1.75rem;
  font-size: 1.05rem;
  line-height: 1.6;
  color: #3a3a3a;
}

/* Explainer block */
.clusters-explainer {
  max-width: 65ch;
  margin-bottom: 2.5rem;
}

.clusters-explainer summary {
  cursor: pointer;
  font-weight: 600;
  color: #0a4a7a;
  margin-bottom: 0.5rem;
}

.clusters-explainer summary:focus {
  outline: 2px solid #0a4a7a;
  outline-offset: 2px;
}

.clusters-explainer p,
.clusters-explainer li {
  line-height: 1.6;
  color: #333;
}

/* Section heading */
.clusters-heading {
  margin-top: 2.5rem;
  margin-bottom: 1.25rem;
}

/* Cluster list */
.cluster-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.cluster-item {
  margin-bottom: 0.85rem;
  border: 1px solid #e3e3e3;
  border-radius: 8px;
  background-color: #fafafa;
}

/* Cluster link */
.cluster-link {
  display: block;
  padding: 1rem 1.1rem;
  text-decoration: none;
  color: inherit;
  transition: background-color 0.15s ease;
}

.cluster-link:hover,
.cluster-link:focus {
  background-color: #f1f6fb;
  outline: none;
}

/* Title and description */
.cluster-title {
  display: block;
  font-weight: 600;
  font-size: 1.05rem;
  color: #1a1a1a;
}

.cluster-description {
  display: block;
  margin-top: 0.3rem;
  font-size: 0.95rem;
  color: #555;
}
</style>
