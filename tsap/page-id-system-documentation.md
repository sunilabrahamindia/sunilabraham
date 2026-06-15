---
layout: default
title: "Page ID System (Documentation)"
description: "Documentation for the Page ID system used on The Sunil Abraham Project (TSAP), including its purpose, design principles, implementation methodology, maintenance workflow, and future development."
categories: [TSAP Documentation]
permalink: /tsap/page-id-system-documentation/
page_id: TSAP-1070
created: 2026-06-16
---

{% include documentation-notice.html %}

The **Page ID system** is a permanent identification framework used across The Sunil Abraham Project (TSAP). Each eligible page is assigned a unique identifier in the format `TSAP-0001`, `TSAP-0002`, and so forth. These identifiers are intended to provide a stable internal reference for pages regardless of future changes to titles, categories, metadata, or site structure.

The system was introduced on 16 June 2026, when permanent identifiers were assigned to 1,069 existing pages across the project. Although TSAP already maintains stable permalinks and does not normally change URLs, the introduction of Page IDs provides an additional metadata layer that may support future structured-data initiatives, internal tooling, exports, archival workflows, and repository-wide analysis.

Page IDs are not intended to replace page titles or permalinks. Instead, they function as accession numbers within the archive, providing a permanent identifier for each eligible page.

The implementation was developed with support from ChatGPT. All design decisions, testing, editorial judgement, and final implementation choices were made by the project maintainer.

## Background

As TSAP expanded beyond one thousand pages, the project increasingly began to resemble a structured digital archive rather than a conventional website. Existing metadata systems already included page titles, categories, authorship information, creation dates, and stable permalinks. However, no permanent identifier existed that could uniquely reference a page independently of its title or URL.

Several future initiatives highlighted the potential value of such identifiers. These included machine-readable exports, repository-wide indexing, structured-data experiments, authority-control work, internal references, maintenance reporting, and possible future knowledge-graph style tooling.

Although stable permalinks already provide a practical means of identifying pages, a dedicated identifier system offers a simpler and more consistent reference mechanism for future technical development.

Following discussion and evaluation, the project adopted a permanent Page ID system.

## Objectives

The Page ID system was designed to satisfy several objectives:

1. Provide a unique permanent identifier for eligible pages.
2. Avoid dependence on titles, filenames, or URLs.
3. Remain simple and human-readable.
4. Require minimal ongoing maintenance.
5. Scale to several thousand pages.
6. Integrate naturally with existing metadata structures.
7. Support future structured-data initiatives.

The system deliberately prioritises simplicity over complexity.

## Page ID Format

All identifiers use the following format:

```text
TSAP-0001
TSAP-0002
TSAP-0003
```

The prefix identifies the page as part of The Sunil Abraham Project. The numeric component is sequential and currently uses four digits. The numbering system provides capacity for up to 9,999 identifiers before any expansion would be required.

Page IDs are stored within page front matter:

```yaml
page_id: TSAP-0842
```

The field is positioned immediately before the `created:` field as part of the project's metadata conventions.

## Relationship to Creation Dates

Page IDs and creation dates serve different purposes.

The `created:` field records when a page entered the project.

```yaml
created: 2026-05-15
```

The `page_id:` field records the page's permanent identifier.

```yaml
page_id: TSAP-0842
```

Although the initial migration used creation dates to determine numbering order, the two fields should not be considered interchangeable. Creation dates represent chronology. Page IDs represent identity.

## Initial Migration (16 June 2026)

The Page ID system was introduced through a one-time repository-wide migration completed on 16 June 2026. A Python script scanned eligible Markdown files throughout the repository and assigned identifiers sequentially.

The migration assigned Page IDs to 1,069 pages. Identifiers were generated using the following methodology:

1. Identify eligible pages.
2. Sort pages by `created:` date.
3. Use file path ordering as a secondary tie-breaker.
4. Assign identifiers sequentially.
5. Insert the resulting `page_id:` value into front matter.

The migration was reviewed manually before being committed to the repository.

## Eligibility Rules

The migration was intentionally limited to pages considered part of the active TSAP archive. In general, pages containing a valid `created:` field were considered eligible for inclusion. Some pages were excluded because they had been deleted, converted into drafts, removed from active use, or otherwise fell outside the scope of the migration.

