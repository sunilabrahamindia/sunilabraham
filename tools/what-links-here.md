---
layout: default
title: What Links Here
permalink: /tools/what-links-here/
description: Find pages on this site that link to a selected page.
---

{% assign all_content = site.pages | concat: site.documents %}
{% assign sorted_backlink_keys = site.data.backlinks | sort %}
{% assign default_page = page.default_target | default: "/sunil/" %}

{% capture page_titles_json %}
{
  {% assign first_title = true %}
  {% for item in all_content %}
    {% if item.url %}
      {% unless first_title %},{% endunless %}
      {% assign first_title = false %}
      {{ item.url | jsonify }}: {
        "title": {{ item.title | default: item.name | default: item.url | jsonify }},
        "url": {{ item.url | jsonify }}
      }
    {% endif %}
  {% endfor %}
}
{% endcapture %}

<div class="what-links-here-page">
  <a class="skip-link" href="#what-links-results">Skip to results</a>

  <section class="wlh-shell" aria-labelledby="what-links-here-title">
    <header class="wlh-header">
      <div class="wlh-header-main">
        <p class="wlh-eyebrow">Internal link discovery</p>
        <h1 id="what-links-here-title">What Links Here</h1>
        <p class="wlh-intro">
          Select a page to view other pages on this site that link to it.
        </p>
      </div>

      <button
        type="button"
        class="theme-toggle"
        id="themeToggle"
        aria-label="Switch to dark mode"
        aria-pressed="false">
        <span class="theme-toggle__icon theme-toggle__icon--sun" aria-hidden="true">
          <svg viewBox="0 0 24 24" focusable="false">
            <circle cx="12" cy="12" r="4"></circle>
            <path d="M12 2v2.5M12 19.5V22M4.93 4.93l1.77 1.77M17.3 17.3l1.77 1.77M2 12h2.5M19.5 12H22M4.93 19.07l1.77-1.77M17.3 6.7l1.77-1.77"></path>
          </svg>
        </span>
        <span class="theme-toggle__icon theme-toggle__icon--moon" aria-hidden="true">
          <svg viewBox="0 0 24 24" focusable="false">
            <path d="M21 12.79A9 9 0 1 1 11.21 3a7 7 0 0 0 9.79 9.79z"></path>
          </svg>
        </span>
        <span class="theme-toggle__label">Theme</span>
      </button>
    </header>

    <div class="wlh-panel">
      <form class="wlh-controls" role="search" aria-labelledby="controls-heading" onsubmit="return false;">
        <h2 id="controls-heading" class="sr-only">What Links Here controls</h2>

        <div class="control-group control-group--wide">
          <label for="pageSelector">Select page</label>
          <select id="pageSelector" name="pageSelector">
            {% for backlink_entry in sorted_backlink_keys %}
              {% assign target_url = backlink_entry[0] %}
              {% assign target_page = all_content | where: "url", target_url | first %}
              <option value="{{ target_url | escape }}" {% if target_url == default_page %}selected{% endif %}>
                {% if target_page and target_page.title %}
                  {{ target_page.title }} — {{ target_url }}
                {% else %}
                  {{ target_url }}
                {% endif %}
              </option>
            {% endfor %}
          </select>
        </div>

        <div class="control-group control-group--wide">
          <label for="backlinkSearch">Search backlinks</label>
          <input
            type="search"
            id="backlinkSearch"
            name="backlinkSearch"
            placeholder="Filter by title or URL"
            autocomplete="off"
            inputmode="search">
        </div>

        <div class="control-group control-group--narrow">
          <label for="backlinkSort">Sort</label>
          <select id="backlinkSort" name="backlinkSort">
            <option value="az">A–Z</option>
            <option value="za">Z–A</option>
          </select>
        </div>
      </form>

      <section class="wlh-summary" aria-labelledby="summary-heading">
        <h2 id="summary-heading" class="sr-only">Selection summary</h2>

        <div class="summary-card">
          <span class="summary-label">Selected page</span>
          <p class="summary-title" id="selectedPageTitle">Loading…</p>
          <p class="summary-url" id="selectedPageUrl">Loading…</p>
        </div>

        <div class="summary-card summary-card--count">
          <span class="summary-label">Backlinks shown</span>
          <p class="summary-count">
            <span id="backlinkCount">0</span>
          </p>
          <p class="summary-note" id="backlinkCountNote">No backlinks found.</p>
        </div>
      </section>

      <section class="wlh-results" id="what-links-results" aria-labelledby="results-heading">
        <div class="results-header">
          <h2 id="results-heading">Backlinks</h2>
          <p class="results-status" id="resultsStatus" aria-live="polite">Loading results…</p>
        </div>

        <ul class="backlinks-list" id="backlinksList" aria-live="polite" aria-describedby="resultsStatus"></ul>

        <div class="empty-state" id="emptyState" hidden>
          <p class="empty-state__title">No backlinks found.</p>
          <p class="empty-state__text">Try another page, or refine your search.</p>
        </div>
      </section>
    </div>
  </section>
