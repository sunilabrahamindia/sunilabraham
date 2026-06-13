---
layout: default
title: "Query"
description: "Search and filter indexed content across The Sunil Abraham Project using metadata such as title, author, source, category, and date."
permalink: /query/
categories: [Project pages]
created: 2026-06-13
---

**Query** is a tool on this project that allows users to search and filter indexed records using structured metadata such as title, author, source, category, and date. The tool currently includes selected publications, media mentions, and other indexed records. Results can be filtered, exported, and shared through URL parameters.

<div class="msq-wrap">

  <!-- Toolbar -->
  <div class="msq-toolbar">
    <span class="msq-toolbar-title">🔍 Metadata Search</span>
    <button class="msq-btn" id="msqRun">▶ Run</button>
    <button class="msq-btn-ghost" id="msqClear">Clear</button>
    <button class="msq-btn-ghost" id="msqExportCsv">CSV</button>
    <button class="msq-btn-ghost" id="msqExportJson">JSON</button>
  </div>

  <!-- Filters -->
  <div class="msq-filters">

    <div class="msq-field msq-field--wide">
      <label for="msqQ">🔎 Search <span class="msq-hint">Operators: <code>after:YYYY-MM-DD</code> <code>before:YYYY-MM-DD</code> <code>intitle:word</code></span></label>
      <input type="text" id="msqQ" placeholder="e.g. privacy intitle:safety after:2018-01-01" autocomplete="off" />
    </div>

    <div class="msq-field">
      <label for="msqTitle">📝 Title contains</label>
      <input type="text" id="msqTitle" placeholder="Words in title…" autocomplete="off" />
    </div>

    <div class="msq-field">
      <label for="msqDesc">📄 Description contains</label>
      <input type="text" id="msqDesc" placeholder="Words in description…" autocomplete="off" />
    </div>

    <div class="msq-field">
      <label>✍️ Author(s)</label>
      <div class="msq-suggest-wrap">
        <div class="msq-tags" id="msqAuthorTags"><input type="text" id="msqAuthorInput" placeholder="Type name, press Enter" autocomplete="off" /></div>
        <div class="msq-suggest" id="msqAuthorSuggest" role="listbox"></div>
      </div>
      <span class="msq-tag-tip">Partial match · Sunil Abraham listed first</span>
    </div>

    <div class="msq-field">
      <label>📰 Source</label>
      <div class="msq-suggest-wrap">
        <div class="msq-tags" id="msqSourceTags"><input type="text" id="msqSourceInput" placeholder="Type source, press Enter" autocomplete="off" /></div>
        <div class="msq-suggest" id="msqSourceSuggest" role="listbox"></div>
      </div>
    </div>

    <div class="msq-field">
      <label>🏷️ Categories</label>
      <div class="msq-suggest-wrap">
        <div class="msq-tags" id="msqCatTags"><input type="text" id="msqCatInput" placeholder="Type category, press Enter" autocomplete="off" /></div>
        <div class="msq-suggest" id="msqCatSuggest" role="listbox"></div>
      </div>
    </div>

    <div class="msq-field">
      <label for="msqAfter">📅 After</label>
      <input type="text" id="msqAfter" placeholder="YYYY-MM-DD" autocomplete="off" />
    </div>

    <div class="msq-field">
      <label for="msqBefore">📅 Before</label>
      <input type="text" id="msqBefore" placeholder="YYYY-MM-DD" autocomplete="off" />
    </div>

    <div class="msq-field">
      <label for="msqSort">⇅ Sort by</label>
      <select id="msqSort" aria-label="Sort results">
        <option value="date_desc">Date (newest first)</option>
        <option value="date_asc">Date (oldest first)</option>
        <option value="created_desc">Created (newest first)</option>
        <option value="created_asc">Created (oldest first)</option>
        <option value="title_asc">Title (A–Z)</option>
        <option value="title_desc">Title (Z–A)</option>
      </select>
    </div>

  </div><!-- /msq-filters -->

  <!-- Results bar -->
  <div class="msq-results-bar">
    <span id="msqCount">—</span>
    <span class="msq-url-note">Shareable URL updates automatically</span>
  </div>

  <!-- Results -->
  <div id="msqResults" aria-live="polite">
    <div class="msq-empty">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      Apply filters and click Run to search metadata.
    </div>
  </div>

</div><!-- /msq-wrap -->