The Page ID system therefore reflects the state of the repository at the time the migration was performed rather than every page that has ever existed within the project.

## Maintenance Workflow

Following the initial migration, Page IDs are assigned manually when new pages are created.

The current workflow is:

1. Create a new page.
2. Determine the next available Page ID.
3. Add the identifier to front matter.
4. Publish the page.

Example:

```yaml
page_id: TSAP-1071
```

Once assigned, a Page ID must never be changed.

### Identifiers Are Never Reused

Page IDs are permanent identifiers and must never be reassigned.

If a page is deleted, merged, draftified, or otherwise removed from active use after receiving a Page ID, that identifier remains permanently reserved.

For example, if `TSAP-0773` is assigned to a page that is later removed, future pages will continue with the next available identifier rather than reusing the vacant number.

The numbering sequence therefore records identifier assignment rather than the current number of active pages. Gaps may emerge over time as pages are removed, but such gaps are considered a normal consequence of maintaining permanent identifiers.

## Future Helper Script

A future maintenance utility is planned to simplify assignment of new identifiers. The proposed script will examine existing Page IDs and report the next available value.

Example:

```bash
python3 scripts/next_page_id.py
```

Expected output:

```text
Highest page_id: TSAP-1070
Next available: TSAP-1071
```

At the time of writing, this helper script has not yet been implemented.

## Current Uses

At present, the Page ID system primarily serves as a metadata and archival feature. The identifiers provide:

- Permanent page references.
- Structured metadata.
- Repository-wide consistency.
- Future extensibility.

The system currently operates largely behind the scenes and is not yet heavily utilised by site features.

## Potential Future Uses

Several possible future applications have been identified.

These include:

- Structured JSON exports.
- Internal reference systems.
- Editorial maintenance tools.
- Authority-control integration.
- Data analysis workflows.
- Knowledge-graph experimentation.
- Cross-dataset references.
- Machine-readable catalogues.
- Search and indexing enhancements.

Implementation of these possibilities remains under consideration.

## Advantages

The Page ID system provides several advantages. Because identifiers never change, they offer a stable reference mechanism independent of titles and URLs. The system remains simple, transparent, and easy to understand. It requires very little storage and scales naturally as the repository grows.

The implementation also creates a foundation for future structured-data work without introducing significant maintenance overhead.

## Known Limitations

Several limitations should be understood when interpreting Page IDs.

### Chronology Is Approximate

The initial migration used the `created:` field as the primary sorting mechanism. However, many pages share the same creation date. When this occurred, file path ordering was used as a secondary tie-breaker. As a result, Page IDs should not be interpreted as precise publication-order indicators.

For example, two articles created on the same day may receive identifiers that do not reflect the exact order in which they were originally written or published. An article created later in the day may occasionally receive a lower identifier than an article created earlier or vice versa.

### Deleted and Draft Pages

Before the migration was performed on 16 June 2026, a small number of pages had already been deleted, merged, draftified, or otherwise removed from active use. These pages did not receive identifiers. Consequently, the Page ID system reflects the active archive as it existed at the time of migration rather than every page that has ever existed within the repository.

### Milestone Counts May Differ

Page IDs should not be interpreted as page-count milestones. For example, a Page ID of `TSAP-1000` does not necessarily indicate that the page was the one-thousandth page ever created for the project.

Because some pages were deleted, draftified, merged, or excluded before the migration occurred, Page IDs and milestone counts may occasionally diverge.

The project's page-count milestones, including those documented at:

```text
/articles/sunil-abraham-project/
```

should therefore be treated as separate historical records.

### Manual Assignment

Following the initial migration, new identifiers are assigned manually. This introduces a small possibility of accidental numbering errors until automated helper tooling is introduced.

## Future Improvements

Future enhancements may include:

- Automated next-ID discovery.
- Validation scripts.
- Duplicate-ID detection.
- Missing-ID reporting.
- Integration with JSON exports.
- Additional structured-data tooling.
- Visual display within Page Data components.

Any future developments should continue to prioritise simplicity, transparency, maintainability, and long-term compatibility with TSAP's static-site architecture.
