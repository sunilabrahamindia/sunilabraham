---
layout: default
title: Family Tree
description: Hierarchical family structure of the Abraham–Ayrookuzhiel family
---

# Family Tree

This page presents the Abraham–Ayrookuzhiel family hierarchy in a simple visual form.  
Each box represents a person, connected by lines to parents and children.

<div class="tree">
  <ul>
    <li>
      <a href="#">Abraham (1820–1895)</a>
      <ul>
        <li>
          <a href="#">Mathen Abraham (1850–1920)</a>
          <ul>
            <li><a href="#">A. M. A. Ayrookuzhiel (1933–1996)</a></li>
            <li><a href="#">A. M. B. George (1938– )</a></li>
          </ul>
        </li>
        <li>
          <a href="#">John Abraham (1855–1925)</a>
          <ul>
            <li><a href="#">Paul John (1890–1965)</a></li>
            <li><a href="#">Sara Paul (1895–1970)</a></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</div>

<style>
/* =========================================================
   Sunil Abraham Project — Responsive CSS Family Tree
   Works well on mobile, tablet and desktop
   ========================================================= */
.tree {
  width: 100%;
  overflow-x: auto;
  padding: 1rem 0 3rem;
  text-align: center;
  box-sizing: border-box;
}

/* Base list layout */
.tree ul {
  padding-top: 20px;
  position: relative;
  display: inline-block;
  text-align: center;
}
.tree li {
  display: inline-block;
  list-style-type: none;
  position: relative;
  padding: 20px 5px 0 5px;
  vertical-align: top;
}

/* Connectors between nodes */
.tree li::before,
.tree li::after {
  content: '';
  position: absolute;
  top: 0;
  border-top: 2px solid #ccc;
  width: 50%;
  height: 20px;
}
.tree li::before { right: 50%; border-right: 2px solid #ccc; }
.tree li::after { left: 50%; border-left: 2px solid #ccc; }

.tree li:only-child::before,
.tree li:only-child::after {
  display: none;
}
.tree li:only-child { padding-top: 0; }

.tree li:first-child::before { border: 0 none; }
.tree li:last-child::after { border: 0 none; }

.tree ul ul::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  border-left: 2px solid #ccc;
  height: 20px;
}

/* Person box */
.tree a {
  display: inline-block;
  padding: 8px 12px;
  border: 2px solid #0a2e57;
  border-radius: 10px;
  background: #f9fafb;
  color: #0a2e57;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  min-width: 140px;
  transition: all 0.3s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.tree a:hover {
  background: #0a2e57;
  color: #fff;
}

/* Responsive tweaks */
@media (max-width: 768px) {
  .tree ul,
  .tree li {
    display: block;
    text-align: center;
  }
  .tree li::before,
  .tree li::after,
  .tree ul ul::before {
    display: none;
  }
  .tree a {
    display: block;
    margin: 10px auto;
  }
}
</style>
