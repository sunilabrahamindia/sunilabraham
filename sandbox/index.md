---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

<ol>
{% assign latest = site.posts | sort: "date" | reverse %}
{% for post in latest %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span> — {{ post.date | date: "%d %B %Y" }}</span>
  </li>
{% endfor %}
</ol>