<script>
/* ── DATA (Jekyll Liquid) ── */
const MSQ_DATA = [
{% for p in site.pages %}
{% if p.title and p.created %}
{
  title: {{ p.title | jsonify }},
  description: {{ p.description | default: "" | jsonify }},
  source: {{ p.source | default: "" | jsonify }},
  authors: {{ p.authors | default: "" | jsonify }},
  categories: {{ p.categories | default: "" | jsonify }},
  date: {{ p.date | default: "" | jsonify }},
  created: {{ p.created | jsonify }},
  url: "{{ p.url }}"
},
{% endif %}
{% endfor %}
];

/* ── Normalise arrays ── */
MSQ_DATA.forEach(d => {
  if (!Array.isArray(d.authors))    d.authors    = d.authors    ? [d.authors]    : [];
  if (!Array.isArray(d.categories)) d.categories = d.categories ? [d.categories] : [];
});

/* ── Pool lists ── */
function msqUniq(arr) { return [...new Set((arr||[]).filter(Boolean))].sort(); }
const msqAllAuthors = msqUniq(MSQ_DATA.flatMap(d => d.authors));
if (msqAllAuthors.includes('Sunil Abraham')) {
  const rest = msqAllAuthors.filter(a => a !== 'Sunil Abraham');
  msqAllAuthors.length = 0;
  msqAllAuthors.push('Sunil Abraham', ...rest);
}
const msqAllSources = msqUniq(MSQ_DATA.map(d => d.source));
const msqAllCats    = msqUniq(MSQ_DATA.flatMap(d => d.categories));

/* ── Tag-input factory ── */
function msqMakeTagInput(listEl, inputEl, suggestEl, pool) {
  const tags = [];

  function render() {
    listEl.querySelectorAll('.msq-chip').forEach(c => c.remove());
    tags.forEach((t, i) => {
      const chip = document.createElement('span');
      chip.className = 'msq-chip';
      chip.innerHTML = `${t}<button type="button" aria-label="Remove ${t}">✕</button>`;
      chip.querySelector('button').addEventListener('click', () => { tags.splice(i, 1); render(); });
      listEl.insertBefore(chip, inputEl);
    });
  }

  function add(v) {
    const t = (v || '').trim();
    if (t && !tags.includes(t)) { tags.push(t); render(); }
  }

  function suggest(q) {
    const ql = q.toLowerCase();
    const hits = pool.filter(x => x.toLowerCase().includes(ql) && !tags.includes(x)).slice(0, 25);
    suggestEl.innerHTML = '';
    if (!hits.length) { suggestEl.style.display = 'none'; return; }
    hits.forEach(h => {
      const b = document.createElement('button');
      b.type = 'button'; b.textContent = h;
      b.addEventListener('click', () => { add(h); inputEl.value = ''; suggestEl.style.display = 'none'; });
      suggestEl.appendChild(b);
    });
    suggestEl.style.display = 'block';
  }

  inputEl.addEventListener('keydown', e => {
    if (e.key === 'Enter') { e.preventDefault(); add(inputEl.value); inputEl.value = ''; suggestEl.style.display = 'none'; }
    if (e.key === 'Escape') { inputEl.value = ''; suggestEl.style.display = 'none'; }
  });
  inputEl.addEventListener('input', () => inputEl.value.trim() ? suggest(inputEl.value) : (suggestEl.style.display = 'none'));
  inputEl.addEventListener('blur',  () => setTimeout(() => suggestEl.style.display = 'none', 150));
  listEl.addEventListener('click',  () => inputEl.focus());

  return { add, get: () => tags.slice(), clear: () => { tags.length = 0; render(); } };
}

const msqTiAuthor = msqMakeTagInput(document.getElementById('msqAuthorTags'), document.getElementById('msqAuthorInput'), document.getElementById('msqAuthorSuggest'), msqAllAuthors);
const msqTiSource = msqMakeTagInput(document.getElementById('msqSourceTags'), document.getElementById('msqSourceInput'), document.getElementById('msqSourceSuggest'), msqAllSources);
const msqTiCat    = msqMakeTagInput(document.getElementById('msqCatTags'),    document.getElementById('msqCatInput'),    document.getElementById('msqCatSuggest'),    msqAllCats);

/* ── Operator parser ── */
function msqParseOps(q) {
  const a = q.match(/after:(\d{4}-\d{2}-\d{2})/);
  const b = q.match(/before:(\d{4}-\d{2}-\d{2})/);
  const t = q.match(/intitle:([\w-]+)/);
  return { after: a ? a[1] : null, before: b ? b[1] : null, intitle: t ? t[1] : null };
}

