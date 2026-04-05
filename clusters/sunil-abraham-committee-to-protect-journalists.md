---
layout: default
title: "Sunil Abraham and Committee to Protect Journalists"
description: "A collection of Committee to Protect Journalists articles that reference Sunil Abraham in discussions on press freedom, digital rights, and internet governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-committee-to-protect-journalists/
created: 2026-04-06
---

The ***Committee to Protect Journalists (CPJ)*** is an independent non-profit organisation that monitors press freedom worldwide and advocates for the rights and safety of journalists. Its reporting frequently examines how legal frameworks, state actions, and digital policies affect freedom of expression.

In this context, coverage touching on internet regulation, intermediary liability, and online speech has included references to **Sunil Abraham**, particularly in relation to developments in India.

This page brings together media mentions from the *Committee to Protect Journalists* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Committee to Protect Journalists"
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
- [Official website](https://cpj.org/)

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
