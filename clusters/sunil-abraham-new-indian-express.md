---
layout: default
title: "Sunil Abraham and The New Indian Express"
description: "A compact cluster of reporting from The New Indian Express that includes references to Sunil Abraham’s views on technology policy, digital governance, privacy, and the regulation of internet platforms in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-new-indian-express/
created: 2026-01-31
---

***The New Indian Express*** is a prominent Indian newspaper with national and regional editions, covering politics, public policy, law, technology, and social issues. Its reporting often foregrounds the governance and institutional dimensions of technological change, particularly in relation to citizens’ rights and state accountability.

Within this coverage, **Sunil Abraham** appears as a cited expert offering context on issues such as internet regulation, data governance, surveillance, and the societal implications of digital policy decisions. His contributions are typically situated within policy-oriented or explanatory reporting, helping frame technology-related developments within broader questions of governance and public accountability.

This cluster brings together all available **media mentions** of Sunil Abraham published by *The New Indian Express*, serving as a focused reference rather than an exhaustive archive.

## 📣 Media Mentions {#media}

{% assign media_items = site.pages
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","The New Indian Express"
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
- [Official website](https://www.newindianexpress.com/)

<style>
/* ---------------------------------------------------------
   The New Indian Express Cluster – Minimal styling
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
