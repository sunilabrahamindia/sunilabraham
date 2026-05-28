---
layout: default
title: What Links Here
permalink: /tools/what-links-here/
description: Explore internal backlinks across The Sunil Abraham Project.
created: 2026-05-29
exclude_from_backlinks: true
---

{% include under-construction.html %}

{% assign requested_page = "/sunil/" %}
{% assign backlinks = site.data.backlinks[requested_page] %}
{% assign all_content = site.pages | concat: site.documents %}

<div class="backlinks-tool">

  <div class="backlinks-header">

    <h2>
      Pages linking to "{{ requested_page }}"
    </h2>

    {% if backlinks %}
      <p class="backlinks-count">
        Total backlinks: {{ backlinks.size }}
      </p>
    {% endif %}

  </div>

  {% if backlinks %}

    <div class="backlinks-controls">

      <label for="backlinkSort">Sort:</label>

      <select id="backlinkSort">
        <option value="az">A–Z</option>
        <option value="za">Z–A</option>
      </select>

    </div>

    <ul class="backlinks-list" id="backlinksList">

      {% for source in backlinks %}

        {% assign source_page = all_content | where: "url", source | first %}

        <li class="backlink-item">

          {% if source_page %}

            <a href="{{ source }}">
              {{ source_page.title }}
            </a>

          {% else %}

            <a href="{{ source }}">
              {{ source }}
            </a>

          {% endif %}

        </li>

      {% endfor %}

    </ul>

  {% else %}

    <p>No backlinks found.</p>

  {% endif %}

</div>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const sortSelect = document.getElementById("backlinkSort");
  const list = document.getElementById("backlinksList");

  if (!sortSelect || !list) return;

  sortSelect.addEventListener("change", function () {

    const items = Array.from(list.querySelectorAll(".backlink-item"));

    items.sort((a, b) => {
      const textA = a.innerText.trim().toLowerCase();
      const textB = b.innerText.trim().toLowerCase();

      if (sortSelect.value === "az") {
        return textA.localeCompare(textB);
      } else {
        return textB.localeCompare(textA);
      }
    });

    items.forEach(item => list.appendChild(item));

  });

});
</script>

<style>
.backlinks-tool {
  margin-top: 2rem;
}

.backlinks-header {
  margin-bottom: 1.5rem;
}

.backlinks-header h2 {
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
}

.backlinks-count {
  color: #444;
}

.backlinks-controls {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
}

.backlinks-controls select {
  padding: 0.4rem 0.6rem;
  border: 1px solid #999;
  border-radius: 6px;
  background: #fff;
  color: #111;
}

.backlinks-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.backlink-item {
  padding: 0.8rem 1rem;
  margin-bottom: 0.7rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #fafafa;
  line-height: 1.5;
  word-break: break-word;
}

.backlink-item a {
  text-decoration: none;
}

.backlink-item a:hover {
  text-decoration: underline;
}

@media (prefers-color-scheme: dark) {

  .backlinks-count {
    color: #ccc;
  }

  .backlinks-controls select {
    background: #222;
    color: #eee;
    border-color: #555;
  }

  .backlink-item {
    background: #1e1e1e;
    border-color: #444;
  }

}

@media (max-width: 700px) {

  .backlink-item {
    padding: 0.75rem;
  }

  .backlinks-header h2 {
    font-size: 1.25rem;
  }

}
</style>
