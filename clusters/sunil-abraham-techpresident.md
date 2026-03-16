---
layout: default
title: "Sunil Abraham and TechPresident"
description: "A collection of TechPresident articles that reference Sunil Abraham in discussions on technology policy, digital governance, and internet rights."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-techpresident/
created: 2026-03-16
---

***TechPresident*** was a technology and politics publication associated with the Personal Democracy Forum. Several of its articles examined the intersection of technology, governance, and civil society, including discussions that drew on insights from **Sunil Abraham**.

This page gathers media mentions from *TechPresident* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","TechPresident"
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
