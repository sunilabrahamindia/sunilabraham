---
layout: default
title: "Page ID Sequence Gap and Correction (15 October 2026)"
description: "Documentation of the missing TSAP-1321 identifier, the investigation into the Page ID sequence, the correction of five existing pages, and the assignment of IDs to ten new pages."
categories: [TSAP Documentation, TSAP Incidents]
permalink: /tsap/page-id-sequence-correction/
created: 2026-10-15
---

{% include documentation-notice.html %}

On **15 October 2026**, a gap was identified in the sequential Page ID system used by The Sunil Abraham Project (TSAP). The identifier `TSAP-1321` was missing, even though later identifiers had already been assigned. The gap was discovered during a review of the repository's Page IDs and page inventory.

This document records the investigation, the corrective changes, the verification performed, and the maintenance lessons arising from the incident. The precise event that originally caused `TSAP-1321` to be skipped was not established.

## Incident Summary

The Page ID system assigns identifiers in the format `TSAP-0001`, `TSAP-0002`, and so on. The identifiers are intended to provide stable, unique references to individual pages.

During the review, the sequence contained the following gap:

- `TSAP-1321` had no corresponding page.
- `TSAP-1322` through `TSAP-1326` were assigned to five existing pages.
- Ten newly added Markdown pages did not yet have Page IDs.

The gap was close to the end of the assigned sequence, so it could be corrected without renumbering a large part of the repository.

## Investigation

### 1. Checking for References

A repository-wide text search was performed for the identifiers `TSAP-1321` through `TSAP-1326`, excluding the Git database and `pages.json`. The search found no references to these identifiers outside the relevant pages' own `page_id` fields. A separate search of `pages.json` did not find these identifier strings.

This check helped establish that the five existing identifiers could be adjusted without finding any additional in-repository references that also needed changing.

### 2. Establishing the Correction

The five existing Page IDs were shifted down by one position. The change restored the missing identifier and kept the existing pages in sequence:

| Page | Previous Page ID | Corrected Page ID |
|---|---|---|
| `tspa/0022.md` | `TSAP-1322` | `TSAP-1321` |
| `tspa/0023.md` | `TSAP-1323` | `TSAP-1322` |
| `tito/mind.md` | `TSAP-1324` | `TSAP-1323` |
| `tspa/0024.md` | `TSAP-1325` | `TSAP-1324` |
| `tspa/0025.md` | `TSAP-1326` | `TSAP-1325` |

The five corrections were committed together on GitHub. The change can be inspected in the [Page ID correction commit](https://github.com/sunilabrahamindia/sunilabraham/commit/ee3ec42a2ee6cdfcef6661d315b651ce38fcb4d7).

### 3. Assigning IDs to New Pages

After pulling the correction into the local working copy, the existing script was run:

```bash
git pull
python3 scripts/add_page_ids.py
```

The script assigned the next ten identifiers, from `TSAP-1326` through `TSAP-1335`, to the ten Markdown pages that lacked IDs. It reported `TSAP-1336` as the next available identifier.

The script's output confirmed that ten assignments had been made. The resulting changes were then reviewed manually in the VS Code diff window. This review method made it possible to inspect the modified files side by side and check that the intended Page ID lines had changed.

## Resolution and Verification

The correction restored the sequence at the point where the gap had occurred:

- `TSAP-1321` through `TSAP-1325` now belong to the five existing pages listed above.
- `TSAP-1326` through `TSAP-1335` were assigned to the ten previously unassigned pages.
- `TSAP-1336` is the next available identifier.

The repository-wide search found no additional in-repository references to the affected IDs outside their own Page ID fields. The new assignments were also reviewed through the VS Code diff window. The incident did not require a broad renumbering of the site's pages.

## Maintenance Lessons

1. **A page count alone does not prove that the sequence is complete.** A repository can contain the expected number of pages and still have a missing identifier if another part of the sequence is affected.

2. **Assigning IDs and auditing IDs are different tasks.** The `scripts/add_page_ids.py` script assigns identifiers to pages that do not have them. A separate integrity check should detect gaps, duplicate assignments, malformed IDs, and unexpected sequence changes.

3. **Manual diff review remains useful.** Reviewing the script's changes in VS Code provides a clear way to confirm that only the intended lines have changed. Automated checks can complement this review rather than replace it.

4. **Investigate before renumbering.** Before correcting a gap, search for references to the affected identifiers and establish the scope of the change. In this incident, the missing identifier was near the end of the sequence, limiting the repair to five existing pages.

5. **Keep the cause distinct from the evidence.** The gap was confirmed and corrected, but the exact action that originally caused `TSAP-1321` to be skipped was not established. The record should not claim a root cause that the investigation did not prove.

## Recommended Follow-up

A separate, read-only Page ID audit script would reduce reliance on manual detection. It should report missing sequence numbers, duplicate IDs, malformed identifiers, and pages without IDs, without modifying any files. It can be run alongside the existing assignment script during the usual periodic maintenance routine.

{% include navbox-tsap.html %}
