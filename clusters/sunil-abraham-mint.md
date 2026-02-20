---
layout: default
title: "Sunil Abraham and Mint"
description: "An archive of Sunil Abraham's articles in Mint and Mint news reports featuring his analysis on technology policy, privacy, and digital governance."
categories: [Clusters, Media mentions]
permalink: /clusters/sunil-abraham-mint/
created: 2026-02-20
---

***Mint*** is a leading Indian business and public policy newspaper published by HT Media. It has established a reputation for careful reporting on regulation, markets, and the governance of emerging technologies, with particular attention to how digital systems reshape economic and civic life.

**Sunil Abraham**'s engagement with Mint spans both authored opinion pieces and quoted commentary in reported articles. His contributions and cited views have addressed subjects including privacy safeguards, digital identity systems, platform regulation, and the institutional design of technology governance.

This page consolidates all Mint material connected to Sunil Abraham, including his own publications and Mint's journalistic coverage referencing his work. It provides a structured archive for readers, researchers, and students seeking a clear view of his presence in Mint's reporting and editorial record.


## ✍️ Publications {#publications}

### Sort by:
<div class="cluster-sort">
  <button data-sort="alpha">Alphabetical</button>
  <button data-sort="newest">Newest First</button>
  <button data-sort="oldest">Oldest First</button>
</div>

{% assign pub_items = site.pages 
     | where_exp:"p","p.categories contains 'Publications'"
     | where:"source","Mint" 
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
     | where:"source","Mint" 
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

- [Sunil Abraham](https://www.livemint.com/search?q=Sunil%20Abraham) on Mint


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
   ANIMATION
--------------------------------------------------------- */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(3px); }
  to { opacity: 1; transform: translateY(0); }
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

      buttons.forEach(btn =>
        btn.classList.remove("active-sort")
      );

      document.querySelector(`#${sectionId}`)
        .previousElementSibling
        .querySelector(`[data-sort="${type}"]`)
        .classList.add("active-sort");
    }

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
