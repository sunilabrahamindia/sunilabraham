---
layout: default
title: "Repository Size History"
description: "Daily measurements of the GitHub repository size for The Sunil Abraham Project, with change history and the latest recorded value."
permalink: /tsap/repository-size/
categories: [TSAP Documentation]
created: 2026-11-02
sitemap: true
---

{% assign measurements = site.data.repository_size_log.measurements %}
{% assign latest = measurements | last %}
{% assign measurement_count = measurements | size %}

<p class="rs-intro">This page tracks the reported size of the <a href="https://github.com/sunilabrahamindia/sunilabraham">The Sunil Abraham Project GitHub repository</a>. Measurements are recorded by an automated Google Apps Script and published here from the repository's data file.</p>

{% if latest %}
<section class="rs-summary" aria-labelledby="rs-latest-heading">
  <div class="rs-summary-main">
    <p class="rs-eyebrow" id="rs-latest-heading">Latest recorded size</p>
    <p class="rs-size">{{ latest.sizeMB | round: 2 }} <span>MB</span></p>
    <p class="rs-updated">Recorded: <time datetime="{{ latest.timestamp }}">{{ latest.timestamp | date: "%-d %B %Y, %H:%M UTC" }}</time></p>
  </div>
  <div class="rs-summary-details">
    <div class="rs-stat">
      <span class="rs-stat-label">Measurements</span>
      <strong>{{ measurement_count }}</strong>
    </div>
    <div class="rs-stat">
      <span class="rs-stat-label">Change from previous measurement</span>
      <strong>
        {% if latest.changeMB == nil %}
          Baseline
        {% elsif latest.changeMB > 0 %}
          +{{ latest.changeMB | round: 2 }} MB
        {% elsif latest.changeMB < 0 %}
          {{ latest.changeMB | round: 2 }} MB
        {% else %}
          0.00 MB
        {% endif %}
      </strong>
      {% if latest.changePercent != nil %}
        {% assign latest_change_percent = latest.changePercent | times: 100 | round: 2 %}
        <span class="rs-stat-note">
          {% if latest_change_percent > 0 %}+{% endif %}{{ latest_change_percent }}% since the previous measurement
        </span>
      {% endif %}
    </div>
  </div>
</section>
{% else %}
<p class="rs-empty">No repository size measurements are available yet. The summary will appear after the first successful data publication.</p>
{% endif %}

<h2 id="how-it-works">How this monitor works</h2>

<p>The monitor records the repository size once a day, usually around 9 a.m. India Standard Time. The schedule may run a little earlier or later because Google Apps Script uses a time window. A measurement appears here after the script runs successfully and the site rebuilds.</p>

<p>The figures are the repository-size values returned by GitHub's API. They are not a count of pages, files, or commits. A change in the reported size can reflect changes to the repository and its Git data.</p>

<h2 id="measurement-history">Measurement history</h2>

<p class="rs-history-note">Newest measurements appear first. Timestamps are shown in UTC. On narrow screens, each record becomes a compact card for easier reading.</p>

{% if measurements and measurement_count > 0 %}
<div class="rs-table-wrap">
  <table class="rs-history">
    <caption>Recorded GitHub repository sizes, newest first</caption>
    <thead>
      <tr>
        <th scope="col">Recorded (UTC)</th>
        <th scope="col">Size</th>
        <th scope="col">Change</th>
        <th scope="col">Change (%)</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody>
      {% for measurement in measurements reversed %}
      <tr>
        <td data-label="Recorded (UTC)"><time datetime="{{ measurement.timestamp }}">{{ measurement.timestamp | date: "%-d %b %Y, %H:%M" }}</time></td>
        <td data-label="Size"><strong>{{ measurement.sizeMB | round: 2 }} MB</strong></td>
        <td data-label="Change">
          {% if measurement.changeMB == nil %}
            —
          {% elsif measurement.changeMB > 0 %}
            +{{ measurement.changeMB | round: 2 }} MB
          {% elsif measurement.changeMB < 0 %}
            {{ measurement.changeMB | round: 2 }} MB
          {% else %}
            0.00 MB
          {% endif %}
        </td>
        <td data-label="Change (%)">
          {% if measurement.changePercent == nil %}
            —
          {% else %}
            {% assign row_change_percent = measurement.changePercent | times: 100 | round: 2 %}
            {% if row_change_percent > 0 %}+{% endif %}{{ row_change_percent }}%
          {% endif %}
        </td>
        <td data-label="Status">{{ measurement.status | default: "Recorded" | escape }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% else %}
<p class="rs-empty">The measurement history is not available yet.</p>
{% endif %}

<p class="rs-source">Source data: <a href="https://github.com/sunilabrahamindia/sunilabraham/blob/main/_data/repository_size_log.json">repository_size_log.json</a>. The source file is updated by the monitoring script; this page does not make live API requests when opened.</p>