</div>

<script>
  window.WLH_BACKLINKS = {{ site.data.backlinks | jsonify }};
  window.WLH_TITLES = {{ page_titles_json | strip | replace: '
', ' ' }};
  window.WLH_DEFAULT_PAGE = {{ default_page | jsonify }};
</script>

<script>
(function () {
  var root = document.documentElement;
  var themeToggle = document.getElementById("themeToggle");
  var pageSelector = document.getElementById("pageSelector");
  var searchInput = document.getElementById("backlinkSearch");
  var sortSelect = document.getElementById("backlinkSort");
  var backlinksList = document.getElementById("backlinksList");
  var backlinkCount = document.getElementById("backlinkCount");
  var backlinkCountNote = document.getElementById("backlinkCountNote");
  var selectedPageTitle = document.getElementById("selectedPageTitle");
  var selectedPageUrl = document.getElementById("selectedPageUrl");
  var resultsStatus = document.getElementById("resultsStatus");
  var emptyState = document.getElementById("emptyState");

  var backlinksData = window.WLH_BACKLINKS || {};
  var titlesData = window.WLH_TITLES || {};
  var defaultPage = window.WLH_DEFAULT_PAGE || "";
  var currentTheme = "";

  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function applyTheme(theme) {
    currentTheme = theme === "dark" ? "dark" : "light";
    root.setAttribute("data-theme", currentTheme);

    if (themeToggle) {
      var nextTheme = currentTheme === "dark" ? "light" : "dark";
      themeToggle.setAttribute("aria-label", "Switch to " + nextTheme + " mode");
      themeToggle.setAttribute("aria-pressed", String(currentTheme === "dark"));
    }
  }

  function initialiseTheme() {
    applyTheme(systemPrefersDark() ? "dark" : "light");
  }

  function getPageMeta(url) {
    if (url && titlesData[url]) {
      return titlesData[url];
    }

    return {
      title: url,
      url: url
    };
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function getSelectedTarget() {
    return pageSelector ? pageSelector.value : "";
  }

  function getBacklinksForTarget(targetUrl) {
    var links = backlinksData[targetUrl];
    return Array.isArray(links) ? links.slice() : [];
  }

  function normaliseText(value) {
    return String(value || "").toLocaleLowerCase();
  }

  function buildResultObjects(targetUrl) {
    var query = normaliseText(searchInput ? searchInput.value : "");
    var sortOrder = sortSelect ? sortSelect.value : "az";
    var sourceUrls = getBacklinksForTarget(targetUrl);

    var results = sourceUrls.map(function (url) {
      var meta = getPageMeta(url);
      var title = meta && meta.title ? meta.title : url;
      return {
        url: url,
        title: title,
        resolved: Boolean(titlesData[url]),
        sortText: normaliseText(title + " " + url)
      };
    });

    if (query) {
      results = results.filter(function (item) {
        return normaliseText(item.title).indexOf(query) !== -1 ||
               normaliseText(item.url).indexOf(query) !== -1;
      });
    }

    results.sort(function (a, b) {
      var comparison = a.sortText.localeCompare(b.sortText);
      return sortOrder === "za" ? comparison * -1 : comparison;
    });

    return results;
  }

  function renderSummary(targetUrl, visibleCount, totalCount) {
    var meta = getPageMeta(targetUrl);
    var hasResolvedTitle = Boolean(titlesData[targetUrl]);

    selectedPageTitle.textContent = hasResolvedTitle ? meta.title : "Unresolved page";
    selectedPageUrl.textContent = targetUrl || "No page selected";

    backlinkCount.textContent = String(visibleCount);

    if (totalCount === 0) {
      backlinkCountNote.textContent = "No backlinks found for this page.";
    } else if (visibleCount !== totalCount) {
      backlinkCountNote.textContent = "Showing " + visibleCount + " of " + totalCount + " backlinks.";
    } else if (visibleCount === 1) {
      backlinkCountNote.textContent = "Showing 1 backlink.";
    } else {
      backlinkCountNote.textContent = "Showing all " + visibleCount + " backlinks.";
    }
  }

  function renderResults() {
    var targetUrl = getSelectedTarget();
    var allResults = getBacklinksForTarget(targetUrl);
    var visibleResults = buildResultObjects(targetUrl);

    renderSummary(targetUrl, visibleResults.length, allResults.length);

    if (!visibleResults.length) {
      backlinksList.innerHTML = "";
      emptyState.hidden = false;

      if (allResults.length === 0) {
        resultsStatus.textContent = "No pages link to the selected page.";
      } else {
        resultsStatus.textContent = "No backlinks match the current search.";
      }

      return;
    }

    emptyState.hidden = true;

    backlinksList.innerHTML = visibleResults.map(function (item) {
      var titleHtml = escapeHtml(item.title);
      var urlHtml = escapeHtml(item.url);
      var unresolvedBadge = item.resolved
        ? ""
        : '<span class="backlink-badge">Unresolved title</span>';

      return '' +
        '<li class="backlink-item">' +
          '<a class="backlink-link" href="' + urlHtml + '">' +
            '<span class="backlink-title">' + titleHtml + '</span>' +
            unresolvedBadge +
            '<span class="backlink-url">' + urlHtml + '</span>' +
          '</a>' +
        '</li>';
    }).join("");

    if (visibleResults.length === 1) {
      resultsStatus.textContent = "1 backlink shown.";
    } else {
      resultsStatus.textContent = visibleResults.length + " backlinks shown.";
    }
  }

  function syncFromHash() {
    if (!window.location.hash) {
      return false;
    }

    var rawHash = window.location.hash.replace(/^#/, "");
    if (!rawHash) {
      return false;
    }

    var decoded;
    try {
      decoded = decodeURIComponent(rawHash);
    } catch (error) {
      return false;
    }

    if (pageSelector && backlinksData.hasOwnProperty(decoded)) {
      pageSelector.value = decoded;
      return true;
    }

    return false;
  }

  function updateHash(targetUrl) {
    if (!targetUrl) {
      return;
    }

    var encoded = encodeURIComponent(targetUrl);
    if (window.location.hash !== "#" + encoded) {
      if (history && history.replaceState) {
        history.replaceState(null, "", "#" + encoded);
      } else {
        window.location.hash = encoded;
      }
    }
  }

  function initialiseSelection() {
    var hasHashSelection = syncFromHash();

    if (!hasHashSelection && pageSelector) {
      if (defaultPage && backlinksData.hasOwnProperty(defaultPage)) {
        pageSelector.value = defaultPage;
      } else if (pageSelector.options.length) {
        pageSelector.selectedIndex = 0;
      }
    }

    renderResults();
    updateHash(getSelectedTarget());
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      applyTheme(currentTheme === "dark" ? "light" : "dark");
    });
  }

  if (pageSelector) {
    pageSelector.addEventListener("change", function () {
      renderResults();
      updateHash(getSelectedTarget());
    });
  }

  if (searchInput) {
    searchInput.addEventListener("input", renderResults);
  }

  if (sortSelect) {
    sortSelect.addEventListener("change", renderResults);
  }

  window.addEventListener("hashchange", function () {
    if (syncFromHash()) {
      renderResults();
    }
  });

  initialiseTheme();
  initialiseSelection();
})();
</script>

<style>
  :root {
    --wlh-bg: #fcfcfd;
    --wlh-surface: #ffffff;
    --wlh-surface-2: #f4f6fb;
    --wlh-border: #d6dbe7;
    --wlh-border-strong: #b8c1d6;
    --wlh-text: #1b2330;
    --wlh-text-muted: #526076;
    --wlh-accent: #1456c0;
    --wlh-accent-hover: #0f469d;
    --wlh-accent-soft: #e8f0ff;
    --wlh-focus: #1456c0;
    --wlh-shadow: 0 12px 30px rgba(17, 24, 39, 0.08);
    --wlh-radius: 16px;
    --wlh-radius-sm: 10px;
    --wlh-control-height: 2.9rem;
    --wlh-max-width: 72rem;
  }

  [data-theme="dark"] {
    --wlh-bg: #0f141c;
    --wlh-surface: #161d27;
    --wlh-surface-2: #1d2633;
    --wlh-border: #2a3648;
    --wlh-border-strong: #3a4a62;
    --wlh-text: #edf2f8;
    --wlh-text-muted: #b5c0d3;
    --wlh-accent: #7fb0ff;
    --wlh-accent-hover: #a8c8ff;
    --wlh-accent-soft: #1b2d4a;
    --wlh-focus: #9ac0ff;
    --wlh-shadow: 0 14px 36px rgba(0, 0, 0, 0.32);
  }

  @media (prefers-color-scheme: dark) {
    :root:not([data-theme]) {
      --wlh-bg: #0f141c;
      --wlh-surface: #161d27;
      --wlh-surface-2: #1d2633;
      --wlh-border: #2a3648;
      --wlh-border-strong: #3a4a62;
      --wlh-text: #edf2f8;
      --wlh-text-muted: #b5c0d3;
      --wlh-accent: #7fb0ff;
      --wlh-accent-hover: #a8c8ff;
      --wlh-accent-soft: #1b2d4a;
      --wlh-focus: #9ac0ff;
      --wlh-shadow: 0 14px 36px rgba(0, 0, 0, 0.32);
    }
  }

  .what-links-here-page {
    background: var(--wlh-bg);
    color: var(--wlh-text);
    margin-block: 1.5rem 3rem;
  }

  .skip-link {
    position: absolute;
    left: -9999px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
  }

  .skip-link:focus {
    left: 1rem;
    top: 1rem;
    width: auto;
    height: auto;
    padding: 0.75rem 1rem;
    background: var(--wlh-surface);
    color: var(--wlh-text);
    border: 2px solid var(--wlh-focus);
    border-radius: 0.5rem;
    z-index: 1000;
    box-shadow: var(--wlh-shadow);
  }

  .wlh-shell {
    max-width: var(--wlh-max-width);
    margin-inline: auto;
    padding-inline: 1rem;
  }

  .wlh-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
  }

  .wlh-header-main {
    min-width: 0;
  }

  .wlh-eyebrow {
    margin: 0 0 0.35rem;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--wlh-text-muted);
  }

  .wlh-header h1 {
    margin: 0;
    font-size: clamp(1.8rem, 3vw, 2.5rem);
    line-height: 1.15;
  }

  .wlh-intro {
    margin: 0.75rem 0 0;
    max-width: 48rem;
    color: var(--wlh-text-muted);
  }

  .theme-toggle {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    min-height: 2.75rem;
    padding: 0.7rem 0.95rem;
    border: 1px solid var(--wlh-border);
    border-radius: 999px;
    background: var(--wlh-surface);
    color: var(--wlh-text);
    box-shadow: var(--wlh-shadow);
    flex-shrink: 0;
  }

  .theme-toggle:hover {
    border-color: var(--wlh-border-strong);
    background: var(--wlh-surface-2);
  }

  .theme-toggle__icon {
    width: 1.1rem;
    height: 1.1rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }

  .theme-toggle__icon svg {
    width: 1.1rem;
    height: 1.1rem;
    stroke: currentColor;
    fill: none;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  [data-theme="light"] .theme-toggle__icon--moon,
  :root:not([data-theme]) .theme-toggle__icon--moon {
    display: none;
  }

  [data-theme="dark"] .theme-toggle__icon--sun {
    display: none;
  }

  .wlh-panel {
    background: var(--wlh-surface);
    border: 1px solid var(--wlh-border);
    border-radius: var(--wlh-radius);
    box-shadow: var(--wlh-shadow);
    padding: 1rem;
  }

  .wlh-controls {
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(0, 1.4fr) minmax(10rem, 0.7fr);
    gap: 1rem;
    align-items: end;
    margin-bottom: 1rem;
  }

  .control-group {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    min-width: 0;
  }

  .control-group label {
    font-weight: 700;
    color: var(--wlh-text);
  }

  .control-group input,
  .control-group select {
    width: 100%;
    min-height: var(--wlh-control-height);
    padding: 0.7rem 0.85rem;
    border: 1px solid var(--wlh-border);
    border-radius: 0.8rem;
    background: var(--wlh-surface);
    color: var(--wlh-text);
  }

  .control-group input::placeholder {
    color: var(--wlh-text-muted);
    opacity: 1;
  }

  .control-group input:hover,
  .control-group select:hover {
    border-color: var(--wlh-border-strong);
  }

  .control-group input:focus,
  .control-group select:focus,
  .theme-toggle:focus,
  .backlink-link:focus {
    outline: 3px solid var(--wlh-focus);
    outline-offset: 2px;
  }

  .wlh-summary {
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(13rem, 1fr);
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .summary-card {
    background: var(--wlh-surface-2);
    border: 1px solid var(--wlh-border);
    border-radius: 1rem;
    padding: 1rem;
    min-width: 0;
  }

  .summary-label {
    display: inline-block;
    margin-bottom: 0.45rem;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--wlh-text-muted);
  }

  .summary-title {
    margin: 0;
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.35;
    word-break: break-word;
  }

  .summary-url {
    margin: 0.5rem 0 0;
    color: var(--wlh-text-muted);
    word-break: break-all;
  }

  .summary-card--count {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .summary-count {
    margin: 0;
    font-size: clamp(1.9rem, 4vw, 2.8rem);
    font-weight: 800;
    line-height: 1;
  }

  .summary-note {
    margin: 0.55rem 0 0;
    color: var(--wlh-text-muted);
  }

  .results-header {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.9rem;
  }

  .results-header h2 {
    margin: 0;
    font-size: 1.2rem;
  }

  .results-status {
    margin: 0;
    color: var(--wlh-text-muted);
  }

  .backlinks-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    gap: 0.85rem;
  }

  .backlink-item {
    margin: 0;
  }

  .backlink-link {
    display: block;
    min-height: 44px;
    padding: 1rem;
    border: 1px solid var(--wlh-border);
    border-radius: 1rem;
    background: var(--wlh-surface);
    color: inherit;
    text-decoration: none;
  }

  .backlink-link:hover {
    border-color: var(--wlh-accent);
    background: var(--wlh-accent-soft);
  }

  .backlink-title {
    display: block;
    font-weight: 700;
    line-height: 1.4;
    word-break: break-word;
  }

  .backlink-url {
    display: block;
    margin-top: 0.45rem;
    color: var(--wlh-text-muted);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 0.95rem;
    word-break: break-all;
  }

  .backlink-badge {
    display: inline-flex;
    align-items: center;
    margin-top: 0.55rem;
    padding: 0.22rem 0.55rem;
    border: 1px solid var(--wlh-border-strong);
    border-radius: 999px;
    background: var(--wlh-surface);
    color: var(--wlh-text-muted);
    font-size: 0.78rem;
    font-weight: 700;
  }

  .empty-state {
    padding: 1.5rem 1rem;
    border: 1px dashed var(--wlh-border-strong);
    border-radius: 1rem;
    background: var(--wlh-surface-2);
  }

  .empty-state__title {
    margin: 0;
    font-weight: 700;
  }

  .empty-state__text {
    margin: 0.45rem 0 0;
    color: var(--wlh-text-muted);
  }

  .sr-only {
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

  @media (max-width: 860px) {
    .wlh-controls,
    .wlh-summary {
      grid-template-columns: 1fr;
    }

    .wlh-header {
      flex-direction: column;
      align-items: stretch;
    }

    .theme-toggle {
      align-self: flex-start;
    }
  }

  @media (max-width: 640px) {
    .what-links-here-page {
      margin-block: 1rem 2rem;
    }

    .wlh-shell {
      padding-inline: 0.75rem;
    }

    .wlh-panel {
      padding: 0.85rem;
      border-radius: 1rem;
    }

    .wlh-header h1 {
      font-size: 1.75rem;
    }

    .summary-card,
    .backlink-link {
      padding: 0.9rem;
    }

    .theme-toggle {
      width: 100%;
      justify-content: center;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    html:focus-within {
      scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
      transition: none !important;
      animation: none !important;
    }
  }
</style>