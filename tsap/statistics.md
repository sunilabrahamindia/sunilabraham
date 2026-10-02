---
layout: default
title: "Statistics"
description: "A build-time statistical overview of the Sunil Abraham Project, including published page counts, publication timeline, category distribution and metadata coverage."
permalink: /statistics/
categories: [TSAP Documentation]
page_id: TSAP-0929
created: 2026-04-30
---

{% assign dated_pages = site.pages | where_exp: "p", "p.created" | sort: "created" %}
{% assign all_categories = "" | split: "," %}
{% assign years = "" | split: "," %}
{% assign months = "" | split: "," %}
{% assign id_count = 0 %}
{% assign description_count = 0 %}
{% assign category_count = 0 %}
{% for page in dated_pages %}
  {% assign year = page.created | date: "%Y" %}
  {% assign month = page.created | date: "%Y-%m" %}
  {% unless years contains year %}{% assign years = years | push: year %}{% endunless %}
  {% unless months contains month %}{% assign months = months | push: month %}{% endunless %}
  {% if page.page_id %}{% assign id_count = id_count | plus: 1 %}{% endif %}
  {% if page.description and page.description != "" %}{% assign description_count = description_count | plus: 1 %}{% endif %}
  {% if page.categories and page.categories.size > 0 %}
    {% assign category_count = category_count | plus: 1 %}
    {% for category in page.categories %}
      {% unless all_categories contains category %}{% assign all_categories = all_categories | push: category %}{% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign sorted_years = years | sort %}
{% assign sorted_months = months | sort %}
{% assign first_page = dated_pages | first %}
{% assign latest_page = dated_pages | last %}
{% assign current_year = site.time | date: "%Y" %}
{% assign current_month = site.time | date: "%Y-%m" %}
{% assign current_year_count = 0 %}
{% assign current_month_count = 0 %}
{% for page in dated_pages %}
  {% assign page_year = page.created | date: "%Y" %}
  {% assign page_month = page.created | date: "%Y-%m" %}
  {% if page_year == current_year %}{% assign current_year_count = current_year_count | plus: 1 %}{% endif %}
  {% if page_month == current_month %}{% assign current_month_count = current_month_count | plus: 1 %}{% endif %}
{% endfor %}

The figures below are generated from page metadata during the Jekyll build. They describe pages carrying a created date, not visitor analytics or search-engine index counts. The total may include documentation and utility pages as well as articles.

## At a glance

<div class="stats-grid" aria-label="Project statistics">
  <div class="stats-card"><span class="stats-number">{{ dated_pages | size }}</span><span class="stats-label">Dated pages</span></div>
  <div class="stats-card"><span class="stats-number">{{ all_categories | size }}</span><span class="stats-label">Distinct categories</span></div>
  <div class="stats-card"><span class="stats-number">{{ current_year_count }}</span><span class="stats-label">Created in {{ current_year }}</span></div>
  <div class="stats-card"><span class="stats-number">{{ id_count }}</span><span class="stats-label">Pages with permanent IDs</span></div>
</div>

## Publication timeline

{% if first_page and latest_page %}
- **Earliest recorded creation date:** {{ first_page.created | date: "%d %B %Y" }}
- **Latest recorded creation date:** {{ latest_page.created | date: "%d %B %Y" }} - [{{ latest_page.title | escape }}]({{ latest_page.url | relative_url }})
- **Months represented:** {{ months | size }}
- **Pages created this month ({{ site.time | date: "%B %Y" }}):** {{ current_month_count }}
{% endif %}

### Pages created by year

<table class="stats-table">
<thead><tr><th scope="col">Year</th><th scope="col">Pages</th></tr></thead>
<tbody>
{% for year in sorted_years reversed %}
{% assign year_total = 0 %}
{% for page in dated_pages %}
{% assign page_year = page.created | date: "%Y" %}
{% if page_year == year %}{% assign year_total = year_total | plus: 1 %}{% endif %}
{% endfor %}
<tr><th scope="row">{{ year }}</th><td>{{ year_total }}</td></tr>
{% endfor %}
</tbody>
</table>

### Pages created by month

<table class="stats-table">
<thead><tr><th scope="col">Month</th><th scope="col">Pages</th></tr></thead>
<tbody>
{% for month in sorted_months reversed %}
{% assign month_total = 0 %}
{% for page in dated_pages %}
{% assign page_month = page.created | date: "%Y-%m" %}
{% if page_month == month %}{% assign month_total = month_total | plus: 1 %}{% endif %}
{% endfor %}
<tr><th scope="row">{{ month | date: "%B %Y" }}</th><td>{{ month_total }}</td></tr>
{% endfor %}
</tbody>
</table>

## Metadata coverage

<table class="stats-table">
<thead><tr><th scope="col">Indicator</th><th scope="col">Count</th></tr></thead>
<tbody>
<tr><th scope="row">Pages with a permanent page ID</th><td>{{ id_count }} / {{ dated_pages | size }}</td></tr>
<tr><th scope="row">Pages with a description</th><td>{{ description_count }} / {{ dated_pages | size }}</td></tr>
<tr><th scope="row">Pages assigned to at least one category</th><td>{{ category_count }} / {{ dated_pages | size }}</td></tr>
</tbody>
</table>

These are coverage counts, not a full validation audit. Duplicate IDs, duplicate permalinks, malformed dates and broken internal links require a separate repository-wide check and are not inferred here.

## Method

- A page is included when it has a non-empty created field.
- Dates use created metadata, not Git commit time or last-modified time.
- Category totals count distinct category names attached to included pages.
- The current year and month use the build's site.time.
- This page does not measure traffic, readership, search visibility or social-media reach.

<style>
.stats-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.85rem;margin:1.25rem 0 1.75rem}
.stats-card{min-width:0;padding:1rem;border:1px solid var(--border-sub,#d8dee4);border-radius:10px;background:var(--bg-surface,#fff);text-align:center}
.stats-number{display:block;color:var(--text-heading,#0a2e57);font-size:clamp(1.6rem,3.5vw,2.4rem);font-weight:700;line-height:1.25;font-variant-numeric:tabular-nums}
.stats-label{display:block;margin-top:.35rem;color:var(--text-muted,#444);font-size:.92rem;line-height:1.4}
.stats-table{width:100%;display:table;table-layout:auto}
.stats-table th,.stats-table td{overflow-wrap:anywhere}
@media(max-width:700px){.stats-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:.55rem}.stats-card{padding:.8rem .55rem}.stats-label{font-size:.84rem}.stats-table{font-size:.9rem}.stats-table th,.stats-table td{padding:.55rem .45rem}}
@media(max-width:360px){.stats-grid{grid-template-columns:1fr 1fr}}
body.tsap-dark-mode .stats-card{background:var(--bg-surface,#1f2937);border-color:var(--border-sub,#374151)}
body.tsap-dark-mode .stats-number{color:var(--text-heading,#f3f4f6)}
body.tsap-dark-mode .stats-label{color:var(--text-muted,#cbd5e1)}
</style>
