---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

<!--
  Metadata Search - full file
  - Single column, mobile-first
  - Header texts are outside the container (left as normal text)
  - Container width: 90%
  - Authors/Sources/Categories: one input each; type + Enter to add tag
  - Advanced operators supported in main search: after:, before:, intitle:
  - CSV / JSON exports, Sort, URL-sync
  - Subtle animations on buttons and result cards
-->

<style>
:root{
  --bg: #ffffff;
  --page-bg: #fbfcfd;
  --card-bg: #f6f8fa;
  --text: #0f1720;
  --muted: #556072;
  --accent: #0b76ef;
  --accent-hover: #095fcc;
  --accent-contrast: #ffffff;
  --radius: 10px;
  --focus: 3px solid rgba(11,118,239,0.18);
  --trans: 180ms;
}

/* Page header (outside container) */
.page-info { max-width: 90%; margin: 1.25rem auto; color: var(--muted); font-size: 0.98rem; }
.page-info h1 { margin: 0 0 .25rem 0; color: var(--text); font-size: 1.4rem; }

/* Container */
.container { max-width: 90%; margin: .8rem auto 2rem; padding: 1rem; background: var(--bg); border-radius: var(--radius); border: 1px solid rgba(0,0,0,0.06); box-shadow: 0 6px 18px rgba(15,23,32,0.02); }

/* Forms */
.form-row { display:flex; flex-direction:column; gap:.4rem; margin-bottom:1rem; }
label { font-weight:600; font-size:.92rem; color:var(--text); }
input[type="text"], textarea, select { padding:.6rem .7rem; border-radius:8px; border:1px solid rgba(15,23,32,0.08); font-size:1rem; width:100%; box-sizing:border-box; }
textarea { min-height:84px; resize:vertical; }
input:focus, textarea:focus, select:focus { outline: var(--focus); }

/* Buttons */
.btn { background: linear-gradient(180deg,var(--accent),var(--accent-hover)); color: var(--accent-contrast); border:0; padding: .6rem .9rem; border-radius:8px; cursor:pointer; transition: transform var(--trans), box-shadow var(--trans); box-shadow: 0 6px 14px rgba(11,118,239,0.08); }
.btn:hover { transform: translateY(-2px); }
.btn-ghost { background: transparent; border:1px solid rgba(15,23,32,0.08); padding:.55rem .85rem; border-radius:8px; cursor:pointer; transition: background var(--trans); }
.btn-ghost:hover { background: rgba(15,23,32,0.03); }

/* Tags */
.tags-box { display:flex; flex-wrap:wrap; gap:.45rem; padding:.5rem; border-radius:8px; border:1px solid rgba(15,23,32,0.08); min-height:48px; align-items:center; }
.tag { background:var(--card-bg); padding:.28rem .6rem; border-radius:999px; font-size:.88rem; display:inline-flex; align-items:center; gap:.45rem; transition: transform var(--trans), opacity var(--trans); }
.tag button { background:transparent; border:0; cursor:pointer; font-size:0.95rem; color:var(--muted); padding:0; }
.tags-box input { border:0; padding:.35rem; outline:none; min-width:140px; font-size:1rem; }

/* Suggestions list */
.suggestions { position:relative; }
.suggestions-list { display:none; position:absolute; left:0; right:0; z-index:50; max-height:180px; overflow:auto; margin-top:.3rem; background:var(--bg); border:1px solid rgba(15,23,32,0.08); border-radius:8px; box-shadow: 0 6px 18px rgba(15,23,32,0.04); }
.suggestions-list button { display:block; width:100%; background:transparent; border:0; text-align:left; padding:.55rem .7rem; cursor:pointer; font-size:0.95rem; }
.suggestions-list button:hover { background: rgba(11,118,239,0.06); }

/* Results */
.results-meta { display:flex; justify-content:space-between; align-items:center; margin:1rem 0; color:var(--muted); font-size:0.95rem; }
#resultsArea { margin-top:1rem; display:grid; gap:0.9rem; }
.card { padding:0.9rem; border-radius:10px; border:1px solid rgba(15,23,32,0.06); background:var(--bg); transform-origin:center; transition: transform var(--trans), box-shadow var(--trans), opacity var(--trans); }
.card:hover { box-shadow: 0 10px 30px rgba(15,23,32,0.06); transform: translateY(-4px); }
.card h3 { margin:0 0 .35rem 0; font-size:1.05rem; }
.card .meta { font-size:0.88rem; color:var(--muted); display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:.45rem; }
.no-results { padding:2rem; color:var(--muted); text-align:center; }

