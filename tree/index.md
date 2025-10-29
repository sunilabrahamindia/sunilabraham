---
layout: default
title: Family Tree
description: Hierarchical family structure of the Abraham–Ayrookuzhiel family
---

# Family Tree

This visual family tree shows key generations of the Abraham–Ayrookuzhiel family.

<div class="tree">
  <ul>
    <li>
      <a href="#">
        <img src="/assets/images/abraham.jpg" alt="Abraham" />
        <div class="name">Abraham</div>
        <div class="years">(1820–1895)</div>
      </a>
      <ul>
        <li>
          <a href="#">
            <img src="/assets/images/mathen.jpg" alt="Mathen Abraham" />
            <div class="name">Mathen Abraham</div>
            <div class="years">(1850–1920)</div>
          </a>
          <ul>
            <li>
              <a href="#">
                <img src="/assets/images/amaa.jpg" alt="A. M. A. Ayrookuzhiel" />
                <div class="name">A. M. A. Ayrookuzhiel</div>
                <div class="years">(1933–1996)</div>
              </a>
            </li>
            <li>
              <a href="#">
                <img src="/assets/images/george.jpg" alt="A. M. B. George" />
                <div class="name">A. M. B. George</div>
                <div class="years">(1938– )</div>
              </a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#">
            <img src="/assets/images/john.jpg" alt="John Abraham" />
            <div class="name">John Abraham</div>
            <div class="years">(1855–1925)</div>
          </a>
          <ul>
            <li>
              <a href="#">
                <img src="/assets/images/paul.jpg" alt="Paul John" />
                <div class="name">Paul John</div>
                <div class="years">(1890–1965)</div>
              </a>
            </li>
            <li>
              <a href="#">
                <img src="/assets/images/sara.jpg" alt="Sara Paul" />
                <div class="name">Sara Paul</div>
                <div class="years">(1895–1970)</div>
              </a>
            </li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</div>

<style>
/* =========================================================
   Simple CSS Family Tree (Responsive, with photos)
   Works inside Markdown + Jekyll default layout
   ========================================================= */
.tree {
  width: 100%;
  overflow-x: auto;
  padding-bottom: 2rem;
  text-align: center;
}

.tree ul {
  padding-top: 20px;
  position: relative;
  transition: all 0.5s;
  display: inline-block;
}

.tree li {
  float: left;
  text-align: center;
  list-style-type: none;
  position: relative;
  padding: 20px 5px 0 5px;
  transition: all 0.5s;
}

/* Connectors */
.tree li::before,
.tree li::after {
  content: '';
  position: absolute;
  top: 0;
  right: 50%;
  border-top: 2px solid #ccc;
  width: 50%;
  height: 20px;
}

.tree li::after {
  right: auto;
  left: 50%;
  border-left: 2px solid #ccc;
}

.tree li:only-child::after,
.tree li:only-child::before {
  display: none;
}

.tree li:only-child {
  padding-top: 0;
}

.tree li:first-child::before,
.tree li:last-child::after {
  border: 0 none;
}

.tree li:last-child::before {
  border-right: 2px solid #ccc;
  border-radius: 0 5px 0 0;
}

.tree li:first-child::after {
  border-radius: 5px 0 0 0;
}

.tree ul ul::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  border-left: 2px solid #ccc;
  width: 0;
  height: 20px;
}

/* Node cards */
.tree a {
  border: 2px solid #0a2e57;
  padding: 10px;
  text-decoration: none;
  color: #0a2e57;
  font-weight: 600;
  display: inline-block;
  border-radius: 10px;
  transition: all 0.3s;
  background: #f9fafb;
  width: 130px;
}

.tree a:hover {
  background: #0a2e57;
  color: #fff;
  border-color: #0a2e57;
}

.tree a img {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #0a2e57;
  margin-bottom: 8px;
}

.tree a .name {
  font-size: 0.95rem;
  font-weight: 600;
}

.tree a .years {
  font-size: 0.8rem;
  color: #555;
  font-weight: 400;
}

/* Clearfix */
.tree ul::after {
  content: "";
  display: table;
  clear: both;
}

/* Mobile adjustments */
@media (max-width: 600px) {
  .tree li {
    display: block;
    float: none;
    padding: 10px 0;
  }
  .tree ul ul::before,
  .tree li::before,
  .tree li::after {
    display: none;
  }
}
</style>
