---
layout: default
title: "Sunil Abraham and Voice of America"
description: "A collection of Voice of America articles that reference Sunil Abraham in discussions on free speech, internet regulation, and digital policy."
categories: [Clusters]
permalink: /clusters/sunil-abraham-voice-of-america/
created: 2026-03-20
---

***Voice of America*** is an international broadcaster that covers global developments in politics, governance, and technology. Its reporting on digital rights and online regulation has occasionally included perspectives from **Sunil Abraham**.

This page brings together media mentions from *Voice of America* that relate to [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Voice of America"
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
- [Official website](https://www.voanews.com/)

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
