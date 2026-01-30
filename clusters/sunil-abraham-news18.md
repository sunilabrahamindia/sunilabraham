---
layout: default
title: "Sunil Abraham and News18"
description: "A small curated cluster of News18 reporting that references Sunil Abraham’s commentary on technology policy, digital governance, privacy, and the public impact of internet regulation in India."
categories: [Clusters]
permalink: /clusters/sunil-abraham-news18/
source: "News18"
created: 2026-01-30
---

***News18*** is a major Indian news network with a strong digital presence, covering national politics, public policy, technology, and social issues. Its reporting often brings regulatory and governance questions to a broad, general audience through accessible news formats.

In a limited number of articles, **Sunil Abraham** appears as a cited voice providing context on issues such as data governance, platform accountability, privacy, and the regulatory consequences of technological change. These references typically occur in explanatory or policy-focused reporting rather than regular technology coverage.

This cluster brings together all available **media mentions** of Sunil Abraham published by *News18*, serving as a compact reference point rather than a comprehensive archive.

## 📣 Media Mentions {#media}

{% assign media_items = site.pages
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","News18"
     | sort:"date" | reverse
%}

<ol class="cluster-list">
{% for item in media_items %}
  <li>
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%-d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## External links
- [Official website](https://www.news18.com/)

<style>
/* ---------------------------------------------------------
   News18 Cluster – Minimal, proportional styling
--------------------------------------------------------- */

.cluster-list {
  margin: 1rem 0 2rem 0;
  padding-left: 1.1rem;
}

.cluster-list li {
  margin-bottom: 0.8rem;
}

.cluster-list a {
  text-decoration: none;
}

.cluster-list a:hover {
  text-decoration: underline;
}

.meta {
  font-size: 0.9rem;
  color: #555;
}

.desc {
  font-size: 0.95rem;
  color: #444;
  margin-top: 0.2rem;
}
</style>
