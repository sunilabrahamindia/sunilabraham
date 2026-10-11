---
layout: default
title: "Recent Changes"
description: "Explore recent edits, new pages and repository activity across The Sunil Abraham Project."
permalink: /recent-changes/
categories: [Project pages]
page_id: TSAP-0787
created: 2026-03-25
---

**Recent Changes** brings together repository edits and newly created pages from The Sunil Abraham Project (TSAP). The feed is generated from the repository history, so change types are based on changed-file status rather than commit-message guesses.

<div class="rc-wrap" id="rc-root">
  <div class="rc-tabs" role="tablist" aria-label="Recent changes views">
    <button type="button" class="rc-tab is-active" role="tab" id="rc-tab-edits" aria-controls="rc-panel" aria-selected="true" tabindex="0" data-tab="edits">Edits</button>
    <button type="button" class="rc-tab" role="tab" id="rc-tab-pages" aria-controls="rc-panel" aria-selected="false" tabindex="-1" data-tab="pages">New pages</button>
  </div>

  <div id="rc-panel" role="tabpanel" aria-labelledby="rc-tab-edits" tabindex="0">
    <div class="rc-stats" id="rc-stats" aria-live="polite" aria-atomic="true"></div>

    <div class="rc-toolbar">
      <div class="rc-field rc-field-wide">
        <label for="rc-search">Search</label>
        <input type="search" id="rc-search" placeholder="Search messages, files, authors, titles or categories" autocomplete="off">
      </div>
      <div class="rc-field">
        <label for="rc-days">Time period</label>
        <select id="rc-days">
          <option value="1">Last 24 hours</option>
          <option value="7" selected>Last 7 days</option>
          <option value="30">Last 30 days</option>
          <option value="90">Last 90 days</option>
          <option value="365">Last year</option>
          <option value="all">All available history</option>
        </select>
      </div>
      <div class="rc-field">
        <label for="rc-limit">Show per batch</label>
        <select id="rc-limit">
          <option value="20">20</option>
          <option value="50" selected>50</option>
          <option value="100">100</option>
          <option value="200">200</option>
        </select>
      </div>
      <div class="rc-field" id="rc-f-author">
        <label for="rc-author">Author</label>
        <select id="rc-author"><option value="">All authors</option></select>
      </div>
      <div class="rc-field" id="rc-f-type">
        <label for="rc-type">Change type</label>
        <select id="rc-type">
          <option value="">All types</option>
          <option value="created">Created</option>
          <option value="updated">Updated</option>
          <option value="removed">Removed</option>
          <option value="automated">Automated</option>
        </select>
      </div>
      <div class="rc-field" id="rc-f-cat" hidden>
        <label for="rc-cat">Category</label>
        <select id="rc-cat"><option value="">All categories</option></select>
      </div>
      <div class="rc-field" id="rc-f-sort" hidden>
        <label for="rc-sort">Sort pages</label>
        <select id="rc-sort">
          <option value="new">Newest first</option>
          <option value="old">Oldest first</option>
          <option value="az">Title A to Z</option>
        </select>
      </div>
    </div>

    <div class="rc-options">
      <label class="rc-check" id="rc-o-bot"><input type="checkbox" id="rc-hidebot"> Hide automated commits</label>
      <label class="rc-check" id="rc-o-cat" hidden><input type="checkbox" id="rc-hidecat"> Hide category pages</label>
      <label class="rc-check"><input type="checkbox" id="rc-group" checked> Group by day</label>
      <label class="rc-check"><input type="checkbox" id="rc-compact"> Compact view</label>
      <span class="rc-spacer"></span>
      <button type="button" class="rc-btn" id="rc-refresh">Refresh data</button>
      <button type="button" class="rc-btn" id="rc-export">Export CSV</button>
      <button type="button" class="rc-btn rc-btn-ghost" id="rc-reset">Reset filters</button>
    </div>

    <p class="rc-status" id="rc-status" role="status" aria-live="polite" aria-atomic="true"></p>
    <div id="recent-changes" aria-live="polite" aria-busy="true">
      <p class="rc-loading">Loading recent changes...</p>
    </div>
    <div class="rc-more-wrap">
      <button id="rc-load-more" class="rc-more-btn" type="button" hidden>Load more</button>
    </div>
    <p class="rc-note" id="rc-note"></p>
  </div>
</div>

