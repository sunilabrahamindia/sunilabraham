---
layout: default
title: "Sunil Abraham and The Statesman"
description: "A collection of articles from The Statesman that reference Sunil Abraham in discussions on technology policy, privacy, and digital governance."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-the-statesman/
created: 2026-03-18
---

***The Statesman*** is an Indian newspaper covering public policy, governance, and current affairs. Some of its reporting on technology and digital regulation includes references to **Sunil Abraham**.

This page brings together media mentions from *The Statesman* that relate to [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","The Statesman"
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
- [Official website](https://www.thestatesman.com/)

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
