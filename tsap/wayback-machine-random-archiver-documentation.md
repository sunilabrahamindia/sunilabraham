---
layout: default
title: "Wayback Machine Random Archiver (Documentation)"
description: "Documentation for the Wayback Machine Random Archiver used by The Sunil Abraham Project (TSAP) to gradually preserve pages in the Internet Archive."
categories: [TSAP Documentation]
permalink: /tsap/wayback-machine-random-archiver-documentation/
created: 2026-07-03
---

{% include documentation-notice.html %}

{% include under-construction.html %}

The **Wayback Machine Random Archiver** is a Python utility developed for The Sunil Abraham Project (TSAP) to simplify the preservation of website pages in the Internet Archive's Wayback Machine. Instead of manually submitting individual URLs through the Save Page Now interface, the script automatically selects pages from the repository, archives them one at a time, and records the results for future reference.

The tool was developed as the website expanded beyond one thousand published pages. Although the Internet Archive regularly crawls many public websites, manual submission provides an additional layer of preservation by requesting an immediate snapshot of important pages. The script enables this process to be carried out gradually without requiring continuous user intervention.

Unlike large-scale website crawlers, the Wayback Machine Random Archiver intentionally adopts a conservative approach. Pages are archived individually with a delay between requests, allowing long-running sessions while reducing the likelihood of triggering rate limits. Progress is displayed throughout execution, successful archives are logged, and reports are generated at the end of each session.

The implementation was developed with assistance from AI coding tools. The overall architecture, workflow, testing, and operational decisions were designed and validated by the project maintainer.

## Background

Digital preservation has always been an important objective of TSAP. In addition to Git history, GitHub, Cloudflare Pages, Software Heritage and independent backups, the Internet Archive provides another important preservation layer by periodically capturing publicly accessible versions of the website.

Initially, pages were submitted manually through the Wayback Machine whenever significant additions or updates were made. As the repository grew, this approach became increasingly time-consuming. Repeating the same sequence hundreds of times was inefficient and made it difficult to ensure consistent preservation across the site.

The Wayback Machine Random Archiver was therefore developed to automate this repetitive task while remaining simple, transparent and easy to maintain. Rather than attempting to archive the entire website in one operation, the script processes one page at a time and can be stopped safely at any point. This incremental workflow makes it practical to run the script in the background during normal development or maintenance sessions.

## Objectives

The script was designed with the following objectives:

- Automate routine submission of TSAP pages to the Internet Archive.
- Preserve the repository as a read-only source during execution.
- Store all runtime data outside the repository.
- Process pages gradually to minimise the likelihood of rate limiting.
- Allow interrupted sessions to resume without losing completed work.
- Generate human-readable logs and reports documenting each archiving session.
- Keep the implementation simple, portable and easy to maintain.

## System Architecture

The Wayback Machine Random Archiver consists of several independent components that work together during an archiving session.

### Repository Scanning

When executed, the script scans the TSAP repository to discover pages that are eligible for archiving. It first attempts to use the site's generated `pages.json` file as the primary source of URLs. Using `pages.json` ensures that the script archives only pages that are intended to be published.

If `pages.json` is unavailable, the script automatically falls back to scanning Markdown files throughout the repository. During this process, it reads each page's YAML front matter and considers only pages that contain a `created:` field. Pages explicitly marked `published: false` are ignored.

### URL Generation

Whenever a page contains an explicit `permalink:` field, that value is used to construct the public URL.

If no permalink is present, the script derives the public URL from the repository path using Jekyll's default page URL conventions. This allows pages to be archived correctly without requiring additional metadata.

### Random Page Selection

After collecting eligible pages, the script randomises their order before beginning the archiving session.

Randomisation prevents the same sections of the website from always being archived first and distributes preservation activity across the site over multiple sessions.

Pages that have already been recorded in the archive log are skipped automatically.

### Wayback Machine Submission

Each page is submitted individually to the Internet Archive's Save Page Now service.

The script waits for the response before proceeding to the next page. Successful submissions display the returned HTTP status together with the URL of the archived snapshot.

A configurable delay is inserted between requests to reduce the likelihood of triggering rate limits or placing unnecessary load on the Internet Archive.

Temporary network failures are retried automatically. If the Wayback Machine responds with HTTP 429 (Too Many Requests), the script pauses before retrying the request.

### Archive Log

Successful archives are recorded in a persistent JSON log.

The log prevents the same page from being submitted repeatedly during subsequent sessions and allows interrupted runs to resume without losing progress.

Each successful entry records the archived URL, the corresponding Wayback Machine snapshot, the archive timestamp and the HTTP response status.

### Reporting

At the end of every session, the script generates a Markdown report summarising the run.

The report records the session start and finish times, elapsed duration, numbers of successful and failed submissions, skipped pages, and the snapshot URLs returned by the Internet Archive.

These reports provide a permanent record of preservation activity and simplify verification of completed sessions.

### Graceful Shutdown

Long-running archiving sessions can be interrupted safely using `Ctrl+C`.

Rather than terminating immediately, the script completes the page currently being archived, writes the archive log, generates the session report, and exits cleanly. This ensures that completed work is not lost and that subsequent sessions can resume from the correct state.

## Script Location

The Wayback Machine Random Archiver is maintained within the TSAP repository at:

```text
scripts/wayback_random_archiver.py
```

The script is intended as a maintenance utility and is not used during normal Jekyll site generation. It may be executed manually whenever Internet Archive preservation work is required.

## Maintenance Workflow

The script is intended to be run manually whenever preservation work is required. A typical workflow is:

1. Update or publish new content on TSAP.
2. Run the Wayback Machine Random Archiver.
3. Allow the script to archive pages for the desired period.
4. Interrupt the session when appropriate using `Ctrl+C`.
5. Review the generated report and archive log.
6. Repeat the process during future maintenance sessions.

The script is designed for occasional maintenance rather than continuous background operation.

## Advantages

The selected architecture provides several advantages.

Because the script reads repository data without modifying it, the website remains unaffected during archiving sessions. Runtime files are stored entirely outside the repository, preventing accidental commits of generated logs or reports.

The incremental approach also keeps Internet Archive requests modest, reducing the likelihood of rate limiting while allowing preservation work to continue over multiple sessions.

Finally, the implementation remains simple. It requires only Python together with the Requests and PyYAML libraries, making it straightforward to maintain and run on different systems.

## Future Improvements

Several enhancements may be considered in future versions.

Possible improvements include configurable delays and archive limits through command-line options, automatic re-archiving after a configurable interval, additional progress statistics, improved reporting, and support for selectively archiving specific sections of the website.

Any future development should continue to prioritise simplicity, transparency, repository safety, and compatibility with TSAP's long-term preservation strategy.
