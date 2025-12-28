---
layout: default
title: "Sunil Abraham and Hindustan Times"
description: "A consolidated archive of Sunil Abraham’s contributions to Hindustan Times and news coverage that references his views on technology, digital rights, platform governance, and public policy in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-hindustan-times/
created: 2025-12-24
---

***Hindustan Times*** is one of India’s most widely circulated English-language newspapers, with strong national coverage spanning politics, law, technology, society, and public affairs. Its reporting frequently engages with how technological change affects governance, civil liberties, and everyday life.

Across opinion writing and reported stories, **Sunil Abraham** has appeared both as a contributor and as a cited expert. His presence in *Hindustan Times* coverage often situates questions of digital rights, surveillance, platform accountability, and internet regulation within broader democratic and constitutional debates rather than narrow sectoral discussions.

This cluster brings together all **publications** and **media mentions** associated with *Hindustan Times*, offering a unified reference point for readers tracing how technology policy and digital governance issues have been addressed in mainstream Indian journalism over time.

## ✍️ Publications {#publications}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Hindustan Times" 
%}
{% assign pub_sorted = pub_items | sort:"title" %}

<ol id="pub-list" class="cluster-list">
{% for item in pub_sorted %}
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

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Hindustan Times" 
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
- [Official website](https://www.hindustantimes.com/)

<style>

/* ---------------------------------------------------------
   LIST DESIGN (consistent with other clusters)
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

.desc {
  font-size: 0.92rem;
  color: #444;
  margin-top: 0.2rem;
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
   Fade animation
--------------------------------------------------------- */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: translateY(0); }
}

</style>

<script>
document.addEventListener("DOMContentLoaded", () => {

  function attachSort(sectionId) {
    const list = document.getElementById(sectionId);
    const items = Array.from(list.querySelectorAll("li"));
    const buttons = list.previousElementSibling.querySelectorAll("button");

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
      document.querySelector(`#${sectionId}`)
        .previousElementSibling
        .querySelector(`[data-sort="${type}"]`)
        .classList.add("active-sort");
    }

    /* Default sort: alphabetical */
    sortList("alpha");

    buttons.forEach(btn => {
      btn.addEventListener("click", () => {
        sortList(btn.dataset.sort);
      });
    });
  }

  attachSort("pub-list");
  attachSort("media-list");
});
</script>
