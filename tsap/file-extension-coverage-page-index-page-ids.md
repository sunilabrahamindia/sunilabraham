---
layout: default
title: "File Extension Coverage Gap in Page Indexing and Page ID Assignment (11 November 2026)"
description: "Documentation of the file-extension coverage gap affecting the TSAP Pages Index and Page ID assignment scripts, the inclusion of SVG pages, and the introduction of a repository-wide Page ID audit."
categories: [TSAP Documentation, TSAP Incidents]
permalink: /tsap/file-extension-coverage-page-index-page-ids/
created: 2026-11-11
---

{% include documentation-notice.html %}

On **11 November 2026**, a discrepancy was identified between the files appearing in TSAP's page listings and the files included in its machine-readable pages.json index and Page ID assignment process. An SVG page, amaa/invitation.svg, was present as a TSAP page but was not being included by the scripts responsible for generating the Pages Index and assigning Page IDs.

The investigation established that the relevant scripts used different file-extension filters. The Page ID assignment script scanned Markdown files with the .md extension, while the Pages Index generator scanned .md and .markdown files. Neither script included .svg files. This document records the discovery, the changes made to the scripts, the audit introduced during the correction, and the verification of the resulting repository state.

## Incident Summary

The discrepancy became apparent during a review of the repository's newest pages and the contents of pages.json. The SVG invitation page was visible as a TSAP page but was absent from the generated JSON index. The same extension restriction also meant that the existing Page ID assignment script would not assign an identifier to that SVG page.

The issue was not a missing or malformed Page ID in an otherwise eligible Markdown page. It was a file-eligibility problem: the scripts did not recognise every file type used for TSAP pages.

## Investigation

### 1. Comparing the Scripts

The two scripts had separate extension filters:

- scripts/add_page_ids.py scanned files with the .md extension.
- scripts/generate_pages_json.py scanned files with the .md and .markdown extensions.

Neither script scanned .svg files. As a result, an SVG page containing YAML front matter and a created: field could be omitted from both processes.

### 2. Identifying the Affected Page

The page that exposed the discrepancy was:

~~~text
amaa/invitation.svg
~~~

It contained page metadata and was part of the TSAP content inventory, but the file-extension filters prevented it from being handled by the two scripts.

The investigation therefore focused on aligning the scripts' file coverage while retaining their existing front-matter eligibility rules.

## Corrective Changes

### 1. Updating Page ID Assignment

The file scan in scripts/add_page_ids.py was expanded to include:

- .md
- .markdown
- .svg

The script continues to identify eligible pages through their front matter and created: field. Existing identifiers are retained, and new identifiers are assigned after the highest existing Page ID.

### 2. Updating the Pages Index Generator

The file scan in scripts/generate_pages_json.py was also expanded to include .svg files. The generator continues to include files with valid YAML front matter containing a created: field.

After this correction, the generated pages.json contained **1,378 entries**, including the SVG invitation page.

### 3. Introducing a Read-only Page ID Audit

A separate script, scripts/audit_page_ids.py, was added. Unlike the assignment script, it does not modify files or assign identifiers. It checks the eligible repository pages and reports:

- Pages with valid Page IDs.
- Pages without Page IDs.
- Malformed identifiers.
- Duplicate identifier values.
- Missing sequence numbers.
- The highest valid identifier.
- The next available identifier.

The audit covers the same three file extensions: .md, .markdown, and .svg.

## Page ID Assignment

After the updated scripts were pulled into the local repository, the Page ID assignment script was run again. It assigned six identifiers:

| Page ID | File |
|---|---|
| TSAP-1373 | amaa/30-print-book-production.md |
| TSAP-1374 | amaa/invitation.svg |
| TSAP-1375 | categories/vibodh-parthasarathi.md |
| TSAP-1376 | vibodh/template.md |
| TSAP-1377 | tito/omeconomy.md |
| TSAP-1378 | tspa/0030.md |

The script reported TSAP-1372 as the highest existing identifier before these assignments and TSAP-1379 as the next available identifier afterwards.

The six changes were reviewed, committed, and pushed to the main branch. The commit was:

~~~text
7fe0f7e9
Assign Page IDs to six new pages
~~~

## Audit and Verification

The new read-only audit script was run after the assignments. Its output was:

~~~text
TSAP PAGE ID AUDIT
==================
Eligible pages       : 1378
Pages with valid IDs : 1378
Pages without IDs    : 0
Malformed IDs        : 0
Duplicate ID values  : 0
Missing sequence IDs : 0
Highest valid ID     : TSAP-1378
Next available ID    : TSAP-1379

AUDIT RESULT: PASS
~~~

The audit therefore confirmed that all 1,378 eligible pages had valid identifiers, with no missing IDs, malformed IDs, duplicate values, or missing sequence numbers.

The Pages Index generator had also been updated to include SVG files, and the regenerated pages.json contained 1,378 entries.

## Workflow and Documentation Updates

The following repository files were changed as part of the correction:

- scripts/add_page_ids.py
- scripts/generate_pages_json.py
- scripts/audit_page_ids.py (new)
- tsap/pages-json-documentation.md
- .github/workflows/pages.yml

The GitHub Actions workflow was also updated with concurrency control for generated-index updates and a pull/rebase step before pushing generated changes. These changes were intended to reduce conflicts when workflow runs overlap.

The Pages Index documentation was updated to describe the supported file extensions and the revised generation process.

## Maintenance Lessons

1. **File eligibility must be consistent across related scripts.** A page type recognised by the website or content inventory should not be silently omitted by an index or identifier-assignment process because of a narrower extension filter.

2. **File extensions are part of the indexing rules.** The scripts must explicitly document and maintain the file types they support. Adding a new page format should prompt a review of all repository-wide indexing and metadata scripts.

3. **Assignment and validation are separate operations.** The assignment script adds identifiers to eligible pages. The audit script independently checks the integrity of the resulting identifier set without changing repository files.

4. **A successful assignment run is not a complete integrity check.** A script can assign IDs to the files it scans while remaining unaware of other eligible files excluded by its extension filter. An independent audit using the intended eligibility rules helps expose such omissions.

5. **Generated indexes and page metadata should be checked together.** The Pages Index and Page ID system serve different purposes, but both depend on recognising the same eligible content inventory.

## Status

The extension filters in both scripts were updated to include .svg files. The Pages Index was regenerated with 1,378 entries, and six Page IDs were assigned, including TSAP-1374 for amaa/invitation.svg.

The read-only audit reported **AUDIT RESULT: PASS**, with all 1,378 eligible pages carrying valid, unique, sequential identifiers. The six Page ID assignments were committed and pushed to GitHub.

{% include navbox-tsap.html %}
