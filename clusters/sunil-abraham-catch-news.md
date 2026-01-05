---
layout: default
title: "Sunil Abraham and Catch News"
description: "A curated cluster of Catch News articles that include Sunil Abraham’s writing and quoted commentary on technology policy, digital rights, online speech, and the governance of internet platforms in India."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-catch-news/
created: 2026-01-05
---

***Catch News*** is an Indian digital news platform known for its explanatory reporting, interviews, and opinion-led coverage of politics, policy, and social issues. Its technology reporting often situates digital developments within broader questions of law, rights, and public accountability.

Within this coverage, **Sunil Abraham** appears both as a contributor and as a cited expert. His engagement with *Catch News* typically focuses on how internet regulation, surveillance practices, and platform governance intersect with constitutional values and democratic oversight, rather than on product- or industry-led narratives.

This cluster brings together all available **publications** and **media mentions** associated with *Catch News*, offering a consolidated reference for readers tracing how technology policy debates have been presented through this outlet.

## ✍️ Publications {#publications}

<ol class="cluster-list">
{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Catch News" 
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

## 📣 Media Mentions {#media}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign media_items = site.pages 
     | where_exp:"p","p.categories contains 'Media mentions'"
     | where:"source","Catch News"
%}
{% assign media_sorted = media_items | sort:"title" %}

<ol id="media-list" class="cluster-list">
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

## External links
- [Official website](https://www.catchnews.com/)

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
   SORT BUTTONS (media only)
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
      const sorted = [...items];

      if (type === "alpha") {
        sorted.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
      } else if (type === "newest") {
        sorted.sort((a, b) => b.dataset.date.localeCompare(a.dataset.date));
      } else if (type === "oldest") {
        sorted.sort((a, b) => a.dataset.date.localeCompare(b.dataset.date));
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
      btn.addEventListener("click", () => sortList(btn.dataset.sort));
    });
  }

  attachSort("media-list");
});
</script>