<style>
.rs-intro,
.rs-history-note,
.rs-source {
  color: var(--text-muted, #444);
  line-height: 1.65;
}

.rs-summary {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: 1rem;
  margin: 1.25rem 0 1.75rem;
}

.rs-summary-main,
.rs-stat {
  min-width: 0;
  padding: 1.15rem;
  border: 1px solid var(--border-sub, #d8dee4);
  border-radius: 8px;
  background: var(--bg-surface, #fff);
}

.rs-summary-main {
  border-top: 4px solid #1f5fbf;
}

.rs-eyebrow,
.rs-stat-label {
  display: block;
  margin: 0;
  color: var(--text-muted, #444);
  font-size: 0.92rem;
}

.rs-size {
  margin: 0.2rem 0;
  color: var(--text-heading, #0a2e57);
  font-size: clamp(2rem, 6vw, 3rem);
  font-weight: 700;
  line-height: 1.2;
  overflow-wrap: anywhere;
}

.rs-size span {
  font-size: 0.55em;
  font-weight: 600;
}

.rs-updated {
  margin: 0.5rem 0 0;
  color: var(--text-muted, #444);
  font-size: 0.9rem;
}

.rs-summary-details {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}

.rs-stat strong {
  display: block;
  margin-top: 0.25rem;
  color: var(--text-heading, #0a2e57);
  font-size: 1.2rem;
  overflow-wrap: anywhere;
}

.rs-stat-note {
  display: block;
  margin-top: 0.25rem;
  color: var(--text-muted, #444);
  font-size: 0.88rem;
}

.rs-table-wrap {
  width: 100%;
  margin: 1rem 0;
}

.rs-history {
  width: 100%;
  table-layout: fixed;
  font-variant-numeric: tabular-nums;
}

.rs-history caption {
  padding: 0.6rem 0;
  text-align: left;
  color: var(--text-muted, #444);
  font-weight: 600;
}

.rs-history th,
.rs-history td {
  overflow-wrap: anywhere;
}

.rs-history th:nth-child(1) { width: 25%; }
.rs-history th:nth-child(2) { width: 15%; }
.rs-history th:nth-child(3) { width: 18%; }
.rs-history th:nth-child(4) { width: 16%; }
.rs-history th:nth-child(5) { width: 16%; }

.rs-empty {
  padding: 1rem;
  border: 1px solid var(--border-sub, #d8dee4);
  border-radius: 8px;
  color: var(--text-main, #1a1a1a);
}

.rs-source {
  margin-top: 1.5rem;
  font-size: 0.92rem;
  overflow-wrap: anywhere;
}

body.tsap-dark-mode .rs-intro,
body.tsap-dark-mode .rs-history-note,
body.tsap-dark-mode .rs-source,
body.tsap-dark-mode .rs-eyebrow,
body.tsap-dark-mode .rs-stat-label,
body.tsap-dark-mode .rs-updated,
body.tsap-dark-mode .rs-stat-note,
body.tsap-dark-mode .rs-history caption {
  color: var(--text-muted, #cbd5e1) !important;
}

body.tsap-dark-mode .rs-summary-main,
body.tsap-dark-mode .rs-stat,
body.tsap-dark-mode .rs-empty {
  background: var(--bg-surface, #1f2937) !important;
  border-color: var(--border-sub, #374151) !important;
  color: var(--text-main, #e5e7eb) !important;
  box-shadow: none !important;
}

body.tsap-dark-mode .rs-summary-main {
  border-top-color: #60a5fa !important;
}

body.tsap-dark-mode .rs-size,
body.tsap-dark-mode .rs-stat strong {
  color: var(--text-heading, #f3f4f6) !important;
}

body.tsap-dark-mode .rs-history {
  background: var(--bg-surface, #1f2937) !important;
  color: var(--text-main, #e5e7eb) !important;
}

body.tsap-dark-mode .rs-history th {
  background: var(--table-th-bg, #374151) !important;
  color: var(--table-th-text, #f3f4f6) !important;
}

body.tsap-dark-mode .rs-history td,
body.tsap-dark-mode .rs-history th {
  border-color: var(--table-border, #4b5563) !important;
}

@media (max-width: 700px) {
  /* Keep the mobile layout inside the viewport without changing desktop tables. */
  .rs-table-wrap {
    box-sizing: border-box;
    width: 100%;
    max-width: 100%;
    min-width: 0;
  }

  .rs-summary {
    grid-template-columns: 1fr;
  }

  .rs-summary-details {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .rs-summary-main,
  .rs-stat {
    padding: 0.9rem;
  }

  .rs-history,
  .rs-history tbody,
  .rs-history tr,
  .rs-history td {
    box-sizing: border-box;
    display: block;
    width: 100%;
    max-width: 100%;
    min-width: 0;
  }

  .rs-history {
    table-layout: auto;
    background: transparent;
    box-shadow: none;
  }

  .rs-history thead {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  .rs-history tbody {
    display: grid;
    gap: 0.85rem;
  }

  .rs-history tr {
    box-sizing: border-box;
    margin: 0;
    padding: 0.55rem 0.85rem;
    border: 1px solid var(--border-sub, #d8dee4);
    border-radius: 8px;
    background: var(--bg-surface, #fff);
  }

  .rs-history td {
    display: grid;
    grid-template-columns: minmax(7rem, 0.9fr) minmax(0, 1.1fr);
    gap: 0.6rem;
    padding: 0.45rem 0;
    border-bottom: 1px solid var(--table-border, #ddd);
    text-align: right;
  }

  .rs-history td:last-child {
    border-bottom: 0;
  }

  .rs-history td::before {
    content: attr(data-label);
    color: var(--text-muted, #444);
    font-weight: 600;
    text-align: left;
  }

  body.tsap-dark-mode .rs-history tr {
    background: var(--bg-surface, #1f2937) !important;
    border-color: var(--border-sub, #374151) !important;
  }

  body.tsap-dark-mode .rs-history td::before {
    color: var(--text-muted, #cbd5e1) !important;
  }
}

@media (max-width: 380px) {
  .rs-summary-details {
    grid-template-columns: 1fr;
  }

  .rs-history td {
    grid-template-columns: minmax(6.5rem, 0.85fr) minmax(0, 1.15fr);
    gap: 0.4rem;
    font-size: 0.9rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rs-summary-main,
  .rs-stat {
    transition: none !important;
  }
}
</style>

{% include navbox-tsap.html %}