/* ── Match logic ── */
function msqMatches(item, s) {
  if (s.title && !(item.title && item.title.toLowerCase().includes(s.title.toLowerCase()))) return false;
  if (s.desc  && !(item.description && item.description.toLowerCase().includes(s.desc.toLowerCase()))) return false;
  if (s.intitle && !(item.title && item.title.toLowerCase().includes(s.intitle.toLowerCase()))) return false;

  const qClean = (s.q || '')
    .replace(/after:\d{4}-\d{2}-\d{2}/g, '')
    .replace(/before:\d{4}-\d{2}-\d{2}/g, '')
    .replace(/intitle:[\w-]+/g, '')
    .trim().toLowerCase();
  if (qClean) {
    const hay = [item.title, item.description, item.source].join(' ').toLowerCase();
    if (!hay.includes(qClean)) return false;
  }

  if (s.authors.length && !item.authors.some(a => s.authors.some(v => a.toLowerCase().includes(v.toLowerCase())))) return false;
  if (s.sources.length && !s.sources.some(v => (item.source || '').toLowerCase().includes(v.toLowerCase()))) return false;
  if (s.categories.length && !item.categories.some(c => s.categories.some(v => c.toLowerCase().includes(v.toLowerCase())))) return false;

  if (s.after  && !(item.date && item.date >= s.after))  return false;
  if (s.before && !(item.date && item.date <= s.before)) return false;
  return true;
}

/* ── Sort ── */
function msqSort(items, mode) {
  return items.slice().sort((a, b) => {
    if (mode === 'date_desc')    return (b.date    || '').localeCompare(a.date    || '');
    if (mode === 'date_asc')     return (a.date    || '').localeCompare(b.date    || '');
    if (mode === 'created_desc') return (b.created || '').localeCompare(a.created || '');
    if (mode === 'created_asc')  return (a.created || '').localeCompare(b.created || '');
    if (mode === 'title_asc')    return (a.title   || '').localeCompare(b.title   || '');
    if (mode === 'title_desc')   return (b.title   || '').localeCompare(a.title   || '');
    return 0;
  });
}

/* ── Format date ── */
function msqFmtDate(d) {
  if (!d) return '—';
  const dt = new Date(d);
  if (isNaN(dt)) return d;
  return dt.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
}

/* ── Render ── */
function msqRender(items) {
  const area  = document.getElementById('msqResults');
  const count = document.getElementById('msqCount');

  if (!items.length) {
    count.textContent = '0 results';
    area.innerHTML = `<div class="msq-empty">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      No results. Try broadening your filters.</div>`;
    return;
  }

  count.textContent = items.length + (items.length === 1 ? ' result' : ' results');
  const sorted = msqSort(items, document.getElementById('msqSort').value);

  area.innerHTML = `<div class="msq-cards">${sorted.map(it => `
    <article class="msq-card">
      <h3><a href="${it.url}">${it.title}</a></h3>
      <div class="msq-card-meta">
        ${it.source     ? `<span>📰 ${it.source}</span>` : ''}
        ${it.date       ? `<span>📅 ${msqFmtDate(it.date)}</span>` : ''}
        ${it.authors && it.authors.length ? `<span>✍️ ${it.authors.join(', ')}</span>` : ''}
        ${it.categories && it.categories.length ? `<span>${it.categories.map(c=>`<span class="msq-tag-pill">${c}</span>`).join('')}</span>` : ''}
      </div>
      ${it.description ? `<p class="msq-card-desc">${it.description}</p>` : ''}
    </article>`).join('')}
  </div>`;
}

/* ── Gather state ── */
function msqState() {
  const q   = document.getElementById('msqQ').value.trim();
  const ops = msqParseOps(q);
  const afterField  = document.getElementById('msqAfter').value.trim()  || null;
  const beforeField = document.getElementById('msqBefore').value.trim() || null;
  return {
    q,
    title:      document.getElementById('msqTitle').value.trim(),
    desc:       document.getElementById('msqDesc').value.trim(),
    authors:    msqTiAuthor.get(),
    sources:    msqTiSource.get(),
    categories: msqTiCat.get(),
    after:      afterField  || ops.after  || null,
    before:     beforeField || ops.before || null,
    intitle:    ops.intitle || null,
    sort:       document.getElementById('msqSort').value
  };
}

