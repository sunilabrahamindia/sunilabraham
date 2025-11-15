---
layout: default
title: Lobby
description: "Interactive photorealistic Indian–modern lobby — click the sofa, books, newspaper rack, coffee table and window to open details."
permalink: /lobby/
categories: [Project pages]
---

<style>
/* Interactive photorealistic lobby — responsive hotspot overlay.
   Uses a single background image and percentage-positioned hotspots.
   Accessible focus, keyboard support, no external libs.
*/

:root{
  --lobby-image: url("https://github.com/sunilabrahamindia/sunilabraham/blob/main/assets/images/TSAP%20Lobby.png?raw=true");
  --overlay-bg: rgba(0,0,0,0.5);
  --accent: #0b5ed7;
  --muted: #6b6b6b;
  --panel-bg: rgba(255,255,255,0.96);
  --radius: 12px;
}

.lobby-wrap{
  max-width:1100px;
  margin:1.4rem auto;
  padding:0.8rem;
  background:linear-gradient(180deg,#fffaf7 0%,#fffefc 100%);
  border-radius:14px;
  box-shadow:0 12px 36px rgba(10,10,10,0.06);
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color:#222;
}

/* Stage: image container */
.lobby-stage{
  position:relative;
  width:100%;
  /* maintain a 16:9-ish aspect ratio but allow height to adapt on small screens */
  padding-bottom:62%; /* controls height relative to width */
  border-radius:10px;
  overflow:hidden;
  background-image: var(--lobby-image);
  background-size:cover;
  background-position: center 35%;
  border:1px solid rgba(0,0,0,0.04);
}

/* overlay slight vignette for text readability */
.lobby-stage::after{
  content:'';
  position:absolute;
  inset:0;
  background:linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(0,0,0,0.06) 100%);
  pointer-events:none;
}

/* Hotspot button base */
.hotspot{
  position:absolute;
  border-radius:10px;
  background:rgba(255,255,255,0.8);
  padding:0.4rem 0.5rem;
  display:flex;
  gap:0.5rem;
  align-items:center;
  box-shadow:0 6px 18px rgba(10,10,10,0.12);
  border:1px solid rgba(0,0,0,0.06);
  cursor:pointer;
  transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
  min-width:48px;
  max-width:38%;
  font-size:0.95rem;
  color:#1f1f1f;
}

/* small icon circle inside hotspot */
.hotspot .dot{
  width:12px; height:12px; border-radius:999px;
  background:var(--accent); flex:0 0 12px;
  box-shadow:0 2px 6px rgba(11,94,215,0.18);
}

/* hover/focus */
.hotspot:hover, .hotspot:focus{
  transform: translateY(-6px);
  background:var(--panel-bg);
  outline:none;
}
.hotspot:focus { box-shadow:0 8px 26px rgba(11,94,215,0.16); }

/* hotspot label hidden on very small screens to avoid clutter */
@media (max-width:420px){
  .hotspot { font-size:0.85rem; padding:0.35rem 0.45rem; }
  .hotspot .label { display:none; }
}

/* Positions: percentages tuned to the generated image.
   When you replace image file, tweak these percentages if needed. */
.hs-sofa     { left:26%;  top:45%; transform:translate(-50%,-50%); }
.hs-cushion1 { left:36%;  top:44%; transform:translate(-50%,-50%); }
.hs-cushion2 { left:50%;  top:44%; transform:translate(-50%,-50%); }
.hs-cushion3 { left:64%;  top:44%; transform:translate(-50%,-50%); }
.hs-table    { left:48%;  top:58%; transform:translate(-50%,-50%); }
.hs-books    { left:84%;  top:34%; transform:translate(-50%,-50%); }
.hs-newspaper{ left:86%;  top:68%; transform:translate(-50%,-50%); }
.hs-window   { left:13%;  top:36%; transform:translate(-50%,-50%); }
.hs-plant    { left:9%;   top:66%; transform:translate(-50%,-50%); }