<script>
(function () {
  'use strict';

  var REPO = 'sunilabrahamindia/sunilabraham';
  var REPO_URL = 'https://github.com/' + REPO;
  var FEED_URL = '/recent-changes.json';
  var PAGES_URL = '/pages.json';
  var AUTHORS = {
    'sunilabrahamindia': 'Tito (TSAP moderator)',
    'sunilabrahamayrookhuziel': 'Sunil Abraham (Owner)',
    'github-actions[bot]': 'GitHub Actions (automated)'
  };
  var $ = function (id) { return document.getElementById(id); };
  var el = {
    list: $('recent-changes'), more: $('rc-load-more'), stats: $('rc-stats'), note: $('rc-note'), status: $('rc-status'),
    search: $('rc-search'), days: $('rc-days'), limit: $('rc-limit'), author: $('rc-author'),
    type: $('rc-type'), cat: $('rc-cat'), sort: $('rc-sort'), hidebot: $('rc-hidebot'), hidecat: $('rc-hidecat'),
    group: $('rc-group'), compact: $('rc-compact'), refresh: $('rc-refresh'), exportBtn: $('rc-export'),
    reset: $('rc-reset'), root: $('rc-root'), panel: $('rc-panel')
  };

  var state = {
    tab: 'edits', commits: [], pages: null, pageBySource: {}, feed: null,
    visible: 50, dataError: null, pendingDays: null, pendingAuthor: '', pendingCat: ''
  };

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function asArray(value) {
    if (Array.isArray(value)) return value.map(function (x) { return String(x); });
    if (value == null || value === '') return [];
    return [String(value)];
  }
  function fmtDate(value) {
    var d = new Date(value);
    if (isNaN(d.getTime())) return String(value || '');
    return d.toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' });
  }
  function fmtCreated(value) {
    var d = parseCreated(value);
    return d ? d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) : '';
  }
  function parseCreated(value) {
    if (!value) return null;
    var d = new Date(String(value).slice(0, 10) + 'T00:00:00');
    return isNaN(d.getTime()) ? null : d;
  }
  function dayKey(value) {
    var d = new Date(value);
    if (isNaN(d.getTime())) return '';
    return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
  }
  function dayLabel(value) {
    var key = dayKey(value), today = new Date(), yesterday = new Date();
    yesterday.setDate(today.getDate() - 1);
    if (key === dayKey(today)) return 'Today';
    if (key === dayKey(yesterday)) return 'Yesterday';
    var d = new Date(value);
    return d.toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
  }
  function relativeDate(value) {
    var seconds = Math.round((Date.now() - new Date(value).getTime()) / 1000);
    if (!isFinite(seconds)) return '';
    if (seconds < 60) return 'just now';
    var minutes = Math.round(seconds / 60);
    if (minutes < 60) return minutes + ' min ago';
    var hours = Math.round(minutes / 60);
    if (hours < 24) return hours + ' hr ago';
    var days = Math.round(hours / 24);
    if (days < 30) return days + (days === 1 ? ' day ago' : ' days ago');
    var months = Math.round(days / 30);
    if (months < 12) return months + (months === 1 ? ' month ago' : ' months ago');
    var years = Math.round(months / 12);
    return years + (years === 1 ? ' year ago' : ' years ago');
  }
  function normaliseCommit(c) {
    var files = Array.isArray(c.files) ? c.files : [];
    var message = String(c.message || '(No commit message)');
    var markdownFile = files.find(function (f) { return /\.md(own)?$/i.test(f.path || ''); });
    return {
      sha: String(c.sha || ''), url: String(c.url || (REPO_URL + '/commit/' + c.sha)),
      date: String(c.date || ''), first: message, body: String(c.body || ''),
      file: markdownFile ? markdownFile.path.split('/').pop() : '',
      type: ['created', 'updated', 'removed', 'automated'].indexOf(c.type) >= 0 ? c.type : 'updated',
      bot: !!c.automated || c.type === 'automated',
      login: String(c.author_login || ''),
      name: String(c.author_name || c.author || 'Unknown'),
      authorKey: String(c.author_login || ('name:' + (c.author_name || c.author || 'Unknown'))),
      files: files, fileCount: Number(c.file_count) || files.length,
      filesTruncated: !!c.files_truncated,
      stats: c.stats || { additions: 0, deletions: 0 }
    };
  }
  function setStatus(message) { el.status.textContent = message || ''; }

  async function loadData() {
    el.list.setAttribute('aria-busy', 'true');
    el.list.innerHTML = '<p class="rc-loading">Loading recent changes...</p>';
    el.stats.innerHTML = '';
    el.note.textContent = '';
    setStatus('');
    try {
      var stamp = Date.now();
      var results = await Promise.all([
        fetch(FEED_URL + '?v=' + stamp, { cache: 'no-store' }),
        fetch(PAGES_URL + '?v=' + stamp, { cache: 'no-store' })
      ]);
      if (!results[0].ok) throw new Error('The recent changes feed returned HTTP ' + results[0].status + '.');
      if (!results[1].ok) throw new Error('The page index returned HTTP ' + results[1].status + '.');
      var feed = await results[0].json();
      var pages = await results[1].json();
      if (!feed || !Array.isArray(feed.commits)) throw new Error('The recent changes feed has an unexpected format.');
      if (!Array.isArray(pages)) throw new Error('The page index has an unexpected format.');
      state.feed = feed;
      state.commits = feed.commits.map(normaliseCommit);
      state.pages = pages.map(function (p) {
        var sourcePath = String(p.source_path || '').replace(/^\\.\\//, '');
        return {
          title: p.title || '(Untitled)', description: p.description || '', created: p.created || null,
          date: p.date || null, source: p.source || '', authors: asArray(p.authors),
          categories: asArray(p.categories), permalink: p.permalink || null,
          source_path: sourcePath
        };
      });
      state.pageBySource = {};
      state.pages.forEach(function (p) { if (p.source_path) state.pageBySource[p.source_path] = p; });
      state.dataError = null;
      refreshAuthorOptions();
      refreshCategoryOptions();
      if (state.pendingAuthor && Array.prototype.some.call(el.author.options, function (o) { return o.value === state.pendingAuthor; })) el.author.value = state.pendingAuthor;
      if (state.pendingCat && Array.prototype.some.call(el.cat.options, function (o) { return o.value === state.pendingCat; })) el.cat.value = state.pendingCat;
    } catch (error) {
      state.dataError = error.message || 'Unable to load the recent changes data.';
      console.error(error);
    }
    render();
  }

  function cutoff() {
    var value = el.days.value;
    if (value === 'all') return null;
    if (state.tab === 'pages') {
      var start = new Date();
      start.setHours(0, 0, 0, 0);
      if (value === 'today') return start;
      start.setDate(start.getDate() - (parseInt(value, 10) - 1));
      return start;
    }
    if (value === '1') return new Date(Date.now() - 24 * 60 * 60 * 1000);
    var d = new Date();
    d.setDate(d.getDate() - parseInt(value, 10));
    return d;
  }
  function passesDate(value, co, dateOnly) {
    if (!co) return true;
    if (dateOnly) {
      var d = parseCreated(value);
      return !!d && d >= co;
    }
    var d2 = new Date(value);
    return !isNaN(d2.getTime()) && d2 >= co;
  }
  function filteredCommits() {
    var q = el.search.value.trim().toLowerCase(), author = el.author.value, type = el.type.value;
    var co = cutoff();
    return state.commits.filter(function (c) {
      if (!passesDate(c.date, co, false)) return false;
      if (el.hidebot.checked && c.bot) return false;
      if (author && c.authorKey !== author) return false;
      if (type && c.type !== type) return false;
      if (q) {
        var fileNames = c.files.map(function (f) { return (f.path || '') + ' ' + (f.previous_filename || ''); }).join(' ');
        var hay = [c.first, c.body, c.name, c.file, fileNames, c.sha, c.type].join(' ').toLowerCase();
        if (hay.indexOf(q) < 0) return false;
      }
      return true;
    });
  }
  function filteredPages() {
    if (!state.pages) return [];
    var q = el.search.value.trim().toLowerCase(), cat = el.cat.value, co = cutoff();
    var out = state.pages.filter(function (p) {
      if (el.hidecat.checked && /^category:/i.test(p.title)) return false;
      if (cat && p.categories.indexOf(cat) < 0) return false;
      if (!passesDate(p.created, co, true)) return false;
      if (q) {
        var hay = [p.title, p.description, p.categories.join(' '), p.authors.join(' '), p.source, p.source_path].join(' ').toLowerCase();
        if (hay.indexOf(q) < 0) return false;
      }
      return true;
    });
    out.sort(function (a, b) {
      if (el.sort.value === 'az') return a.title.localeCompare(b.title, 'en');
      var da = parseCreated(a.created), db = parseCreated(b.created);
      var va = da ? da.getTime() : 0, vb = db ? db.getTime() : 0;
      return el.sort.value === 'old' ? va - vb : vb - va;
    });
    return out;
  }

  function refreshAuthorOptions() {
    var current = el.author.value, seen = {};
    state.commits.forEach(function (c) { seen[c.authorKey] = c.name; });
    var html = '<option value="">All authors</option>';
    Object.keys(seen).sort(function (a, b) { return seen[a].localeCompare(seen[b], 'en'); }).forEach(function (key) {
      html += '<option value="' + esc(key) + '">' + esc(seen[key]) + '</option>';
    });
    el.author.innerHTML = html;
    el.author.value = seen[current] ? current : '';
  }
  function refreshCategoryOptions() {
    if (!state.pages) return;
    var current = el.cat.value, set = {};
    state.pages.forEach(function (p) { p.categories.forEach(function (category) { set[category] = (set[category] || 0) + 1; }); });
    var html = '<option value="">All categories</option>';
    Object.keys(set).sort(function (a, b) { return a.localeCompare(b, 'en'); }).forEach(function (key) {
      html += '<option value="' + esc(key) + '">' + esc(key) + ' (' + set[key] + ')</option>';
    });
    el.cat.innerHTML = html;
    el.cat.value = set[current] ? current : '';
  }
  function pageForSource(path) {
    return state.pageBySource[path] || null;
  }

  var TYPE_LABEL = {
    created: 'Created', updated: 'Updated', removed: 'Removed', automated: 'Automated'
  };
  function commitCard(c, index) {
    var variant = (index % 6) + 1;
    var title = esc(c.first);
    var body = c.body ? '<div class="rc-body">' + esc(c.body) + '</div>' : '';
    var fileNote = c.file ? '<div class="rc-msg">Markdown file: ' + esc(c.file) + '</div>' : '';
    var fileSummary = c.fileCount + ' changed file' + (c.fileCount === 1 ? '' : 's');
    var additions = Number(c.stats.additions) || 0, deletions = Number(c.stats.deletions) || 0;
    return '<article class="rc-item rc-card-variant-' + variant + ' rc-type-' + esc(c.type) + '" data-sha="' + esc(c.sha) + '">' +
      '<div class="rc-title">' + title + '</div>' + fileNote + body +
      '<div class="rc-meta"><span class="rc-badge rc-badge-' + esc(c.type) + '">' + TYPE_LABEL[c.type] + '</span>' +
      '<time datetime="' + esc(c.date) + '" title="' + esc(fmtDate(c.date)) + '">' + esc(fmtDate(c.date)) + '</time>' +
      '<span class="rc-rel">(' + esc(relativeDate(c.date)) + ')</span><span>' + esc(fileSummary) + '</span></div>' +
      '<div class="rc-author"><span aria-hidden="true">Author:</span> <span>' + esc(c.name) + '</span> <code class="rc-sha" title="Full commit SHA">' + esc(c.sha.slice(0, 7)) + '</code></div>' +
      '<div class="rc-links"><a href="' + esc(c.url) + '" rel="nofollow">View commit</a>' +
      '<button type="button" class="rc-link-btn" data-act="files" aria-expanded="false">Changed files</button>' +
      '<button type="button" class="rc-link-btn" data-act="copy" data-sha="' + esc(c.sha) + '">Copy SHA</button></div>' +
      '<div class="rc-details" hidden></div></article>';
  }

  function pageCard(p, index) {
    var variant = (index % 6) + 1;
    var chips = p.categories.map(function (category) { return '<span class="rc-chip">' + esc(category) + '</span>'; }).join('');
    var bits = [];
    if (p.authors.length) bits.push('Authors: ' + esc(p.authors.join(', ')));
    if (p.source) bits.push('Source: ' + esc(p.source));
    if (p.date) bits.push('Published: ' + esc(fmtCreated(p.date)));
    var title = p.permalink
      ? '<a href="' + esc(p.permalink) + '">' + esc(p.title) + '</a>'
      : esc(p.title);
    var sourceLink = p.source_path
      ? '<a href="' + esc(REPO_URL + '/blob/main/' + p.source_path.split('/').map(encodeURIComponent).join('/')) + '" rel="nofollow">View source</a>'
      : '';
    var desc = p.description ? '<div class="rc-msg">' + esc(p.description) + '</div>' : '';
    return '<article class="rc-item rc-card-variant-' + variant + ' rc-type-created"><div class="rc-title">' + title + '</div>' + desc +
      '<div class="rc-meta"><span class="rc-badge rc-badge-created">Created</span><time datetime="' + esc(p.created || '') + '">' + esc(fmtCreated(p.created)) + '</time></div>' +
      (bits.length ? '<div class="rc-author">' + bits.join(' &nbsp;·&nbsp; ') + '</div>' : '') +
      (chips ? '<div class="rc-chips">' + chips + '</div>' : '') +
      (sourceLink ? '<div class="rc-links">' + sourceLink + '</div>' : '') + '</article>';
  }

  function renderList(items, dateOf, cardFn) {
    var shown = items.slice(0, state.visible);
    var group = el.group.checked && (state.tab === 'edits' || el.sort.value !== 'az');
    var html = '', lastKey = '';
    shown.forEach(function (item, index) {
      if (group) {
        var date = dateOf(item);
        var key = state.tab === 'edits' ? dayKey(date) : (date || '');
        if (key !== lastKey) {
          var label = state.tab === 'edits' ? dayLabel(date) : (date ? fmtCreated(date) : 'Undated');
          html += '<h3 class="rc-day">' + esc(label) + '</h3>';
          lastKey = key;
        }
      }
      html += cardFn(item, index);
    });
    el.list.innerHTML = html;
    return shown.length;
  }

  function updateStats(items, shownCount) {
    var parts = [];
    if (state.tab === 'edits') {
      var people = {};
      items.forEach(function (c) { people[c.authorKey] = true; });
      parts.push('<span class="rc-stat"><b>' + items.length + '</b> matching commits in feed</span>');
      parts.push('<span class="rc-stat"><b>' + Object.keys(people).length + '</b> contributors in feed</span>');
      parts.push('<span class="rc-stat"><b>' + items.filter(function (c) { return c.type === 'created'; }).length + '</b> created</span>');
      parts.push('<span class="rc-stat"><b>' + items.filter(function (c) { return c.type === 'automated'; }).length + '</b> automated</span>');
    } else {
      parts.push('<span class="rc-stat"><b>' + items.length + '</b> matching pages in index</span>');
      parts.push('<span class="rc-stat"><b>' + items.filter(function (p) { return !/^category:/i.test(p.title); }).length + '</b> excluding category pages</span>');
    }
    parts.push('<span class="rc-stat">Showing <b>' + shownCount + '</b></span>');
    el.stats.innerHTML = parts.join('');
  }

  function setNote() {
    if (state.tab === 'pages') {
      el.note.textContent = 'New pages are filtered by their created date, which is date-based rather than an exact time. The list comes from pages.json; edits to existing pages appear under Edits.';
      return;
    }
    if (!state.feed) {
      el.note.textContent = '';
      return;
    }
    var included = Number(state.feed.included_commits) || state.commits.length;
    var total = Number(state.feed.total_commits_in_repo) || included;
    var generated = state.feed.generated_at ? fmtDate(state.feed.generated_at) : 'unknown';
    var note = 'Feed generated ' + generated + '. Showing the latest ' + included + ' of ' + total + ' repository commits.';
    if (state.feed.history_truncated) note += ' Older commits are outside this feed; a time range or search may extend beyond the available history.';
    if (state.feed.files_per_commit_limit) note += ' Up to ' + state.feed.files_per_commit_limit + ' changed files are listed per commit; commit links show the complete file list.';
    el.note.textContent = note;
  }

  function render() {
    el.list.setAttribute('aria-busy', 'true');
    if (state.dataError) {
      el.list.innerHTML = '<p class="rc-empty">' + esc(state.dataError) + ' Please try Refresh data later.</p>';
      el.stats.innerHTML = '';
      el.more.hidden = true;
      el.note.textContent = '';
      el.list.setAttribute('aria-busy', 'false');
      syncUrl();
      return;
    }
    if (!state.feed || !state.pages) {
      el.list.innerHTML = '<p class="rc-loading">Loading recent changes...</p>';
      el.list.setAttribute('aria-busy', 'false');
      return;
    }
    var items, shown;
    if (state.tab === 'edits') {
      items = filteredCommits();
      if (!items.length) {
        var co = cutoff(), oldest = state.feed.oldest_included_date ? new Date(state.feed.oldest_included_date) : null;
        var beyond = !!(state.feed.history_truncated && co && oldest && co < oldest);
        el.list.innerHTML = '<p class="rc-empty">' + (beyond
          ? 'No matching commits in the available feed. The selected period may include older commits that are not included here.'
          : (state.feed.history_truncated && el.days.value === 'all'
            ? 'No commits match these filters in the available feed. Older history is not included.'
            : 'No commits match the selected filters in the available feed.')) + '</p>';
        shown = 0;
      } else {
        shown = renderList(items, function (c) { return c.date; }, commitCard);
      }
      updateStats(items, shown);
      el.more.hidden = items.length <= state.visible;
    } else {
      items = filteredPages();
      if (!items.length) {
        el.list.innerHTML = '<p class="rc-empty">No pages match the selected filters in the current page index.</p>';
        shown = 0;
      } else {
        shown = renderList(items, function (p) { return p.created; }, pageCard);
      }
      updateStats(items, shown);
      el.more.hidden = items.length <= state.visible;
    }
    setNote();
    el.list.setAttribute('aria-busy', 'false');
    syncUrl();
  }

  function setTab(tab) {
    state.tab = tab === 'pages' ? 'pages' : 'edits';
    document.querySelectorAll('.rc-tab').forEach(function (button) {
      var active = button.dataset.tab === state.tab;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', active ? 'true' : 'false');
      button.tabIndex = active ? 0 : -1;
    });
    el.panel.setAttribute('aria-labelledby', state.tab === 'edits' ? 'rc-tab-edits' : 'rc-tab-pages');
    var edits = state.tab === 'edits';
    $('rc-f-author').hidden = !edits;
    $('rc-f-type').hidden = !edits;
    $('rc-o-bot').hidden = !edits;
    $('rc-f-cat').hidden = edits;
    $('rc-f-sort').hidden = edits;
    $('rc-o-cat').hidden = edits;
    var old = el.days.value;
    var options = edits
      ? [['1', 'Last 24 hours'], ['7', 'Last 7 days'], ['30', 'Last 30 days'], ['90', 'Last 90 days'], ['365', 'Last year'], ['all', 'All available history']]
      : [['today', 'Today'], ['7', 'Last 7 days'], ['30', 'Last 30 days'], ['90', 'Last 90 days'], ['365', 'Last year'], ['all', 'All dates']];
    el.days.innerHTML = options.map(function (option) {
      return '<option value="' + option[0] + '">' + option[1] + '</option>';
    }).join('');
    var allowed = options.some(function (option) { return option[0] === old; });
    el.days.value = allowed ? old : '7';
    if (state.pendingDays) {
      var pendingAllowed = options.some(function (option) { return option[0] === state.pendingDays; });
      if (pendingAllowed) el.days.value = state.pendingDays;
      state.pendingDays = null;
    }
    state.visible = parseInt(el.limit.value, 10) || 50;
  }

  function toggleFiles(card, button) {
    var panel = card.querySelector('.rc-details');
    var open = !panel.hidden;
    if (open) {
      panel.hidden = true;
      button.setAttribute('aria-expanded', 'false');
      return;
    }
    panel.hidden = false;
    button.setAttribute('aria-expanded', 'true');
    var sha = card.dataset.sha;
    var commit = state.commits.find(function (item) { return item.sha === sha; });
    if (!commit) {
      panel.innerHTML = '<p class="rc-empty">File details are not available.</p>';
      return;
    }
    var icon = { added: '+', modified: '~', removed: '-', renamed: '→', copied: '↗' };
    var rows = commit.files.map(function (file) {
      var path = String(file.path || '');
      var status = String(file.status || 'modified');
      var page = pageForSource(path);
      var link = '';
      if (page && page.permalink && status !== 'removed') {
        link = '<a href="' + esc(page.permalink) + '">' + esc(page.title) + '</a> <span class="rc-path">' + esc(path) + '</span>';
      } else if (status !== 'removed' && path) {
        link = '<a href="' + esc(REPO_URL + '/blob/' + sha + '/' + path.split('/').map(encodeURIComponent).join('/')) + '" rel="nofollow">' + esc(path) + '</a>';
      } else {
        link = '<span>' + esc(path) + '</span>';
      }
      var add = Number(file.additions) || 0, del = Number(file.deletions) || 0;
      return '<li class="rc-file rc-file-' + esc(status) + '"><span class="rc-ficon" aria-label="' + esc(status) + '">' + (icon[status] || '~') + '</span>' +
        '<span class="rc-file-main">' + link + (file.previous_filename ? '<span class="rc-path"> (from ' + esc(file.previous_filename) + ')</span>' : '') + '</span>' +
        '<span class="rc-fstat"><span class="rc-add">+' + add + '</span> <span class="rc-del">-' + del + '</span></span></li>';
    }).join('');
    var total = '<div class="rc-diffstat">+' + (Number(commit.stats.additions) || 0) + ' / -' +
      (Number(commit.stats.deletions) || 0) + ' lines across ' + commit.fileCount + ' changed files.</div>';
    var extra = commit.filesTruncated
      ? '<p class="rc-note">Showing ' + commit.files.length + ' files. Open the commit to see the complete list.</p>'
      : '';
    panel.innerHTML = total + '<ul class="rc-files">' + rows + '</ul>' + extra;
  }

  function download(name, text, mime) {
    var blob = new Blob([text], { type: mime });
    var url = URL.createObjectURL(blob);
    var anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = name;
    document.body.appendChild(anchor);
    anchor.click();
    setTimeout(function () { URL.revokeObjectURL(url); anchor.remove(); }, 500);
  }
  function csvCell(value) {
    var text = String(value == null ? '' : value);
    if (/^[\\s\\u0000-\\u001f]*[=+\\-@]/.test(text) || /^[\\t\\r]/.test(text)) text = "'" + text;
    return '"' + text.replace(/"/g, '""') + '"';
  }
  function exportCsv() {
    var stamp = new Date().toISOString().slice(0, 10), rows;
    if (state.tab === 'edits') {
      rows = [['date', 'type', 'author', 'message', 'files', 'sha', 'url']];
      filteredCommits().forEach(function (c) {
        rows.push([c.date, c.type, c.name, c.first, c.files.map(function (f) { return f.path; }).join('; '), c.sha, c.url]);
      });
      download('tsap-recent-edits-' + stamp + '.csv', rows.map(function (row) { return row.map(csvCell).join(','); }).join('\\r\\n'), 'text/csv;charset=utf-8');
    } else {
      rows = [['created', 'title', 'categories', 'authors', 'source', 'published', 'source_path', 'url']];
      filteredPages().forEach(function (p) {
        rows.push([p.created || '', p.title, p.categories.join('; '), p.authors.join('; '), p.source, p.date || '', p.source_path, p.permalink || '']);
      });
      download('tsap-new-pages-' + stamp + '.csv', rows.map(function (row) { return row.map(csvCell).join(','); }).join('\\r\\n'), 'text/csv;charset=utf-8');
    }
    setStatus('CSV export prepared.');
  }

  function syncUrl() {
    try {
      var params = new URLSearchParams();
      if (state.tab !== 'edits') params.set('tab', state.tab);
      if (el.search.value.trim()) params.set('q', el.search.value.trim());
      if (el.days.value !== '7') params.set('days', el.days.value);
      if (el.limit.value !== '50') params.set('limit', el.limit.value);
      if (el.author.value) params.set('author', el.author.value);
      if (el.type.value) params.set('type', el.type.value);
      if (el.cat.value) params.set('cat', el.cat.value);
      if (el.sort.value !== 'new') params.set('sort', el.sort.value);
      if (el.hidebot.checked) params.set('hidebot', '1');
      if (el.hidecat.checked) params.set('hidecat', '1');
      var query = params.toString();
      history.replaceState(null, '', location.pathname + (query ? '?' + query : '') + location.hash);
    } catch (error) {}
  }
  function readUrl() {
    var params = new URLSearchParams(location.search);
    state.tab = params.get('tab') === 'pages' ? 'pages' : 'edits';
    state.pendingDays = params.get('days') || null;
    state.pendingAuthor = params.get('author') || '';
    state.pendingCat = params.get('cat') || '';
    if (params.has('q')) el.search.value = params.get('q').slice(0, 200);
    if (['20', '50', '100', '200'].indexOf(params.get('limit')) >= 0) el.limit.value = params.get('limit');
    if (['created', 'updated', 'removed', 'automated'].indexOf(params.get('type')) >= 0) el.type.value = params.get('type');
    if (['new', 'old', 'az'].indexOf(params.get('sort')) >= 0) el.sort.value = params.get('sort');
    el.hidebot.checked = params.get('hidebot') === '1';
    el.hidecat.checked = params.get('hidecat') === '1';
  }
  function loadPrefs() {
    try {
      el.compact.checked = localStorage.getItem('rc:compact') === '1';
      el.group.checked = localStorage.getItem('rc:group') !== '0';
    } catch (error) {}
    el.root.classList.toggle('rc-compact', el.compact.checked);
  }
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.setAttribute('readonly', '');
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      var success = false;
      try { success = document.execCommand('copy'); } catch (error) {}
      textarea.remove();
      if (success) resolve(); else reject(new Error('Clipboard copy failed'));
    });
  }

  var searchTimer;
  el.search.addEventListener('input', function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () { state.visible = parseInt(el.limit.value, 10) || 50; render(); }, 200);
  });
  [el.author, el.type, el.cat, el.sort, el.hidebot, el.hidecat, el.group].forEach(function (control) {
    control.addEventListener('change', function () {
      try { localStorage.setItem('rc:group', el.group.checked ? '1' : '0'); } catch (error) {}
      state.visible = parseInt(el.limit.value, 10) || 50;
      render();
    });
  });
  el.limit.addEventListener('change', function () { state.visible = parseInt(el.limit.value, 10) || 50; render(); });
  el.days.addEventListener('change', function () { state.visible = parseInt(el.limit.value, 10) || 50; render(); });
  el.compact.addEventListener('change', function () {
    el.root.classList.toggle('rc-compact', el.compact.checked);
    try { localStorage.setItem('rc:compact', el.compact.checked ? '1' : '0'); } catch (error) {}
  });
  el.more.addEventListener('click', function () {
    state.visible += parseInt(el.limit.value, 10) || 50;
    render();
  });
  el.refresh.addEventListener('click', function () {
    state.pendingDays = null; state.pendingAuthor = ''; state.pendingCat = '';
    loadData();
  });
  el.exportBtn.addEventListener('click', exportCsv);
  el.reset.addEventListener('click', function () {
    el.search.value = ''; el.days.value = '7'; el.limit.value = '50'; el.author.value = '';
    el.type.value = ''; el.cat.value = ''; el.sort.value = 'new';
    el.hidebot.checked = false; el.hidecat.checked = false;
    state.visible = 50;
    render();
    setStatus('Filters reset. Saved display preferences were kept.');
  });
  document.querySelectorAll('.rc-tab').forEach(function (button) {
    button.addEventListener('click', function () {
      setTab(button.dataset.tab);
      render();
    });
    button.addEventListener('keydown', function (event) {
      var tabs = Array.prototype.slice.call(document.querySelectorAll('.rc-tab'));
      var index = tabs.indexOf(button), next = null;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = tabs[(index + 1) % tabs.length];
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = tabs[(index - 1 + tabs.length) % tabs.length];
      else if (event.key === 'Home') next = tabs[0];
      else if (event.key === 'End') next = tabs[tabs.length - 1];
      if (next) {
        event.preventDefault();
        next.focus();
        setTab(next.dataset.tab);
        render();
      }
    });
  });
  el.list.addEventListener('click', function (event) {
    var button = event.target.closest('button[data-act]');
    if (!button) return;
    var card = button.closest('.rc-item');
    if (button.dataset.act === 'files') toggleFiles(card, button);
    if (button.dataset.act === 'copy') {
      var sha = button.dataset.sha, old = 'Copy SHA';
      button.disabled = true;
      copyText(sha).then(function () {
        button.textContent = 'Copied';
        setStatus('Commit SHA copied to the clipboard.');
      }).catch(function () {
        button.textContent = 'Copy failed';
        setStatus('Could not copy the SHA automatically. Select the commit SHA shown on the card and copy it manually.');
      }).finally(function () {
        setTimeout(function () {
          button.textContent = old;
          button.disabled = false;
        }, 2200);
      });
    }
  });

  readUrl();
  loadPrefs();
  setTab(state.tab);
  state.visible = parseInt(el.limit.value, 10) || 50;
  loadData();
})();
</script>

