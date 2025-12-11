---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

<!--
  Metadata Search — polished single-file prototype
  - Uses site pages metadata exported as JSON by Liquid
  - Features: filter chips, visual query builder, CSV/JSON export,
    sort controls, live URL sync, advanced Google-style operators
  - Accessibility-friendly controls, keyboard operable
  - Styling keeps to site tokens (use your :root variables in main stylesheet)
-->

<style>
:root{
  --bg: #ffffff;
  --page-bg: #fbfcfd;
  --card-bg: #f6f8fa;
  --text: #0f1720;
  --muted: #5b6b76;
  --accent: #0b76ef;
  --accent-contrast: #ffffff;
  --success: #0a8a5f;
  --danger: #c23d3d;
  --focus: 3px solid rgba(11,118,239,0.18);
  --radius: 10px;
}

/* Layout */
.metadata-wrap{max-width:1100px;margin:2rem auto;padding:1rem}
.header-row{display:flex;gap:1rem;align-items:center;justify-content:space-between;margin-bottom:1rem}
.header-row h1{margin:0;font-size:1.35rem}
.controls-grid{display:grid;grid-template-columns:1fr 320px;gap:1rem}
.panel{background:var(--card-bg);border-radius:var(--radius);padding:1rem;border:1px solid rgba(15,23,32,0.06)}

/* Search input */
.search-input{display:flex;gap:.5rem;align-items:center}
.search-input input[type="text"]{flex:1;padding:.6rem .8rem;border-radius:8px;border:1px solid rgba(15,23,32,0.08);font-size:1rem}
.search-input button{background:var(--accent);color:var(--accent-contrast);border:0;padding:.5rem .7rem;border-radius:8px;cursor:pointer}
.search-input input[type="text"]:focus{outline:var(--focus)}

/* Filters */
.filters{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem}
.filter-select{display:flex;flex-direction:column;gap:.4rem}
.filter-select label{font-size:.85rem;color:var(--muted)}
.select{padding:.45rem .6rem;border-radius:8px;border:1px solid rgba(15,23,32,0.06);min-width:160px}

/* Chips */
.chips{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.5rem}
.chip{background:white;border:1px solid rgba(15,23,32,0.06);padding:.35rem .6rem;border-radius:999px;font-size:.85rem;cursor:pointer}
.chip.selected{background:var(--accent);color:var(--accent-contrast);border-color:transparent}
.chip:focus{outline:var(--focus)}

/* Results */
.results-meta{display:flex;align-items:center;gap:1rem;justify-content:space-between;margin:1rem 0}
.results-list{display:grid;grid-template-columns:1fr;gap:0.9rem}
.card{background:var(--bg);border-radius:8px;padding:1rem;border:1px solid rgba(15,23,32,0.05)}
.card h3{margin:0 0 .4rem 0}
.meta-row{font-size:.88rem;color:var(--muted);display:flex;gap:1rem;flex-wrap:wrap}
.no-results{padding:2rem;text-align:center;color:var(--muted)}

/* Visual query builder */
.query-builder{margin-top:1rem;background:linear-gradient(180deg, rgba(11,118,239,0.03), transparent);padding:.75rem;border-radius:8px}
.q-row{display:flex;gap:.5rem;align-items:center;margin-bottom:.5rem}
.q-row select,.q-row input{padding:.4rem .5rem;border-radius:6px;border:1px solid rgba(15,23,32,0.06)}
.q-row .op{min-width:130px}
.btn-ghost{background:transparent;border:1px solid rgba(15,23,32,0.06);padding:.4rem .5rem;border-radius:6px;cursor:pointer}

/* Responsive */
@media (max-width:880px){
  .controls-grid{grid-template-columns:1fr}
}
</style>