/* Side panel under the image in narrow screens */
.lobby-legend{
  margin-top:0.85rem;
  display:flex;
  gap:0.8rem;
  align-items:center;
  justify-content:space-between;
  flex-wrap:wrap;
}
.legend-left { display:flex; gap:0.6rem; align-items:center; }
.legend-right { color:var(--muted); font-size:0.92rem; }

/* modal (overlay) */
.lobby-modal-overlay{
  display:none;
  position:fixed;
  inset:0;
  background:var(--overlay-bg);
  z-index:2000;
  align-items:center;
  justify-content:center;
  padding:1rem;
}
.lobby-modal-overlay.active { display:flex; }

.lobby-modal{
  width:100%;
  max-width:640px;
  background:var(--panel-bg);
  border-radius:12px;
  padding:1.1rem 1.2rem;
  box-shadow:0 20px 60px rgba(10,10,10,0.22);
  text-align:left;
  border:1px solid rgba(0,0,0,0.06);
}
.lobby-modal h2{ margin:0 0 0.45rem 0; font-size:1.1rem; color:#4b2f25; }
.lobby-modal p{ margin:0 0 0.6rem 0; color:#333; line-height:1.45; }
.lobby-modal .actions{ display:flex; gap:0.5rem; justify-content:flex-end; margin-top:0.6rem; }
.lobby-modal .btn {
  background:var(--accent);
  color:#fff;
  border:0;
  padding:0.5rem 0.9rem;
  border-radius:8px;
  cursor:pointer;
  font-size:0.95rem;
}
.lobby-modal .btn.secondary {
  background:transparent; color:#333; border:1px solid rgba(0,0,0,0.06);
}

/* accessibility */
.hotspot:focus { outline-offset:4px; }

/* reduced motion honour */
@media (prefers-reduced-motion: reduce) {
  .hotspot, .lobby-modal { transition:none; transform:none; }
}
</style>

<div class="lobby-wrap" role="main" aria-labelledby="lobby-heading">
  <h1 id="lobby-heading" style="margin:0 0 0.6rem 0; font-size:1.3rem;">Lobby</h1>

  <div class="lobby-stage" role="region" aria-label="Interactive lobby image" tabindex="0">

    <!-- hotspots: use <button> for semantics and keyboard accessibility -->
    <button class="hotspot hs-sofa" data-title="Sit on the sofa" data-text="Have a comfortable seat. The sofa is perfect for reading or thinking." aria-label="Sofa - click to sit">
      <span class="dot" aria-hidden="true"></span><span class="label">Sofa</span>
    </button>

    <button class="hotspot hs-cushion1" data-title="Teal cushion" data-text="A teal cushion for calm focus." aria-label="Teal cushion">
      <span class="dot" aria-hidden="true"></span><span class="label">Cushion</span>
    </button>

    <button class="hotspot hs-cushion2" data-title="Coral cushion" data-text="A warm coral cushion for contrast." aria-label="Coral cushion">
      <span class="dot" aria-hidden="true"></span><span class="label">Cushion</span>
    </button>

    <button class="hotspot hs-cushion3" data-title="Gold cushion" data-text="A gold cushion that brightens the space." aria-label="Gold cushion">
      <span class="dot" aria-hidden="true"></span><span class="label">Cushion</span>
    </button>

    <button class="hotspot hs-table" data-title="Coffee table" data-text="A small coffee table. Click to open the featured publication." aria-label="Coffee table - featured item">
      <span class="dot" aria-hidden="true"></span><span class="label">Table</span>
    </button>

    <button class="hotspot hs-books" data-title="Bookshelf" data-text="Browse the publications, media articles and collections." aria-label="Bookshelf - click to open publications">
      <span class="dot" aria-hidden="true"></span><span class="label">Bookshelf</span>
    </button>

    <button class="hotspot hs-newspaper" data-title="Newspaper stand" data-text="Daily papers: The Hindu, Indian Express, Deccan Herald." aria-label="Newspaper stand">
      <span class="dot" aria-hidden="true"></span><span class="label">Newspapers</span>
    </button>

    <button class="hotspot hs-window" data-title="Window view" data-text="Open the window view and let your mind wander." aria-label="Window">
      <span class="dot" aria-hidden="true"></span><span class="label">Window</span>
    </button>

    <button class="hotspot hs-plant" data-title="Potted plant" data-text="A quiet plant keeping the room calm." aria-label="Plant">
      <span class="dot" aria-hidden="true"></span><span class="label">Plant</span>
    </button>

  </div> <!-- .lobby-stage -->

  <div class="lobby-legend" role="contentinfo" aria-hidden="false">
    <div class="legend-left">
      <div style="font-weight:600; color:#3e2b25;">Interactive lobby</div>
      <div style="color:var(--muted); font-size:0.95rem;">Click objects to open short notes or links.</div>
    </div>
  </div>

  {% include back-to-top.html %}
</div>

<!-- Modal overlay (appended in page; works with Jekyll) -->
<div id="lobbyModalOverlay" class="lobby-modal-overlay" aria-hidden="true">
  <div class="lobby-modal" role="dialog" aria-modal="true" aria-labelledby="modalHeading" aria-describedby="modalBody">
    <h2 id="modalHeading">Item</h2>
    <p id="modalBody">Details...</p>
    <div class="actions" style="margin-top:0.6rem; text-align:right;">
      <button class="btn secondary" id="modalOpenLink">Open</button>
      <button class="btn" id="modalCloseBtn">Close</button>
    </div>
  </div>
</div>

<script>
/* Interactive lobby hotspot JS
   - Uses percentage-positioned hotspots so they scale with background image
   - Keyboard accessible (Enter / Space)
   - Replaces placeholders with actual site routes if provided
*/

(function(){
  const overlay = document.getElementById('lobbyModalOverlay');
  const modal = overlay && overlay.querySelector('.lobby-modal');
  const titleEl = document.getElementById('modalHeading');
  const bodyEl = document.getElementById('modalBody');
  const openBtn = document.getElementById('modalOpenLink');
  const closeBtn = document.getElementById('modalCloseBtn');

  // mapping from hotspot -> link (change these later to real routes)
  const hotspotLinks = {
    'Sofa': '#',                 // replace with action or route
    'Cushion': '#',
    'Table': '/publications/',   // example: featured publications
    'Bookshelf': '/publications/',
    'Newspapers': 'https://www.thehindu.com/', // external; will open same tab — replace as needed
    'Window': '#',
    'Plant': '#'
  };

  function showModal(title, text, link){
    titleEl.textContent = title;
    bodyEl.textContent = text;
    // if link not provided or '#', keep Open button hidden/disabled
    if(!link || link === '#'){
      openBtn.style.display = 'none';
    } else {
      openBtn.style.display = 'inline-block';
      openBtn.onclick = function(){
        // navigate in same tab (no target="_blank")
        window.location.href = link;
      };
    }
    overlay.classList.add('active');
    overlay.setAttribute('aria-hidden','false');
    closeBtn.focus();
  }
  function closeModal(){
    overlay.classList.remove('active');
    overlay.setAttribute('aria-hidden','true');
    openBtn.onclick = null;
  }

  // close handlers
  closeBtn.addEventListener('click', closeModal);
  overlay.addEventListener('click', function(e){
    if(e.target === overlay) closeModal();
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape') closeModal();
  });

  // bind hotspots
  document.querySelectorAll('.lobby-stage .hotspot').forEach(function(btn){
    // read title/text from data attrs
    const title = btn.getAttribute('data-title') || 'Item';
    const text  = btn.getAttribute('data-text') || '';
    const label = btn.querySelector('.label') ? btn.querySelector('.label').textContent.trim() : title;
    const link  = hotspotLinks[label] || '#';

    function activate(e){
      e.preventDefault();
      showModal(title, text, link);
    }

    btn.addEventListener('click', activate);
    btn.addEventListener('keypress', function(e){
      if(e.key === 'Enter' || e.key === ' ') activate(e);
    });

    // ensure button is keyboard focusable
    if(!btn.hasAttribute('tabindex')) btn.setAttribute('tabindex', '0');
  });

})();
</script>