/* Responsive */
@media (max-width:640px) {
  .page-info, .container { max-width:96%; }
  .card:hover { transform:none; box-shadow:none; }
}
</style>

<!-- header texts outside the container -->
<div class="page-info" aria-hidden="false">
  <h1>Metadata search</h1>
  <div>Page initially shows no results. Use filters or the search box and click Apply.</div>
  <div>Shareable query URL updates automatically.</div>
</div>

<!-- main panel -->
<div class="container" role="region" aria-label="Metadata search panel">

  <!-- Search -->
  <div class="form-row">
    <label for="q">Search (advanced operators supported: after:YYYY-MM-DD before:YYYY-MM-DD intitle:word)</label>
    <input id="q" type="text" placeholder="e.g. online safety intitle:privacy after:2018-01-01" aria-label="Search input" />
  </div>

  <!-- Title -->
  <div class="form-row">
    <label for="titleInput">Title contains</label>
    <input id="titleInput" type="text" placeholder="Words that appear in the title" />
  </div>

  <!-- Description -->
  <div class="form-row">
    <label for="descInput">Description contains</label>
    <textarea id="descInput" placeholder="Words that appear in the description"></textarea>
  </div>

  <!-- Author(s) tag input -->
  <div class="form-row">
    <label for="authorInput">Author(s)</label>
    <div class="suggestions">
      <div id="authorTags" class="tags-box" aria-live="polite" aria-atomic="true"></div>
      <input id="authorInput" type="text" placeholder="Type any part of name and press Enter" aria-label="Author input" />
      <div id="authorSuggest" class="suggestions-list" role="listbox" aria-label="Author suggestions"></div>
    </div>
    <div class="tag-instruction" style="font-size:.88rem;color:var(--muted)">Type any part of a name and press Enter. 'Sunil Abraham' appears first when present.</div>
  </div>

  <!-- Source tag input -->
  <div class="form-row">
    <label for="sourceInput">Source</label>
    <div class="suggestions">
      <div id="sourceTags" class="tags-box"></div>
      <input id="sourceInput" type="text" placeholder="Type source and press Enter" aria-label="Source input" />
      <div id="sourceSuggest" class="suggestions-list" role="listbox" aria-label="Source suggestions"></div>
    </div>
  </div>

  <!-- Category tag input -->
  <div class="form-row">
    <label for="catInput">Categories</label>
    <div class="suggestions">
      <div id="catTags" class="tags-box"></div>
      <input id="catInput" type="text" placeholder="Type category and press Enter" aria-label="Category input" />
      <div id="catSuggest" class="suggestions-list" role="listbox" aria-label="Category suggestions"></div>
    </div>
  </div>

  <!-- Date range -->
  <div class="form-row">
    <label for="after">After (YYYY-MM-DD)</label>
    <input id="after" type="text" placeholder="after:2015-01-01" />
  </div>

  <div class="form-row">
    <label for="before">Before (YYYY-MM-DD)</label>
    <input id="before" type="text" placeholder="before:2022-12-31" />
  </div>

  <!-- Sort -->
  <div class="form-row">
    <label for="sortSelect">Sort</label>
    <select id="sortSelect" aria-label="Sort results">
      <option value="date_desc">Date (newest)</option>
      <option value="date_asc">Date (oldest)</option>
      <option value="created_desc">Created (newest)</option>
      <option value="created_asc">Created (oldest)</option>
      <option value="title_asc">Title (A–Z)</option>
      <option value="title_desc">Title (Z–A)</option>
    </select>
  </div>

  <!-- Actions -->
  <div style="display:flex;gap:.6rem;flex-wrap:wrap;margin-top:.5rem">
    <button id="apply" class="btn" aria-label="Apply filters">Apply</button>
    <button id="clear" class="btn-ghost" aria-label="Clear all">Clear</button>
    <button id="exportCsv" class="btn-ghost" aria-label="Export CSV">Export CSV</button>
    <button id="exportJson" class="btn-ghost" aria-label="Export JSON">Export JSON</button>
  </div>

  <!-- Results summary -->
  <div class="results-meta" aria-live="polite">
    <div id="resultCount">0 results</div>
    <div>Filtered results</div>
  </div>

  <!-- Results -->
  <div id="resultsArea" aria-live="polite">
    <div class="no-results">No results yet — apply filters or search.</div>
  </div>

