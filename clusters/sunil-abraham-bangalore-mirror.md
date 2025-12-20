---
layout: default
title: "Sunil Abraham and Bangalore Mirror"
description: "A consolidated archive of Sunil Abraham's writings for Bangalore Mirror and media coverage featuring his commentary on technology, privacy, social media, and digital culture in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-bangalore-mirror/
created: 2025-12-20
---

***Bangalore Mirror*** is an Indian daily newspaper known for its city-focused reporting, opinion writing, and long-form weekend features that explore urban life, culture, and social change. Alongside local news and commentary, the paper has regularly published reflective pieces on how technology and digital platforms shape everyday experiences in India.

Over the years, **Sunil Abraham** has contributed opinion writing to *Bangalore Mirror* and has also appeared as a quoted source across its reporting and Sunday Read features. His presence in the paper often connects questions of technology policy and digital rights with the lived experiences of internet users, particularly in urban contexts.

This cluster brings together all **publications** and **media mentions** connected to *Bangalore Mirror*, providing a single reference point for readers tracing how issues such as online privacy, social media behaviour, digital exit, and platform power were discussed in mainstream city journalism.


## ✍️ Publications

<ul class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Bangalore Mirror"
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
</ul>

## 📣 Media Mentions

<ul class="cluster-list">
{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Bangalore Mirror"
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
</ul>

<style>
/* ---------------------------------------------------------
   Bangalore Mirror Cluster – Minimal Styling
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
