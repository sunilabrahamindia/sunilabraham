---
layout: default
title: What Links Here
permalink: /tools/what-links-here/
description: Explore internal backlinks across The Sunil Abraham Project.
created: 2026-05-29
exclude_from_backlinks: true
---

{% include under-construction.html %}

{% assign requested_page = page.url %}
{% assign backlinks = site.data.backlinks[requested_page] %}

<div class="backlinks-tool">

  <div class="backlinks-group">

    <h2 class="backlinks-target">
      Pages linking to "{{ page.title }}"
    </h2>

    {% if backlinks %}

      <p><strong>Total backlinks:</strong> {{ backlinks.size }}</p>

      <ul class="backlinks-list">

        {% assign all_content = site.pages | concat: site.documents %}

        {% for source in backlinks %}

          {% assign source_page = all_content | where: "url", source | first %}

          <li>
            {% if source_page %}
              <a href="{{ source }}">{{ source_page.title }}</a>
            {% else %}
              <a href="{{ source }}">{{ source }}</a>
            {% endif %}
          </li>

        {% endfor %}

      </ul>

    {% else %}

      <p>No backlinks found.</p>

    {% endif %}

  </div>

</div>

<style>
.backlinks-tool {
  margin-top: 2rem;
}

.backlinks-group {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #fafafa;
}

.backlinks-target {
  margin-top: 0;
  margin-bottom: 0.8rem;
  font-size: 1.2rem;
}

.backlinks-target a {
  text-decoration: none;
}

.backlinks-list {
  margin: 0;
  padding-left: 1.4rem;
}

.backlinks-list li {
  margin-bottom: 0.4rem;
}

@media (prefers-color-scheme: dark) {
  .backlinks-group {
    background: #1e1e1e;
    border-color: #444;
  }
}
</style>
