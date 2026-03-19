---
layout: default
title: "Sunil Abraham and BW Businessworld"
description: "A collection of BW Businessworld articles that include commentary from Sunil Abraham on technology policy, privacy, and digital governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-bw-businessworld/
created: 2026-03-13
---

***BW Businessworld*** is an Indian business magazine and digital publication covering policy, technology, markets, and public affairs. Some of its reporting on technology and digital policy includes comments from **Sunil Abraham**.

This cluster brings together media mentions from *BW Businessworld* related to [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","BW Businessworld"
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
- [Official website](https://www.businessworld.in/)

<style>

/* ---------------------------------------------------------
   LIST DESIGN
--------------------------------------------------------- */
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
