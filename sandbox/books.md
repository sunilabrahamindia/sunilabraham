---
layout: default
title: "Books"
description: "Create printable collections and reading packets from pages across The Sunil Abraham Project."
categories: [TSAP Tools]
permalink: /sandbox/books/
---

<section class="books-tool" aria-labelledby="books-title">
  <header class="books-tool__header">
    <p class="books-tool__eyebrow">TSAP Tools</p>
    <h1 id="books-title">Books</h1>
    <p class="books-tool__lede">
      Create temporary printable collections from pages across The Sunil Abraham Project. This early prototype keeps your selected list in your browser only and is designed to stay simple, calm, and easy to extend.
    </p>
  </header>

  <div class="books-tool__layout">
    <section class="books-panel books-panel--search" aria-labelledby="search-panel-title">
      <h2 id="search-panel-title">Find pages</h2>
      <p class="books-panel__intro">
        Search a small local index, review suggestions, and add pages to your current book.
      </p>

      <form class="books-search" id="books-search-form" autocomplete="off" role="search">
        <label for="books-search-input">Search TSAP pages</label>
        <div class="books-search__controls">
          <input
            id="books-search-input"
            name="books-search"
            type="search"
            inputmode="search"
            placeholder="Type a title or topic"
            aria-describedby="books-search-help books-search-status"
            aria-autocomplete="list"
            aria-expanded="false"
            aria-controls="books-suggestions"
            aria-activedescendant=""
          />
          <button type="submit" class="button button--primary">Add selected page</button>
        </div>
        <p id="books-search-help" class="books-search__help">
          Use the arrow keys to move through suggestions, then press Enter to select.
        </p>
        <p id="books-search-status" class="books-search__status" aria-live="polite"></p>

        <div class="books-suggestions" id="books-suggestions-wrapper">
          <ul
            id="books-suggestions"
            class="books-suggestions__list"
            role="listbox"
            aria-label="Suggested TSAP pages"
          ></ul>
        </div>
      </form>
    </section>

    <section class="books-panel books-panel--book" aria-labelledby="book-panel-title">
      <div class="books-panel__heading-row">
        <div>
          <h2 id="book-panel-title">My Book</h2>
          <p class="books-panel__intro">
            Reorder, remove, clear, or print your current selection.
          </p>
        </div>
        <p class="books-count" id="books-count" aria-live="polite">0 pages</p>
      </div>

      <div class="books-actions" aria-label="Book actions">
        <button type="button" class="button button--secondary" id="books-clear-button">Clear book</button>
        <button type="button" class="button button--primary" id="books-print-button">Print book</button>
      </div>

      <div class="books-empty" id="books-empty" hidden>
        <p>Your book is empty. Search for a page above and add it to begin a printable reading packet.</p>
      </div>

      <ol class="books-list" id="books-list"></ol>
      <div id="book-content"></div>
    </section>
  </div>
</section>

