---
layout: default
title: "Sunil Abraham and Mumbai Mirror"
description: "A consolidated archive of Sunil Abraham's writings for Mumbai Mirror and media coverage featuring his commentary on technology, privacy, social media, and digital culture in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-mumbai-mirror/
created: 2025-12-21
---

***Mumbai Mirror*** is a metropolitan daily newspaper recognised for its opinion pages, lifestyle coverage, and weekend features that examine contemporary social trends alongside city news. Its reporting has frequently engaged with the cultural and behavioural shifts brought about by digital technologies in urban India.

Within *Mumbai Mirror*, **Sunil Abraham** has appeared both as an author of opinion pieces and as a quoted commentator in feature stories and reported articles. His contributions typically address the social implications of technology use, ranging from online privacy and platform norms to changing patterns of participation, withdrawal, and visibility in networked spaces.

This cluster assembles all **publications** and **media mentions** associated with *Mumbai Mirror*, offering a consolidated view of how debates around technology, digital rights, and everyday internet practices have been reflected in mainstream city journalism.

## ✍️ Publications

<ol class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Mumbai Mirror"
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
     | where:"source","Mumbai Mirror"
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
   Mumbai Mirror Cluster – Minimal Styling
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
