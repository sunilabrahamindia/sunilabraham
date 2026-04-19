---
layout: default
title: "Sunil Abraham and GovTech"
description: "A collection of GovTech articles that reference Sunil Abraham in discussions on digital governance, public technology systems, and policy."
categories: [Clusters]
permalink: /clusters/sunil-abraham-govtech/
created: 2026-04-19
---

***GovTech*** is a publication focused on the use of technology in government, covering public-sector innovation, digital infrastructure, and policy developments.

This page brings together media mentions from *GovTech* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","GovTech"
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
- [Official website](https://www.govtech.com/)

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