<style>
  /*
    TSAP Books tool, version 1.
    Architecture notes:
    - This page is fully self-contained for static-site compatibility.
    - The only persisted data is a small localStorage array of { title, url } objects.
    - Search uses a local mock index so the interface can later be replaced by a richer site index.
  */

  :root {
    --books-bg: #faf9f7;
    --books-surface: #ffffff;
    --books-surface-muted: #f3f1ec;
    --books-border: #d8d2c8;
    --books-border-strong: #b8afa2;
    --books-text: #1f1c18;
    --books-text-soft: #5e574d;
    --books-accent: #244a65;
    --books-accent-soft: #dce6ee;
    --books-danger: #7a2f2f;
    --books-shadow: 0 1px 2px rgba(20, 18, 15, 0.06);
    --books-radius: 0.5rem;
    --books-space-1: 0.25rem;
    --books-space-2: 0.5rem;
    --books-space-3: 0.75rem;
    --books-space-4: 1rem;
    --books-space-5: 1.25rem;
    --books-space-6: 1.5rem;
    --books-space-8: 2rem;
    --books-space-10: 2.5rem;
    --books-max-width: 72rem;
  }

  .books-tool {
    max-width: var(--books-max-width);
    margin: 0 auto;
    padding: var(--books-space-8) var(--books-space-4) var(--books-space-10);
    color: var(--books-text);
  }

  .books-tool__header {
    margin-bottom: var(--books-space-8);
    max-width: 46rem;
  }

  .books-tool__eyebrow {
    margin: 0 0 var(--books-space-2);
    color: var(--books-text-soft);
    font-size: 0.875rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .books-tool h1,
  .books-tool h2 {
    line-height: 1.2;
  }

  .books-tool h1 {
    margin: 0;
    font-size: clamp(2rem, 1.8rem + 1vw, 2.6rem);
  }

  .books-tool__lede,
  .books-panel__intro,
  .books-empty p,
  .books-item__meta,
  .books-search__help,
  .books-search__status {
    color: var(--books-text-soft);
  }

  .books-tool__lede {
    margin: var(--books-space-4) 0 0;
    font-size: 1.0625rem;
    line-height: 1.7;
  }

  .books-tool__layout {
    display: grid;
    gap: var(--books-space-6);
    grid-template-columns: repeat(2, minmax(0, 1fr));
    align-items: start;
  }

  .books-panel {
    background: var(--books-surface);
    border: 1px solid var(--books-border);
    border-radius: var(--books-radius);
    box-shadow: var(--books-shadow);
    padding: var(--books-space-6);
  }

  .books-panel__heading-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: var(--books-space-4);
    margin-bottom: var(--books-space-5);
  }

  .books-panel h2 {
    margin: 0;
    font-size: 1.375rem;
  }

  .books-panel__intro {
    margin: var(--books-space-2) 0 0;
    line-height: 1.6;
  }

  .books-count {
    margin: 0;
    padding: var(--books-space-2) var(--books-space-3);
    border: 1px solid var(--books-border);
    border-radius: 999px;
    background: var(--books-surface-muted);
    font-size: 0.9375rem;
    white-space: nowrap;
  }

  .books-search {
    position: relative;
  }

  .books-search label {
    display: inline-block;
    margin-bottom: var(--books-space-2);
    font-weight: 600;
  }

  .books-search__controls {
    display: grid;
    gap: var(--books-space-3);
    grid-template-columns: minmax(0, 1fr) auto;
    align-items: start;
  }

  .books-search input {
    width: 100%;
    min-height: 2.875rem;
    padding: 0 var(--books-space-4);
    border: 1px solid var(--books-border-strong);
    border-radius: var(--books-radius);
    background: #fff;
    color: var(--books-text);
  }

  .books-search input::placeholder {
    color: #7b7469;
  }

  .books-search__help,
  .books-search__status {
    margin: var(--books-space-2) 0 0;
    font-size: 0.9375rem;
    line-height: 1.5;
  }

  .books-suggestions {
    position: relative;
  }

  .books-suggestions__list {
    display: none;
    position: absolute;
    top: var(--books-space-2);
    left: 0;
    right: 0;
    z-index: 10;
    margin: 0;
    padding: var(--books-space-2);
    list-style: none;
    border: 1px solid var(--books-border-strong);
    border-radius: var(--books-radius);
    background: var(--books-surface);
    box-shadow: 0 10px 24px rgba(20, 18, 15, 0.08);
  }

  .books-suggestions__list[data-open="true"] {
    display: block;
  }

  .books-suggestion {
    width: 100%;
    padding: var(--books-space-3);
    border: 0;
    border-radius: calc(var(--books-radius) - 0.125rem);
    background: transparent;
    text-align: left;
  }

  .books-suggestion:hover,
  .books-suggestion:focus-visible,
  .books-suggestion[aria-selected="true"] {
    background: var(--books-accent-soft);
  }

  .books-suggestion__title {
    display: block;
    font-weight: 600;
  }

  .books-suggestion__url {
    display: block;
    margin-top: var(--books-space-1);
    color: var(--books-text-soft);
    font-size: 0.9rem;
  }

  .books-actions {
    display: flex;
    flex-wrap: wrap;
    gap: var(--books-space-3);
    margin-bottom: var(--books-space-5);
  }

  .button {
    min-height: 2.875rem;
    padding: 0.7rem 1rem;
    border: 1px solid var(--books-border-strong);
    border-radius: var(--books-radius);
    background: var(--books-surface);
    color: var(--books-text);
    font-weight: 600;
  }

  .button:hover,
  .button:focus-visible {
    border-color: var(--books-accent);
  }

  .button--primary {
    background: var(--books-accent);
    border-color: var(--books-accent);
    color: #ffffff;
  }

  .button--primary:hover,
  .button--primary:focus-visible {
    background: #1c3b52;
    border-color: #1c3b52;
  }

  .button--secondary {
    background: var(--books-surface-muted);
  }

  .books-empty {
    padding: var(--books-space-5);
    border: 1px dashed var(--books-border-strong);
    border-radius: var(--books-radius);
    background: var(--books-surface-muted);
  }

  .books-list {
    margin: 0;
    padding-left: 1.5rem;
  }

  .books-item {
    margin-bottom: var(--books-space-4);
    padding: var(--books-space-4);
    border: 1px solid var(--books-border);
    border-radius: var(--books-radius);
    background: #fff;
  }

  .books-item__row {
    display: flex;
    justify-content: space-between;
    gap: var(--books-space-4);
    align-items: start;
  }

  .books-item__title {
    margin: 0;
    font-size: 1.05rem;
    line-height: 1.5;
  }

  .books-item__title a {
    color: var(--books-text);
    text-decoration-thickness: 0.08em;
    text-underline-offset: 0.16em;
  }

  .books-item__meta {
    margin: var(--books-space-1) 0 0;
    font-size: 0.9375rem;
    word-break: break-word;
  }

  .books-item__actions {
    display: flex;
    flex-wrap: wrap;
    gap: var(--books-space-2);
    justify-content: flex-end;
  }

  .books-item__button {
    min-width: 2.75rem;
    min-height: 2.75rem;
    padding: 0.5rem 0.75rem;
    border: 1px solid var(--books-border-strong);
    border-radius: 0.4rem;
    background: var(--books-surface-muted);
    color: var(--books-text);
    font-size: 0.95rem;
  }

  .books-item__button:hover,
  .books-item__button:focus-visible {
    border-color: var(--books-accent);
    background: #edf3f7;
  }

  .books-item__button--danger:hover,
  .books-item__button--danger:focus-visible {
    border-color: var(--books-danger);
    color: var(--books-danger);
    background: #faf0f0;
  }

  @media (max-width: 56rem) {
    .books-tool__layout {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 40rem) {
    .books-tool {
      padding-inline: var(--books-space-3);
    }

    .books-panel {
      padding: var(--books-space-4);
    }

    .books-search__controls,
    .books-item__row {
      grid-template-columns: 1fr;
      display: grid;
    }

    .books-panel__heading-row {
      flex-direction: column;
      align-items: stretch;
    }

    .books-item__actions {
      justify-content: flex-start;
    }

    .books-count {
      align-self: flex-start;
    }
  }

  @media print {

    .books-tool__header,
    .books-panel--search,
    .books-panel__heading-row,
    .books-actions,
    .books-list,
    .books-empty,
    .books-item__actions {
      display: none !important;
    }

    .books-tool,
    .books-panel,
    .books-item,
    #book-content {
      border: 0 !important;
      box-shadow: none !important;
      padding: 0 !important;
      background: transparent !important;
    }

    .books-tool__layout {
      display: block !important;
    }

    #book-content {
      display: block !important;
    }

    .book-article {
      margin-bottom: 3rem;
      break-inside: avoid;
      page-break-after: always;
    }

    .book-article:last-child {
      page-break-after: auto;
    }
  }

