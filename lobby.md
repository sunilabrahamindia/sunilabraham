---
layout: default
title: Lobby
description: "Interactive Indian–Modern drawing room lobby — click objects to explore: sofa, books, coffee table, bookshelf, newspaper rack, plant and window."
permalink: /lobby/
categories: [Project pages]
---

<style>
/* Interactive Lobby — Jekyll-friendly inline styles
   Indian–Modern palette, responsive, accessible.
   System fonts only; no external assets. */

.lobby {
  max-width: 1100px;
  margin: 1.4rem auto;
  padding: 1rem;
  background: linear-gradient(180deg,#fff9f3 0%,#fffefc 100%);
  border-radius: 12px;
  box-shadow: 0 12px 36px rgba(10,10,10,0.06);
  color:#212121;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
}

/* grid layout: canvas left, quick links right on wide screens */
.lobby-grid {
  display:grid;
  grid-template-columns: 1fr 320px;
  gap:1rem;
  align-items:start;
}

/* canvas container */
.scene {
  background: linear-gradient(180deg, rgba(255,250,246,0.9), rgba(255,255,255,0.6));
  border-radius: 10px;
  padding: 0.8rem;
  border:1px solid rgba(0,0,0,0.03);
  min-height:380px;
}

/* side panel small cards */
.side-card {
  background:#fff;
  border-radius:10px;
  padding:0.7rem;
  border:1px solid rgba(0,0,0,0.035);
  box-shadow:0 6px 14px rgba(10,10,10,0.03);
}
.side-card h3 { margin:0 0 0.4rem 0; font-size:1rem; }
.side-card p { margin:0; color:#444; font-size:0.95rem; }

/* small pill links */
.pills { display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.6rem; }
.pill {
  background: rgba(6, 110, 117, 0.06);
  color:#066e73;
  padding:0.45rem 0.7rem;
  border-radius:999px;
  text-decoration:none;
  border:1px solid rgba(6,110,117,0.08);
  font-size:0.9rem;
}

/* interactive focus */
svg a:focus, .pill:focus { outline:3px solid rgba(6,110,117,0.16); outline-offset:3px; border-radius:6px; }

/* modal/overlay */
.lobby-overlay {
  position: fixed;
  inset:0;
  background: rgba(0,0,0,0.45);
  display:none;
  align-items:center;
  justify-content:center;
  z-index:1000;
  padding:1rem;
}
.lobby-overlay.active { display:flex; }

.lobby-modal {
  background:#fff;
  border-radius:10px;
  padding:1.1rem 1.2rem;
  max-width:520px;
  width:100%;
  box-shadow:0 18px 60px rgba(10,10,10,0.18);
  text-align:left;
}
.lobby-modal h2 { margin:0 0 0.4rem 0; color:#5b3b2e; font-size:1.15rem; }
.lobby-modal p { margin:0 0 0.6rem 0; color:#333; line-height:1.45; }
.lobby-modal .btn {
  background:#c17f4a;
  color:white;
  border:none;
  padding:0.5rem 0.85rem;
  border-radius:8px;
  cursor:pointer;
  font-size:0.95rem;
}
.lobby-modal .btn:focus { outline:3px solid rgba(11,94,215,0.14); }

/* small helpful hint under scene */
.scene-caption { margin-top:0.6rem; color:#444; font-size:0.95rem; }

/* responsive */
@media (max-width:920px){
  .lobby-grid { grid-template-columns: 1fr; }
  .side-card { order:2; }
  .scene { order:1; }
}

/* micro animations for interactive SVG (class names used inside SVG) */
.interactive { cursor:pointer; transition:transform 180ms ease, opacity 180ms ease; }
.interactive:hover { transform: translateY(-4px); }

/* cushion lift */
.cushion { transition: transform 160ms ease, box-shadow 160ms ease; }
.cushion:focus, .cushion:hover { transform: translateY(-6px) scale(1.02); filter:brightness(1.03); }

/* book hover */
.book { transition: transform 160ms ease, opacity 160ms ease; }
.book:hover, .book:focus { transform: translateY(-6px) scale(1.02); opacity:0.95; }

/* newspaper slide */
.newspaper { transition: transform 160ms ease; }
.newspaper:hover { transform: translateX(6px); }

/* subtle plant wiggle via inline animation classes (JS toggles a class for reduced-motion support) */
.leaf-wiggle { animation: leafW 3s ease-in-out infinite; transform-origin:center bottom; }
@keyframes leafW { 0%,100%{ transform:rotate(0deg);} 25%{ transform:rotate(3deg);} 75%{ transform:rotate(-3deg);} }

/* respectful reduced motion fallback */
@media (prefers-reduced-motion: reduce){
  .leaf-wiggle, .interactive, .book, .cushion { animation:none; transition:none; transform:none; }
}
</style>

<div class="lobby" role="main" aria-labelledby="lobby-heading">

  <div class="lobby-grid">

    <!-- LEFT: SVG Scene -->
    <div class="scene" role="region" aria-label="Drawing room lobby scene">

      <!-- Inline SVG: everything clickable inside; links are placeholders '#' -->
      <svg viewBox="0 0 1200 760" width="100%" height="auto" aria-labelledby="svgTitle svgDesc" role="img" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">

        <title id="svgTitle">Interactive drawing room lobby</title>
        <desc id="svgDesc">A warm Indian–modern room illustration. Click the sofa to sit, click books to open items, click newspapers and table for details.</desc>

        <!-- wall -->
        <rect x="0" y="0" width="1200" height="430" rx="0" fill="#fff7f1"/>

        <!-- subtle wall texture band -->
        <rect x="40" y="24" width="1120" height="6" rx="3" fill="#f0e0d3" opacity="0.6" />

        <!-- floor -->
        <rect x="0" y="430" width="1200" height="330" fill="#efe2d6" />

        <!-- window (clickable) -->
        <g class="interactive window" tabindex="0" role="button" aria-label="Window - click to look out" transform="translate(82,48)">
          <rect x="0" y="0" width="260" height="200" rx="10" fill="#e8f7f5" stroke="#d7edea" stroke-width="3"/>
          <rect x="12" y="12" width="236" height="86" rx="6" fill="#ddf3f2"/>
          <rect x="12" y="108" width="110" height="80" rx="6" fill="#dff3f2"/>
          <rect x="138" y="108" width="110" height="80" rx="6" fill="#dff3f2"/>
          <!-- glow -->
          <rect x="-6" y="-6" width="272" height="212" rx="14" fill="url(#windowGlow)" opacity="0.06" />
        </g>

        <!-- potted plant left -->
        <g transform="translate(40,360)" aria-hidden="false">
          <ellipse cx="52" cy="90" rx="46" ry="12" fill="#d8b89a" opacity="0.9"/>
          <rect x="24" y="40" width="56" height="68" rx="8" fill="#b98653"/>
          <g class="leaf-group" transform="translate(10,10)">
            <ellipse class="leaf leaf-wiggle" cx="44" cy="30" rx="18" ry="40" fill="#3b8b5a" opacity="0.95" />
            <ellipse class="leaf leaf-wiggle" cx="24" cy="10" rx="14" ry="30" fill="#2f8b57" opacity="0.95" />
            <ellipse class="leaf leaf-wiggle" cx="64" cy="10" rx="14" ry="30" fill="#2f8b57" opacity="0.95" />
          </g>
        </g>

        <!-- framed art -->
        <g class="interactive frame" tabindex="0" role="button" aria-label="Wall art - click to read" transform="translate(360,44)">
          <rect x="0" y="0" width="280" height="140" rx="10" fill="#fff6f0" stroke="#e8dccf" />
          <rect x="16" y="14" width="248" height="112" rx="6" fill="#f6e4d6"/>
          <circle cx="140" cy="66" r="22" fill="#c07d47"/>
          <text x="30" y="106" font-size="12" fill="#684033" style="font-family: sans-serif;">Sunil Abraham Project</text>
        </g>

        <!-- bookshelf (right side) -->
        <g transform="translate(880,140)" aria-hidden="false">
          <rect x="0" y="0" width="260" height="360" rx="10" fill="#f7efe6" stroke="#e5d6c5"/>
          <!-- shelves -->
          <rect x="12" y="22" width="236" height="6" fill="#d8bca3"/>
          <rect x="12" y="112" width="236" height="6" fill="#d8bca3"/>
          <rect x="12" y="202" width="236" height="6" fill="#d8bca3"/>
          <rect x="12" y="292" width="236" height="6" fill="#d8bca3"/>
          <!-- book blocks (each wrapped in <a> so clickable) -->
          <a href="#" class="book" tabindex="0" aria-label="Open Publications">
            <rect x="26" y="32" width="28" height="64" rx="2" fill="#0b5ed7"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open Media articles">
            <rect x="64" y="32" width="22" height="64" rx="2" fill="#e08a3f"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open Ayrookuzhiel collection">
            <rect x="92" y="32" width="18" height="64" rx="2" fill="#8aa24c"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open Biography">
            <rect x="118" y="32" width="22" height="64" rx="2" fill="#6a4a3a"/>
          </a>

          <a href="#" class="book" tabindex="0" aria-label="Open more">
            <rect x="26" y="122" width="42" height="60" rx="2" fill="#c79a6a"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open archives">
            <rect x="76" y="122" width="32" height="60" rx="2" fill="#f3c27b"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open essays">
            <rect x="116" y="122" width="28" height="60" rx="2" fill="#0b5ed7"/>
          </a>

          <a href="#" class="book" tabindex="0" aria-label="Open reports">
            <rect x="26" y="212" width="32" height="64" rx="2" fill="#6a4a3a"/>
          </a>
          <a href="#" class="book" tabindex="0" aria-label="Open commentaries">
            <rect x="68" y="212" width="28" height="64" rx="2" fill="#ff8c42"/>
          </a>
        </g>

        <!-- rug (centre) -->
        <g transform="translate(200,440)" aria-hidden="true">
          <ellipse cx="400" cy="110" rx="300" ry="96" fill="#f9e9de" stroke="#ead6c7" />
          <ellipse cx="400" cy="110" rx="230" ry="68" fill="#fff4ea" />
        </g>

        <!-- sofa (centre) - clickable as a whole; cushions individually clickable -->
        <g class="interactive" id="sofa" tabindex="0" role="button" aria-label="Sofa - click to sit" transform="translate(180,320)">
          <!-- shadow -->
          <ellipse cx="360" cy="200" rx="250" ry="34" fill="rgba(0,0,0,0.08)"/>
          <!-- seat base -->
          <rect x="70" y="78" width="580" height="110" rx="28" fill="#e9f5f3" stroke="#dbeeea" />
          <!-- back -->
          <rect x="86" y="22" width="552" height="76" rx="22" fill="#0e7c74" />
          <!-- arms -->
          <rect x="28" y="70" width="44" height="130" rx="20" fill="#d9efe9"/>
          <rect x="666" y="70" width="44" height="130" rx="20" fill="#d9efe9"/>
        </g>

        <!-- cushions (separate, clickable) -->
        <g transform="translate(180,320)">
          <a href="#" class="cushion" tabindex="0" role="button" aria-label="Cushion Teal">
            <rect x="160" y="80" width="86" height="64" rx="12" fill="#0fb09e"/>
          </a>
          <a href="#" class="cushion" tabindex="0" role="button" aria-label="Cushion Coral">
            <rect x="300" y="80" width="86" height="64" rx="12" fill="#ff7058"/>
          </a>
          <a href="#" class="cushion" tabindex="0" role="button" aria-label="Cushion Gold">
            <rect x="440" y="80" width="86" height="64" rx="12" fill="#d8a84a"/>
          </a>
        </g>

        <!-- coffee table (clickable) -->
        <g class="interactive" id="table" tabindex="0" role="button" aria-label="Coffee table" transform="translate(290,440)">
          <rect x="0" y="0" width="220" height="68" rx="12" fill="#fffefc" stroke="#e3d0bd" />
          <rect x="10" y="8" width="200" height="52" rx="8" fill="#f7efe7" />
          <!-- legs -->
          <rect x="18" y="66" width="14" height="28" rx="6" fill="#b98458" />
          <rect x="188" y="66" width="14" height="28" rx="6" fill="#b98458" />
          <!-- small book on table (clickable) -->
          <a href="#" class="interactive book-on-table" tabindex="0" aria-label="Open featured publication">
            <rect x="28" y="18" width="76" height="42" rx="6" fill="#fff6ef" stroke="#e6d6c6"/>
            <text x="36" y="42" font-size="10" fill="#6a4a3a" style="font-family:sans-serif">Featured</text>
          </a>
        </g>

        <!-- newspaper rack (near bookshelf) -->
        <g transform="translate(960,480)">
          <rect x="0" y="0" width="110" height="130" rx="8" fill="#f2e3d1" stroke="#d6bda4"/>
          <rect x="8" y="10" width="94" height="12" rx="6" fill="#caa88a"/>
          <!-- papers (each clickable) -->
          <a href="#" class="newspaper" tabindex="0" aria-label="Read The Hindu">
            <rect x="12" y="30" width="86" height="20" rx="4" fill="#fff8f0"/>
            <text x="20" y="44" font-size="10" fill="#4a4a4a" style="font-family:sans-serif">The Hindu</text>
          </a>
          <a href="#" class="newspaper" tabindex="0" aria-label="Read Indian Express">
            <rect x="12" y="56" width="86" height="20" rx="4" fill="#fff9e8"/>
            <text x="20" y="70" font-size="10" fill="#4a4a4a" style="font-family:sans-serif">Indian Express</text>
          </a>
          <a href="#" class="newspaper" tabindex="0" aria-label="Read Deccan Herald">
            <rect x="12" y="82" width="86" height="20" rx="4" fill="#fffef2"/>
            <text x="20" y="96" font-size="10" fill="#4a4a4a" style="font-family:sans-serif">Deccan Herald</text>
          </a>
        </g>

      </svg>

      <div class="scene-caption">Click objects in the room: sofa, cushions, books, coffee table, newspapers, window and framed art.</div>
    </div>

    <!-- RIGHT: Side / quick links -->
    <div class="side" role="complementary" aria-label="Lobby tools and quick links">
      <div class="side-card" role="region" aria-labelledby="welcome-head">
        <h3 id="welcome-head">Welcome</h3>
        <p>Take a seat. This lobby is a calm place to begin exploring the Sunil Abraham Project. Click objects around the room to open content or read short notes.</p>
        <div class="pills" aria-hidden="false">
          <a href="/publications/" class="pill">Publications</a>
          <a href="/media/" class="pill">Media</a>
          <a href="/sunil/" class="pill">Biography</a>
        </div>
      </div>

      <div class="side-card" style="margin-top:0.9rem;" role="region" aria-labelledby="music-head">
        <h3 id="music-head">Music corner</h3>
        <p style="margin-top:0.2rem;">Soft Hindustani and instrumental background.</p>
        <div style="margin-top:0.6rem;">
          <!-- YouTube embed (keep as-is or replace) -->
          <iframe title="Soft Hindustani background" width="100%" height="160" src="https://www.youtube.com/embed/9lY0Xwz0N1M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:8px;"></iframe>
        </div>
      </div>

      <div class="side-card" style="margin-top:0.9rem;" role="region" aria-labelledby="nav-head">
        <h3 id="nav-head">Navigation</h3>
        <p style="margin:0.2rem 0 0 0;">Quick site links.</p>
        <div style="display:flex; gap:0.5rem; margin-top:0.6rem; flex-wrap:wrap;">
          <a href="/" class="pill" style="background:rgba(11,94,215,0.06); color:#0b5ed7;">Home</a>
          <a href="/about/" class="pill">About</a>
          <a href="/sandbox/" class="pill">Sandbox</a>
          <a href="/publications/" class="pill">Publications</a>
        </div>
      </div>
    </div>

  </div> <!-- .lobby-grid -->

  {% include back-to-top.html %}

</div>

<!-- Modal & overlay (Jekyll page-friendly, will be appended to DOM) -->
<div id="lobbyOverlay" class="lobby-overlay" aria-hidden="true">
  <div class="lobby-modal" role="dialog" aria-modal="true" aria-labelledby="modalTitle" aria-describedby="modalText">
    <h2 id="modalTitle">Welcome</h2>
    <p id="modalText">Have a seat and make yourself comfortable.</p>
    <div style="text-align:right;">
      <button class="btn" id="modalClose">Close</button>
    </div>
  </div>
</div>

<script>
/* Small interactive module for the lobby.
   - Uses event delegation for SVG elements
   - Keeps interactions accessible via keyboard (Enter / Space)
   - Uses progressive enhancement; if JS disabled the SVG remains visible
*/

(function () {
  const overlay = document.getElementById('lobbyOverlay');
  const modal = overlay && overlay.querySelector('.lobby-modal');
  const modalTitle = modal && document.getElementById('modalTitle');
  const modalText = modal && document.getElementById('modalText');
  const modalClose = document.getElementById('modalClose');

  function openModal(title, text) {
    if (!overlay) return;
    modalTitle.textContent = title;
    modalText.textContent = text;
    overlay.classList.add('active');
    overlay.setAttribute('aria-hidden','false');
    // trap focus on close button for simplicity
    modalClose.focus();
  }
  function closeModal() {
    if (!overlay) return;
    overlay.classList.remove('active');
    overlay.setAttribute('aria-hidden','true');
  }

  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (overlay) overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeModal();
  });

  // keyboard accessibility: close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });

  // helper to attach click/keyboard handlers to SVG groups
  function bindInteractive(selector, title, text) {
    const el = document.querySelector(selector);
    if (!el) return;
    function activate(e) {
      e.preventDefault();
      openModal(title, text);
    }
    el.addEventListener('click', activate);
    el.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') activate(e);
    });
    // make keyboard focusable if not already
    if (!el.getAttribute('tabindex')) el.setAttribute('tabindex', '0');
  }

  // sofa
  bindInteractive('#sofa', 'The Sofa', 'Have a seat. The sofa is the best spot to read and think. Click cushions to see more options.');

  // cushions (multiple)
  const cushions = document.querySelectorAll('a.cushion, .cushion');
  cushions.forEach(function (c, i) {
    const colours = ['Teal Cushion', 'Coral Cushion', 'Gold Cushion'];
    const notes = [
      'A teal cushion — cool and calm.',
      'A coral cushion — warmth and contrast.',
      'A gold cushion — bright accent.'
    ];
    function act(e) {
      e.preventDefault();
      openModal(colours[i] || 'Cushion', notes[i] || 'Comfort is in the details.');
    }
    c.addEventListener('click', act);
    c.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') act(e);
    });
  });

  // coffee table
  bindInteractive('#table', 'Coffee Table', 'A small table with a featured publication. Click the book on it to open the featured publication.');

  // featured book on table (it is an <a> in SVG)
  (function bindTableBook() {
    const sel = document.querySelector('a.book-on-table');
    if (!sel) return;
    sel.addEventListener('click', function (e) {
      e.preventDefault();
      openModal('Featured publication', 'This opens the featured publication. Replace the placeholder link with a real URL when ready.');
    });
    sel.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sel.click(); }
    });
  })();

  // window (click to relax)
  bindInteractive('.window', 'Window View', 'Look outside and let your mind wander. The window brightens when hovered.');

  // framed art
  bindInteractive('.frame', 'Wall Art', 'Every picture tells a story. This frame hints at the project and its warmth.');

  // books - each <a.book> is clickable; open modal with title inferred from aria-label
  document.querySelectorAll('a.book').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      const label = b.getAttribute('aria-label') || 'Book';
      openModal(label, 'This would open the linked page. Replace the placeholder href="#" with an internal link such as /publications/ or /media/.');
    });
    b.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); b.click(); }
    });
  });

  // newspapers
  document.querySelectorAll('a.newspaper').forEach(function (n) {
    n.addEventListener('click', function (e) {
      e.preventDefault();
      const label = n.getAttribute('aria-label') || 'Newspaper';
      openModal(label, 'This would open an external newspaper link. Replace the placeholder href="#" later.');
    });
    n.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); n.click(); }
    });
  });

  // small accessibility: make all interactive SVG anchors tabbable
  document.querySelectorAll('svg a, svg .interactive').forEach(function (el) {
    if (!el.getAttribute('tabindex')) el.setAttribute('tabindex', '0');
    el.classList.add('interactive');
  });

})();
</script>
