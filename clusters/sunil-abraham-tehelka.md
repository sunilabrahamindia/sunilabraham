---
layout: default
title: "Sunil Abraham and Tehelka"
description: "A collection of articles written by Sunil Abraham for Tehelka magazine, covering technology policy, digital rights, and internet governance."
categories: [Clusters, Publications]
permalink: /clusters/sunil-abraham-tehelka/
created: 2026-03-12
---

***Tehelka*** was an Indian investigative journalism magazine known for long-form reporting on politics, governance, and public policy. Among its essays and commentary on technology and digital society are several articles written by **Sunil Abraham**.

This page gathers those *Tehelka* publications authored by [Sunil Abraham](/sunil/), providing a single reference point for readers and researchers interested in his contributions to the magazine.

## ✍️ Publications {#publications}

{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Tehelka Magazine"
     | sort:"date" | reverse
%}

<ol class="cluster-list">
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

## External links
- [Tehelka](https://en.wikipedia.org/wiki/Tehelka)

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
