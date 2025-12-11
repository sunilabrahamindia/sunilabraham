---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

<!--
  Simplified Metadata Search — single-column, mobile-friendly
  - No visual query builder
  - Advanced operators: after:, before:, intitle:
  - Title, description, author, source, categories: text + suggestion dropdowns
  - Authors/sources/categories: multi-tag input (type + Enter or choose from suggestions)
  - Single-column layout; initial state shows no results
-->

<style>
:root{
  --bg: #ffffff;
  --page-bg: #fbfcfd;
  --card-bg: #f6f8fa;
  --text: #0f1720;
  --muted: #556072;
  --accent: #0b76ef;
  --accent-contrast: #ffffff;
  --radius: 10px;
  --focus: 3px solid rgba(11,118,239,0.18);
}

body { background: var(--page-bg); color: var(--text); font-family: system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial; }
.container{max-width:820px;margin:1.5rem auto;padding:1rem}
.panel{background:var(--bg);border-radius:12px;padding:1rem;border:1px solid rgba(15,23,32,0.06);box-shadow:0 1px 0 rgba(15,23,32,0.02)}
.heading{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-bottom:1rem}
h1{font-size:1.25rem;margin:0}
.note{color:var(--muted);font-size:.95rem}
.form-row{display:flex;flex-direction:column;gap:.4rem;margin-bottom:.9rem}
label{font-weight:600;font-size:.9rem}
input[type="text"], textarea, .select-like{padding:.6rem .7rem;border-radius:8px;border:1px solid rgba(15,23,32,0.06);font-size:1rem}
textarea{min-height:84px}
.actions{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.6rem}
.btn{background:var(--accent);color:var(--accent-contrast);border:0;padding:.55rem .75rem;border-radius:8px;cursor:pointer}
.btn-ghost{background:transparent;border:1px solid rgba(15,23,32,0.06);padding:.45rem .6rem;border-radius:8px;cursor:pointer}
.small{font-size:.9rem;color:var(--muted)}

/* Tags input */
.tags{display:flex;flex-wrap:wrap;gap:.4rem;padding:.35rem;border-radius:8px;border:1px solid rgba(15,23,32,0.06);min-height:44px;align-items:center}
.tag{background:var(--card-bg);padding:.25rem .5rem;border-radius:999px;font-size:.9rem;display:inline-flex;align-items:center;gap:.4rem}
.tag button{background:transparent;border:0;cursor:pointer}
.tags input{border:0;outline:none;padding:.4rem;min-width:120px}

/* Suggestions dropdown */
.suggestions{position:relative}
.suggestions-list{position:absolute;left:0;right:0;z-index:40;background:var(--bg);border:1px solid rgba(15,23,32,0.06);border-radius:6px;margin-top:.25rem;max-height:200px;overflow:auto}
.suggestions-list button{width:100%;text-align:left;padding:.45rem .6rem;border:0;background:transparent;cursor:pointer}
.suggestions-list button:hover{background:rgba(11,118,239,0.04)}

/* Results */
.results-meta{display:flex;justify-content:space-between;align-items:center;margin:1rem 0}
.results-area{display:grid;gap:.9rem}
.card{padding:.9rem;border-radius:10px;background:var(--bg);border:1px solid rgba(15,23,32,0.04)}
.card h3{margin:0 0 .3rem 0}
.meta{font-size:.88rem;color:var(--muted);display:flex;gap:1rem;flex-wrap:wrap}
.no-results{padding:2rem;text-align:center;color:var(--muted)}

@media (max-width:600px){
  .container{padding:.75rem}
  .heading{flex-direction:column;align-items:flex-start;gap:.5rem}
}
</style>

