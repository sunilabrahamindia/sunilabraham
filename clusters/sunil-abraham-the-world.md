---
layout: default
title: "Sunil Abraham and The World"
description: "A collection of articles from The World and GlobalPost that reference Sunil Abraham in reporting on internet governance, digital rights, and technology policy."
categories: [Clusters]
permalink: /clusters/sunil-abraham-the-world/
created: 2026-04-17
---

***The World*** is an international news programme and digital publication produced by Public Radio International (PRI), focusing on global affairs, politics, and society. Its reporting often examines how technological developments intersect with policy and governance across different countries.

Before its integration into *The World*, *GlobalPost* operated as a separate international news platform known for its in-depth foreign reporting. Following organisational changes, *GlobalPost*'s journalism was incorporated into *The World*, and many earlier articles now exist within that broader archive.

In this context, coverage of internet governance, digital rights, and technology policy has included references to **Sunil Abraham**, particularly where developments in India intersect with global debates.

This page brings together media mentions from *The World* and *GlobalPost* that reference [Sunil Abraham](/sunil/).

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","The World"
%}
{% assign media_sorted = media_items | sort:"title" %}

<ol id="media-list" class="cluster-list">
{% for item in media_sorted %}
  <li data-title="{{ item.title | downcase }}"
      data-date="{{ item.date | date: '%Y-%m-%d' }}">
    <a href="{{ item.permalink }}">{{ item.title }}</a>
    <br>
    <span class="meta">{{ item.date | date: "%d %B %Y" }}</span>
    {% if item.description %}
      <div class="desc">{{ item.description }}</div>
    {% endif %}
  </li>
{% endfor %}
</ol>

## External links
- [Official website](https://theworld.org/)

<style>
.cluster-list {
  margin: 0.8rem 0 1.6rem 0;
  padding-left: 1.1rem;
}

.cluster-list li {
  margin-bottom: 0.75rem;
  animation: fadeUp 0.25s ease;
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
  transition: background 0.2s ease, border-color 0.2s ease;
}

.cluster-sort button:hover {
  background: #dbe6f5;
}

.cluster-sort button.active-sort {
  background: #3278d6;
  color: #fff;
  border-color: #3278d6;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(3px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {

  const list = document.getElementById("media-list");
  if (!list) return;

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

  /* Default */
  sortList("alpha");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      sortList(btn.dataset.sort);
    });
  });

});
</script>
