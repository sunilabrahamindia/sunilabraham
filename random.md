---
layout: default
title: Random Page
permalink: /random/
sitemap: false
---

Loading a random page from the Sunil Abraham Project...

<script>
  // Auto-collect all pages except /random/ and _short/ redirects
  const allPages = {{ site.pages
      | where_exp:"p","p.url != '/random/'"
      | where_exp:"p","p.url !contains '/_short/'"
      | map:"url"
      | jsonify
  }};

  const randomPage = allPages[Math.floor(Math.random() * allPages.length)];
  window.location.href = randomPage;
</script>
