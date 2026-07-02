---
layout: default
title: "Git Repository Storage Inflation Incident (1 July 2026)"
description: "Documentation of the repository storage inflation incident on 1 July 2026, the diagnostic tracking, history rewrite operations, and final backend resolution."
categories: [TSAP Documentation, TSAP Incidents]
permalink: /tsap/git-repository-storage-inflation/
created: 2026-07-02
---

{% include documentation-notice.html %}

On **1 July 2026**, the remote GitHub repository for `sunilabrahamindia/sunilabraham` experienced an unexpected storage inflation. The repository size nearly doubled, rising from its long-standing operational baseline of approximately 93–95 MB to over 202 MB, reported by the GitHub API as `202848` KB.

This document records the root cause of the storage spike, the systematic investigation and recovery process, the history rewrite operations executed across the local and remote repositories, and the final verification of the repository's structural integrity.

## Original Repository Baseline

Prior to the incident, the repository had been closely monitored and maintained at a highly optimised footprint of 93–95 MB. This efficient baseline encompassed:

- Over 1,100 structured Markdown documentation pages.
- Associated static assets, including images and PDF reference archives.
- Jekyll layouts, custom stylesheet engines, and reusable includes.
- Automated GitHub Pages deployment infrastructure.

## Root Cause of the Incident

The storage inflation occurred while attempting to clear approximately 3,000 unexpected ghost Git tracking changes within the local development environment. To isolate files safely, a temporary directory named `.git-backup` was created inside the project directory.

The backup directory immediately added substantial weight to the project:

- **`.git-backup` size:** approximately 120 MB

Because the backup directory was created inside the repository working tree, it became visible to Git and was inadvertently staged and committed. Keeping temporary Git backups outside the repository would have avoided this risk.

The GitHub API immediately reflected the increased repository size:

```text
"size": 202848
```

The `.git-backup` directory also became visible through the GitHub web interface.

## Isolation and History Diagnostics

To validate a recovery workflow without risking the production repository, an isolated clone was created at:

```text
~/Documents/tsap-clean
```

Inside this sandbox environment, the repository history was rewritten using:

```bash
git filter-repo --path .git-backup --invert-paths
```

Following the history rewrite, aggressive garbage collection and repository integrity verification were performed.

The isolated test produced several important observations:

- The `.git-backup` directory disappeared completely from repository history.
- The local `.git` database reduced from approximately 235 MB to approximately 92 MB.
- The working tree remained completely intact with no loss of Markdown content or site assets.

These results confirmed that a targeted history rewrite was the correct approach to remove the accidental backup directory without affecting the website itself.

## Implementation and Remote Alignment

Once the recovery workflow had been validated, a complete safety backup of the production repository was created. The same history rewrite process was then repeated inside the primary working copy located at:

```text
~/Projects/sunilabraham
```

### 1. Database Pruning and Credential Alignment

The local Git database was successfully rewritten and compacted to approximately 93 MB.

Since `git filter-repo` intentionally removes existing remote configuration to prevent accidental force-pushes, the GitHub remote was re-added.

GitHub CLI authentication was then configured:

```bash
gh auth setup-git
```

The active credentials for the `sunilabrahamindia` account were verified successfully.

### 2. Overwriting the Remote Repository History

The cleaned repository history was then force-pushed to GitHub:

```bash
git push --force origin main
```

The push completed successfully, and the `.git-backup` directory immediately disappeared from the GitHub web interface.

## The Storage Lag Paradox

Immediately after the successful force-push, the GitHub web interface reflected the corrected repository contents, but the GitHub API continued to report:

```text
"size": 202848
```

This prompted a secondary investigation into whether deleted objects remained referenced elsewhere. This behaviour is expected because GitHub performs garbage collection asynchronously after history rewrites.

### Auditing the `gh-pages` Branch

Attention turned to the legacy `gh-pages` branch, which had not been updated for approximately nine months.

A read-only inspection was performed using:

```bash
git fetch origin
git ls-tree -r --name-only origin/gh-pages | grep "^\.git-backup"
```

The command produced no output, confirming that the `gh-pages` branch did not contain the deleted directory.

This established that the persistent 202 MB measurement did not indicate a failed history rewrite. Instead, it reflected GitHub's normal server-side storage accounting delay while background garbage collection processed the orphaned objects.

## Final Verification and Resolution

Within approximately 24 hours of the history rewrite, GitHub completed its background cleanup process.

A fresh API query reported:

```text
"size": 91587
```

Converting the reported size:

```text
91587 KB ÷ 1024 ≈ 89.4 MB
```

This closely matches the local Git database size of approximately 93 MB, allowing for differences in GitHub's internal storage accounting and compression.

The repository had therefore returned to its expected operational footprint,confirming that the repository had returned to its expected operational state.

## Core Maintenance Lessons

1. **Maintain Explicit Ignore Rules:** A committed `.gitignore` (or appropriate exclusion strategy) should always be maintained so that temporary backups, caches, and local working files cannot accidentally enter repository history.
2. **Treat Local Repositories as Disposable:** Distributed version control allows any verified clone of the repository to serve as a recovery source, reducing dependence on a single working copy or hosting provider.
3. **Separate Content from Repository Metadata:** Static-site content remains independent of Git's internal object database. Even major repository maintenance operations, including history rewriting, do not affect the underlying Markdown content when performed correctly.
4. **Keep Temporary Git Repositories Outside the Working Tree:** Backup repositories, experimental clones, and temporary Git directories should always be created outside the active project directory to prevent accidental staging or commits.
