---
layout: default
title: "Portal: SunilSpeaks"
description: "A curated portal of excerpts, quotations, and sayings drawn from the published work and public interventions of Sunil Abraham."
categories: [Sunil Abraham, TSAP Originals]
permalink: /sunilspeaks/
created: 2026-02-05
---

**SunilSpeaks** is a dedicated portal that brings together excerpts, quotations, and sayings drawn from the published work and public interventions of Sunil Abraham. The selections are sourced from already published materials, including publications, media articles, and media mentions.

The portal serves as a bouquet of handpicked quotes and sayings that reflect recurring ideas, concerns, and reflections expressed across Sunil Abraham's work over time.

Selections and curation are done by Tito Dutta.

> **Gradually, this portal will also include original TSAP quotes and sayings, along with additional curated inputs.**

Quotes are grouped thematically by category to support contextual discovery and exploration.


## Surveillance and Privacy

{% for item in site.data.sunilspeaks %}
  {% if item.categories contains "Surveillance and Privacy" %}
> "{{ item.quote }}"  
> — Sunil Abraham, *[{{ item.source_title }}]({{ item.linked_page }})*
  {% endif %}
{% endfor %}
