---
layout: default
title: "Local Development Environment Crash During Wayback Archiving (5 November 2026)"
description: "Record of the local development environment crash during a TSAP Wayback Machine archiving session, the repository checks performed afterwards, and the findings that remain unconfirmed."
categories: [TSAP Documentation, TSAP Incidents]
permalink: /tsap/local-development-crash-wayback-archiving/
created: 2026-11-05
---

{% include documentation-notice.html %}

On **5 November 2026**, a crash interrupted a local TSAP maintenance session while the [Wayback Machine Random Archiver](/tsap/wayback-machine-random-archiver-documentation/) script was running. Approximately 20–30 pages had been archived successfully before the interruption. The incident affected the local development session and the ability to continue working, but the checks performed afterwards did not establish that the Git repository or its files had been corrupted.

This record documents the observed sequence, the repository checks, the available system-log evidence, and the precautions for resuming the archiving work. The underlying cause of the crash has not been established.

## Incident Summary

The incident took place on the Ubuntu laptop used for local TSAP development. The script being run was:

```text
scripts/wayback_random_archiver.py
```

During the archiving session:

1. The script had successfully archived approximately 20–30 pages.
2. The user switched to Firefox and selected the Edit link for a repository file through a quick link on the website.
3. The first Firefox tab crashed. A second tab also crashed when the same action was attempted.
4. On returning to the terminal, the output included a message resembling a core dump and an indication that the repository or filesystem was read-only.
5. The terminal then crashed while the user was attempting to close it or copy its output.
6. The laptop was powered off and restarted.

The exact order and internal cause of the application failures could not be established from the surviving evidence. In particular, the read-only indication was observed in the terminal, but it was not independently confirmed as a persistent filesystem state.

## Repository Integrity Checks

The local repository was checked after the restart before any further archiving work was attempted.

### 1. Initial Git Status

The first status check reported:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

This showed that Git did not report uncommitted changes or an obvious working-tree problem at the time of that check. It did not, by itself, establish that every local file or the underlying filesystem was free of damage.

### 2. Pulling the Latest Remote Changes

A fast-forward-only pull was then run:

```bash
git pull --ff-only
```

Git updated the local branch from `c9603942` to `6e903939`. The pull brought in 18 files, including changes to documentation, site data, navigation, and the EDRL-II ebook build files. The pull completed as a fast-forward; no merge conflict or manual conflict resolution was reported.

A subsequent status check reported:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

The local repository was therefore clean and aligned with the remote branch after the pull. The earlier status check and the later fast-forward pull are both recorded here as observed. The available information does not establish why the remote changes were not included in the earlier status result.

### 3. Review of GitHub Activity

The relevant GitHub history for 5 November was inspected. The commits examined included:

- A repository-size measurement update that changed only `_data/repository_size_log.json`.
- A research funding guide update affecting `tsap/research-funding-guide.md`.
- A small edit to `tito/continuity.md` removing the `homepage_featured` front-matter setting.

These inspected commits did not indicate an accidental mass edit or a change caused by the local crash. The repository's later fast-forward pull also completed normally.

## System Log Review

The previous boot's kernel warnings and error-level messages were reviewed using the system journal.

The review showed that the system and user journal files were reported as corrupted or not cleanly shut down and were renamed and replaced during the subsequent boot. This is consistent with the laptop having been powered off without a normal shutdown. It is not, on its own, proof of filesystem damage.

The kernel log also showed the normal boot-time sequence in which the root filesystem was initially mounted read-only and then re-mounted read-write. That initial read-only mount is part of the boot sequence and must not be confused with evidence that the filesystem remained read-only during the incident.

A targeted search of the previous boot's kernel log did not return explicit EXT4 filesystem errors, block I/O errors, or NVMe controller reset messages. Some NVMe and graphics firmware warnings were present, but those messages alone do not identify the cause of the crash.

The available log review therefore did not establish a persistent read-only filesystem, an NVMe failure, or an EXT4 error. It also cannot rule out every possible hardware, kernel, application, or resource-related problem.

## Findings and Limits

The checks support the following conclusions:

- The Wayback archiving session was interrupted after approximately 20–30 successful page archives.
- Firefox tabs and the terminal crashed during the same work session.
- The terminal displayed an apparent core-dump message and a read-only indication, but the exact message was not preserved and the read-only state was not independently confirmed.
- Git reported a clean working tree after the restart. A subsequent fast-forward pull completed, and the final Git status was clean and up to date.
- The inspected GitHub commits did not show evidence of accidental repository-wide changes associated with the incident.
- The journal reported an unclean shutdown. The reviewed kernel output did not show explicit EXT4 or NVMe I/O failure messages.
- **The root cause remains unknown.** The available evidence is insufficient to attribute the incident to Firefox, Python, the archiver script, Git, the filesystem, the NVMe drive, memory pressure, or any particular hardware component.

No filesystem repair, Git database repair, history rewrite, or repository reset was required as part of the checks recorded here.

## Recovery and Safe Resumption

The local repository was brought up to date with the remote branch and verified as clean. That resolves the repository synchronisation check, but it does not explain the application and terminal crashes.

Before resuming the random archiving session, the following precautions are appropriate:

1. **Preserve the completed work.** Review the archiver's output or log, if available, and check the relevant Wayback captures before running the script again. This avoids needlessly repeating requests for pages that may already have been archived.
2. **Resume in a separate session.** Do not immediately restart the same long-running process in the same terminal session. Start with a small, controlled run and observe whether the system remains stable.
3. **Keep the repository state verifiable.** Check the working tree before and after the next run. The archiving script should not modify site content unless that is explicitly part of its design.
4. **Retain useful failure output.** If a similar failure recurs, record the exact terminal message and the time of the event before restarting, where it is safe and possible to do so.
5. **Avoid assuming that a successful Git check proves hardware health.** Git status and a successful pull verify repository-level conditions; they are not comprehensive tests of the filesystem, storage device, memory, or operating system.

These are precautionary steps rather than a diagnosis or a claim that the archiver caused the crash.

## Maintenance Lessons

1. **A local development failure is not automatically repository corruption.** Check the Git working tree and remote alignment before attempting destructive recovery operations.
2. **Use the remote repository as a reference, not as a reason to reset immediately.** In this case, a normal fast-forward pull was sufficient. There was no evidence requiring `git reset --hard`, deletion of Git metadata, or history rewriting.
3. **Distinguish an observed message from a verified system condition.** A terminal indication of read-only mode should be investigated, but it should not be recorded as a confirmed filesystem state without corroborating evidence.
4. **Keep archiving progress recoverable.** A record of completed URLs or a clear run log makes it easier to resume a partially completed Wayback session without repeating work.
5. **Record uncertainty explicitly.** The application crashes, unclean shutdown, and journal warnings are confirmed observations. Their causal relationship is not established.

## Status

The local repository was synchronised with the GitHub `main` branch and reported a clean working tree after the pull. No repository corruption was identified in the checks performed. The Wayback archiving task was interrupted, and the cause of the laptop and application crashes remains undetermined.

This incident is recorded because it interrupted a TSAP preservation and maintenance operation and involved the local TSAP development environment. It is not a general record of laptop health or a confirmed storage-device failure.

{% include navbox-tsap.html %}
