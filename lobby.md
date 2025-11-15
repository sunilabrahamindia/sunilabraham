---
layout: default
title: Lobby
description: "A cosy modern-Indian lobby: music, newspaper, bookshelf, and a gentle space to begin."
permalink: /lobby/
categories: [Project pages]
---

<style>
/* Lobby: Hybrid Indian + Modern — Inline CSS for Jekyll Markdown pages.
   Accessible palette, responsive, simple CSS only (no external fonts). */

.lobby-wrap{
  max-width:1100px;
  margin:1.25rem auto;
  padding:1.25rem;
  background:linear-gradient(180deg,#fffaf6 0%, #fffefc 100%);
  border-radius:14px;
  box-shadow:0 8px 30px rgba(20,20,20,0.06);
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color:#222;
  line-height:1.45;
}

/* Room grid */
.lobby-grid{
  display:flex;
  gap:1rem;
  align-items:flex-start;
  justify-content:space-between;
}

/* Left column - sofa + coffee table (main focus) */
.lobby-left{
  flex:1 1 58%;
  min-width:260px;
}

/* Right column - bookshelf + newspaper + plant */
.lobby-right{
  flex:0 0 38%;
  min-width:220px;
}

/* Sofa card */
.sofa{
  background:linear-gradient(180deg,#fff 0%, #fff8f2 100%);
  border-radius:12px;
  padding:1rem;
  box-shadow:0 6px 18px rgba(30,30,30,0.05);
  border:1px solid rgba(0,0,0,0.03);
}

/* Visual sofa header */
.sofa-visual{
  display:flex;
  gap:1rem;
  align-items:center;
  margin-bottom:0.75rem;
}
.sofa-visual .cushion{
  width:88px;
  height:64px;
  border-radius:8px;
  background:linear-gradient(90deg,#f6d7b0,#f8caa2);
  box-shadow:inset 0 -6px 10px rgba(0,0,0,0.03);
  flex-shrink:0;
}
.sofa-visual h2{
  margin:0;
  font-size:1.25rem;
  color:#2b2b2b;
}

/* Coffee table (cards row) */
.table-cards{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:0.5rem;
  margin-top:0.75rem;
}
.table-card{
  background:#fff;
  border-radius:10px;
  padding:0.6rem;
  text-align:center;
  border:1px solid rgba(0,0,0,0.04);
  box-shadow:0 4px 10px rgba(20,20,20,0.03);
  font-size:0.92rem;
}
.table-card a{ color:#0b5ed7; text-decoration:none; }
.table-card p{ margin:0.35rem 0 0; font-size:0.86rem; color:#555; }

/* Music player */
.music-card{
  margin-top:0.9rem;
  border-radius:10px;
  overflow:hidden;
  border:1px solid rgba(0,0,0,0.04);
}

/* Bookshelf */
.bookshelf{
  background:linear-gradient(180deg,#fdfaf8,#fffaf6);
  padding:0.9rem;
  border-radius:12px;
  border:1px solid rgba(0,0,0,0.03);
  box-shadow:0 6px 18px rgba(0,0,0,0.03);
}
.bookshelf h3{ margin-top:0; font-size:1rem; }
.book-list{ list-style:none; padding:0; margin:0.6rem 0 0; }
.book-list li{
  padding:0.45rem 0;
  border-bottom:1px dashed rgba(0,0,0,0.04);
  font-size:0.95rem;
}
.book-list li:last-child{ border-bottom:0; }

/* Newspaper stand */
.news-stand{
  margin-top:1rem;
  background:#fff;
  padding:0.75rem;
  border-radius:10px;
  border:1px solid rgba(0,0,0,0.04);
}
.news-stand a{ color:#0b5ed7; text-decoration:none; display:block; padding:0.35rem 0; }

/* Plant (simple decorative) */
.plant{
  margin-top:1rem;
  display:flex;
  gap:0.6rem;
  align-items:center;
}
.plant .pot{
  width:48px; height:48px; border-radius:6px;
  background:linear-gradient(180deg,#dfead1,#c7d9b4);
  box-shadow:inset 0 -4px 6px rgba(0,0,0,0.04);
}

/* Footer links */
.lobby-footer{
  margin-top:1rem;
  display:flex;
  gap:0.6rem;
  flex-wrap:wrap;
}
.lobby-footer a{
  display:inline-block;
  padding:0.45rem 0.75rem;
  border-radius:999px;
  text-decoration:none;
  font-size:0.9rem;
  border:1px solid rgba(11,94,215,0.08);
  color:#0b5ed7;
  background:rgba(11,94,215,0.04);
}

/* Responsive */
@media (max-width:880px){
  .lobby-grid{ flex-direction:column; }
  .lobby-right{ order:2; }
  .lobby-left{ order:1; }
  .table-cards{ grid-template-columns:repeat(2,1fr); }
}
@media (max-width:480px){
  .table-cards{ grid-template-columns:1fr; }
  .sofa-visual .cushion{ width:64px; height:52px; }
}
</style>

<div class="lobby-wrap" role="main" aria-labelledby="lobby-heading">

  <header class="sofa" aria-hidden="false">
    <div class="sofa-visual" role="region" aria-label="Lobby welcome">
      <div class="cushion" aria-hidden="true"></div>
      <div>
        <h1 id="lobby-heading" style="margin:0; font-size:1.5rem;">Welcome to the Lobby</h1>
        <p style="margin:0.25rem 0 0; color:#444;">A warm, modern-Indian drawing room — music, reading, and a slow cup of ideas.</p>
      </div>
    </div>

    <p style="margin-top:0.8rem;">Take a seat. The lobby is a gentle place to begin: soft music, a newspaper on the table, and a small bookshelf of recommended pages.</p>

    <div class="table-cards" aria-hidden="false">
      <div class="table-card">
        <strong>On the Table</strong>
        <p><a href="/publications/">Featured publications</a></p>
      </div>
      <div class="table-card">
        <strong>Conversation</strong>
        <p><a href="/articles/students-for-peace/">Students for Peace (1993)</a></p>
      </div>
      <div class="table-card">
        <strong>Thoughts</strong>
        <p><a href="/publications/surveillance-project/">Aadhaar & transparency</a></p>
      </div>
    </div>

    <div class="music-card" aria-label="Music corner">
      <!-- Accessible YouTube embed: descriptive title + allow fullscreen -->
      <iframe width="100%" height="160" src="https://www.youtube.com/embed/9lY0Xwz0N1M" title="Soft Hindustani classical - gentle background for reading" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </header>

  <div class="lobby-grid" style="margin-top:1rem;">
    <div class="lobby-left" role="region" aria-label="Main seating area">

      <section class="sofa" aria-labelledby="today-section">
        <h2 id="today-section" style="font-size:1.05rem; margin:0;">Today in the Room</h2>
        <p style="margin:0.5rem 0 0;">A small selection for a relaxed read. These are suggested to begin exploring — like a magazine and a small plate of ideas on the coffee table.</p>

        <ul style="margin:0.9rem 0 0; padding-left:1rem;">
          <li><a href="/publications/data-protection-we-can-innovate-le">Data Protection: We Can Innovate, Leapfrog</a></li>
          <li><a href="/publications/eavesdropping-on-the-freedom-of-expression-in-india/">Intermediaries Guidelines, 2011</a></li>
          <li><a href="/publications/snooping-can">Snooping Can Lead to Data Abuse</a></li>
        </ul>
      </section>

      <section class="sofa" style="margin-top:0.9rem;" aria-labelledby="relax-section">
        <h2 id="relax-section" style="font-size:1.05rem; margin:0;">Relax & Reflect</h2>
        <p style="margin:0.5rem 0 0;">A short prompt to settle in: What idea would you like to take from this room today? A question, a paper, a song?</p>
        <p style="margin-top:0.6rem; font-size:0.95rem; color:#444;"><em>Tip:</em> If you are using mobile, rotate the device for a wider view of the shelf and music card.</p>
      </section>

    </div>

    <aside class="lobby-right" role="complementary" aria-label="Bookshelf and newspaper">

      <div class="bookshelf" role="region" aria-labelledby="bookshelf-heading">
        <h3 id="bookshelf-heading">Bookshelf</h3>
        <p style="margin:0.2rem 0 0; color:#444; font-size:0.95rem;">A small shelf of places to explore — like spines on a shelf.</p>
        <ul class="book-list" role="list">
          <li><a href="/publications/">Publications — full archive</a></li>
          <li><a href="/media/">Media articles & commentaries</a></li>
          <li><a href="/amaa/">A. M. A. Ayrookuzhiel collection</a></li>
          <li><a href="/sunil/">Sunil Abraham — biography</a></li>
        </ul>
      </div>

      <div class="news-stand" role="region" aria-labelledby="news-heading">
        <h3 id="news-heading" style="margin:0 0 0.4rem 0;">Newspaper Stand</h3>
        <p style="margin:0 0 0.5rem 0; color:#444;">Quick links to the day's reading (external papers).</p>
        <a href="https://www.thehindu.com/">The Hindu</a>
        <a href="https://indianexpress.com/">Indian Express</a>
        <a href="https://www.deccanherald.com/">Deccan Herald</a>
      </div>

      <div class="plant" aria-hidden="true">
        <div class="pot" role="img" aria-label="potted plant decorative"></div>
        <div style="font-size:0.92rem; color:#444;">A quiet plant keeping the room calm.</div>
      </div>

      <nav class="lobby-footer" aria-label="Lobby navigation" style="margin-top:0.8rem;">
        <a href="/">Home</a>
        <a href="/about/">About</a>
        <a href="/sandbox/">Sandbox</a>
        <a href="/publications/">Publications</a>
      </nav>

    </aside>
  </div>

  {% include back-to-top.html %}

</div>