/* ── Run ── */
function msqRun() {
  const s = msqState();
  const results = MSQ_DATA.filter(d => msqMatches(d, s));
  msqRender(results);
  msqSyncURL(s);
}

/* ── URL sync ── */
function msqSyncURL(s) {
  const p = new URLSearchParams();
  if (s.q)                  p.set('q',          s.q);
  if (s.title)              p.set('title',       s.title);
  if (s.desc)               p.set('desc',        s.desc);
  if (s.authors.length)     p.set('authors',     s.authors.join('|'));
  if (s.sources.length)     p.set('sources',     s.sources.join('|'));
  if (s.categories.length)  p.set('categories',  s.categories.join('|'));
  if (s.after)              p.set('after',       s.after);
  if (s.before)             p.set('before',      s.before);
  if (s.intitle)            p.set('intitle',     s.intitle);
  p.set('sort', s.sort);
  history.replaceState({}, '', location.pathname + '?' + p.toString());
}

/* ── Restore from URL ── */
function msqRestoreURL() {
  const p = new URLSearchParams(location.search);
  if (p.get('q'))          document.getElementById('msqQ').value     = p.get('q');
  if (p.get('title'))      document.getElementById('msqTitle').value = p.get('title');
  if (p.get('desc'))       document.getElementById('msqDesc').value  = p.get('desc');
  if (p.get('after'))      document.getElementById('msqAfter').value = p.get('after');
  if (p.get('before'))     document.getElementById('msqBefore').value = p.get('before');
  if (p.get('sort'))       document.getElementById('msqSort').value  = p.get('sort');
  if (p.get('intitle')) {
    const v = p.get('intitle');
    const qEl = document.getElementById('msqQ');
    qEl.value = qEl.value ? qEl.value + ' intitle:' + v : 'intitle:' + v;
  }
  if (p.get('authors'))    p.get('authors').split('|').forEach(v    => msqTiAuthor.add(v));
  if (p.get('sources'))    p.get('sources').split('|').forEach(v    => msqTiSource.add(v));
  if (p.get('categories')) p.get('categories').split('|').forEach(v => msqTiCat.add(v));

  /* Auto-run if any param present */
  if ([...p.keys()].length > 0) msqRun();
}

/* ── Exports ── */
document.getElementById('msqExportJson').addEventListener('click', () => {
  const items = MSQ_DATA.filter(d => msqMatches(d, msqState()));
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(items, null, 2)], {type: 'application/json'}));
  a.download = 'metadata-results.json'; a.click();
});

document.getElementById('msqExportCsv').addEventListener('click', () => {
  const items = MSQ_DATA.filter(d => msqMatches(d, msqState()));
  const keys  = ['title','description','source','authors','categories','date','created','url'];
  const rows  = [keys.join(',')].concat(items.map(it =>
    keys.map(k => `"${String(it[k] || '').replace(/"/g, '""')}"`).join(',')));
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([rows.join('\n')], {type: 'text/csv'}));
  a.download = 'metadata-results.csv'; a.click();
});

/* ── Wire controls ── */
document.getElementById('msqRun').addEventListener('click', msqRun);
document.getElementById('msqQ').addEventListener('keydown',     e => { if (e.key === 'Enter') msqRun(); });
document.getElementById('msqTitle').addEventListener('keydown', e => { if (e.key === 'Enter') msqRun(); });
document.getElementById('msqDesc').addEventListener('keydown',  e => { if (e.key === 'Enter') msqRun(); });
document.getElementById('msqAfter').addEventListener('keydown', e => { if (e.key === 'Enter') msqRun(); });
document.getElementById('msqBefore').addEventListener('keydown',e => { if (e.key === 'Enter') msqRun(); });
document.getElementById('msqSort').addEventListener('change',   ()  => {
  if (document.querySelectorAll('.msq-card').length) msqRun();
});

document.getElementById('msqClear').addEventListener('click', () => {
  history.replaceState({}, '', location.pathname);
  location.reload();
});

/* ── Init ── */
msqRestoreURL();
</script>

<style>
/* ══════════════════════════════════════════════
   Media Sandbox Query — page-scoped styles
   Prefix: msq-
   Brighter variant of the Event Query (Sandbox8) design
   ══════════════════════════════════════════════ */

