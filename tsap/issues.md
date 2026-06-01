---
layout: default
title: "Issues (Documentation)"
description: "Documentation for the use of GitHub Issues within The Sunil Abraham Project (TSAP), including purpose, workflow, labels, and early issue history."
categories: [TSAP Documentation]
permalink: /tsap/issues/
created: 2026-06-02
---

{% include documentation-notice.html %}

The **Issues** (or **TSAP GitHub Issues**) system is used within The Sunil Abraham Project (TSAP) to track bugs, investigations, maintenance tasks, feature requests, and other discrete pieces of work. It provides a centralised, version-controlled location where problems can be reported, discussed, documented, and resolved.

Prior to the adoption of GitHub Issues, information of this kind was often distributed across multiple locations, including a laptop notebook, Google Keep, Google Docs, the [Versions](/versions/), [TSAP documentation pages](/tsap/), repository comments, and personal memory. While these methods were useful in specific contexts, they made it difficult to maintain a single overview of outstanding work.

GitHub Issues was adopted to provide a structured workflow for tracking tasks from identification through investigation, implementation, verification, and closure.

## Purpose

GitHub Issues are used for work that is:

* Specific.
* Actionable.
* Capable of being completed.
* Capable of being closed.

Typical examples include:

* Bugs and defects.
* Mobile display problems.
* Accessibility improvements.
* Documentation tasks.
* Maintenance activities.
* Feature requests.
* Technical investigations.

GitHub Issues are not intended to serve as a directory of all project ideas, architectural principles, or long-term aspirations. Broader project philosophy, editorial decisions, workflow guidance, and architectural records continue to be documented through TSAP documentation pages and related project records.

## Relationship to Pull Requests

GitHub uses a shared numbering sequence for both Issues and Pull Requests. As a result, issue numbers do not necessarily begin at Issue #1. If pull requests already exist, the first issue may receive a higher number.

Within TSAP, Pull Requests #1–#5 were created before the first issue. Consequently, the first issue created for the project was numbered Issue #6.

## Workflow

The typical lifecycle of a TSAP issue is:

1. Problem identified.
2. Issue created.
3. Investigation conducted.
4. Fix implemented or conclusion reached.
5. Testing performed.
6. Issue documented.
7. Issue closed.

Not every issue results in a code change. Some issues may conclude that the underlying problem originates outside the project and therefore requires no modification to the repository.

## Labels

The project currently uses GitHub's standard issue labels.

Examples include:

* bug
* documentation
* enhancement
* good first issue
* help wanted
* duplicate
* invalid

Additional labels may be introduced in the future as project requirements evolve.

## Early Issue History

### Issue #6: Mobile Chrome Typography Investigation

Issue #6 was the first issue created for TSAP. Although numbered six, it was in fact the project's first issue, as GitHub uses a shared numbering sequence for both pull requests and issues, and pull requests #1–#5 had already been created earlier.

The issue investigated unusual word spacing and line wrapping observed on some TSAP pages when viewed using Google Chrome on a Samsung Android device. Extensive testing was conducted across multiple browsers, devices, and viewing modes, including Chrome Incognito mode, Firefox, DuckDuckGo Browser, and a second Android device.

The investigation ultimately showed that the problem was caused by browser-side site data rather than a defect in the TSAP stylesheet. The issue was resolved after clearing stored site data associated with the affected domain. No repository changes were required.

### Issue #7: Code Block Overflow on Mobile Devices

Issue #7 addressed code blocks extending beyond the viewport width on mobile devices.

The issue was identified while reviewing the documentation page for the Automatic Last Updated Dates system. Long code examples, file paths, and configuration snippets could exceed the available screen width, reducing readability on smaller devices.

Investigation showed that the stylesheet already contained print-specific handling for code blocks but lacked equivalent handling for normal screen display. A global solution was implemented by adding the following rule to the main stylesheet:

```css
pre {
  overflow-x: auto;
}
```

This allows wide code blocks to scroll horizontally within their container rather than forcing the page itself to overflow. The fix was tested successfully on mobile devices and the issue was subsequently closed.

## Future Development

The use of GitHub Issues within TSAP is expected to evolve over time. Future work may include additional labels, issue templates, workflow refinements, documentation standards, and closer integration with project maintenance activities.

The objective is not to record every idea within the project, but to maintain a clear and manageable record of work that can be investigated, implemented, verified, and completed.
