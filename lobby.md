---
layout: default
title: Lobby
description: "A fully illustrated Indian–Modern drawing room lobby with sofa, rug, coffee table, bookshelf and wooden newspaper stand. Responsive and accessible."
permalink: /lobby/
categories: [Project pages]
---

<style>
/* Final Visual Lobby (CSS + inline SVG)
   - Hybrid Indian + Modern
   - Inline SVG used for crisp scalable illustration
   - Responsive: two-column on desktop, stacked on mobile
   - Accessible colours, system fonts
*/

.lobby-scene {
  --room-bg: #f9f6f2;
  --wall: #fffaf3;
  --floor: #efe6db;
  --accent: #c79a6a; /* warm wood */
  --teal: #0a6d66;
  --text: #1e1e1e;

  max-width: 1200px;
  margin: 1.6rem auto;
  padding: 1.0rem;
  background: linear-gradient(180deg, var(--room-bg) 0%, #fffdf9 100%);
  border-radius: 14px;
  box-shadow: 0 14px 40px rgba(10,10,10,0.06);
  color: var(--text);
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
}

/* layout */
.lobby-row {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 1.2rem;
  align-items: start;
}

/* Left: the room illustration */
.room-canvas {
  background: linear-gradient(180deg, rgba(255,255,255,0.35), rgba(255,255,255,0.15));
  border-radius: 12px;
  padding: 1rem;
  position: relative;
  min-height: 380px;
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.03);
}

/* Right: shelf & stand + nav */
.side-panel {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}

/* framed text panel */
.welcome-frame {
  background: white;
  border-radius: 10px;
  padding: 0.9rem;
  border: 1px solid rgba(0,0,0,0.04);
  box-shadow: 0 6px 12px rgba(10,10,10,0.04);
}
.welcome-frame h1 { margin:0 0 0.35rem 0; font-size:1.2rem; }
.welcome-frame p { margin:0; color:#444; font-size:0.95rem; }

/* music card */
.music-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.04);
  padding: 0.45rem;
}

