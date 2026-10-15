---
layout: default
title: "Hidden Categories and Maintenance Categories"
description: "Documentation of hidden category assignments and automatically populated maintenance categories in The Sunil Abraham Project."
permalink: /tsap/hidden-categories/
categories: [TSAP Documentation]
page_id: TSAP-1328
created: 2026-10-13
---

{% include documentation-notice.html %}


**Hidden and maintenance categories** allow The Sunil Abraham Project to classify pages for maintenance, preservation and technical tracking without displaying those categories in the category list at the bottom of individual pages. This page documents the current maintenance categories, their implementation and how to assign hidden categories through YAML front matter.

## Purpose {#purpose}

Maintenance categories help identify pages that need periodic attention, use particular embeds or templates, or meet specific technical criteria.

Some maintenance categories are populated automatically by the site's Liquid templates, while others can be assigned manually through the `hidden_categories` YAML field.

Hidden categories are not private or access-restricted. Their category pages remain publicly accessible, and assigned pages can still appear in those category listings.

## Current Maintenance Categories {#current-maintenance-categories}

This list is generated from category pages assigned to [Maintenance categories](/categories/maintenance-categories/), so new categories appear here automatically when they are added to that group. Use the controls to search or change the order.

{% assign maintenance_categories = site.pages | where_exp: "p", "p.path contains 'categories/'" | where_exp: "p", "p.categories contains 'Maintenance categories'" | sort: "title" %}

<div class="maintenance-category-browser">
  <div class="maintenance-category-controls" hidden>
    <div>
      <label for="maintenance-category-search">Search categories</label>
      <input id="maintenance-category-search" type="search" autocomplete="off" placeholder="Type a category name">
    </div>
    <div>
      <label for="maintenance-category-sort">Sort by</label>
      <select id="maintenance-category-sort">
        <option value="az">Title: A to Z</option>
        <option value="za">Title: Z to A</option>
        <option value="oldest">Created: oldest first</option>
        <option value="newest">Created: newest first</option>
      </select>
    </div>
    <button type="button" id="maintenance-category-clear">Clear search and sorting</button>
  </div>

  <p id="maintenance-category-count" aria-live="polite">{{ maintenance_categories.size }} maintenance categories</p>
  <p id="maintenance-category-empty" hidden>No maintenance categories match your search.</p>

  <ul id="maintenance-category-list">
    {% for cat in maintenance_categories %}
      {% assign cat_name = cat.title | remove_first: "Category:" | strip %}
      <li data-name="{{ cat_name | downcase | escape }}" data-created="{% if cat.created %}{{ cat.created | date: '%Y-%m-%d' }}{% endif %}">
        <a href="{{ cat.url | relative_url }}">{{ cat_name | escape }}</a>
        {% if cat.created %}<span class="maintenance-category-date">Created: <time datetime="{{ cat.created | date: '%Y-%m-%d' }}">{{ cat.created | date: "%d %b %Y" }}</time></span>{% else %}<span class="maintenance-category-date">Creation date not recorded</span>{% endif %}
      </li>
    {% endfor %}
  </ul>
</div>