<div class="metadata-wrap">
  <div class="header-row">
    <h1>Metadata search &ndash; interactive</h1>
    <div style="font-size:.9rem;color:var(--muted)">No results yet — adjust filters or type a search</div>
  </div>

  <div class="controls-grid">
    <div class="panel">
      <div class="search-input" role="search">
        <input id="q" type="text" placeholder="Search title, description or use advanced operators (after:YYYY-MM-DD before:YYYY-MM-DD intitle:word)" aria-label="Search" />
        <button id="clearBtn" title="Clear search">Clear</button>
        <button id="applyBtn" title="Apply filters">Apply</button>
      </div>

      <div class="filters" aria-hidden="false">
        <div class="filter-select">
          <label for="authorSelect">Author</label>
          <select id="authorSelect" class="select" multiple size="5" aria-label="Filter by author"></select>
        </div>

        <div class="filter-select">
          <label for="sourceSelect">Source</label>
          <select id="sourceSelect" class="select" multiple size="5" aria-label="Filter by source"></select>
        </div>

        <div class="filter-select">
          <label for="categorySelect">Category</label>
          <select id="categorySelect" class="select" multiple size="5" aria-label="Filter by category"></select>
        </div>

        <div class="filter-select">
          <label for="yearSelect">Year</label>
          <select id="yearSelect" class="select" multiple size="5" aria-label="Filter by year"></select>
        </div>
      </div>

      <div style="margin-top:.8rem;display:flex;gap:.5rem;align-items:center;flex-wrap:wrap">
        <div style="font-size:.85rem;color:var(--muted)">Active chips:</div>
        <div id="chips" class="chips" aria-live="polite"></div>
      </div>

      <div class="query-builder" aria-label="Visual query builder">
        <div style="font-weight:600;margin-bottom:.5rem">Visual query builder</div>
        <div id="builderRows"></div>
        <div style="display:flex;gap:.5rem;margin-top:.5rem">
          <button id="addRow" class="btn-ghost">Add condition</button>
          <button id="runBuilder" class="btn-ghost">Run</button>
          <button id="clearBuilder" class="btn-ghost">Clear</button>
        </div>
        <div style="font-size:.85rem;color:var(--muted);margin-top:.5rem">Example: Author = "Sunil Abraham" AND (Category = "Media mentions" OR year > 2020)</div>
      </div>

    </div>

    <div class="panel">
      <div style="display:flex;justify-content:space-between;align-items:center">
        <div>
          <label for="sortSelect" style="font-size:.9rem;color:var(--muted)">Sort</label><br>
          <select id="sortSelect" class="select" aria-label="Sort results">
            <option value="date_desc">Date (newest)</option>
            <option value="date_asc">Date (oldest)</option>
            <option value="created_desc">Created (newest)</option>
            <option value="created_asc">Created (oldest)</option>
            <option value="title_asc">Title (A–Z)</option>
            <option value="title_desc">Title (Z–A)</option>
          </select>
        </div>

        <div>
          <div style="display:flex;flex-direction:column;gap:.5rem">
            <button id="exportCsv" class="btn-ghost">Export CSV</button>
            <button id="exportJson" class="btn-ghost">Export JSON</button>
          </div>
        </div>
      </div>

      <hr style="margin:1rem 0;opacity:.6" />

      <div style="font-weight:600;margin-bottom:.5rem">Google-style quick options</div>
      <div style="font-size:.9rem;color:var(--muted);margin-bottom:.5rem">Use these to build advanced operators like after:YYYY-MM-DD before:YYYY-MM-DD intitle:word</div>
      <div style="display:flex;gap:.5rem;flex-direction:column">
        <input id="after" placeholder="after:YYYY-MM-DD" class="select" />
        <input id="before" placeholder="before:YYYY-MM-DD" class="select" />
        <input id="intitle" placeholder="intitle:word" class="select" />
      </div>

      <div style="margin-top:1rem;color:var(--muted);font-size:.9rem">Shareable URL will update as you change filters.</div>
    </div>
  </div>

  <div class="results-meta">
    <div id="resultCount">0 results</div>
    <div style="font-size:.9rem;color:var(--muted)">Export / share the current query</div>
  </div>

  <div id="resultsArea" class="results-list" role="region" aria-live="polite">
    <div class="no-results">No results yet — try typing a query or enabling filters.</div>
  </div>
</div>


<script>
// --- STEP 1: export site metadata into DATA using Liquid ---
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

// Normalize arrays
DATA.forEach(d=>{
  if(typeof d.authors === 'string') d.authors = d.authors ? [d.authors] : [];
  if(typeof d.categories === 'string') d.categories = d.categories ? [d.categories] : [];
});

// Utilities
function uniq(arr){return [...new Set(arr.filter(Boolean))].sort();}
function yearsFrom(data){return uniq(data.map(x=>x.date && x.date.substring(0,4)).filter(Boolean))}

// Populate selects
function populate(selectId, values){
  const s = document.getElementById(selectId);
  values.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;s.appendChild(o)});
}
populate('authorSelect', uniq(DATA.flatMap(d=>d.authors)));
populate('sourceSelect', uniq(DATA.map(d=>d.source)));
populate('categorySelect', uniq(DATA.flatMap(d=>d.categories)));
populate('yearSelect', yearsFrom(DATA));

