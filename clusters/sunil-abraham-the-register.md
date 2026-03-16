---
layout: default
title: "Sunil Abraham and The Register"
description: "A collection of articles from The Register that reference Sunil Abraham in discussions on internet governance, digital rights, and technology policy."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-the-register/
created: 2026-03-16
---

***The Register*** is an international technology news website known for reporting on computing, cybersecurity, digital policy, and internet infrastructure. Some of its reporting on technology regulation and online governance includes references to **Sunil Abraham** and his work on digital policy.

This page brings together media mentions published in *The Register* that relate to [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","The Register"
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
- [Official website](https://www.theregister.com/)

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