<style>
.maintenance-category-browser {
  margin: 1em 0;
  color: #222;
}
.maintenance-category-controls[hidden],
#maintenance-category-empty[hidden],
#maintenance-category-list li[hidden] {
  display: none !important;
}
.maintenance-category-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr));
  gap: 0.85em;
  margin-bottom: 1em;
  padding: 1em;
  border: 1px solid #b8c2ce;
  background: #f3f6f9;
}
.maintenance-category-controls label {
  display: block;
  margin-bottom: 0.35em;
  font-weight: 600;
}
.maintenance-category-controls input,
.maintenance-category-controls select,
.maintenance-category-controls button {
  box-sizing: border-box;
  width: 100%;
  min-height: 2.75em;
  padding: 0.55em 0.7em;
  border: 1px solid #667788;
  border-radius: 4px;
  background: #fff;
  color: #222;
  font: inherit;
}
.maintenance-category-controls button {
  align-self: end;
  cursor: pointer;
  background: #184c99;
  border-color: #184c99;
  color: #fff;
  font-weight: 600;
}
.maintenance-category-controls button:hover {
  background: #123b78;
}
.maintenance-category-browser a {
  color: #0645ad;
  text-decoration: underline;
  text-underline-offset: 0.15em;
}
.maintenance-category-date {
  display: inline-block;
  margin-left: 0.35em;
  color: #444;
  font-size: 0.9em;
}
#maintenance-category-count {
  color: #444;
  margin: 0.5em 0;
}
#maintenance-category-list {
  line-height: 1.8;
  padding-left: 1.5em;
}
#maintenance-category-list li {
  margin: 0.25em 0;
}
body.tsap-dark-mode .maintenance-category-browser {
  color: #e5e7eb;
}
body.tsap-dark-mode .maintenance-category-controls {
  background: #1f2937;
  border-color: #4b5563;
}
body.tsap-dark-mode .maintenance-category-controls input,
body.tsap-dark-mode .maintenance-category-controls select {
  background: #111827;
  color: #f3f4f6;
  border-color: #6b7280;
}
body.tsap-dark-mode .maintenance-category-controls button {
  background: #1f5fbf;
  color: #fff;
  border-color: #1f5fbf;
}
body.tsap-dark-mode .maintenance-category-controls button:hover {
  background: #184c99;
}
body.tsap-dark-mode .maintenance-category-browser a {
  color: #93c5fd;
}
body.tsap-dark-mode .maintenance-category-browser a:hover {
  color: #bfdbfe;
}
body.tsap-dark-mode .maintenance-category-date,
body.tsap-dark-mode #maintenance-category-count {
  color: #cbd5e1;
}
@media (prefers-reduced-motion: reduce) {
  .maintenance-category-browser * {
    scroll-behavior: auto;
    transition: none !important;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const browser = document.querySelector('.maintenance-category-browser');
  if (!browser) return;

  const controls = browser.querySelector('.maintenance-category-controls');
  const list = browser.querySelector('#maintenance-category-list');
  const search = browser.querySelector('#maintenance-category-search');
  const sort = browser.querySelector('#maintenance-category-sort');
  const clear = browser.querySelector('#maintenance-category-clear');
  const count = browser.querySelector('#maintenance-category-count');
  const empty = browser.querySelector('#maintenance-category-empty');
  const items = Array.from(list.querySelectorAll('li'));

  controls.hidden = false;

  function updateList() {
    const query = search.value.trim().toLocaleLowerCase();
    const order = sort.value;
    const sorted = items.slice().sort(function (a, b) {
      if (order === 'oldest' || order === 'newest') {
        const dateA = a.dataset.created || (order === 'oldest' ? '9999-12-31' : '0000-01-01');
        const dateB = b.dataset.created || (order === 'oldest' ? '9999-12-31' : '0000-01-01');
        const dateOrder = dateA.localeCompare(dateB);
        if (dateOrder !== 0) return order === 'oldest' ? dateOrder : -dateOrder;
      }
      const nameOrder = a.dataset.name.localeCompare(b.dataset.name);
      return order === 'za' ? -nameOrder : nameOrder;
    });

    let visible = 0;
    sorted.forEach(function (item) {
      const matches = item.dataset.name.includes(query);
      item.hidden = !matches;
      list.appendChild(item);
      if (matches) visible += 1;
    });

    count.textContent = 'Showing ' + visible + ' of ' + items.length + ' maintenance categories';
    empty.hidden = visible !== 0;
  }

  search.addEventListener('input', updateList);
  sort.addEventListener('change', updateList);
  clear.addEventListener('click', function () {
    search.value = '';
    sort.value = 'az';
    updateList();
    search.focus();
  });

  updateList();
});
</script>

## YAML syntax {#yaml-syntax}

Add `hidden_categories` to a page's YAML front matter to assign one or more hidden categories manually.

```yaml
hidden_categories:
  - Pages needing regular archiving
```