</div> <!-- /container -->

<script>
/* === Export DATA from Jekyll pages (Liquid) === */
const DATA = [
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

/* === Normalize arrays === */
DATA.forEach(d=>{
  if(typeof d.authors === 'string') d.authors = d.authors ? [d.authors] : [];
  if(typeof d.categories === 'string') d.categories = d.categories ? [d.categories] : [];
});

/* === Utilities === */
function uniq(arr){ return [...new Set((arr||[]).filter(Boolean))].sort(); }
const allAuthors = uniq(DATA.flatMap(d=>d.authors));
/* Put Sunil Abraham first if present */
if(allAuthors.includes('Sunil Abraham')) {
  const rest = allAuthors.filter(a=>a!=='Sunil Abraham');
  allAuthors.length = 0;
  allAuthors.push('Sunil Abraham', ...rest);
}
const allSources = uniq(DATA.map(d=>d.source));
const allCats = uniq(DATA.flatMap(d=>d.categories));

/* === Elements === */
const qEl = document.getElementById('q');
const titleEl = document.getElementById('titleInput');
const descEl = document.getElementById('descInput');
const authorTagsEl = document.getElementById('authorTags');
const authorInputEl = document.getElementById('authorInput');
const authorSuggestEl = document.getElementById('authorSuggest');
const sourceTagsEl = document.getElementById('sourceTags');
const sourceInputEl = document.getElementById('sourceInput');
const sourceSuggestEl = document.getElementById('sourceSuggest');
const catTagsEl = document.getElementById('catTags');
const catInputEl = document.getElementById('catInput');
const catSuggestEl = document.getElementById('catSuggest');
const afterEl = document.getElementById('after');
const beforeEl = document.getElementById('before');
const sortEl = document.getElementById('sortSelect');
const resultsArea = document.getElementById('resultsArea');
const resultCount = document.getElementById('resultCount');

/* === Tag input helper ===
   Single input box (type + Enter to add).
   suggestions list drawn from 'list' argument.
*/
function createTagInput(list, tagsContainer, inputEl, suggEl) {
  const state = { tags: [] };

  function renderTags() {
    tagsContainer.innerHTML = '';
    state.tags.forEach((t, i)=>{
      const span = document.createElement('span');
      span.className = 'tag';
      span.innerText = t;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Remove ' + t);
      btn.innerText = '✕';
      btn.addEventListener('click', ()=>{
        state.tags.splice(i,1);
        renderTags();
      });
      span.appendChild(btn);
      tagsContainer.appendChild(span);
    });
    // ensure an input focus exists visually inside tags container only for accessibility (we use main input)
  }

  function addTag(value) {
    if(!value) return;
    const trimmed = value.trim();
    if(!trimmed) return;
    if(!state.tags.includes(trimmed)) {
      state.tags.push(trimmed);
      renderTags();
    }
  }

  // suggestions logic
  function showSuggestions(q) {
    const ql = (q||'').toLowerCase();
    const candidates = list.filter(x => x.toLowerCase().includes(ql) && !state.tags.includes(x)).slice(0,25);
    if(candidates.length === 0) {
      suggEl.style.display = 'none';
      suggEl.innerHTML = '';
      return;
    }
    suggEl.innerHTML = '';
    candidates.forEach(c=>{
      const b = document.createElement('button');
      b.type = 'button';
      b.textContent = c;
      b.addEventListener('click', ()=>{ addTag(c); suggEl.style.display='none'; inputEl.value=''; runQuery(); });
      suggEl.appendChild(b);
    });
    suggEl.style.display = 'block';
  }

  function hideSuggestions() {
    suggEl.style.display = 'none';
  }

  // wire input: Enter adds tag, input shows suggestions
  inputEl.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter') {
      e.preventDefault();
      const v = inputEl.value.trim();
      if(v) addTag(v);
      inputEl.value = '';
      hideSuggestions();
      runQuery();
    } else if(e.key === 'Escape') {
      inputEl.value = '';
      hideSuggestions();
    }
  });
  inputEl.addEventListener('input', ()=> {
    if(inputEl.value.trim().length === 0) { hideSuggestions(); return; }
    showSuggestions(inputEl.value);
  });
  inputEl.addEventListener('blur', ()=> { setTimeout(hideSuggestions, 120); });

  renderTags();
  return {
    addTag,
    getTags: ()=>state.tags.slice()
  };
}

