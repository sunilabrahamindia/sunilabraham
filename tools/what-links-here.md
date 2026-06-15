---
layout: default
title: What Links Here
permalink: /tools/what-links-here/
description: Find pages on this site that link to a selected page.
page_id: TSAP-1026
created: 2026-05-29
exclude_from_backlinks: true
---

{% include notice.html message="This tool is under active development. The main backlink discovery functionality is working, but some display, title-resolution, duplicate-entry, and interface issues remain and are being refined." %}

{% assign all_content = site.pages | concat: site.documents %}
{% assign sorted_backlink_keys = site.data.backlinks | sort %}
{% assign default_page = page.default_target | default: "/sunil/" %}

{% capture page_titles_json %}
{
  {% assign first_title = true %}
  {% for item in all_content %}
    {% if item.url %}
      {% assign item_title = item.title | default: item.name | default: item.url %}
      {% assign normalised_url = item.url %}
      {% if normalised_url != "/" and normalised_url != "" and normalised_url != nil %}
        {% assign last_character = normalised_url | slice: -1, 1 %}
        {% unless last_character == "/" %}
          {% assign normalised_url = normalised_url | append: "/" %}
        {% endunless %}
      {% endif %}

      {% unless first_title %},{% endunless %}
      {% assign first_title = false %}
      {{ normalised_url | jsonify }}: {
        "title": {{ item_title | jsonify }},
        "url": {{ normalised_url | jsonify }}
      }
    {% endif %}
  {% endfor %}
}
{% endcapture %}

<div class="what-links-here-page">
  <section class="wlh-shell" aria-labelledby="what-links-here-title">

    <div class="wlh-panel">
      <form class="wlh-controls" role="search" aria-labelledby="controls-heading" onsubmit="return false;">
        <h2 id="controls-heading" class="sr-only">What Links Here controls</h2>

        <div class="control-group control-group--selector">
          <label for="pageSelector">Page</label>
          <select id="pageSelector" name="pageSelector">
            {% for backlink_entry in sorted_backlink_keys %}
              {% assign target_url = backlink_entry[0] %}
              {% assign target_page = all_content | where: "url", target_url | first %}
              {% unless target_page %}
                {% assign target_url_without_slash = target_url %}
                {% assign target_last_character = target_url | slice: -1, 1 %}
                {% if target_last_character == "/" and target_url != "/" %}
                  {% assign target_url_without_slash = target_url | slice: 0, target_url.size | minus: 1 %}
                {% endif %}
                {% assign target_page = all_content | where: "url", target_url_without_slash | first %}
              {% endunless %}

              <option value="{{ target_url | escape }}" {% if target_url == default_page %}selected{% endif %}>
                {% if target_page and target_page.title %}
                  {{ target_page.title }}
                {% else %}
                  {{ target_url }}
                {% endif %}
              </option>
            {% endfor %}
          </select>
        </div>

        <div class="control-group control-group--search">
          <label for="backlinkSearch">Search</label>
          <input
            type="search"
            id="backlinkSearch"
            name="backlinkSearch"
            placeholder="Filter by title or URL"
            autocomplete="off"
            inputmode="search">
        </div>

        <div class="control-group control-group--sort">
          <label for="backlinkSort">Sort</label>
          <select id="backlinkSort" name="backlinkSort">
            <option value="az">A–Z</option>
            <option value="za">Z–A</option>
          </select>
        </div>
      </form>

      <section class="wlh-summary" aria-labelledby="summary-heading">
        <h2 id="summary-heading" class="sr-only">Selection summary</h2>

        <p class="wlh-selected-title" id="selectedPageTitle">Loading…</p>
        <p class="wlh-selected-url" id="selectedPageUrl">Loading…</p>
        <p class="wlh-count" id="backlinkCountText" aria-live="polite">Loading…</p>
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
  var pageSelector = document.getElementById("pageSelector");
  var searchInput = document.getElementById("backlinkSearch");
  var sortSelect = document.getElementById("backlinkSort");
  var backlinksList = document.getElementById("backlinksList");
  var backlinkCountText = document.getElementById("backlinkCountText");
  var selectedPageTitle = document.getElementById("selectedPageTitle");
  var selectedPageUrl = document.getElementById("selectedPageUrl");
  var resultsStatus = document.getElementById("resultsStatus");
  var emptyState = document.getElementById("emptyState");

  var backlinksData = window.WLH_BACKLINKS || {};
  var titlesData = window.WLH_TITLES || {};
  var defaultPage = window.WLH_DEFAULT_PAGE || "";

  function normaliseUrl(url) {
    if (!url) {
      return "";
    }

    var normalised = String(url).trim();

    if (normalised === "/") {
      return "/";
    }

    if (normalised.charAt(0) !== "/") {
      normalised = "/" + normalised;
    }

    if (normalised.charAt(normalised.length - 1) !== "/") {
      normalised += "/";
    }

    return normalised;
  }

  function getPageMeta(url) {
    var normalised = normaliseUrl(url);

    if (normalised && titlesData[normalised]) {
      return titlesData[normalised];
    }

    var withoutTrailingSlash = normalised !== "/" ? normalised.replace(/\/$/, "") : normalised;
    if (withoutTrailingSlash && titlesData[withoutTrailingSlash]) {
      return titlesData[withoutTrailingSlash];
    }

    return {
      title: normalised || url || "",
      url: normalised || url || "",
      resolved: false
    };
  }

  function isResolvedUrl(url) {
    var normalised = normaliseUrl(url);
    var withoutTrailingSlash = normalised !== "/" ? normalised.replace(/\/$/, "") : normalised;

    return Boolean(
      (normalised && titlesData[normalised]) ||
      (withoutTrailingSlash && titlesData[withoutTrailingSlash])
    );
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
    var normalised = normaliseUrl(targetUrl);
    var links = backlinksData[normalised] || backlinksData[targetUrl];
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
      var resolved = isResolvedUrl(url);
      var title = resolved && meta && meta.title ? meta.title : normaliseUrl(url);

      return {
        url: normaliseUrl(url),
        title: title,
        resolved: resolved,
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
      if (a.resolved !== b.resolved) {
        return a.resolved ? -1 : 1;
      }

      var comparison = a.sortText.localeCompare(b.sortText);
      return sortOrder === "za" ? comparison * -1 : comparison;
    });

    return results;
  }

  function renderSummary(targetUrl, visibleCount, totalCount) {
    var meta = getPageMeta(targetUrl);
    var resolved = isResolvedUrl(targetUrl);
    var title = resolved && meta && meta.title ? meta.title : normaliseUrl(targetUrl);

    selectedPageTitle.textContent = title || "No page selected";
    selectedPageUrl.textContent = normaliseUrl(targetUrl) || "No page selected";

    if (totalCount === 0) {
      backlinkCountText.textContent = "0 backlinks";
    } else if (visibleCount !== totalCount) {
      backlinkCountText.textContent = visibleCount + " of " + totalCount + " backlinks";
    } else if (visibleCount === 1) {
      backlinkCountText.textContent = "1 backlink";
    } else {
      backlinkCountText.textContent = visibleCount + " backlinks";
    }
  }

  function renderResults() {
    var targetUrl = getSelectedTarget();
    var allResults = getBacklinksForTarget(targetUrl);
    var visibleResults = buildResultObjects(targetUrl);

    renderSummary(targetUrl, visibleCount = visibleResults.length, totalCount = allResults.length);

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
      var unresolvedMarkup = item.resolved
        ? ""
        : '<span class="backlink-unresolved" aria-label="Unresolved page title">Unresolved</span>';

      return '' +
        '<li class="backlink-item' + (item.resolved ? '' : ' backlink-item--unresolved') + '">' +
          '<a class="backlink-link" href="' + urlHtml + '">' +
            '<span class="backlink-title-row">' +
              '<span class="backlink-title">' + titleHtml + '</span>' +
              unresolvedMarkup +
            '</span>' +
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

    var normalised = normaliseUrl(decoded);

    if (pageSelector && (backlinksData.hasOwnProperty(normalised) || backlinksData.hasOwnProperty(decoded))) {
      pageSelector.value = backlinksData.hasOwnProperty(normalised) ? normalised : decoded;
      return true;
    }

    return false;
  }

  function updateHash(targetUrl) {
    if (!targetUrl) {
      return;
    }

    var encoded = encodeURIComponent(normaliseUrl(targetUrl));
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
      var normalisedDefault = normaliseUrl(defaultPage);

      if (normalisedDefault && backlinksData.hasOwnProperty(normalisedDefault)) {
        pageSelector.value = normalisedDefault;
      } else if (defaultPage && backlinksData.hasOwnProperty(defaultPage)) {
        pageSelector.value = defaultPage;
      } else if (pageSelector.options.length) {
        pageSelector.selectedIndex = 0;
      }
    }

    renderResults();
    updateHash(getSelectedTarget());
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

  initialiseSelection();
})();
</script>