:root {
  --msq-blue:        #0077aa;   /* slightly brighter than #006699 */
  --msq-blue-hover:  #005f8e;
  --msq-blue-light:  #e0f2fa;
  --msq-blue-mid:    #b8dfef;
  --msq-blue-faint:  #f0f8fc;
  --msq-border:      #c8d6e0;
  --msq-bg:          #ffffff;
  --msq-surface:     #f4f8fb;
  --msq-text:        #1a2530;
  --msq-muted:       #4e6070;
  --msq-radius:      4px;
  --msq-radius-pill: 999px;
  --msq-trans:       150ms ease;
  --msq-shadow-sm:   0 1px 3px rgba(0,119,170,0.06);
  --msq-shadow-md:   0 4px 14px rgba(0,119,170,0.09);
}

*, *::before, *::after { box-sizing: border-box; }

/* ── Outer wrap ── */
.msq-wrap {
  width: 100%;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--msq-text);
}

/* ── Toolbar ── */
.msq-toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 0;
  border-bottom: 2px solid var(--msq-blue);
  margin-bottom: 1.1rem;
}

.msq-toolbar-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--msq-blue);
  margin-right: auto;
  letter-spacing: 0.01em;
}

.msq-btn {
  background: var(--msq-blue);
  color: #fff;
  border: none;
  padding: 0.42rem 1.05rem;
  border-radius: var(--msq-radius);
  cursor: pointer;
  font-size: 0.88rem;
  font-weight: 600;
  transition: background var(--msq-trans), box-shadow var(--msq-trans);
  box-shadow: var(--msq-shadow-sm);
}
.msq-btn:hover  { background: var(--msq-blue-hover); box-shadow: var(--msq-shadow-md); }
.msq-btn:focus-visible { outline: 2px solid var(--msq-blue); outline-offset: 2px; }

.msq-btn-ghost {
  background: var(--msq-bg);
  color: var(--msq-blue);
  border: 1px solid var(--msq-blue);
  padding: 0.38rem 0.9rem;
  border-radius: var(--msq-radius);
  cursor: pointer;
  font-size: 0.88rem;
  transition: background var(--msq-trans);
}
.msq-btn-ghost:hover { background: var(--msq-blue-light); }
.msq-btn-ghost:focus-visible { outline: 2px solid var(--msq-blue); outline-offset: 2px; }

/* ── Filter panel ── */
.msq-filters {
  background: var(--msq-surface);
  border: 1px solid var(--msq-border);
  border-radius: var(--msq-radius);
  padding: 0.85rem 1rem;
  margin-bottom: 1rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 0.8rem;
}

/* Wide field spans full row on larger screens */
.msq-field--wide {
  grid-column: 1 / -1;
}

.msq-field label {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--msq-muted);
  margin-bottom: 0.28rem;
}

.msq-hint {
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
  color: var(--msq-muted);
  font-size: 0.75rem;
  margin-left: 0.35rem;
}
.msq-hint code {
  background: var(--msq-blue-light);
  color: var(--msq-blue);
  padding: 0.05rem 0.3rem;
  border-radius: 3px;
  font-size: 0.72rem;
}

.msq-field input[type="text"],
.msq-field select {
  width: 100%;
  padding: 0.4rem 0.55rem;
  border: 1px solid var(--msq-border);
  border-radius: var(--msq-radius);
  font-size: 0.9rem;
  background: var(--msq-bg);
  color: var(--msq-text);
  transition: border-color var(--msq-trans), box-shadow var(--msq-trans);
}
.msq-field input[type="text"]:focus,
.msq-field select:focus {
  outline: none;
  border-color: var(--msq-blue);
  box-shadow: 0 0 0 3px rgba(0,119,170,0.14);
}

.msq-tag-tip {
  display: block;
  font-size: 0.74rem;
  color: var(--msq-muted);
  margin-top: 0.22rem;
}

/* ── Tag-chip container ── */
.msq-suggest-wrap { position: relative; }

.msq-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  padding: 0.3rem 0.45rem;
  border: 1px solid var(--msq-border);
  border-radius: var(--msq-radius);
  background: var(--msq-bg);
  min-height: 38px;
  align-items: center;
  cursor: text;
  transition: border-color var(--msq-trans), box-shadow var(--msq-trans);
}
.msq-tags:focus-within {
  border-color: var(--msq-blue);
  box-shadow: 0 0 0 3px rgba(0,119,170,0.14);
}