<div class="container">
  <div class="panel">
    <div class="heading">
      <div>
        <h1>Metadata search</h1>
        <div class="note">Page initially shows no results. Use filters or the search box and click Apply.</div>
      </div>
      <div class="small">Shareable query URL updates automatically</div>
    </div>

    <!-- Search and filters: single column -->
    <div class="form-row">
      <label for="q">Search (advanced operators: after:YYYY-MM-DD before:YYYY-MM-DD intitle:word)</label>
      <input id="q" type="text" placeholder="e.g. online shaming intitle:shaming after:2015-01-01" aria-label="Search" />
    </div>

    <div class="form-row">
      <label for="titleInput">Title (contains words)</label>
      <input id="titleInput" type="text" placeholder="Any words in title" />
    </div>

    <div class="form-row">
      <label for="descInput">Description (contains words)</label>
      <textarea id="descInput" placeholder="Any words in description"></textarea>
    </div>

    <div class="form-row">
      <label>Author(s)</label>
      <div class="suggestions">
        <div id="authorTags" class="tags" aria-live="polite"></div>
        <div style="margin-top:.5rem;">
          <input id="authorInput" type="text" placeholder="Type name and press Enter or choose from suggestions" aria-label="Author input" />
        </div>
        <div id="authorSuggest" class="suggestions-list" style="display:none"></div>
      </div>
      <div class="small">Sunil Abraham appears first in suggestions when present.</div>
    </div>

    <div class="form-row">
      <label>Source</label>
      <div class="suggestions">
        <div id="sourceTags" class="tags"></div>
        <div style="margin-top:.5rem"><input id="sourceInput" type="text" placeholder="Type source and press Enter or choose" /></div>
        <div id="sourceSuggest" class="suggestions-list" style="display:none"></div>
      </div>
    </div>

    <div class="form-row">
      <label>Categories</label>
      <div class="suggestions">
        <div id="catTags" class="tags"></div>
        <div style="margin-top:.5rem"><input id="catInput" type="text" placeholder="Type category and press Enter or choose" /></div>
        <div id="catSuggest" class="suggestions-list" style="display:none"></div>
      </div>
    </div>

    <div class="form-row">
      <label for="after">After (YYYY-MM-DD)</label>
      <input id="after" type="text" placeholder="after:YYYY-MM-DD" />
    </div>
    <div class="form-row">
      <label for="before">Before (YYYY-MM-DD)</label>
      <input id="before" type="text" placeholder="before:YYYY-MM-DD" />
    </div>

    <div class="form-row">
      <label for="sortSelect">Sort</label>
      <select id="sortSelect" class="select-like">
        <option value="date_desc">Date (newest)</option>
        <option value="date_asc">Date (oldest)</option>
        <option value="created_desc">Created (newest)</option>
        <option value="created_asc">Created (oldest)</option>
        <option value="title_asc">Title (A–Z)</option>
        <option value="title_desc">Title (Z–A)</option>
      </select>
    </div>

    <div class="actions">
      <button id="apply" class="btn">Apply</button>
      <button id="clear" class="btn-ghost">Clear</button>
      <button id="exportCsv" class="btn-ghost">Export CSV</button>
      <button id="exportJson" class="btn-ghost">Export JSON</button>
    </div>
  </div>

  <div class="results-meta">
    <div id="resultCount">0 results</div>
    <div class="small">Results reflect currently applied filters</div>
  </div>

  <div id="resultsArea" class="results-area">
    <div class="no-results">No results yet — please apply filters or a search.</div>
  </div>
</div>

<script>
// === Data exported from Liquid ===
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

// Normalise arrays
DATA.forEach(d=>{
  if(typeof d.authors === 'string') d.authors = d.authors ? [d.authors] : [];
  if(typeof d.categories === 'string') d.categories = d.categories ? [d.categories] : [];
});

// Utility
function uniq(arr){ return [...new Set(arr.filter(Boolean))].sort(); }
const allAuthors = uniq(DATA.flatMap(d=>d.authors));
if(allAuthors.includes('Sunil Abraham')){
  const others = allAuthors.filter(a=>a!=='Sunil Abraham');
  allAuthors.length = 0; allAuthors.push('Sunil Abraham', ...others);
}
const allSources = uniq(DATA.map(d=>d.source));
const allCats = uniq(DATA.flatMap(d=>d.categories));

// Elements
const qEl = document.getElementById('q');
const titleEl = document.getElementById('titleInput');
const descEl = document.getElementById('descInput');
const afterEl = document.getElementById('after');
const beforeEl = document.getElementById('before');
const sortEl = document.getElementById('sortSelect');
const resultsArea = document.getElementById('resultsArea');
const resultCount = document.getElementById('resultCount');