// State
let STATE = {
  q: '',
  authors: [],
  sources: [],
  categories: [],
  years: [],
  after: null,
  before: null,
  intitle: null,
  sort: 'date_desc',
  builder: [] // visual builder rows
};

// Elements
const qEl = document.getElementById('q');
const chipsEl = document.getElementById('chips');
const resultsArea = document.getElementById('resultsArea');
const resultCount = document.getElementById('resultCount');
const authorSelect = document.getElementById('authorSelect');
const sourceSelect = document.getElementById('sourceSelect');
const categorySelect = document.getElementById('categorySelect');
const yearSelect = document.getElementById('yearSelect');
const afterEl = document.getElementById('after');
const beforeEl = document.getElementById('before');
const intitleEl = document.getElementById('intitle');
const sortSelect = document.getElementById('sortSelect');

// Helper: read selected values from multi-select
function selectedValues(select){return [...select.selectedOptions].map(o=>o.value)}

// Build chips UI
function refreshChips(){
  chipsEl.innerHTML = '';
  const pairs = [
    ['Author', STATE.authors],
    ['Source', STATE.sources],
    ['Category', STATE.categories],
    ['Year', STATE.years]
  ];
  pairs.forEach(([label, arr])=>{
    arr.forEach(v=>{
      const c = document.createElement('button');
      c.className='chip selected';
      c.textContent = label+': '+v;
      c.setAttribute('aria-label','Remove filter '+label+': '+v);
      c.addEventListener('click',()=>{ removeChip(label, v) });
      chipsEl.appendChild(c);
    });
  });
}
function removeChip(label, value){
  if(label==='Author') STATE.authors = STATE.authors.filter(x=>x!==value);
  if(label==='Source') STATE.sources = STATE.sources.filter(x=>x!==value);
  if(label==='Category') STATE.categories = STATE.categories.filter(x=>x!==value);
  if(label==='Year') STATE.years = STATE.years.filter(x=>x!==value);
  syncSelects();
  runQuery();
}

function syncSelects(){
  // set selected options based on STATE
  function set(select, arr){for(let i=0;i<select.options.length;i++){select.options[i].selected = arr.includes(select.options[i].value)}}
  set(authorSelect, STATE.authors);
  set(sourceSelect, STATE.sources);
  set(categorySelect, STATE.categories);
  set(yearSelect, STATE.years);
}

// Advanced operators parsing from q
function parseOperators(q){
  const afterMatch = q.match(/after:(\d{4}-\d{2}-\d{2})/);
  const beforeMatch = q.match(/before:(\d{4}-\d{2}-\d{2})/);
  const intitleMatch = q.match(/intitle:([\w-]+)/);
  return {
    after: afterMatch ? afterMatch[1] : null,
    before: beforeMatch ? beforeMatch[1] : null,
    intitle: intitleMatch ? intitleMatch[1] : null
n  };
}

// Core matching logic
function matchItem(item){
  // text match (excluding operators)
  const q = STATE.q.replace(/after:\d{4}-\d{2}-\d{2}/g,'').replace(/before:\d{4}-\d{2}-\d{2}/g,'').replace(/intitle:[\w-]+/g,'').trim().toLowerCase();
  const inText = !q || [item.title, item.description, (item.source||'')].join(' ').toLowerCase().includes(q);
  if(!inText) return false;

  // intitle
  if(STATE.intitle && !(item.title && item.title.toLowerCase().includes(STATE.intitle.toLowerCase()))) return false;

  // authors
  if(STATE.authors.length && !item.authors.some(a=>STATE.authors.includes(a))) return false;
  // sources
  if(STATE.sources.length && !STATE.sources.includes(item.source)) return false;
  // categories
  if(STATE.categories.length && !item.categories.some(c=>STATE.categories.includes(c))) return false;
  // years
  if(STATE.years.length){ const y = item.date && item.date.substring(0,4); if(!STATE.years.includes(y)) return false }

  // date range
  if(STATE.after){ if(!(item.date && item.date >= STATE.after)) return false }
  if(STATE.before){ if(!(item.date && item.date <= STATE.before)) return false }

  // Visual builder (if present) - evaluate rows with simple boolean logic (AND across rows)
  for(const row of STATE.builder){
    if(!evalBuilderRow(row, item)) return false;
  }

  return true;
}

