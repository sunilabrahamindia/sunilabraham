---
layout: default
title: "Linux and Git Commands for TSAP Repository Maintenance"
description: "A practical reference of Linux, Git, and GitHub CLI commands used to inspect, diagnose, and maintain The Sunil Abraham Project (TSAP) repository."
categories: [TSAP Documentation]
permalink: /tsap/linux-git-commands/
created: 2026-07-16
---

{% include documentation-notice.html %}

The **Linux and Git Commands for TSAP Repository Maintenance** page documents commands that have proved useful in maintaining, inspecting, and troubleshooting The Sunil Abraham Project (TSAP) repository. It is intended as a practical project-specific reference rather than a general Linux, Git, or command-line tutorial.

The commands documented here include tools for checking repository size, identifying large files and Git objects, and inspecting commits and diffs. Most commands are standard Linux or Git commands, while future additions may include GitHub CLI commands or utilities commonly available on Ubuntu.

This reference is intended to grow gradually as commands prove useful in actual TSAP maintenance. Commands are included based on practical project needs rather than to provide a comprehensive Linux or Git command reference.

## Check Git Repository Storage Usage

This command shows how much storage is being used by Git objects in the local repository. It provides information about loose objects, packed objects, pack files, and any garbage objects that may be present.

Run the command from the repository directory:

```bash
git count-objects -vH
```

A typical output may look like:

```text
count: 701
size: 6.16 MiB
in-pack: 20901
packs: 2
size-pack: 90.67 MiB
prune-packable: 4
garbage: 0
size-garbage: 0 bytes
```

The values mean:

- `count`: Number of loose Git objects that have not been packed.
- `size`: Total storage occupied by loose Git objects.
- `in-pack`: Number of Git objects stored inside pack files.
- `packs`: Number of pack files in the repository.
- `size-pack`: Total storage occupied by the pack files. This is particularly useful for monitoring the size of packed Git history.
- `prune-packable`: Number of loose objects that also exist inside pack files and may therefore be eligible for removal.
- `garbage`: Number of files in the Git object database that Git considers invalid or unusable.
- `size-garbage`: Total storage occupied by garbage files.

For routine TSAP repository monitoring, `size` and `size-pack` are the most useful values. Changes in these figures over time can help identify unexpected repository growth.

## Check the Total Size of the Local Git Repository

This command shows the total disk space occupied by the repository's `.git` directory. Unlike `git count-objects -vH`, it provides a simple overall measurement that includes Git objects and other internal Git data.

Run the command from the repository directory:

```bash
du -sh .git
```

A typical output may look like:

```text
100M    .git
```

The value represents the total local size of the `.git` directory. It is useful for quickly monitoring repository growth, but it should not be treated as identical to the repository size reported by GitHub because local and remote Git storage may be packed and maintained differently.

## Find the 20 Largest Files in Git History

This command identifies the 20 largest file objects stored anywhere in the repository's Git history. It can reveal large files that currently exist in the repository as well as older versions or deleted files that remain stored in Git history.

Run the command from the repository directory:

```bash
git rev-list --objects --all |
git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
awk '$1=="blob"' |
sort -k3 -nr |
head -20 |
numfmt --field=3 --to=iec
```

The results are displayed from largest to smallest, with file sizes shown in a human-readable format such as MB or KB.

## Inspect What a Specific Commit Changed

These commands show what changed in a particular Git commit. They are useful for investigating unexpectedly large commits, identifying affected files, and determining how many lines were added or removed.

First, view a summary of the commit:

```bash
git show --stat COMMIT_ID
```

To see the number of added and deleted lines for each affected file:

```bash
git diff COMMIT_ID^ COMMIT_ID --numstat
```

To view the complete diff of the commit:

```bash
git diff COMMIT_ID^ COMMIT_ID
```

Replace `COMMIT_ID` with the commit hash being investigated. For example:

```bash
git show --stat 936d737
git diff 936d737^ 936d737 --numstat
git diff 936d737^ 936d737
```

These commands are particularly useful when a commit appears to have unexpectedly rewritten a large file, as happened during the investigation of repeated `pages.json` reordering.