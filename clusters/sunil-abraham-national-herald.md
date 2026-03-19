---
layout: default
title: "Sunil Abraham and National Herald"
description: "A collection of National Herald articles that reference Sunil Abraham in discussions related to technology policy, digital rights, and internet governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-national-herald/
created: 2026-03-15
---

***National Herald*** is an Indian news publication covering politics, public policy, society, and technology. Some of its reporting on digital governance and technology regulation includes references to **Sunil Abraham** and his work in the field of internet policy.

This page gathers media mentions from *National Herald* that relate to [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","National Herald"
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
- [Official website](https://www.nationalheraldindia.com/)

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