function evalBuilderRow(row, item){
  // row: {field, op, value}
  const f = row.field;
  const v = row.value;
  if(f==='Author') return item.authors.some(a=>compare(a, row.op, v));
  if(f==='Source') return compare(item.source, row.op, v);
  if(f==='Category') return item.categories.some(c=>compare(c, row.op, v));
  if(f==='Year') return compare(item.date && item.date.substring(0,4), row.op, v);
  if(f==='Title') return compare(item.title, row.op, v);
  return true;
}
function compare(a, op, b){ if(a==null) return false; a = String(a); b = String(b); switch(op){ case 'contains': return a.toLowerCase().includes(b.toLowerCase()); case 'equals': return a.toLowerCase()===b.toLowerCase(); case 'gt': return a>b; case 'lt': return a<b; default: return false }}

// Run query and render
function runQuery(){
  // parse operators
  const ops = parseOperators(STATE.q);
  STATE.after = afterEl.value || ops.after;
  STATE.before = beforeEl.value || ops.before;
  STATE.intitle = intitleEl.value || ops.intitle;

  // filter data
  const results = DATA.filter(matchItem);

  // sort
  results.sort((a,b)=>{
    const s = STATE.sort;
    if(s==='date_desc') return (b.date||'').localeCompare(a.date||'');
    if(s==='date_asc') return (a.date||'').localeCompare(b.date||'');
    if(s==='created_desc') return (b.created||'').localeCompare(a.created||'');
    if(s==='created_asc') return (a.created||'').localeCompare(b.created||'');
    if(s==='title_asc') return (a.title||'').localeCompare(b.title||'');
    if(s==='title_desc') return (b.title||'').localeCompare(a.title||'');
    return 0;
  });

  renderResults(results);
  updateURL();
}

function renderResults(items){
  resultsArea.innerHTML = '';
  if(items.length===0){
    resultsArea.innerHTML = '<div class="no-results">No results. Try clearing filters or broadening your query.</div>';
    resultCount.textContent = '0 results';
    return;
  }
  resultCount.textContent = items.length + (items.length===1 ? ' result' : ' results');
  items.forEach(it=>{
    const div = document.createElement('article'); div.className='card';
    div.innerHTML = `<h3><a href='${it.url}'>${it.title}</a></h3>
      <div class='meta-row'>
        <div>${it.source || '-'} </div>
        <div>${(it.authors||[]).join(', ')}</div>
        <div>${it.date || '-'}</div>
      </div>
      <p>${it.description || ''}</p>`;
    resultsArea.appendChild(div);
  });
}

// URL sync
function updateURL(){
  const params = new URLSearchParams();
  if(STATE.q) params.set('q', STATE.q);
  if(STATE.authors.length) params.set('authors', STATE.authors.join('|'));
  if(STATE.sources.length) params.set('sources', STATE.sources.join('|'));
  if(STATE.categories.length) params.set('categories', STATE.categories.join('|'));
  if(STATE.years.length) params.set('years', STATE.years.join('|'));
  if(STATE.after) params.set('after', STATE.after);
  if(STATE.before) params.set('before', STATE.before);
  if(STATE.intitle) params.set('intitle', STATE.intitle);
  if(STATE.sort) params.set('sort', STATE.sort);
  history.replaceState({}, '', location.pathname + '?' + params.toString());
}
function restoreFromURL(){
  const params = new URLSearchParams(location.search);
  STATE.q = params.get('q') || '';
  STATE.authors = params.get('authors') ? params.get('authors').split('|') : [];
  STATE.sources = params.get('sources') ? params.get('sources').split('|') : [];
  STATE.categories = params.get('categories') ? params.get('categories').split('|') : [];
  STATE.years = params.get('years') ? params.get('years').split('|') : [];
  STATE.after = params.get('after');
  STATE.before = params.get('before');
  STATE.intitle = params.get('intitle');
  STATE.sort = params.get('sort') || STATE.sort;

  // set UI
  qEl.value = STATE.q;
  afterEl.value = STATE.after || '';
  beforeEl.value = STATE.before || '';
  intitleEl.value = STATE.intitle || '';
  sortSelect.value = STATE.sort;
  syncSelects();
}

