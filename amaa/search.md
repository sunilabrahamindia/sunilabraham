---
layout: none
title: "A. M. A. Ayrookuzhiel — Knowledge Engine"
description: "Explore and interact with the writings, research, and archival material of A. M. A. Ayrookuzhiel."
permalink: /amaa/search/
categories: [A. M. A. Ayrookuzhiel]
created: 2026-08-26
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }} | {{ site.title }}</title>
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      font-size: 16px;
      -webkit-text-size-adjust: 100%;
      text-size-adjust: 100%;
    }

    :root {
      /* Light Mode Palette */
      --bg-canvas: #f8fafc;
      --bg-surface: #ffffff;
      --bg-elevated: #f1f5f9;
      --text-primary: #1e293b;
      --text-secondary: #475569;
      --text-muted: #64748b;
      --border-subtle: #cbd5e1;
      --border-focus: #1f5fbf;
      
      --wordmark-primary: #1e293b;
      --wordmark-accent: #1f5fbf;
      --badge-bg: #e0f2fe;
      --badge-text: #0369a1;
      --badge-border: #bae6fd;
      
      --ambient-glow: radial-gradient(circle at 50% 18%, rgba(224, 242, 254, 0.6) 0%, rgba(248, 250, 252, 0) 65%);
      --card-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05), 0 1px 3px rgba(15, 23, 42, 0.04);
      --card-shadow-focus: 0 12px 32px -4px rgba(31, 95, 191, 0.12), 0 0 0 3px rgba(31, 95, 191, 0.2);
      
      --portrait-opacity: 0.92;
      --portrait-filter: grayscale(10%) contrast(102%);
      --portrait-ring: #cbd5e1;
    }

    /* Fallback for OS dark preference before JS init */
    @media (prefers-color-scheme: dark) {
      body:not(.tsap-light-mode) {
        --bg-canvas: #0f172a;
        --bg-surface: #1e293b;
        --bg-elevated: #1b283a;
        --text-primary: #f3f4f6;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --border-subtle: #374151;
        --border-focus: #38bdf8;
        
        --wordmark-primary: #f3f4f6;
        --wordmark-accent: #38bdf8;
        --badge-bg: #172554;
        --badge-text: #7dd3fc;
        --badge-border: #1e3a8a;
        
        --ambient-glow: radial-gradient(circle at 50% 18%, rgba(56, 189, 248, 0.08) 0%, rgba(15, 23, 42, 0) 60%);
        --card-shadow: 0 4px 24px -2px rgba(0, 0, 0, 0.4), 0 1px 3px rgba(0, 0, 0, 0.3);
        --card-shadow-focus: 0 12px 36px -4px rgba(0, 0, 0, 0.6), 0 0 0 3px rgba(56, 189, 248, 0.25);
        
        --portrait-opacity: 0.88;
        --portrait-filter: grayscale(15%) brightness(95%) contrast(105%);
        --portrait-ring: #374151;
      }
    }

    /* =========================================================
       Active Class Architecture Dark Mode Overrides
       ========================================================= */
    body.tsap-dark-mode {
      --bg-canvas: #0f172a !important;
      --bg-surface: #1e293b !important;
      --bg-elevated: #172334 !important;
      --text-primary: #f3f4f6 !important;
      --text-secondary: #cbd5e1 !important;
      --text-muted: #94a3b8 !important;
      --border-subtle: #374151 !important;
      --border-focus: #38bdf8 !important;
      
      --wordmark-primary: #f3f4f6 !important;
      --wordmark-accent: #38bdf8 !important;
      --badge-bg: #172554 !important;
      --badge-text: #7dd3fc !important;
      --badge-border: #1e3a8a !important;
      
      --ambient-glow: radial-gradient(circle at 50% 18%, rgba(56, 189, 248, 0.08) 0%, rgba(15, 23, 42, 0) 60%) !important;
      --card-shadow: 0 4px 24px -2px rgba(0, 0, 0, 0.4), 0 1px 3px rgba(0, 0, 0, 0.3) !important;
      --card-shadow-focus: 0 12px 36px -4px rgba(0, 0, 0, 0.6), 0 0 0 3px rgba(56, 189, 248, 0.25) !important;
      
      --portrait-opacity: 0.88 !important;
      --portrait-filter: grayscale(15%) brightness(95%) contrast(105%) !important;
      --portrait-ring: #374151 !important;
    }

    @media (prefers-reduced-motion: reduce) {
      * {
        transition: none !important;
        animation: none !important;
      }
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      color: var(--text-primary);
      background-color: var(--bg-canvas);
      background-image: var(--ambient-glow);
      background-repeat: no-repeat;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    .sans-ui {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    .skip-link {
      position: absolute;
      top: -48px;
      left: 16px;
      background: var(--text-primary);
      color: var(--bg-canvas);
      padding: 10px 18px;
      z-index: 100;
      text-decoration: none;
      font-weight: 500;
      border-radius: 6px;
      transition: top 0.2s ease;
    }

    .skip-link:focus {
      top: 16px;
    }

    .page-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      max-width: 760px;
      margin: 0 auto;
      padding: 88px 24px 48px;
      width: 100%;
    }

    /* Header Composition */
    .page-header {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-bottom: 40px;
    }

    .portrait-frame {
      position: relative;
      width: 68px;
      height: 68px;
      margin-bottom: 20px;
      border-radius: 50%;
      padding: 3px;
      background: linear-gradient(135deg, var(--portrait-ring), transparent 75%);
    }

    .header-portrait {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      display: block;
      opacity: var(--portrait-opacity);
      filter: var(--portrait-filter);
      background-color: var(--bg-elevated);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    .archive-title {
      font-size: 2.5rem;
      font-weight: 600;
      letter-spacing: -0.025em;
      line-height: 1.15;
      margin-bottom: 12px;
      color: var(--wordmark-primary);
    }

    .title-initials {
      color: var(--wordmark-accent);
      font-style: normal;
      font-weight: 700;
    }

    .title-surname {
      color: var(--wordmark-primary);
    }

    .archive-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 14px;
      border-radius: 999px;
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
      color: var(--badge-text);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }

    .badge-prefix {
      opacity: 0.85;
      font-weight: 500;
    }

    .badge-dot {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background-color: var(--wordmark-accent);
    }

    /* Search Input */
    .search-section {
      margin-bottom: 32px;
    }

    .search-form {
      position: relative;
    }

    .search-input-wrapper {
      display: flex;
      align-items: stretch;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 4px;
      box-shadow: var(--card-shadow);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .search-input-wrapper:focus-within {
      border-color: var(--border-focus);
      box-shadow: var(--card-shadow-focus);
    }

    .search-input {
      flex: 1;
      border: none;
      padding: 14px 18px;
      font-size: 1.02rem;
      background: transparent;
      color: var(--text-primary);
      outline: none;
      min-width: 0;
      font-family: inherit;
    }

    .search-input::placeholder {
      color: var(--text-muted);
      font-size: 0.95rem;
      font-weight: 400;
    }

    .search-button {
      background: var(--wordmark-accent);
      color: #ffffff;
      border: none;
      padding: 0 24px;
      margin: 2px;
      font-size: 0.92rem;
      font-weight: 600;
      letter-spacing: 0.02em;
      border-radius: 10px;
      cursor: pointer;
      transition: opacity 0.15s ease, background-color 0.15s ease;
      white-space: nowrap;
    }

    body.tsap-dark-mode .search-button {
      background: #1e5fbf !important;
      color: #ffffff !important;
    }

    body.tsap-dark-mode .search-button:hover {
      background: #38bdf8 !important;
      color: #0f172a !important;
    }

    .search-button:hover {
      opacity: 0.9;
    }

    .search-button:focus {
      outline: 2px solid var(--wordmark-accent);
      outline-offset: 2px;
    }

    .search-button:disabled {
      opacity: 0.45;
      cursor: not-allowed;
    }

    /* States & Results Presentation */
    .loading-state {
      display: none;
      text-align: center;
      padding: 48px 20px;
      color: var(--text-muted);
      font-size: 0.95rem;
      font-style: italic;
    }

    .loading-state.visible {
      display: block;
    }

    .error-state {
      display: none;
      text-align: center;
      padding: 28px 24px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      color: var(--text-secondary);
      font-size: 0.95rem;
      box-shadow: var(--card-shadow);
    }

    .error-state.visible {
      display: block;
    }

    .results-section {
      display: none;
      margin-top: 40px;
      padding: 32px 28px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      box-shadow: var(--card-shadow);
    }

    .results-section.visible {
      display: block;
    }

    .result-question {
      font-size: 0.92rem;
      color: var(--text-muted);
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .result-question-label {
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--wordmark-accent);
    }

    .result-question-text {
      color: var(--text-secondary);
      font-style: italic;
    }

    .result-answer {
      margin-bottom: 28px;
    }

    .result-answer-content {
      font-size: 1.05rem;
      line-height: 1.75;
      color: var(--text-primary);
    }

    .result-answer-content p {
      margin-bottom: 1.15em;
    }

    .result-answer-content p:last-child {
      margin-bottom: 0;
    }

    .result-sources {
      margin-top: 32px;
      padding-top: 24px;
      border-top: 1px dashed var(--border-subtle);
    }

    .result-sources-label {
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 14px;
    }

    .sources-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .source-item {
      margin: 0;
    }

    .source-link {
      font-size: 0.9rem;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 10px 14px;
      border-radius: 8px;
      display: block;
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease;
    }

    .source-link:hover {
      background-color: var(--bg-surface);
      color: var(--wordmark-accent);
      border-color: var(--wordmark-accent);
    }

    .source-link:focus {
      outline: 2px solid var(--border-focus);
      outline-offset: 2px;
    }

    .new-search-container {
      margin-top: 28px;
      text-align: right;
    }

    .new-search-link {
      display: inline-flex;
      align-items: center;
      font-size: 0.86rem;
      font-weight: 500;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 8px 16px;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      background: var(--bg-canvas);
      transition: all 0.15s ease;
    }

    .new-search-link:hover {
      border-color: var(--border-focus);
      color: var(--wordmark-accent);
    }

    .new-search-link:focus {
      outline: 2px solid var(--border-focus);
      outline-offset: 2px;
    }

    /* Footer */
    .page-footer {
      margin-top: auto;
      padding-top: 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }

    .footer-divider {
      width: 40px;
      height: 1px;
      background: var(--border-subtle);
      margin-bottom: 8px;
    }

    .footer-link {
      font-size: 0.88rem;
      color: var(--text-muted);
      text-decoration: none;
      padding: 2px 8px;
      border-radius: 4px;
      transition: color 0.15s ease;
      line-height: 1.35;
    }

    .footer-link:hover {
      color: var(--text-primary);
    }

    .footer-link:focus {
      outline: 2px solid var(--border-focus);
      outline-offset: 2px;
    }

    .footer-link.primary-nav {
      color: var(--text-secondary);
      font-weight: 500;
    }

    .footer-link.primary-nav:hover {
      color: var(--wordmark-accent);
    }

    @media (max-width: 640px) {
      .page-container {
        padding: 48px 16px 36px;
      }

      .portrait-frame {
        width: 56px;
        height: 56px;
        margin-bottom: 16px;
      }

      .archive-title {
        font-size: 1.95rem;
      }

      .archive-badge {
        font-size: 0.72rem;
        padding: 4px 10px;
        letter-spacing: 0.04em;
      }

      .search-input-wrapper {
        flex-direction: column;
        padding: 6px;
        border-radius: 12px;
      }

      .search-input {
        padding: 12px 14px;
        font-size: 0.95rem;
      }

      .search-input::placeholder {
        font-size: 0.86rem;
      }

      .search-button {
        padding: 12px;
        width: 100%;
        margin: 4px 0 0 0;
      }

      .results-section {
        padding: 24px 18px;
      }
    }

    :focus-visible {
      outline: 2px solid var(--border-focus);
      outline-offset: 2px;
    }
  </style>
</head>
<body>
  <script>
    // Sync active theme class from localStorage if present
    (function() {
      try {
        const theme = localStorage.getItem('tsap-theme');
        if (theme === 'dark') {
          document.body.classList.add('tsap-dark-mode');
        } else if (theme === 'light') {
          document.body.classList.add('tsap-light-mode');
        }
      } catch (e) {}
    })();
  </script>

  <a href="#search-input" class="skip-link sans-ui">Skip to search</a>

  <main class="page-container" role="main">
    <header class="page-header">
      <div class="portrait-frame">
        <img 
          src="/amaa/images/A.%20M.%20A.%20Ayrookuzhiel%20photo%20low%20resolution.png" 
          alt="" 
          class="header-portrait" 
          aria-hidden="true"
        >
      </div>
      <h1 class="archive-title" aria-label="A. M. A. Ayrookuzhiel">
        <span class="title-initials">A. M. A.</span> <span class="title-surname">Ayrookuzhiel</span>
      </h1>
      <div class="archive-badge sans-ui">
        <span class="badge-prefix">Preparatory version:</span>
        <span>Knowledge Engine</span>
        <span class="badge-dot" aria-hidden="true"></span>
      </div>
    </header>

    <section class="search-section" aria-label="Search">
      <form class="search-form" id="search-form" role="search">
        <label for="search-input" style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;">Search the archive</label>
        <div class="search-input-wrapper">
          <input
            type="text"
            id="search-input"
            class="search-input"
            placeholder="🔍 Ask about A. M. A. Ayrookuzhiel's work..."
            autocomplete="off"
            required
          >
          <button type="submit" class="search-button sans-ui" id="search-button">
            Search
          </button>
        </div>
      </form>
    </section>

    <div class="loading-state" id="loading-state" aria-live="polite" aria-busy="true">
      Consulting the archive...
    </div>

    <div class="error-state sans-ui" id="error-state" aria-live="assertive">
      Unable to search the archive right now. Please try again in a moment.
    </div>

    <section class="results-section" id="results-section" aria-label="Search results" aria-live="polite">
      <div class="result-question">
        <span class="result-question-label sans-ui">Query</span>
        <span class="result-question-text" id="result-question-text"></span>
      </div>

      <div class="result-answer">
        <div class="result-answer-content" id="result-answer-content"></div>
      </div>

      <div class="result-sources" id="result-sources" style="display:none;">
        <div class="result-sources-label sans-ui">Sources & References</div>
        <ul class="sources-list sans-ui" id="sources-list"></ul>
      </div>

      <div class="new-search-container">
        <a href="#" class="new-search-link sans-ui" id="new-search-link">New Search</a>
      </div>
    </section>

    <footer class="page-footer sans-ui">
      <div class="footer-divider" aria-hidden="true"></div>
      <a href="/" class="footer-link primary-nav">The Sunil Abraham Project</a>
      <a href="/amaa/" class="footer-link">A. M. A. Ayrookuzhiel</a>
    </footer>
  </main>

  <script>
    (function() {
      const API_BASE = 'https://c530c997-1f95-4b27-9ff5-b5e4fd54dd9e.search.ai.cloudflare.com';
      const API_URL = API_BASE + '/chat/completions';

      const searchForm = document.getElementById('search-form');
      const searchInput = document.getElementById('search-input');
      const searchButton = document.getElementById('search-button');
      const loadingState = document.getElementById('loading-state');
      const errorState = document.getElementById('error-state');
      const resultsSection = document.getElementById('results-section');
      const resultQuestionText = document.getElementById('result-question-text');
      const resultAnswerContent = document.getElementById('result-answer-content');
      const resultSources = document.getElementById('result-sources');
      const sourcesList = document.getElementById('sources-list');
      const newSearchLink = document.getElementById('new-search-link');

      function sanitizeUrl(url) {
        if (!url) return '#';
        const trimmed = url.trim();
        if (/^(https?:|\/)/i.test(trimmed)) {
          return encodeURI(trimmed);
        }
        return '#';
      }

      function renderSafeAnswer(rawText) {
        resultAnswerContent.innerHTML = '';
        if (!rawText) return;

        const paragraphs = rawText.split(/\n\s*\n/);
        paragraphs.forEach(pText => {
          const trimmed = pText.trim();
          if (trimmed) {
            const p = document.createElement('p');
            const lines = trimmed.split('\n');
            lines.forEach((line, index) => {
              if (index > 0) {
                p.appendChild(document.createElement('br'));
              }
              p.appendChild(document.createTextNode(line));
            });
            resultAnswerContent.appendChild(p);
          }
        });
      }

      function showLoading() {
        loadingState.classList.add('visible');
        errorState.classList.remove('visible');
        resultsSection.classList.remove('visible');
        searchButton.disabled = true;
      }

      function showError() {
        loadingState.classList.remove('visible');
        errorState.classList.add('visible');
        resultsSection.classList.remove('visible');
        searchButton.disabled = false;
        searchInput.focus();
      }

      function showResults(question, answer, sources) {
        loadingState.classList.remove('visible');
        errorState.classList.remove('visible');
        searchButton.disabled = false;

        resultQuestionText.textContent = question;
        renderSafeAnswer(answer);

        if (sources && sources.length > 0) {
          sourcesList.innerHTML = '';
          sources.forEach(source => {
            const li = document.createElement('li');
            li.className = 'source-item';
            const a = document.createElement('a');
            a.className = 'source-link';
            a.href = sanitizeUrl(source.url);
            a.textContent = source.title || source.url;
            li.appendChild(a);
            sourcesList.appendChild(li);
          });
          resultSources.style.display = 'block';
        } else {
          resultSources.style.display = 'none';
        }

        resultsSection.classList.add('visible');
        searchInput.blur();
      }

      async function performSearch(query) {
        if (!query.trim()) return;

        showLoading();

        try {
          const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              messages: [
                {
                  role: 'system',
                  content: 'You are a research archive assistant for A. M. A. Ayrookuzhiel. Provide accurate answers based on the indexed archive material. Cite sources where available. Keep responses concise and scholarly.'
                },
                {
                  role: 'user',
                  content: query
                }
              ],
              temperature: 0.3,
              max_tokens: 1000
            })
          });

          if (!response.ok) {
            throw new Error('API request failed');
          }

          const data = await response.json();

          if (data.choices && data.choices.length > 0) {
            const answer = data.choices[0].message.content;
            const sources = data.search_info?.search_results || [];
            showResults(query, answer, sources);
          } else {
            throw new Error('No answer returned');
          }
        } catch (error) {
          console.error('Search error:', error);
          showError();
        }
      }

      searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
          performSearch(query);
        }
      });

      newSearchLink.addEventListener('click', function(e) {
        e.preventDefault();
        searchInput.value = '';
        resultsSection.classList.remove('visible');
        searchInput.focus();
      });

      searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
          searchInput.value = '';
          resultsSection.classList.remove('visible');
        }
      });
    })();
  </script>
</body>
</html>
