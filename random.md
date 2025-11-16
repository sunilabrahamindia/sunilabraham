---
layout: default
title: Random Page
permalink: /random/
sitemap: false
---

Loading a random page...

<script>
  // Build the page list using Liquid
  const allPages = [
    {% for p in site.pages %}
      {% unless p.url == "/random/" %}
        {% unless p.url contains "/_short/" %}
          "{{ p.url }}",
        {% endunless %}
      {% endunless %}
    {% endfor %}
  ];

  const randomPage = allPages[Math.floor(Math.random() * allPages.length)];
  window.location.href = randomPage;
</script>