</style>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    /*
      Version 1 data model:
      - pages: local mock index used only for client-side suggestions.
      - myBook: persistent user list stored in localStorage with minimal metadata.
      - selectedSuggestionIndex: tracks keyboard navigation in the suggestions list.
    */

    const STORAGE_KEY = "tsap-books-v1";

const pages = [
  {% assign all_pages = site.pages | concat: site.documents %}

  {% assign filtered_pages = all_pages | sort: "title" %}

  {% for p in filtered_pages %}
    {% if p.title and p.url and p.title != "Redirect" %}

    {
      title: {{ p.title | jsonify }},
      url: {{ p.url | jsonify }}
    }{% unless forloop.last %},{% endunless %}

    {% endif %}
  {% endfor %}
];

    const searchForm = document.getElementById("books-search-form");
    const searchInput = document.getElementById("books-search-input");
    const suggestionsList = document.getElementById("books-suggestions");
    const suggestionsWrapper = document.getElementById("books-suggestions-wrapper");
    const searchStatus = document.getElementById("books-search-status");
    const booksList = document.getElementById("books-list");
    const booksEmpty = document.getElementById("books-empty");
    const booksCount = document.getElementById("books-count");
    const clearButton = document.getElementById("books-clear-button");
    const printButton = document.getElementById("books-print-button");

    let myBook = loadBook();
    let filteredPages = [];
    let selectedSuggestionIndex = -1;
    let selectedPage = null;

    renderBook();
    updateSuggestions([]);

    searchInput.addEventListener("input", function () {
      const query = searchInput.value.trim().toLowerCase();

      selectedPage = null;
      selectedSuggestionIndex = -1;

      if (!query) {
        updateSuggestions([]);
        setStatus("Start typing to search the local page index.");
        return;
      }

      filteredPages = pages
        .filter(function (page) {
          return page.title.toLowerCase().includes(query) || page.url.toLowerCase().includes(query);
        })
        .slice(0, 8);

      if (filteredPages.length > 0) {
        updateSuggestions(filteredPages);
        setStatus(filteredPages.length + " suggestion" + (filteredPages.length === 1 ? "" : "s") + " available.");
      } else {
        updateSuggestions([]);
        setStatus("No matching pages found in the current local index.");
      }
    });

    searchInput.addEventListener("keydown", function (event) {
      if (!filteredPages.length) {
        return;
      }

      if (event.key === "ArrowDown") {
        event.preventDefault();
        selectedSuggestionIndex = Math.min(selectedSuggestionIndex + 1, filteredPages.length - 1);
        updateActiveSuggestion();
      }

      if (event.key === "ArrowUp") {
        event.preventDefault();
        selectedSuggestionIndex = Math.max(selectedSuggestionIndex - 1, 0);
        updateActiveSuggestion();
      }

      if (event.key === "Escape") {
        updateSuggestions([]);
        selectedSuggestionIndex = -1;
        searchInput.setAttribute("aria-expanded", "false");
        searchInput.setAttribute("aria-activedescendant", "");
        setStatus("Suggestions closed.");
      }

      if (event.key === "Enter" && selectedSuggestionIndex >= 0) {
        event.preventDefault();
        choosePage(filteredPages[selectedSuggestionIndex]);
      }
    });

    searchForm.addEventListener("submit", function (event) {
      event.preventDefault();

      if (selectedPage) {
        addPageToBook(selectedPage);
        return;
      }

      if (filteredPages.length === 1) {
        choosePage(filteredPages);
        addPageToBook(filteredPages);
        return;
      }

      setStatus("Select a page from the suggestions before adding it.");
    });

    suggestionsList.addEventListener("click", function (event) {
      const button = event.target.closest("button[data-index]");
      if (!button) {
        return;
      }

      const index = Number(button.getAttribute("data-index"));
      choosePage(filteredPages[index]);
      addPageToBook(filteredPages[index]);
    });

    document.addEventListener("click", function (event) {
      if (!searchForm.contains(event.target)) {
        updateSuggestions([]);
      }
    });

    clearButton.addEventListener("click", function () {
      if (!myBook.length) {
        setStatus("Your book is already empty.");
        return;
      }

      const confirmed = window.confirm("Clear the current book list?");
      if (!confirmed) {
        return;
      }

      myBook = [];
      saveBook();
      renderBook();
      setStatus("Book cleared.");
    });