For multiple assignments, add each category as a separate list item.

```yaml
hidden_categories:
  - Pages needing regular archiving
  - Pages needing review
```

The category name must match the corresponding category's name exactly.

## How hidden categories work {#how-hidden-categories-work}

The `hidden_categories` field is separate from the regular `categories` field. Regular categories appear in the category list at the bottom of a page, while hidden categories support maintenance and classification without appearing in that list.

A hidden category is not private or access-restricted. Its category page remains publicly accessible, and its assigned pages can still be listed there.

## Automatically populated maintenance categories {#automatic-maintenance-categories}

Not every maintenance category is assigned through the `hidden_categories` YAML field. Several are populated automatically by rules in the site's category layout, which checks page content for particular embeds, templates, links or reference headings.

The current automatic detection rules cover embedded YouTube videos, PDF documents, X posts and Facebook posts; media repository files; CIS website citations; custom notices; under construction templates; and pages with references.

For these automatically detected categories, a page can appear in the category listing because its content matches the relevant rule, without having that category name in either `categories` or `hidden_categories`. These rules are distinct from manually assigned hidden categories.

## How the layouts work {#how-the-layouts-work}

The site's [`_layouts/default.html`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/_layouts/default.html) includes [`_includes/categories.html`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/_includes/categories.html), which displays the page's regular `categories` assignments at the bottom of the page. It does not perform the special content detection used by maintenance category pages.

The [`_layouts/category.html`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/_layouts/category.html) layout contains the automatic detection rules for the special maintenance categories. For other categories, it combines pages assigned through the regular `categories` field with pages assigned through `hidden_categories`.

The category index in [`categories/index.md`](https://github.com/sunilabrahamindia/sunilabraham/blob/main/categories/index.md) contains corresponding counting rules for automatically detected categories and counts regular and hidden assignments for other categories.

When adding or modifying an automatically populated category, keep the listing logic in `_layouts/category.html` and the counting logic in `categories/index.md` consistent.

## Creating a hidden maintenance category {#creating-a-hidden-maintenance-category}

To create a new manually assigned hidden maintenance category:

1. Create a category page in the `categories/` directory.
2. Give it a descriptive title, permalink, description and creation date.
3. Assign it to the `Maintenance categories` category so that it appears in the maintenance category index.
4. Add its exact category name to the `hidden_categories` field of each relevant page.
5. Check the category page and one of the assigned pages to confirm that the category works as intended.

For example, a new category page could use this front matter:

```yaml
---
layout: category
title: "Category:Pages needing review"
description: "Pages identified for editorial or technical review."
permalink: /categories/pages-needing-review/
categories: [Maintenance categories]
created: 2026-10-13
---
```

A page that needs review can then include:

```yaml
hidden_categories:
  - Pages needing review
```

A manually assigned hidden category does not require a new automatic detection rule. However, if the category needs to identify pages automatically, the relevant layout and category-counting logic must also be updated.

## Future possibilities {#future-possibilities}

Additional maintenance categories may be introduced when a recurring editorial, preservation or technical requirement justifies them.

Possible examples include pages using other external embeds, pages needing review, and pages that depend on external resources that may change or disappear.

Before creating a new category, check whether an existing category already covers the requirement and whether the proposed category needs manual assignment or automatic detection.

## Best practices {#best-practices}

- Use descriptive category names that clearly explain the maintenance requirement.
- Keep category names consistent between category pages and YAML assignments.
- Use `hidden_categories` when a category is useful for maintenance but should not appear in the page's public category list.
- Use automatic detection only when a reliable rule can identify the relevant pages.
- Keep automatic listing and counting logic consistent.
- Review maintenance categories periodically and remove obsolete assignments when they are no longer needed.

## See also {#see-also}

- [TSAP documentation](/tsap/)
- [YAML front matter](/tsap/yaml/)
- [Site structure](/tsap/structure/)
- [Maintenance categories](/categories/maintenance-categories/)
- [All categories](/categories/)

{% include navbox-tsap.html %}
