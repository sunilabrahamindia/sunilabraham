---
layout: default
title: "Sunil Abraham and Mid-Day"
description: "A collection of Mid-Day articles that reference Sunil Abraham in discussions on digital rights, technology policy, and internet governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-mid-day/
page_id: TSAP-0958
created: 2026-05-11
---

*Mid-Day* is a Mumbai-based newspaper with a strong readership across print and digital formats. Known for its sharp, accessible reporting on city affairs, national news, and popular culture, it has long served as a key voice in western Indian media. Its technology and policy coverage occasionally draws on expert commentary from civil society and the digital rights space.

Among those voices, **Sunil Abraham** has been cited in *Mid-Day* coverage touching on questions of surveillance, data privacy, and the evolving regulatory landscape around technology in India. These appearances place specialist perspectives within a wider public conversation.

This page brings together media mentions from *Mid-Day* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Mid-Day"
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
- [Official website](https://www.mid-day.com/)

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