<style>
  .what-links-here-page {
    margin-top: 1.5rem;
  }

  .wlh-panel {
    margin-top: 0;
  }

  .wlh-controls {
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(0, 1.3fr) minmax(10rem, 0.7fr);
    gap: 0.875rem;
    align-items: end;
    margin-bottom: 1rem;
  }

  .control-group {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    min-width: 0;
  }

  .control-group label {
    font-weight: 600;
  }

  .control-group input,
  .control-group select {
    width: 100%;
    min-height: 2.75rem;
    padding: 0.6rem 0.75rem;
    font: inherit;
  }

  .wlh-summary {
    margin-bottom: 1rem;
  }

  .wlh-selected-title {
    margin: 0;
    font-size: 1.2rem;
    font-weight: 700;
    line-height: 1.35;
    word-break: break-word;
  }

  .wlh-selected-url {
    margin: 0.3rem 0 0;
    word-break: break-all;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  }

  .wlh-count {
    margin: 0.4rem 0 0;
  }

  .results-header {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
  }

  .results-header h2 {
    margin: 0;
  }

  .results-status {
    margin: 0;
  }

  .backlinks-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .backlink-item + .backlink-item {
    margin-top: 0.75rem;
  }

  .backlink-link {
    display: block;
    min-height: 44px;
    padding: 0.9rem 1rem;
    text-decoration: none;
  }

  .backlink-title-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
  }

  .backlink-title {
    font-weight: 600;
    word-break: break-word;
  }

  .backlink-url {
    display: block;
    margin-top: 0.35rem;
    word-break: break-all;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 0.95em;
  }

  .backlink-unresolved {
    display: inline-block;
    font-size: 0.8em;
    font-weight: 600;
    white-space: nowrap;
  }

  .empty-state {
    padding: 1rem 0;
  }

  .empty-state__title,
  .empty-state__text {
    margin: 0;
  }

  .empty-state__text {
    margin-top: 0.35rem;
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

  @media (max-width: 900px) {
    .wlh-controls {
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    }

    .control-group--selector {
      grid-column: 1 / -1;
    }
  }

  @media (max-width: 640px) {
    .what-links-here-page {
      margin-top: 1rem;
    }

    .wlh-controls {
      grid-template-columns: 1fr;
      gap: 0.75rem;
    }

    .control-group--selector,
    .control-group--search,
    .control-group--sort {
      grid-column: auto;
    }

    .backlink-link {
      padding: 0.85rem 0.9rem;
    }
  }
</style>