// Tag input builder (simple, accessible)
function setupTagInput(list, tagsId, inputId, suggId){
  const tagsEl = document.getElementById(tagsId);
  const inputBase = document.getElementById(inputId);
  const suggEl = document.getElementById(suggId);
  const state = { tags: [] };

  function renderTags(){
    tagsEl.innerHTML = '';
    state.tags.forEach((t, idx)=>{
      const span = document.createElement('span'); span.className = 'tag';
      const btn = document.createElement('button'); btn.type='button'; btn.setAttribute('aria-label','Remove '+t); btn.textContent = '✕';
      btn.addEventListener('click', ()=>{ state.tags.splice(idx,1); renderTags(); });
      span.appendChild(document.createTextNode(t));
      span.appendChild(btn);
      tagsEl.appendChild(span);
    });
    // attach small input inside tags container for flow and focus
    const inEl = document.createElement('input');
    inEl.placeholder = 'Add...';
    inEl.addEventListener('keydown', e=>{
      const v = inEl.value.trim();
      if(e.key === 'Enter' && v){ e.preventDefault(); addTag(v); inEl.value=''; hideSuggestions(); runQuery(); }
      if(e.key === 'Backspace' && !v && state.tags.length){ state.tags.pop(); renderTags(); runQuery(); }
    });
    inEl.addEventListener('input', ()=> showSuggestions(inEl.value));
    tagsEl.appendChild(inEl);
    inEl.focus();
  }

  function addTag(v){ if(!v) return; if(!state.tags.includes(v)) state.tags.push(v); renderTags(); }
  function showSuggestions(q){
    const ql = (q||'').toLowerCase();
    const candidates = list.filter(x=> x.toLowerCase().includes(ql) && !state.tags.includes(x)).slice(0,20);
    if(candidates.length===0){ suggEl.style.display='none'; return; }
    suggEl.innerHTML = ''; suggEl.style.display='block';
    candidates.forEach(c=>{ const b = document.createElement('button'); b.type='button'; b.textContent = c; b.addEventListener('click', ()=>{ addTag(c); hideSuggestions(); runQuery(); }); suggEl.appendChild(b); });
  }
  function hideSuggestions(){ suggEl.style.display = 'none'; }
  function getTags(){ return state.tags.slice(); }

  // initialise: if the visible inputBase (outside) is used to paste or seed tags
  inputBase.addEventListener('keydown', e=>{
    if(e.key === 'Enter'){ e.preventDefault(); const v = inputBase.value.trim(); if(v){ addTag(v); inputBase.value=''; runQuery(); hideSuggestions(); } }
  });
  inputBase.addEventListener('input', ()=> showSuggestions(inputBase.value));

  // allow programmatic adding (for URL restore)
  function addTagProgrammatic(t){ if(!state.tags.includes(t)) state.tags.push(t); renderTags(); }

  renderTags();
  return { getTags, addTag: addTagProgrammatic };
}

// Initialise tag UIs
const authorsInput = setupTagInput(allAuthors, 'authorTags', 'authorInput', 'authorSuggest');
const sourcesInput = setupTagInput(allSources, 'sourceTags', 'sourceInput', 'sourceSuggest');
const catsInput = setupTagInput(allCats, 'catTags', 'catInput', 'catSuggest');

// Operators parsing (search box)
function parseOperators(q){
  const afterMatch = q.match(/after:(\d{4}-\d{2}-\d{2})/);
  const beforeMatch = q.match(/before:(\d{4}-\d{2}-\d{2})/);
  const intitleMatch = q.match(/intitle:([\\w-]+)/);
  return { after: afterMatch ? afterMatch[1] : null, before: beforeMatch ? beforeMatch[1] : null, intitle: intitleMatch ? intitleMatch[1] : null };
}

// Matching
function itemMatches(item, state){
  // title and description fields
  if(state.title && !(item.title && item.title.toLowerCase().includes(state.title.toLowerCase()))) return false;
  if(state.desc && !(item.description && item.description.toLowerCase().includes(state.desc.toLowerCase()))) return false;

  // q basic (remove operators)
  const qClean = (state.q||'').replace(/after:\d{4}-\d{2}-\d{2}/g,'').replace(/before:\d{4}-\d{2}-\d{2}/g,'').replace(/intitle:[\\w-]+/g,'').trim().toLowerCase();
  if(qClean){
    const hay = [item.title, item.description, item.source].join(' ').toLowerCase();
    if(!hay.includes(qClean)) return false;
  }

  // intitle operator
  if(state.intitle && !(item.title && item.title.toLowerCase().includes(state.intitle.toLowerCase()))) return false;

  // authors (partial match allowed)
  if(state.authors.length){
    if(!item.authors.some(a=> state.authors.some(s=> a.toLowerCase().includes(s.toLowerCase())))) return false;
  }
  // sources
  if(state.sources.length){
    if(!state.sources.some(s=> (item.source||'').toLowerCase().includes(s.toLowerCase()))) return false;
  }
  // categories
  if(state.categories.length){
    if(!item.categories.some(c=> state.categories.some(s=> c.toLowerCase().includes(s.toLowerCase())))) return false;
  }

  // date range
  if(state.after){ if(!(item.date && item.date >= state.after)) return false; }
  if(state.before){ if(!(item.date && item.date <= state.before)) return false; }

  return true;
}

