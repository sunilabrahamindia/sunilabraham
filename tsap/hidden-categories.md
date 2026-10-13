---
layout: default
title: "Hidden Categories and Maintenance Categories"
description: "Documentation of hidden category assignments and automatically populated maintenance categories in The Sunil Abraham Project."
permalink: /tsap/hidden-categories/
categories: [TSAP Documentation]
created: 2026-10-13
---

{% include documentation-notice.html %}


**Hidden and maintenance categories** allow The Sunil Abraham Project to classify pages for maintenance, preservation and technical tracking without displaying those categories in the category list at the bottom of individual pages. This page documents the current maintenance categories, their implementation and how to assign hidden categories through YAML front matter.

## Purpose {#purpose}

Maintenance categories help identify pages that need periodic attention, use particular embeds or templates, or meet specific technical criteria.

Some maintenance categories are populated automatically by the site's Liquid templates, while others can be assigned manually through the `hidden_categories` YAML field.

Hidden categories are not private or access-restricted. Their category pages remain publicly accessible, and assigned pages can still appear in those category listings.

## Current Maintenance Categories {#current-maintenance-categories}

The following maintenance categories currently exist:

1. [Pages using embedded YouTube videos](/categories/pages-using-embedded-youtube-videos/)
2. [Pages using embedded PDF documents](/categories/pages-using-embedded-pdf-documents/)
3. [Pages using embedded X posts](/categories/pages-using-embedded-x-posts/)
4. [Pages using embedded Facebook posts](/categories/pages-using-embedded-facebook-posts/)
5. [Pages using media repository files](/categories/pages-using-media-repository-files/)
6. [Pages citing CIS website](/categories/pages-citing-cis-website/)
7. [Pages displaying custom notices](/categories/pages-displaying-custom-notices/)
8. [Pages using under construction template](/categories/pages-using-under-construction-template/)
9. [Pages with references](/categories/pages-with-references/)
10. [Pages needing regular archiving](/categories/pages-needing-regular-archiving/)

These categories are collected under [Maintenance categories](/categories/maintenance-categories/).

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
