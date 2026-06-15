---
layout: default
title: "Sunil Abraham and IBN Live"
description: "A collection of IBN Live articles that reference Sunil Abraham in discussions on digital rights, internet governance, and technology policy."
categories: [Clusters]
permalink: /clusters/sunil-abraham-ibn-live/
page_id: TSAP-0957
created: 2026-05-11
---

***IBN Live*** was the digital news platform of the CNN-IBN network, one of India's prominent English-language television news channels. The site carried breaking news, opinion pieces, and in-depth reports spanning politics, business, and technology, making it a significant record of mainstream Indian media coverage through its active years.

References to **Sunil Abraham** appear within IBN Live's coverage where conversations around digital rights, surveillance, internet policy, and civil liberties in India reached a broader public audience. These mentions reflect how issues debated in specialist circles were brought into mainstream news discourse.

This page brings together media mentions from *IBN Live* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","IBN Live"
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
