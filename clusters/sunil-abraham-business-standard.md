---
layout: default
title: "Sunil Abraham and Business Standard"
description: "A consolidated archive of Sunil Abraham's writings for Business Standard and related news coverage that references his commentary on technology policy, regulation, digital rights, and the political economy of the internet in India."
categories: [Clusters]
permalink: /clusters/sunil-abraham-business-standard/
created: 2026-01-08
---

***Business Standard*** is a leading Indian newspaper known for its in-depth coverage of the economy, public policy, regulation, and corporate affairs. Its reporting on technology frequently situates digital developments within broader discussions of governance, markets, and institutional reform.

Across opinion pieces and reported stories, **Sunil Abraham** has appeared both as a contributor and as a cited expert. His engagement with *Business Standard* typically focuses on the structural dimensions of technology policy, including regulation, surveillance, platform accountability, and the interaction between digital systems and democratic institutions, rather than consumer-facing technology trends.

This cluster brings together all **publications** and **media mentions** associated with *Business Standard*, offering a single reference point for readers examining how technology and digital governance debates have been addressed within Indian business and policy journalism.

## ✍️ Publications

<ol class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Business Standard"
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

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

<ol id="media-list" class="cluster-list">
{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Business Standard"
%}
{% assign media_sorted = media_items | sort:"title" %}

{% for item in media_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
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
   Business Standard Cluster – Minimal Styling
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

/* Sort buttons */
.cluster-sort {
  margin: 0.6rem 0 1rem 0;
}

.cluster-sort button {
  background: #eef3fa;
  border: 1px solid #cdd7e5;
  padding: 0.4rem 0.8rem;
  margin-right: 0.45rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.88rem;
}

.cluster-sort button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {

  const list = document.getElementById("media-list");
  const items = Array.from(list.querySelectorAll("li"));
  const buttons = document.querySelectorAll(".cluster-sort button");

  function sortList(type) {
    let sorted = [...items];

    if (type === "alpha") {
      sorted.sort((a, b) =>
        a.dataset.title.localeCompare(b.dataset.title)
      );
    } 
    else if (type === "newest") {
      sorted.sort((a, b) =>
        b.dataset.date.localeCompare(a.dataset.date)
      );
    } 
    else if (type === "oldest") {
      sorted.sort((a, b) =>
        a.dataset.date.localeCompare(b.dataset.date)
      );
    }

    list.innerHTML = "";
    sorted.forEach(li => list.appendChild(li));

    buttons.forEach(btn => btn.classList.remove("active-sort"));
    document.querySelector(`[data-sort="${type}"]`)
      .classList.add("active-sort");
  }

  sortList("alpha");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => sortList(btn.dataset.sort));
  });

});
</script>