<style>
.rc-wrap {
  --rc-bg: #ffffff;
  --rc-surface: #f8fafc;
  --rc-border: #cbd5e1;
  --rc-border-strong: #94a3b8;
  --rc-text: #172033;
  --rc-muted: #475569;
  --rc-link: #1d4ed8;
  --rc-accent: #1d4ed8;
  --rc-accent-soft: #dbeafe;
  --rc-input: #ffffff;
  --rc-add: #166534;
  --rc-del: #991b1b;
  color: var(--rc-text);
}
.rc-tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--rc-border); margin: 18px 0 16px; }
.rc-tab {
  appearance: none; border: 1px solid transparent; border-bottom: 3px solid transparent;
  background: transparent; padding: 10px 16px; font-size: .95rem; font-weight: 600;
  color: var(--rc-muted); cursor: pointer; margin-bottom: -1px; font-family: inherit;
}
.rc-tab:hover { color: var(--rc-text); }
.rc-tab.is-active { color: var(--rc-accent); border-bottom-color: var(--rc-accent); }
.rc-tab:focus-visible, .rc-btn:focus-visible, .rc-more-btn:focus-visible, .rc-link-btn:focus-visible,
.rc-wrap a:focus-visible, .rc-field select:focus-visible, .rc-field input:focus-visible, .rc-check input:focus-visible {
  outline: 3px solid var(--rc-accent); outline-offset: 3px;
}
.rc-stats { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; min-height: 28px; }
.rc-stat {
  font-size: .82rem; padding: 4px 10px; border: 1px solid var(--rc-border);
  background: var(--rc-surface); color: var(--rc-muted); border-radius: 999px;
}
.rc-stat b { color: var(--rc-text); }
.rc-toolbar {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px;
  padding: 14px; border: 1px solid var(--rc-border); background: var(--rc-surface); border-radius: 12px;
}
.rc-field { display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.rc-field-wide { grid-column: 1 / -1; }
.rc-field label { font-size: .78rem; font-weight: 700; color: var(--rc-muted); text-transform: uppercase; letter-spacing: .04em; }
.rc-field select, .rc-field input[type="search"] {
  width: 100%; padding: 9px 10px; font-size: .92rem; border: 1px solid var(--rc-border-strong);
  border-radius: 8px; background: var(--rc-input); color: var(--rc-text); min-height: 42px; font-family: inherit;
}
.rc-options { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 18px; margin: 12px 0 18px; }
.rc-check { display: inline-flex; align-items: center; gap: 7px; font-size: .88rem; color: var(--rc-text); cursor: pointer; }
.rc-check input { width: 18px; height: 18px; accent-color: var(--rc-accent); }
.rc-spacer { flex: 1 1 auto; }
.rc-btn, .rc-more-btn {
  padding: 8px 14px; border: 1px solid var(--rc-border-strong); background: var(--rc-input);
  color: var(--rc-text); border-radius: 8px; font-size: .88rem; font-weight: 600;
  cursor: pointer; min-height: 40px; transition: background-color .15s ease, border-color .15s ease; font-family: inherit;
}
.rc-btn:hover, .rc-more-btn:hover { background: var(--rc-accent-soft); border-color: var(--rc-accent); }
.rc-btn:disabled { opacity: .7; cursor: wait; }
.rc-btn-ghost { background: transparent; }
.rc-more-btn { padding: 10px 24px; font-size: .95rem; }
.rc-day { margin: 26px 0 10px; padding-bottom: 6px; font-size: .95rem; font-weight: 700; color: var(--rc-muted); border-bottom: 1px solid var(--rc-border); }
.rc-day:first-child { margin-top: 6px; }
.rc-item {
  border: 1px solid var(--rc-border); border-left-width: 4px; border-radius: 10px;
  padding: 14px 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,.04);
  color: var(--rc-text); transition: background-color .15s ease, border-color .15s ease; overflow-wrap: anywhere;
}
.rc-type-created { border-left-color: #166534; }
.rc-type-updated { border-left-color: #1d4ed8; }
.rc-type-removed { border-left-color: #991b1b; }
.rc-type-automated { border-left-color: #475569; }
.rc-card-variant-1 { background-color: #f8fbff; }
.rc-card-variant-2 { background-color: #f5fbf7; }
.rc-card-variant-3 { background-color: #fffaf5; }
.rc-card-variant-4 { background-color: #faf8ff; }
.rc-card-variant-5 { background-color: #f4fbfc; }
.rc-card-variant-6 { background-color: #fff7fa; }
.rc-title { font-size: 1.02rem; font-weight: 700; line-height: 1.45; margin-bottom: 6px; color: var(--rc-text); }
.rc-title a { color: var(--rc-link); text-decoration: underline; text-underline-offset: .15em; }
.rc-msg { font-size: .9rem; color: var(--rc-muted); margin-bottom: 6px; line-height: 1.5; }
.rc-body { font-size: .88rem; color: var(--rc-muted); white-space: pre-wrap; overflow-wrap: anywhere; margin-bottom: 6px; }
.rc-meta, .rc-author { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; font-size: .86rem; color: var(--rc-muted); margin-bottom: 5px; }
.rc-rel { color: var(--rc-muted); }
.rc-sha { font-size: .78rem; padding: 2px 6px; border-radius: 5px; background: var(--rc-surface); border: 1px solid var(--rc-border); color: var(--rc-muted); }
.rc-badge { font-size: .76rem; font-weight: 700; padding: 3px 9px; border-radius: 999px; border: 1px solid transparent; }
.rc-badge-created { background: #dcfce7; color: #14532d; border-color: #86efac; }
.rc-badge-updated { background: #dbeafe; color: #1e3a8a; border-color: #93c5fd; }
.rc-badge-removed { background: #fee2e2; color: #7f1d1d; border-color: #fca5a5; }
.rc-badge-automated { background: #e2e8f0; color: #334155; border-color: #cbd5e1; }
.rc-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
.rc-chip { font-size: .76rem; padding: 3px 9px; border-radius: 999px; background: var(--rc-surface); border: 1px solid var(--rc-border); color: var(--rc-muted); }
.rc-links { display: flex; flex-wrap: wrap; gap: 6px 16px; margin-top: 10px; font-size: .88rem; }
.rc-links a, .rc-link-btn { color: var(--rc-link); text-decoration: underline; text-underline-offset: .15em; font-weight: 600; background: none; border: 0; padding: 5px 0; font-size: inherit; cursor: pointer; font-family: inherit; }
.rc-details { margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--rc-border-strong); }
.rc-diffstat { font-size: .84rem; color: var(--rc-muted); margin-bottom: 8px; }
.rc-files { list-style: none; margin: 0; padding: 0; }
.rc-file { display: flex; align-items: baseline; gap: 8px; padding: 6px 0; font-size: .86rem; flex-wrap: wrap; }
.rc-file-main { min-width: 0; overflow-wrap: anywhere; }
.rc-file a { color: var(--rc-link); text-decoration: underline; text-underline-offset: .15em; }
.rc-ficon { font-weight: 800; width: 16px; text-align: center; }
.rc-file-added .rc-ficon { color: var(--rc-add); }
.rc-file-removed .rc-ficon { color: var(--rc-del); }
.rc-path { color: var(--rc-muted); font-size: .78rem; overflow-wrap: anywhere; }
.rc-fstat { margin-left: auto; font-size: .78rem; white-space: nowrap; }
.rc-add { color: var(--rc-add); font-weight: 600; }
.rc-del { color: var(--rc-del); font-weight: 600; }
.rc-more-wrap { text-align: center; margin: 24px 0 8px; }
.rc-loading { font-style: italic; color: var(--rc-muted); margin: 16px 0; }
.rc-empty { text-align: center; padding: 28px 16px; border: 1px dashed var(--rc-border-strong); border-radius: 10px; color: var(--rc-muted); }
.rc-note, .rc-status { font-size: .82rem; color: var(--rc-muted); margin-top: 10px; line-height: 1.5; }
.rc-note { text-align: center; }
.rc-status:empty { display: none; }
.rc-compact .rc-item { padding: 8px 12px; margin-bottom: 8px; }
.rc-compact .rc-body, .rc-compact .rc-msg, .rc-compact .rc-rel, .rc-compact .rc-chips { display: none; }
.rc-compact .rc-title { font-size: .95rem; margin-bottom: 2px; }
.rc-compact .rc-links { margin-top: 4px; }
@media (max-width: 600px) {
  .rc-toolbar { grid-template-columns: 1fr 1fr; padding: 12px; gap: 10px; }
  .rc-field-wide { grid-column: 1 / -1; }
  .rc-options { gap: 8px 14px; }
  .rc-spacer { flex-basis: 100%; height: 0; }
  .rc-btn { flex: 1 1 30%; }
  .rc-tab { flex: 1; text-align: center; }
  .rc-item { padding: 12px; }
  .rc-fstat { margin-left: 24px; }
}
@media (max-width: 380px) { .rc-toolbar { grid-template-columns: 1fr; } }
body.tsap-dark-mode .rc-wrap {
  --rc-bg: #0f172a; --rc-surface: #1e293b; --rc-border: #475569; --rc-border-strong: #64748b;
  --rc-text: #f1f5f9; --rc-muted: #cbd5e1; --rc-link: #93c5fd; --rc-accent: #93c5fd;
  --rc-accent-soft: #1e3a5f; --rc-input: #0f172a; --rc-add: #86efac; --rc-del: #fca5a5;
}
body.tsap-dark-mode .rc-card-variant-1 { background-color: #17243a; }
body.tsap-dark-mode .rc-card-variant-2 { background-color: #172e29; }
body.tsap-dark-mode .rc-card-variant-3 { background-color: #30271d; }
body.tsap-dark-mode .rc-card-variant-4 { background-color: #28243d; }
body.tsap-dark-mode .rc-card-variant-5 { background-color: #172d37; }
body.tsap-dark-mode .rc-card-variant-6 { background-color: #30212b; }
body.tsap-dark-mode .rc-badge-created { background: #14532d; color: #dcfce7; border-color: #4ade80; }
body.tsap-dark-mode .rc-badge-updated { background: #1e3a8a; color: #dbeafe; border-color: #60a5fa; }
body.tsap-dark-mode .rc-badge-removed { background: #7f1d1d; color: #fee2e2; border-color: #f87171; }
body.tsap-dark-mode .rc-badge-automated { background: #334155; color: #f1f5f9; border-color: #64748b; }
@media (prefers-reduced-motion: reduce) {
  .rc-item, .rc-btn, .rc-more-btn { transition: none; }
}
@media (prefers-contrast: more) {
  .rc-item, .rc-toolbar, .rc-stat, .rc-chip { border-width: 2px; }
  .rc-title a, .rc-links a, .rc-link-btn { text-decoration: underline; }
}
</style>
