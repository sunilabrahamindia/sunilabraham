---
layout: default
title: "Sunil Abraham and Business Standard"
description: "A consolidated archive of Sunil Abraham’s writings for Business Standard and related news coverage that references his commentary on technology policy, regulation, digital rights, and the political economy of the internet in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-business-standard/
created: 2026-01-08
---

***Business Standard*** is a leading Indian newspaper known for its in-depth coverage of the economy, public policy, regulation, and corporate affairs. Its reporting on technology frequently situates digital developments within broader discussions of governance, markets, and institutional reform.

Across opinion pieces and reported stories, **Sunil Abraham** has appeared both as a contributor and as a cited expert. His engagement with *Business Standard* typically focuses on the structural dimensions of technology policy — including regulation, surveillance, platform accountability, and the interaction between digital systems and democratic institutions — rather than consumer-facing technology trends.

This cluster brings together all **publications** and **media mentions** associated with *Business Standard*, offering a single reference point for readers examining how technology and digital governance debates have been addressed within Indian business and policy journalism.

## ✍️ Publications

<ol class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Business Standard"
     | sort:"date" | reverse
%}

{% for item in pub_items %}
  <li>
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## 📣 Media Mentions

<ol class="cluster-list">
{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Business Standard"
     | sort:"date" | reverse
%}

{% for item in media_items %}
  <li>
    <a href="{{ item.permalink }}">{{ item.title }}</a><br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

<style>
/* ---------------------------------------------------------
   Business Standard Cluster – Minimal Styling
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