/* bookshelf & news stand */
.bookshelf, .news-stand {
  background: linear-gradient(180deg,#fcf9f6,#fffdf9);
  border-radius: 10px;
  padding: 0.9rem;
  border: 1px solid rgba(0,0,0,0.03);
  box-shadow: 0 6px 14px rgba(10,10,10,0.03);
}
.bookshelf h3, .news-stand h3 { margin:0 0 0.45rem 0; font-size:1rem; }
.book-links, .news-links { margin:0; padding-left:1rem; color:#0b5ed7; }

/* scene scaling and placement */
.svg-scene {
  width:100%;
  height:auto;
  display:block;
}

/* small caption row under scene */
.scene-actions {
  display:flex;
  gap:0.6rem;
  margin-top:0.6rem;
  flex-wrap:wrap;
}
.scene-actions a {
  background: rgba(11,94,215,0.06);
  color:#0b5ed7;
  padding:0.45rem 0.7rem;
  border-radius:999px;
  text-decoration:none;
  font-size:0.9rem;
  border: 1px solid rgba(11,94,215,0.07);
}

/* responsive behaviour */
@media (max-width:980px){
  .lobby-row { grid-template-columns: 1fr 320px; }
  .room-canvas { min-height: 420px; }
}
@media (max-width:720px){
  .lobby-row { grid-template-columns: 1fr; }
  .side-panel { order:2; }
  .room-canvas { order:1; min-height:360px; }
  .scene-actions { justify-content:center; }
}

/* accessibility: focus styles */
a:focus { outline:3px solid rgba(11,94,215,0.18); outline-offset:2px; border-radius:6px; }

/* small utility styles for links in side panel */
.side-panel a { color:#0b5ed7; text-decoration:none; }
.side-panel a:hover { text-decoration:underline; }
</style>

<div class="lobby-scene" role="main" aria-labelledby="lobby-title">

  <div class="lobby-row">

    <!-- LEFT: Room Illustration -->
    <div class="room-canvas" aria-hidden="false">

      <!-- Inline SVG: Wall, window, sofa, rug, coffee table, plant, bookshelf hint -->
      <svg class="svg-scene" viewBox="0 0 1200 700" role="img" aria-labelledby="svgTitle svgDesc" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">

        <title id="svgTitle">Lobby drawing room scene</title>
        <desc id="svgDesc">A warm Indian–modern drawing room with a teal sofa, rug, wooden coffee table, bookshelf, potted plant and wooden newspaper rack by the side window.</desc>

        <!-- Background wall -->
        <rect x="0" y="0" width="1200" height="420" fill="#fff8f1" />
        <!-- Floor -->
        <rect x="0" y="420" width="1200" height="280" fill="#efe6db" />

        <!-- Window (left wall) -->
        <g transform="translate(60,40)">
          <rect x="0" y="0" width="260" height="150" rx="8" fill="#e8f6f4" stroke="#d3ecea" stroke-width="2"/>
          <rect x="12" y="12" width="100" height="60" rx="4" fill="#dff3f1" />
          <rect x="138" y="12" width="100" height="60" rx="4" fill="#dff3f1" />
          <rect x="12" y="84" width="226" height="44" rx="4" fill="#dff3f1" />
          <!-- subtle curtains -->
          <path d="M0 0 C20 18 20 132 0 150 L0 0" fill="#fff3ea" opacity="0.6"/>
          <path d="M260 0 C240 18 240 132 260 150 L260 0" fill="#fff3ea" opacity="0.6"/>
        </g>

        <!-- Framed art on wall -->
        <g transform="translate(360,36)">
          <rect x="0" y="0" width="260" height="120" rx="6" fill="#fffefc" stroke="#e9dfd3" />
          <rect x="14" y="12" width="232" height="96" rx="4" fill="#f7e9df"/>
          <circle cx="120" cy="60" r="20" fill="#c79a6a" opacity="0.9"/>
          <text x="26" y="95" font-size="12" fill="#6a4a3a" font-family="sans-serif">Sunil Abraham Project</text>
        </g>

        <!-- Sofa (center-left) -->
        <g transform="translate(180,200)">
          <!-- base shadow under sofa -->
          <ellipse cx="280" cy="230" rx="260" ry="36" fill="rgba(0,0,0,0.08)"/>
          <!-- sofa seat -->
          <rect x="40" y="60" rx="30" ry="30" width="480" height="150" fill="#e8f4f2" stroke="#d5e8e6" stroke-width="2"/>
          <!-- sofa back -->
          <rect x="60" y="18" rx="26" ry="26" width="440" height="78" fill="#0fa29c" />
          <!-- sofa arms -->
          <rect x="10" y="66" rx="18" ry="18" width="40" height="140" fill="#d8efec" />
          <rect x="530" y="66" rx="18" ry="18" width="40" height="140" fill="#d8efec" />
          <!-- cushions -->
          <rect x="120" y="20" rx="10" ry="10" width="80" height="60" fill="#f7d5b0"/>
          <rect x="220" y="20" rx="10" ry="10" width="100" height="60" fill="#ffd9b3"/>
          <rect x="360" y="20" rx="10" ry="10" width="80" height="60" fill="#f7d5b0"/>
        </g>

        <!-- Rug under table -->
        <g transform="translate(300,360)">
          <ellipse cx="300" cy="80" rx="260" ry="70" fill="#fff5ee" stroke="#efd9c6" />
          <ellipse cx="300" cy="80" rx="200" ry="50" fill="#f9efe6" />
        </g>

        <!-- Coffee table (center) -->
        <g transform="translate(380,320)">
          <!-- table top -->
          <rect x="0" y="0" rx="12" ry="12" width="240" height="72" fill="#fffefc" stroke="#d9c2a6" />
          <!-- inlay -->
          <rect x="8" y="8" rx="8" ry="8" width="224" height="56" fill="#f7efe7" />
          <!-- legs -->
          <rect x="20" y="76" width="12" height="36" rx="4" fill="#b98555" />
          <rect x="208" y="76" width="12" height="36" rx="4" fill="#b98555" />
          <rect x="20" y="76" width="200" height="12" rx="6" fill="#d6b48b" opacity="0.2"/>
          <!-- items on table: a small book and a cup -->
          <rect x="28" y="12" width="60" height="36" rx="6" fill="#fff7f0" stroke="#e6d2c0"/>
          <rect x="110" y="18" width="36" height="20" rx="8" fill="#c79a6a"/>
          <circle cx="130" cy="28" r="6" fill="#fff"/>
        </g>

        <!-- Wooden bookshelf (right-back) -->
        <g transform="translate(900,200)">
          <rect x="0" y="0" width="220" height="260" rx="8" fill="#f7eee5" stroke="#e2d3c4"/>
          <!-- shelves -->
          <rect x="10" y="16" width="200" height="6" fill="#d9c1ab"/>
          <rect x="10" y="86" width="200" height="6" fill="#d9c1ab"/>
          <rect x="10" y="156" width="200" height="6" fill="#d9c1ab"/>
          <rect x="10" y="226" width="200" height="6" fill="#d9c1ab"/>
          <!-- books (simple colour blocks) -->
          <rect x="18" y="26" width="22" height="44" fill="#0b5ed7"/>
          <rect x="46" y="26" width="16" height="44" fill="#e08a3f"/>
          <rect x="68" y="26" width="14" height="44" fill="#8aa24c"/>
          <rect x="90" y="96" width="40" height="44" fill="#6a4a3a"/>
          <rect x="136" y="96" width="26" height="44" fill="#c79a6a"/>
          <rect x="18" y="166" width="40" height="44" fill="#0b5ed7"/>
          <rect x="70" y="166" width="26" height="44" fill="#f3c27b"/>
          <rect x="110" y="166" width="24" height="44" fill="#8aa24c"/>
        </g>

        <!-- Wooden newspaper rack (beside bookshelf) -->
        <g transform="translate(900,480)">
          <rect x="0" y="0" width="220" height="120" rx="10" fill="#f3e3d2" stroke="#d5bba7"/>
          <rect x="12" y="12" width="196" height="14" rx="6" fill="#caa88a"/>
          <rect x="12" y="34" width="196" height="10" rx="6" fill="#e9d2c0"/>
          <rect x="22" y="50" width="160" height="56" rx="6" fill="#fffefc"/>
          <text x="26" y="74" font-size="14" fill="#6a4a3a" font-family="sans-serif">The Hindu · Indian Express · Deccan Herald</text>
        </g>

        <!-- Potted plant (left of sofa) -->
        <g transform="translate(80,360)">
          <rect x="0" y="0" width="70" height="100" rx="10" fill="#fff" opacity="0"/>
          <rect x="24" y="80" width="22" height="28" rx="4" fill="#c29f76" />
          <g transform="translate(10,6)" fill="#87b27b">
            <ellipse cx="26" cy="40" rx="14" ry="26"/>
            <ellipse cx="8" cy="40" rx="8" ry="18" />
            <ellipse cx="44" cy="40" rx="8" ry="18" />
          </g>
        </g>

        <!-- small floor shadow -->
        <ellipse cx="600" cy="560" rx="340" ry="18" fill="rgba(0,0,0,0.03)"/>
      </svg>

      <!-- Scene caption & quick actions -->
      <div style="padding:0.6rem 0 0 0;">
        <p style="margin:0 0 0.4rem 0; font-size:0.98rem;"><strong id="lobby-title">A warm Indian–Modern drawing room</strong> — sit on the sofa, browse the books, or pick a newspaper from the rack.</p>

        <div class="scene-actions" role="navigation" aria-label="Quick links in lobby">
          <a href="/publications/">Featured publications</a>
          <a href="/articles/students-for-peace/">Students for Peace</a>
          <a href="/publications/surveillance-project/">Aadhaar & transparency</a>
        </div>
      </div>
    </div>

    <!-- RIGHT: Side panel - welcome, music, bookshelf & news links -->
    <aside class="side-panel" aria-label="Lobby side panel">

      <div class="welcome-frame" role="region" aria-labelledby="welcome-head">
        <h1 id="welcome-head">Welcome to the Lobby</h1>
        <p>Take a slow seat. This room is a calm place to start: music, reading, and a few highlighted items.</p>
      </div>

      <div class="music-card" role="region" aria-labelledby="music-head">
        <h3 id="music-head" style="margin:0 0 0.5rem 0;">Music corner</h3>
        <!-- Embedded YouTube (replace href if you prefer another) -->
        <iframe title="Soft Hindustani classical background" width="100%" height="160" src="https://www.youtube.com/embed/9lY0Xwz0N1M" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>

      <div class="bookshelf" role="region" aria-labelledby="shelf-head">
        <h3 id="shelf-head">Bookshelf</h3>
        <ul class="book-links" role="list">
          <li><a href="/publications/">Publications — full archive</a></li>
          <li><a href="/media/">Media articles & commentary</a></li>
          <li><a href="/amaa/">A. M. A. Ayrookuzhiel collection</a></li>
          <li><a href="/sunil/">Sunil Abraham — biography</a></li>
        </ul>
      </div>

      <div class="news-stand" role="region" aria-labelledby="news-head">
        <h3 id="news-head">Newspaper stand</h3>
        <ul class="news-links" role="list">
          <li><a href="https://www.thehindu.com/">The Hindu</a></li>
          <li><a href="https://indianexpress.com/">Indian Express</a></li>
          <li><a href="https://www.deccanherald.com/">Deccan Herald</a></li>
        </ul>
      </div>

      <nav class="welcome-frame" aria-label="Lobby navigation">
        <div style="display:flex; gap:0.6rem; flex-wrap:wrap;">
          <a href="/" style="font-size:0.92rem;">Home</a>
          <a href="/about/" style="font-size:0.92rem;">About</a>
          <a href="/sandbox/" style="font-size:0.92rem;">Sandbox</a>
          <a href="/publications/" style="font-size:0.92rem;">Publications</a>
        </div>
      </nav>

    </aside>
  </div>

  {% include back-to-top.html %}

</div>
