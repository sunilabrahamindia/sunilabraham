---
layout: default
title: "Sunil Abraham and Internet Democracy Project"
description: "A collection of Internet Democracy Project articles that reference or discuss Sunil Abraham in the context of digital rights, internet governance, and technology policy."
categories: [Clusters]
permalink: /clusters/sunil-abraham-internet-democracy-project/
created: 2026-03-13
---

***Internet Democracy Project*** is a research initiative that studies the political, social, and legal implications of the internet, with particular attention to digital rights, governance, and technology policy in India and the Global South.

Some of its articles discuss developments in internet regulation and platform governance that involve or reference **Sunil Abraham** and his work on digital policy. This page gathers those media mentions published by the *Internet Democracy Project*, allowing readers to locate the relevant pieces in one place.

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Internet Democracy Project"
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
- [Internet Democracy Project](https://internetdemocracy.in/)

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
