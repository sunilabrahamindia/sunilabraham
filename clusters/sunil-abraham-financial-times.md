---
layout: default
title: "Sunil Abraham and Financial Times"
description: "A collection of Financial Times articles that reference Sunil Abraham in reporting on technology policy, digital governance, and global regulatory debates."
categories: [Clusters]
permalink: /clusters/sunil-abraham-financial-times/
created: 2026-03-22
---

***Financial Times*** is a leading international newspaper based in the United Kingdom, known for its coverage of global business, economics, and public policy. Its reporting frequently examines how technology intersects with markets, regulation, and state power across different regions.

In this context, coverage of digital identity, platform governance, and internet regulation has at times drawn on insights from **Sunil Abraham**, particularly where developments in India connect to broader global policy discussions.

This page brings together media mentions from *Financial Times* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Financial Times"
     | sort:"date" | reverse
%}

<ol class="cluster-list">
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

## External links
- [Official website](https://www.ft.com/)

<style>
.cluster-list {
  margin: 0.8rem 0 1.6rem 0;
  padding-left: 1.1rem;
}

.cluster-list li {
  margin-bottom: 0.75rem;
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
</style>