.msq-tags input {
  border: none;
  outline: none;
  padding: 0;
  font-size: 0.9rem;
  min-width: 110px;
  flex: 1;
  background: transparent;
  color: var(--msq-text);
}

.msq-chip {
  background: var(--msq-blue-light);
  border: 1px solid var(--msq-blue-mid);
  color: var(--msq-blue);
  border-radius: var(--msq-radius-pill);
  padding: 0.1rem 0.55rem;
  font-size: 0.82rem;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  animation: msqChipIn 0.15s ease;
}

@keyframes msqChipIn {
  from { opacity: 0; transform: scale(0.85); }
  to   { opacity: 1; transform: scale(1); }
}

.msq-chip button {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--msq-blue);
  font-size: 0.82rem;
  padding: 0;
  line-height: 1;
  transition: color var(--msq-trans);
}
.msq-chip button:hover { color: var(--msq-blue-hover); }

/* ── Suggestions dropdown ── */
.msq-suggest {
  display: none;
  position: absolute;
  top: 100%;
  left: 0; right: 0;
  z-index: 100;
  background: var(--msq-bg);
  border: 1px solid var(--msq-border);
  border-top: none;
  border-radius: 0 0 var(--msq-radius) var(--msq-radius);
  max-height: 168px;
  overflow-y: auto;
  box-shadow: var(--msq-shadow-md);
}
.msq-suggest button {
  display: block;
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  padding: 0.45rem 0.7rem;
  font-size: 0.88rem;
  cursor: pointer;
  color: var(--msq-text);
  transition: background var(--msq-trans), color var(--msq-trans);
}
.msq-suggest button:hover { background: var(--msq-blue-light); color: var(--msq-blue); }

/* ── Results bar ── */
.msq-results-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 0.7rem;
  font-size: 0.88rem;
  color: var(--msq-muted);
}

.msq-url-note {
  font-size: 0.78rem;
  color: var(--msq-muted);
  opacity: 0.8;
}

/* ── Cards grid ── */
.msq-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 0.8rem;
}

.msq-card {
  border: 1px solid var(--msq-border);
  border-top: 3px solid var(--msq-blue);
  border-radius: var(--msq-radius);
  padding: 0.8rem 1rem;
  background: var(--msq-bg);
  transition: box-shadow var(--msq-trans), transform var(--msq-trans);
}
.msq-card:hover {
  box-shadow: var(--msq-shadow-md);
  transform: translateY(-2px);
}

.msq-card h3 {
  margin: 0 0 0.4rem;
  font-size: 0.96rem;
  line-height: 1.3;
}
.msq-card h3 a {
  color: var(--msq-blue);
  text-decoration: none;
}
.msq-card h3 a:hover { text-decoration: underline; }

.msq-card-meta {
  display: flex;
  flex-direction: column;
  gap: 0.22rem;
  font-size: 0.82rem;
  color: var(--msq-muted);
  margin-bottom: 0.45rem;
}

.msq-card-desc {
  font-size: 0.86rem;
  color: var(--msq-muted);
  margin: 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* ── Tag pills on cards ── */
.msq-tag-pill {
  display: inline-block;
  background: var(--msq-blue-light);
  color: var(--msq-blue);
  border: 1px solid var(--msq-blue-mid);
  border-radius: var(--msq-radius-pill);
  padding: 0.08rem 0.48rem;
  font-size: 0.76rem;
  margin: 0.1rem 0.1rem 0.1rem 0;
}

/* ── Empty state ── */
.msq-empty {
  text-align: center;
  padding: 3rem 1rem;
  color: var(--msq-muted);
  font-size: 0.95rem;
  border: 1px solid var(--msq-border);
  border-radius: var(--msq-radius);
  background: var(--msq-surface);
}
.msq-empty svg {
  display: block;
  margin: 0 auto 0.8rem;
  opacity: 0.28;
  color: var(--msq-blue);
}

/* ── Mobile ── */
@media (max-width: 640px) {
  .msq-filters        { grid-template-columns: 1fr; padding: 0.7rem 0.75rem; }
  .msq-field--wide    { grid-column: 1; }
  .msq-cards          { grid-template-columns: 1fr; }
  .msq-card:hover     { transform: none; box-shadow: none; }
  .msq-toolbar        { gap: 0.4rem; }
  .msq-btn,
  .msq-btn-ghost      { padding: 0.42rem 0.75rem; font-size: 0.85rem; }
}
</style>
