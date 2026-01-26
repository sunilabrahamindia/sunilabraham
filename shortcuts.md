---
layout: default
title: "Keyboard and URL Shortcuts"
description: "A directory of assigned short URLs and keyboard shortcuts for fast and accessible navigation on sunilabraham.in."
categories: [Project pages]
permalink: /shortcuts/
created: 2025-11-06
sitemap: true
---

**Shortcuts** page lists all assigned short URL paths and keyboard shortcuts that provide quick access to main sections of the website.  
These shortcuts are designed to improve accessibility for keyboard users, screen reader users, and power users.


# URL Shortcuts

These are normal, accessible URLs (not JavaScript shortcuts).  
Each uses a compliant HTML meta refresh redirect.

| Shortcut | Redirects to | Description |
|-----------|---------------|--------------|
| [`/1`](https://sunilabraham.in/1) | [`/`](https://sunilabraham.in/) | Home page |
| [`/c`](https://sunilabraham.in/c) | [`/contact/`](https://sunilabraham.in/contact/) | Contact information |
| [`/h`](https://sunilabraham.in/h) | [`/`](https://sunilabraham.in/) | Home page |
| [`/p`](https://sunilabraham.in/p) | [`/projects/`](https://sunilabraham.in/projects/) | Projects |
| [`/u`](https://sunilabraham.in/u) | [`/publications/`](https://sunilabraham.in/publications/) | Publications, articles, and book chapters |
| [`/v`](https://sunilabraham.in/v) | [`/videos/`](https://sunilabraham.in/videos/) | Videos |


# Keyboard Shortcuts

Keyboard shortcuts work everywhere on the site and provide instant navigation without using the mouse.  
These are implemented using lightweight, accessible JavaScript in the site footer.

# Keyboard Shortcuts

Keyboard shortcuts work everywhere on the site and provide instant navigation without using the mouse.  
These are implemented using lightweight, accessible JavaScript in the site footer.

| Keys | Action | Description |
|------|--------|-------------|
| **Alt + Shift + G** | Open GitHub source | Opens the GitHub repository page for the exact source file of the current page |
| **Alt + Shift + X** | Load a random page | Takes you to `/random/`, which instantly redirects to a random page across the site |


## Accessibility Notes

- URL shortcuts are simple, predictable, and compatible with all browsers and assistive technologies.  
- Keyboard shortcuts are designed to avoid conflicts with common browser shortcuts.  
- The `Alt + Shift` modifier combination follows accessibility guidelines used by MediaWiki (Wikipedia) for cross-browser compatibility.  
- Shortcut pages use compliant HTML redirects.  
- This directory **is** listed in the sitemap, but the individual shortcut pages are **not**, to avoid SEO duplication.

<style>
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 1rem;
}
th, td {
  border: 1px solid #ddd;
  padding: 0.6em 0.8em;
  text-align: left;
}
th {
  background-color: #f2f2f2;
  color: #333;
}
tr:nth-child(even) {
  background-color: #fafafa;
}
@media (max-width: 600px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }
  tr {
    margin-bottom: 0.8em;
    border: 1px solid #e5e5e5;
    padding: 0.5em;
  }
  th {
    display: none;
  }
  td {
    border: none;
    padding: 0.4em 0;
  }
  td::before {
    content: attr(data-label);
    font-weight: bold;
    display: block;
  }
}
</style>