/* init tag inputs */
const authorsInput = createTagInput(allAuthors, authorTagsEl, authorInputEl, authorSuggestEl);
const sourcesInput = createTagInput(allSources, sourceTagsEl, sourceInputEl, sourceSuggestEl);
const catsInput = createTagInput(allCats, catTagsEl, catInputEl, catSuggestEl);

/* === Operator parsing for main search box === */
function parseOperators(q) {
  const afterMatch = q.match(/after:(\d{4}-\d{2}-\d{2})/);
  const beforeMatch = q.match(/before:(\d{4}-\d{2}-\d{2})/);
  const intitleMatch = q.match(/intitle:([\w-]+)/);
  return {
    after: afterMatch ? afterMatch[1] : null,
    before: beforeMatch ? beforeMatch[1] : null,
    intitle: intitleMatch ? intitleMatch[1] : null
  };
}

/* === Matching logic === */
function itemMatches(item, state) {
  // Title filter (contains)
  if(state.title && !(item.title && item.title.toLowerCase().includes(state.title.toLowerCase()))) return false;

  // Description
  if(state.desc && !(item.description && item.description.toLowerCase().includes(state.desc.toLowerCase()))) return false;

  // Main q cleaned (strip operators)
  const qClean = (state.q||'').replace(/after:\d{4}-\d{2}-\d{2}/g,'').replace(/before:\d{4}-\d{2}-\d{2}/g,'').replace(/intitle:[\w-]+/g,'').trim().toLowerCase();
  if(qClean) {
    const hay = [item.title, item.description, item.source].join(' ').toLowerCase();
    if(!hay.includes(qClean)) return false;
  }

  // intitle operator
  if(state.intitle && !(item.title && item.title.toLowerCase().includes(state.intitle.toLowerCase()))) return false;

  // Authors: allow partial case-insensitive matches; if user supplied multiple, match if any author in item matches any provided tag
  if(state.authors && state.authors.length) {
    if(!item.authors.some(a => state.authors.some(s => a.toLowerCase().includes(s.toLowerCase())))) return false;
  }

  // Sources: partial match
  if(state.sources && state.sources.length) {
    if(!state.sources.some(s => (item.source||'').toLowerCase().includes(s.toLowerCase()))) return false;
  }

  // Categories: partial match
  if(state.categories && state.categories.length) {
    if(!item.categories.some(c => state.categories.some(s => c.toLowerCase().includes(s.toLowerCase())))) return false;
  }

  // Date range
  if(state.after) { if(!(item.date && item.date >= state.after)) return false; }
  if(state.before) { if(!(item.date && item.date <= state.before)) return false; }

  return true;
}

/* === Sorting === */
function sortResults(list, mode) {
  const copy = list.slice();
  copy.sort((a,b)=>{
    if(mode === 'date_desc') return (b.date||'').localeCompare(a.date||'');
    if(mode === 'date_asc') return (a.date||'').localeCompare(b.date||'');
    if(mode === 'created_desc') return (b.created||'').localeCompare(a.created||'');
    if(mode === 'created_asc') return (a.created||'').localeCompare(b.created||'');
    if(mode === 'title_asc') return (a.title||'').localeCompare(b.title||'');
    if(mode === 'title_desc') return (b.title||'').localeCompare(a.title||'');
    return 0;
  });
  return copy;
}

/* === Render results === */
function renderResults(items) {
  resultsArea.innerHTML = '';
  if(!items || items.length === 0) {
    resultsArea.innerHTML = '<div class="no-results">No results. Please broaden filters or clear them.</div>';
    resultCount.textContent = '0 results';
    return;
  }
  resultCount.textContent = items.length + (items.length === 1 ? ' result' : ' results');
  const list = sortResults(items, sortEl.value);
  list.forEach(it => {
    const c = document.createElement('article');
    c.className = 'card';
    c.innerHTML = `
      <h3><a href="${it.url}">${it.title}</a></h3>
      <div class="meta"><div>${it.source || '-'}</div><div>${(it.authors||[]).join(', ')}</div><div>${it.date || '-'}</div></div>
      <p>${it.description || ''}</p>
    `;
    resultsArea.appendChild(c);
  });
}