// Sorting
function sortResults(list, mode){
  const copy = list.slice();
  copy.sort((a,b)=>{
    if(mode==='date_desc') return (b.date||'').localeCompare(a.date||'');
    if(mode==='date_asc') return (a.date||'').localeCompare(b.date||'');
    if(mode==='created_desc') return (b.created||'').localeCompare(a.created||'');
    if(mode==='created_asc') return (a.created||'').localeCompare(b.created||'');
    if(mode==='title_asc') return (a.title||'').localeCompare(b.title||'');
    if(mode==='title_desc') return (b.title||'').localeCompare(a.title||'');
    return 0;
  });
  return copy;
}

// Render
function renderResults(items){
  resultsArea.innerHTML = '';
  if(items.length === 0){
    resultsArea.innerHTML = '<div class="no-results">No results. Please broaden filters or clear them.</div>';
    resultCount.textContent = '0 results';
    return;
  }
  resultCount.textContent = items.length + (items.length===1 ? ' result' : ' results');
  const list = sortResults(items, sortEl.value);
  list.forEach(it=>{
    const el = document.createElement('div'); el.className = 'card';
    el.innerHTML = `<h3><a href="${it.url}">${it.title}</a></h3>
      <div class="meta"><div>${it.source||'-'}</div><div>${(it.authors||[]).join(', ')}</div><div>${it.date||'-'}</div></div>
      <p>${it.description||''}</p>`;
    resultsArea.appendChild(el);
  });
}

// Gather state
function gatherState(){
  const s = { q: qEl.value.trim(), title: titleEl.value.trim(), desc: descEl.value.trim(),
    authors: authorsInput.getTags(), sources: sourcesInput.getTags(), categories: catsInput.getTags(),
    after: afterEl.value.trim() || null, before: beforeEl.value.trim() || null, intitle: null };
  const ops = parseOperators(s.q);
  s.after = s.after || ops.after; s.before = s.before || ops.before; s.intitle = ops.intitle || null;
  return s;
}

// Run query
function runQuery(){
  const state = gatherState();
  const results = DATA.filter(d => itemMatches(d, state));
  renderResults(results);
  updateURL(state);
}

// Export
function exportJson(){ const items = DATA.filter(d => itemMatches(d, gatherState())); const blob = new Blob([JSON.stringify(items,null,2)], {type:'application/json'}); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'metadata-results.json'; a.click(); }
function exportCsv(){ const items = DATA.filter(d => itemMatches(d, gatherState())); const keys = ['title','description','source','authors','categories','date','created','url']; const rows = [keys.join(',')].concat(items.map(it=> keys.map(k=>`"${String(it[k]||'').replace(/"/g,'""')}"`).join(','))); const blob = new Blob([rows.join('\\n')], {type:'text/csv'}); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'metadata-results.csv'; a.click(); }

// URL sync
function updateURL(state){
  const params = new URLSearchParams();
  if(state.q) params.set('q', state.q);
  if(state.title) params.set('title', state.title);
  if(state.desc) params.set('desc', state.desc);
  if(state.authors.length) params.set('authors', state.authors.join('|'));
  if(state.sources.length) params.set('sources', state.sources.join('|'));
  if(state.categories.length) params.set('categories', state.categories.join('|'));
  if(state.after) params.set('after', state.after);
  if(state.before) params.set('before', state.before);
  if(state.intitle) params.set('intitle', state.intitle);
  params.set('sort', sortEl.value);
  history.replaceState({}, '', location.pathname + '?' + params.toString());
}

function restoreFromURL(){
  const p = new URLSearchParams(location.search);
  if(p.get('q')) qEl.value = p.get('q');
  if(p.get('title')) titleEl.value = p.get('title');
  if(p.get('desc')) descEl.value = p.get('desc');
  if(p.get('after')) afterEl.value = p.get('after');
  if(p.get('before')) beforeEl.value = p.get('before');
  if(p.get('intitle')) { const val = p.get('intitle'); qEl.value = qEl.value ? qEl.value + ' intitle:'+val : 'intitle:'+val; }
  if(p.get('authors')) p.get('authors').split('|').forEach(a => authorsInput.addTag(a));
  if(p.get('sources')) p.get('sources').split('|').forEach(s => sourcesInput.addTag(s));
  if(p.get('categories')) p.get('categories').split('|').forEach(c => catsInput.addTag(c));
  if(p.get('sort')) sortEl.value = p.get('sort');
}

// Controls
document.getElementById('apply').addEventListener('click', runQuery);
document.getElementById('clear').addEventListener('click', ()=>{ qEl.value=''; titleEl.value=''; descEl.value=''; afterEl.value=''; beforeEl.value=''; sortEl.value='date_desc'; history.replaceState({}, '', location.pathname); location.reload(); });
document.getElementById('exportJson').addEventListener('click', exportJson);
document.getElementById('exportCsv').addEventListener('click', exportCsv);

// Initialise: do not auto-run — page must show no results initially
restoreFromURL();
</script>