printButton.addEventListener("click", async function () {

  const container = document.getElementById("book-content");

  container.innerHTML = "";

  for (const item of myBook) {

    try {

      const response = await fetch(item.url);
      const html = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      const content = doc.querySelector("#maincontent");
      if (content) {

        const article = document.createElement("article");

        article.className = "book-article";
article.innerHTML = content.innerHTML;
        container.appendChild(article);

      }

    } catch (error) {

      console.error("Failed to load:", item.url);

    }

  }

  window.print();

});

    booksList.addEventListener("click", function (event) {
      const actionButton = event.target.closest("button[data-action]");
      if (!actionButton) {
        return;
      }

      const index = Number(actionButton.getAttribute("data-index"));
      const action = actionButton.getAttribute("data-action");

      if (action === "remove") {
        const removed = myBook[index];
        myBook.splice(index, 1);
        saveBook();
        renderBook();
        setStatus("Removed \"" + removed.title + "\" from your book.");
      }

      if (action === "move-up" && index > 0) {
        swapItems(index, index - 1);
        setStatus("Moved item up.");
      }

      if (action === "move-down" && index < myBook.length - 1) {
        swapItems(index, index + 1);
        setStatus("Moved item down.");
      }
    });

    function loadBook() {
      try {
        const stored = window.localStorage.getItem(STORAGE_KEY);
        if (!stored) {
          return [];
        }

        const parsed = JSON.parse(stored);
        if (!Array.isArray(parsed)) {
          return [];
        }

        return parsed.filter(function (item) {
          return item && typeof item.title === "string" && typeof item.url === "string";
        });
      } catch (error) {
        return [];
      }
    }

    function saveBook() {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(myBook));
    }

    function choosePage(page) {
      if (!page) {
        return;
      }

      selectedPage = page;
      searchInput.value = page.title;
      updateSuggestions([]);
      setStatus("Selected \"" + page.title + "\".");
    }

    function addPageToBook(page) {
      const exists = myBook.some(function (item) {
        return item.url === page.url;
      });

      if (exists) {
        setStatus("That page is already in your book.");
        return;
      }

      myBook.push({ title: page.title, url: page.url });
      saveBook();
      renderBook();
      setStatus("Added \"" + page.title + "\" to your book.");
      searchInput.value = "";
      selectedPage = null;
      filteredPages = [];
      updateSuggestions([]);
      searchInput.focus();
    }

    function swapItems(fromIndex, toIndex) {
      const temp = myBook[fromIndex];
      myBook[fromIndex] = myBook[toIndex];
      myBook[toIndex] = temp;
      saveBook();
      renderBook();
    }

    function renderBook() {
      booksList.innerHTML = "";
      booksCount.textContent = myBook.length + " page" + (myBook.length === 1 ? "" : "s");
      booksEmpty.hidden = myBook.length !== 0;
      clearButton.disabled = myBook.length === 0;
      printButton.disabled = myBook.length === 0;

      if (!myBook.length) {
        return;
      }

      myBook.forEach(function (item, index) {
        const li = document.createElement("li");
        li.className = "books-item";

        li.innerHTML = [
          '<div class="books-item__row">',
          '  <div class="books-item__content">',
          '    <h3 class="books-item__title"><a href="' + escapeHtml(item.url) + '">' + escapeHtml(item.title) + '</a></h3>',
          '    <p class="books-item__meta">' + escapeHtml(item.url) + '</p>',
          '  </div>',
          '  <div class="books-item__actions" aria-label="Actions for ' + escapeHtml(item.title) + '">',
          '    <button type="button" class="books-item__button" data-action="move-up" data-index="' + index + '"' + (index === 0 ? ' disabled aria-disabled="true"' : '') + '>Up</button>',
          '    <button type="button" class="books-item__button" data-action="move-down" data-index="' + index + '"' + (index === myBook.length - 1 ? ' disabled aria-disabled="true"' : '') + '>Down</button>',
          '    <button type="button" class="books-item__button books-item__button--danger" data-action="remove" data-index="' + index + '">Remove</button>',
          '  </div>',
          '</div>'
        ].join("");

        booksList.appendChild(li);
      });
    }

    function updateSuggestions(results) {
      suggestionsList.innerHTML = "";
      filteredPages = results;

      if (!results.length) {
        suggestionsList.dataset.open = "false";
        searchInput.setAttribute("aria-expanded", "false");
        searchInput.setAttribute("aria-activedescendant", "");
        return;
      }

      results.forEach(function (page, index) {
        const li = document.createElement("li");
        const suggestionId = "books-suggestion-" + index;

        li.innerHTML = [
          '<button type="button" id="' + suggestionId + '" class="books-suggestion" role="option" aria-selected="false" data-index="' + index + '">',
          '  <span class="books-suggestion__title">' + escapeHtml(page.title) + '</span>',
          '  <span class="books-suggestion__url">' + escapeHtml(page.url) + '</span>',
          '</button>'
        ].join("");

        suggestionsList.appendChild(li);
      });

      suggestionsList.dataset.open = "true";
      searchInput.setAttribute("aria-expanded", "true");
    }

    function updateActiveSuggestion() {
      const suggestionButtons = suggestionsList.querySelectorAll(".books-suggestion");

      suggestionButtons.forEach(function (button, index) {
        const isSelected = index === selectedSuggestionIndex;
        button.setAttribute("aria-selected", isSelected ? "true" : "false");

        if (isSelected) {
          searchInput.setAttribute("aria-activedescendant", button.id);
          selectedPage = filteredPages[index];
          button.scrollIntoView({ block: "nearest" });
        }
      });
    }

    function setStatus(message) {
      searchStatus.textContent = message;
    }

    function escapeHtml(value) {
      return value
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/\"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }
  });
</script>