// Exports
function exportJson(){
  const items = DATA.filter(matchItem);
  const blob = new Blob([JSON.stringify(items, null, 2)], {type:'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href=url; a.download='metadata-results.json'; document.body.appendChild(a); a.click(); a.remove();
}
function exportCsv(){
  const items = DATA.filter(matchItem);
  const keys = ['title','description','source','authors','categories','date','created','url'];
  const rows = [keys.join(',')].concat(items.map(it=>keys.map(k=>`"${String(it[k]||'').replace(/"/g,'""')}"`).join(',')));
  const blob = new Blob([rows.join('\n')], {type:'text/csv'});
  const url = URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='metadata-results.csv'; document.body.appendChild(a); a.click(); a.remove();
}

// Visual query builder UI
const builderRowsEl = document.getElementById('builderRows');
function addBuilderRow(row){
  const r = row || {field:'Author',op:'contains',value:''};
  STATE.builder.push(r);
  renderBuilder();
}
function renderBuilder(){
  builderRowsEl.innerHTML = '';
  STATE.builder.forEach((r, idx)=>{
    const row = document.createElement('div'); row.className='q-row';
    // field
    const f = document.createElement('select'); ['Author','Source','Category','Year','Title'].forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v; if(v===r.field) o.selected=true; f.appendChild(o)});
    // op
    const op = document.createElement('select'); op.className='op'; [['contains','contains'],['equals','equals'],['>','gt'],['<','lt']].forEach(([val,label])=>{const o=document.createElement('option');o.value=val; o.textContent=label; if(val===r.op) o.selected=true; op.appendChild(o)});
    const val = document.createElement('input'); val.value=r.value; val.placeholder='Value';
    const del = document.createElement('button'); del.className='btn-ghost'; del.textContent='Delete'; del.addEventListener('click',()=>{ STATE.builder.splice(idx,1); renderBuilder(); runQuery(); });
    // wire
    f.addEventListener('change',()=>{ r.field=f.value });
    op.addEventListener('change',()=>{ r.op=op.value });
    val.addEventListener('input',()=>{ r.value=val.value });
    row.appendChild(f); row.appendChild(op); row.appendChild(val); row.appendChild(del);
    builderRowsEl.appendChild(row);
  });
}

// Events
document.getElementById('applyBtn').addEventListener('click',()=>{ STATE.q = qEl.value; STATE.authors = selectedValues(authorSelect); STATE.sources = selectedValues(sourceSelect); STATE.categories = selectedValues(categorySelect); STATE.years = selectedValues(yearSelect); STATE.sort = sortSelect.value; refreshChips(); runQuery(); });
document.getElementById('clearBtn').addEventListener('click',()=>{ qEl.value=''; authorSelect.selectedIndex=-1; sourceSelect.selectedIndex=-1; categorySelect.selectedIndex=-1; yearSelect.selectedIndex=-1; afterEl.value=''; beforeEl.value=''; intitleEl.value=''; STATE = {q:'',authors:[],sources:[],categories:[],years:[],after:null,before:null,intitle:null,sort:'date_desc',builder:[]}; renderBuilder(); refreshChips(); runQuery(); });
[authorSelect,sourceSelect,categorySelect,yearSelect].forEach(s=>s.addEventListener('change',()=>{ STATE.authors = selectedValues(authorSelect); STATE.sources = selectedValues(sourceSelect); STATE.categories = selectedValues(categorySelect); STATE.years = selectedValues(yearSelect); refreshChips(); runQuery(); }));
sortSelect.addEventListener('change',()=>{ STATE.sort = sortSelect.value; runQuery(); });
afterEl.addEventListener('change',()=>{ STATE.after = afterEl.value; runQuery(); });
beforeEl.addEventListener('change',()=>{ STATE.before = beforeEl.value; runQuery(); });
intitleEl.addEventListener('change',()=>{ STATE.intitle = intitleEl.value; runQuery(); });

document.getElementById('exportJson').addEventListener('click',exportJson);
document.getElementById('exportCsv').addEventListener('click',exportCsv);

// builder buttons
document.getElementById('addRow').addEventListener('click',()=>addBuilderRow());
document.getElementById('runBuilder').addEventListener('click',()=>runQuery());
document.getElementById('clearBuilder').addEventListener('click',()=>{ STATE.builder=[]; renderBuilder(); runQuery(); });

// init
restoreFromURL(); renderBuilder(); refreshChips(); if(STATE.q||STATE.authors.length||STATE.sources.length||STATE.categories.length||STATE.years.length) runQuery();

</script>