/* === Gather state === */
function gatherStateFromUI() {
  const s = {
    q: qEl.value.trim(),
    title: titleEl.value.trim(),
    desc: descEl.value.trim(),
    authors: authorsInput.getTags(),
    sources: sourcesInput.getTags(),
    categories: catsInput.getTags(),
    after: afterEl.value.trim() || null,
    before: beforeEl.value.trim() || null,
    intitle: null
  };
  const ops = parseOperators(s.q);
  s.after = s.after || ops.after;
  s.before = s.before || ops.before;
  s.intitle = ops.intitle || null;
  return s;
}

/* === Run query === */
function runQuery() {
  const state = gatherStateFromUI();
  const results = DATA.filter(d => itemMatches(d, state));
  renderResults(results);
  updateURL(state);
}

/* === Exports === */
function exportJson() {
  const state = gatherStateFromUI();
  const items = DATA.filter(d => itemMatches(d, state));
  const blob = new Blob([JSON.stringify(items, null, 2)], { type: 'application/json' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'metadata-results.json'; a.click();
}
function exportCsv() {
  const state = gatherStateFromUI();
  const items = DATA.filter(d => itemMatches(d, state));
  const keys = ['title','description','source','authors','categories','date','created','url'];
  const rows = [keys.join(',')].concat(items.map(it => keys.map(k => `"${String(it[k]||'').replace(/"/g,'""')}"`).join(',')));
  const blob = new Blob([rows.join('\n')], { type: 'text/csv' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'metadata-results.csv'; a.click();
}

/* === URL sync === */
function updateURL(state) {
  const params = new URLSearchParams();
  if(state.q) params.set('q', state.q);
  if(state.title) params.set('title', state.title);
  if(state.desc) params.set('desc', state.desc);
  if(state.authors && state.authors.length) params.set('authors', state.authors.join('|'));
  if(state.sources && state.sources.length) params.set('sources', state.sources.join('|'));
  if(state.categories && state.categories.length) params.set('categories', state.categories.join('|'));
  if(state.after) params.set('after', state.after);
  if(state.before) params.set('before', state.before);
  if(state.intitle) params.set('intitle', state.intitle);
  params.set('sort', sortEl.value);
  history.replaceState({}, '', location.pathname + '?' + params.toString());
}
function restoreFromURL() {
  const p = new URLSearchParams(location.search);
  if(p.get('q')) qEl.value = p.get('q');
  if(p.get('title')) titleEl.value = p.get('title');
  if(p.get('desc')) descEl.value = p.get('desc');
  if(p.get('after')) afterEl.value = p.get('after');
  if(p.get('before')) beforeEl.value = p.get('before');
  if(p.get('intitle')) {
    const val = p.get('intitle');
    qEl.value = qEl.value ? qEl.value + ' intitle:' + val : 'intitle:' + val;
  }
  if(p.get('authors')) p.get('authors').split('|').forEach(a => authorsInput.addTag(a));
  if(p.get('sources')) p.get('sources').split('|').forEach(s => sourcesInput.addTag(s));
  if(p.get('categories')) p.get('categories').split('|').forEach(c => catsInput.addTag(c));
  if(p.get('sort')) sortEl.value = p.get('sort');
}

/* === Wire controls === */
document.getElementById('apply').addEventListener('click', runQuery);
document.getElementById('clear').addEventListener('click', ()=>{
  qEl.value = ''; titleEl.value = ''; descEl.value = ''; afterEl.value = ''; beforeEl.value = ''; sortEl.value = 'date_desc';
  // reload page to reset tag internal state; simpler than manipulating internals
  history.replaceState({}, '', location.pathname);
  location.reload();
});
document.getElementById('exportJson').addEventListener('click', exportJson);
document.getElementById('exportCsv').addEventListener('click', exportCsv);
sortEl.addEventListener('change', ()=> {
  // If results are visible, re-run to reorder
  const current = document.getElementById('resultsArea').querySelectorAll('.card').length;
  if(current) runQuery();
});

/* === Initialise (do not auto-run query) === */
restoreFromURL(); // populate fields and tags from URL but do not auto-run (per your request)

/* End of script */
</script>
