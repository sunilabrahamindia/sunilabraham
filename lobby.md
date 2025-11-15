---
layout: default
title: Lobby
description: "A visual Indian–Modern drawing room lobby with sofa, rug, coffee table, bookshelf and a wooden newspaper rack."
permalink: /lobby/
categories: [Project pages]
---

<style>
/* -----------------------
   LOBBY ROOM STYLES
   Hybrid Modern + Indian
   ----------------------- */

/* Room wrapper */
.room {
  max-width: 900px;
  margin: 1.5rem auto;
  padding: 1.2rem;
  background: #fdf9f4;
  border-radius: 14px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  border: 1px solid #f3e5d8;
  font-family: system-ui, -apple-system, Roboto, "Segoe UI", Arial;
  color: #222;
}

/* Wall frame (top welcome panel) */
.wall-frame {
  background: #fffdfa;
  border: 2px solid #e8dccf;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  margin-bottom: 1.4rem;
}

/* Sofa */
.sofa {
  background: linear-gradient(180deg, #f4e4d4, #efd9c6);
  border-radius: 18px;
  padding: 1rem;
  margin: auto;
  width: 88%;
  box-shadow: inset 0 -8px 10px rgba(0,0,0,0.06), 0 6px 18px rgba(0,0,0,0.08);
  position: relative;
}

/* Sofa arms */
.sofa::before, .sofa::after {
  content: "";
  width: 18%;
  height: 60px;
  background: linear-gradient(180deg, #e8ccb5, #e1bfa4);
  position: absolute;
  top: 40%;
  border-radius: 14px;
  box-shadow: inset 0 -4px 8px rgba(0,0,0,0.08);
}
.sofa::before { left: -10%; }
.sofa::after { right: -10%; }

/* Cushions */
.cushions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 0.5rem;
}
.cushion {
  width: 65px;
  height: 55px;
  border-radius: 8px;
  background: linear-gradient(180deg, #ffe3c4, #f7cfa4);
  box-shadow: inset 0 -5px 8px rgba(0,0,0,0.07);
}

/* Rug */
.rug {
  margin: 1.2rem auto;
  width: 92%;
  padding: 1rem;
  background: repeating-linear-gradient(90deg, #f0e9e0, #f0e9e0 8px, #f7f3ee 8px, #f7f3ee 16px);
  border-radius: 12px;
  box-shadow: inset 0 0 15px rgba(0,0,0,0.1);
}

/* Coffee table */
.table {
  background: #ffffff;
  width: 70%;
  margin: 0.5rem auto;
  padding: 0.8rem;
  border-radius: 10px;
  border: 1px solid #e5d4c4;
  box-shadow: 0 4px 8px rgba(0,0,0,0.07);
  text-align: center;
  position: relative;
}
.table-leg {
  width: 20%;
  height: 10px;
  background: #c29f76;
  border-radius: 3px;
  margin: 0.2rem auto 0 auto;
  box-shadow: inset 0 -3px 5px rgba(0,0,0,0.2);
}

/* Bookshelf */
.bookshelf {
  background: #f7eee5;
  border: 1px solid #e2d3c4;
  border-radius: 10px;
  padding: 1rem;
  margin-top: 1.2rem;
  box-shadow: 0 5px 12px rgba(0,0,0,0.04);
}
.shelf {
  height: 4px;
  background: #d9c1ab;
  margin: 0.8rem 0;
  border-radius: 2px;
}

/* Wooden newspaper stand */
.news-stand {
  margin-top: 1.3rem;
  background: #f3e3d2;
  border-radius: 10px;
  border: 1px solid #d5bba7;
  padding: 0.8rem;
  box-shadow: inset 0 -8px 12px rgba(0,0,0,0.07);
}
.news-bar {
  height: 6px;
  background: #caa88a;
  border-radius: 4px;
  margin-bottom: 0.6rem;
}

/* Links */
a {
  color: #0b5ed7;
  text-decoration: none;
}

/* Responsive */
@media (max-width: 600px) {
  .sofa::before, .sofa::after { display: none; }
  .sofa { width: 100%; }
  .table { width: 88%; }
}
</style>

<div class="room">

  <!-- Wall Frame -->
  <div class="wall-frame">
    <h1 style="margin:0; font-size:1.4rem;">Welcome to the Lobby</h1>
    <p style="margin:0.5rem 0 0;">A warm Indian–modern drawing room to relax, browse, and settle in.</p>
  </div>

  <!-- Sofa -->
  <div class="sofa">
    <h2 style="margin:0; font-size:1.15rem;">Please have a seat</h2>
    <p style="margin:0.5rem 0 0;">Get comfortable. The coffee table has a few things for you today.</p>

    <div class="cushions">
      <div class="cushion"></div>
      <div class="cushion"></div>
      <div class="cushion"></div>
    </div>
  </div>

  <!-- Rug -->
  <div class="rug">

    <!-- Coffee Table -->
    <div class="table">
      <strong>Today's Highlights</strong>
      <p style="margin:0.5rem 0 0;"><a href="/publications/">Featured publications</a></p>
      <p><a href="/articles/students-for-peace/">Students for Peace (1993)</a></p>
      <p><a href="/publications/surveillance-project/">Aadhaar & Transparency</a></p>
    </div>
    <div class="table-leg"></div>

  </div>

  <!-- Bookshelf -->
  <div class="bookshelf">
    <h3 style="margin:0;">Bookshelf</h3>
    <div class="shelf"></div>
    <p><a href="/publications/">Publications (full archive)</a></p>
    <div class="shelf"></div>
    <p><a href="/media/">Media Articles & Commentary</a></p>
    <div class="shelf"></div>
    <p><a href="/amaa/">A. M. A. Ayrookuzhiel</a></p>
    <div class="shelf"></div>
    <p><a href="/sunil/">Biography of Sunil Abraham</a></p>
  </div>

  <!-- Newspaper Stand -->
  <div class="news-stand">
    <h3 style="margin:0;">Newspaper Stand</h3>
    <div class="news-bar"></div>
    <a href="https://www.thehindu.com/">The Hindu</a><br>
    <a href="https://indianexpress.com/">Indian Express</a><br>
    <a href="https://www.deccanherald.com/">Deccan Herald</a><br>
  </div>

  {% include back-to-top.html %}
</div>
