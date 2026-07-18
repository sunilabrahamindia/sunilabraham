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

## Diagnose Website Network and Response Times

These commands are useful for investigating whether slow website responses are caused by the website itself, DNS resolution, network connectivity, TLS negotiation, or temporary routing and CDN latency.

### Check Basic Network Latency

Use `ping` to check network latency and packet loss:

```bash
ping sunilabraham.in
```

Stop the test with `Ctrl+C`.

The summary shows the number of packets transmitted and received, packet loss, and minimum, average, and maximum round-trip times.

Because the TSAP domain is proxied through Cloudflare, this command measures the network path to a Cloudflare server rather than directly to the GitHub Pages origin. It should therefore be used as a general connectivity diagnostic rather than a measurement of website loading speed.

### Measure Different Stages of an HTTPS Request

The following command measures several stages involved in requesting the TSAP homepage:

```bash
curl -s -o /dev/null -w 'DNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTLS: %{time_appconnect}s\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\n' https://sunilabraham.in/
```

The values mean:

- `DNS`: Time required to resolve the domain name.
- `Connect`: Time elapsed before the network connection was established.
- `TLS`: Time elapsed before the HTTPS/TLS connection was established.
- `TTFB`: Time to First Byte, or the time before the server began returning the response.
- `Total`: Total time required to complete the request.

These measurements can help distinguish a slow network connection from delayed server or CDN responses.

### Inspect HTTP Response Headers

Use the following command to inspect the response headers returned for the TSAP homepage:

```bash
curl -I https://sunilabraham.in/
```

Headers such as `cf-ray`, `cf-cache-status`, `x-cache`, `x-served-by`, and `server` can provide information about Cloudflare, GitHub Pages, Fastly caching, and the data centre involved in serving a request.

These headers may change between requests and should be treated as diagnostic information rather than permanent site configuration.

### Run Repeated Website Response-Time Tests

The following command performs ten separate requests to the TSAP homepage and reports connection, TLS, Time to First Byte, and total response times:

```bash
for i in {1..10}; do
  curl -s -o /dev/null -w "$i  Connect:%{time_connect}s TLS:%{time_appconnect}s TTFB:%{time_starttransfer}s Total:%{time_total}s\n" https://sunilabraham.in/
  sleep 1
done
```

Running repeated tests is useful when investigating intermittent performance problems. A single unusually slow request followed by several normal responses may indicate temporary network, routing, CDN, or monitoring-system latency rather than a sustained website performance problem.

The results should not be interpreted as complete page-loading measurements because `curl` does not measure the loading and rendering of all page resources in a web browser.

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

## Investigate Recent Repository Growth

These commands are useful when the repository appears to have grown unexpectedly and recent commits need to be examined.

### Check File Size Changes During the Last Three Days

The following command examines files changed during the last three days and reports the change in their actual file size for each commit:

```bash
git log --since="3 days ago" --format="%H" | while read commit; do
    parent=$(git rev-parse "$commit^" 2>/dev/null) || continue

    git diff --name-only "$parent" "$commit" | while read file; do
        old=$(git cat-file -s "$parent:$file" 2>/dev/null || echo 0)
        new=$(git cat-file -s "$commit:$file" 2>/dev/null || echo 0)
        diff=$((new - old))

        if [ "$diff" -ne 0 ]; then
            printf "%+10d bytes  %s\n" "$diff" "$file"
        fi
    done
done | sort -nr
```

This can help identify new or edited files that contributed to recent repository growth. A file may appear more than once if it was changed in multiple commits.

The figures represent changes in the uncompressed file contents and should not be interpreted as the exact amount of Git repository storage consumed.

### Inspect Recent Size Changes to `pages.json`

The following command reports the actual change in the size of `pages.json` for each commit during the last three days:

```bash
git log --since="3 days ago" --format='%H %ad %s' --date=short -- pages.json |
while read hash date subject; do
    parent="${hash}^"
    old=$(git cat-file -s "$parent:pages.json" 2>/dev/null || echo 0)
    new=$(git cat-file -s "$hash:pages.json" 2>/dev/null || echo 0)
    diff=$((new - old))

    printf "%+8d bytes (%+.2f KB) | %s | %s\n" \
        "$diff" "$(awk "BEGIN {print $diff/1024}")" "$date" "$subject"
done
```

This is particularly useful for monitoring the automatically generated Pages Index. It measures the difference in the complete file size between successive versions.

A result of `+0 bytes` does not necessarily mean that the file was unchanged. Lines may have been reordered or replaced while the total file size remained identical. The commit diff should be inspected separately when this is suspected.

### Inspect the Storage Used by Recent Versions of `pages.json`

The following command lists Git objects associated with `pages.json` encountered when examining recent repository history and shows both their uncompressed size and their current on-disk object size:

```bash
git rev-list --since="3 days ago" --all --objects -- pages.json |
awk '{print $1}' |
git cat-file --batch-check='%(objectname) %(objectsize) %(objectsize:disk)' |
sort -k3 -nr
```

The output contains three columns:

- Git object ID.
- Uncompressed object size in bytes.
- Current on-disk object size in bytes.

The on-disk size should be interpreted carefully. Loose Git objects and packed, delta-compressed objects can occupy very different amounts of storage, and the results may change after Git garbage collection and repacking.

## Repack and Clean the Local Git Object Database

The following command allows Git to clean up unnecessary objects and repack the repository efficiently:

```bash
git gc
```

Afterwards, repository object storage can be checked again:

```bash
git count-objects -vH
```

A successfully packed repository may show no loose objects and a reduced number of pack files.

`git gc` is a normal Git maintenance operation, but it should not be confused with rewriting repository history. It optimises the local Git object database without removing files or commits that remain reachable from the repository's current history.

## List All Files Inside a Directory

This command lists all files contained within a specified directory and its subdirectories. It is useful for inspecting parts of the TSAP repository without manually opening each folder.

For example, to list all files inside the `.github` directory:

```bash
find .github -type f | sort
```

A typical output may look like:

```text
.github/README.md
.github/workflows/pages.yml
```

The command consists of:

- `find .github`: Searches the `.github` directory and all of its subdirectories.
- `-type f`: Limits the results to regular files and excludes directories.
- `|`: Passes the output of the `find` command to the next command.
- `sort`: Sorts the resulting file paths alphabetically.

Replace `.github` with another directory path to inspect a different part of the repository.
