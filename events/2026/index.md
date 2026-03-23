---
layout: default
title: "Events in 2026"
description: "Events organised and participated in by Sunil Abraham in 2026."
categories: [Events]
permalink: /events/2026/
created: 2026-03-23
---

**Events in 2026** lists events organised and participated in by [Sunil Abraham](/sunil/) during the year.

<ul>
{% assign count = 0 %}

{% assign participated = site.categories["Events participated"] %}
{% if participated %}
{% for post in participated %}
{% if post.date >= "2026-01-01" and post.date <= "2026-12-31" %}
{% assign count = count | plus: 1 %}
<li><a href="{{ post.url }}">{{ post.title }}</a> <span style="color:#555;font-size:0.9em;">({{ post.date | date: "%d %b %Y" }})</span></li>
{% endif %}
{% endfor %}
{% endif %}

{% assign organised = site.categories["Events organised"] %}
{% if organised %}
{% for post in organised %}
{% if post.date >= "2026-01-01" and post.date <= "2026-12-31" %}
{% assign count = count | plus: 1 %}
<li><a href="{{ post.url }}">{{ post.title }}</a> <span style="color:#555;font-size:0.9em;">({{ post.date | date: "%d %b %Y" }})</span></li>
{% endif %}
{% endfor %}
{% endif %}

{% if count == 0 %}
<li style="list-style:none;color:#666;">No events recorded for 2026 yet.</li>
{% endif %}
</ul>

<style>
ul{padding-left:1.2em}
li{margin-bottom:0.5em;line-height:1.4}
@media(max-width:600px){
li span{display:block;font-size:0.85em;color:#666}
}
</style>
