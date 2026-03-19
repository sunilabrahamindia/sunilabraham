---
layout: default
title: "Sunil Abraham and Newslaundry"
description: "A collection of Newslaundry reports and stories that include commentary from Sunil Abraham on technology policy, privacy, and digital governance."
categories: [Clusters]
permalink: /clusters/sunil-abraham-newslaundry/
created: 2026-03-09
---

***Newslaundry*** is an independent Indian digital media platform focusing on journalism, media criticism, public policy, and technology. Some of its reporting on digital rights, internet governance, and technology policy includes comments and analysis from **Sunil Abraham**.

This page gathers those media mentions from *Newslaundry* so that readers can easily find the relevant articles published by the platform.

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Newslaundry" 
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
- [Sunil Abraham](https://www.newslaundry.com/search?q=Sunil+Abraham) search results on *Newslaundry*

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

/* ---------------------------------------------------------
   SORT BUTTONS
--------------------------------------------------------- */
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

/* ---------------------------------------------------------
   Animation
--------------------------------------------------------- */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(3px); }
  to { opacity: 1; transform: translateY(0); }
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

  /* Default sort */
  sortList("alpha");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      sortList(btn.dataset.sort);
    });
  });

});
</script>
