---
layout: default
title: "Sunil Abraham and Electronic Frontier Foundation"
description: "A collection of Electronic Frontier Foundation articles that reference Sunil Abraham in discussions on digital rights, privacy, and internet governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-electronic-frontier-foundation/
created: 2026-04-04
---

The ***Electronic Frontier Foundation (EFF)*** is a US-based non-profit organisation focused on defending civil liberties in the digital world. Its work spans issues such as privacy, free expression, surveillance, and the governance of online platforms, often combining legal advocacy with detailed policy analysis.

Within this context, discussions on intermediary liability, digital identity, and internet governance have included references to **Sunil Abraham**, particularly in relation to developments in India and broader global debates.

This page brings together media mentions from the *Electronic Frontier Foundation* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Electronic Frontier Foundation"
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
- [Official website](https://www.eff.org/)

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
