---
layout: default
title: "If Tito Is Not Around"
description: "A guide to understanding and continuing The Sunil Abraham Project through its repository, website, documentation, and recorded workflows."
permalink: /tito/if-tito-is-not-around/
categories: [Tito Dutta]
created: 2026-11-03
homepage_featured: true
---

Tito Dutta has been the primary editor, working on the project and its planning since its beginning in October 2025.

He created the pages and introduced and implemented various workflows.

*What happens if Tito is not available tomorrow?*

How can someone else understand "what exactly" has been done? What exactly works, what has failed, how were problems resolved, and what remains to be done?

This page explains how to reconstruct that knowledge from the project's repository, published website, documentation, GitHub issues, and project boards.

## Explore the repository and website

### GitHub repository

The [GitHub repository](https://github.com/sunilabrahamindia/sunilabraham) contains the source files, Markdown pages, configuration, scripts, templates, and version history. It helps establish what was written or changed and, through Git history, when those changes were made.

### TSAP documentation

The [TSAP Documentation hub](https://sunilabraham.in/tsap/) contains documentation about the project's structure, decisions, workflows, experiments, troubleshooting, implementation details, and lessons learned.

The repository and the published website serve different purposes. The repository helps establish what is present in the source and how it changed; the website shows the published output. Documentation helps explain why particular approaches were taken and what was learned along the way.

Start with the [TSAP documentation template](/tsap/template/) to explore the project's documentation.

## TSAP Preservation

The [TSAP Preservation](/tsap/preservation/) page documents how the project's content, source files, metadata, and research materials are protected against loss and kept accessible over time. It describes web archiving, repository backups, Software Heritage, offline copies, and mirror infrastructure.

If you need to recover the project or continue maintaining it after an interruption, consult this page to understand which preservation mechanisms exist and what limitations remain. A documented or planned recovery method should not automatically be assumed to have been tested successfully.

## GitHub Issues and Projects

[GitHub Issues](https://github.com/sunilabrahamindia/sunilabraham/issues) records problems, investigations, maintenance work, documentation tasks, and proposed features. Issues can preserve the problem identified, evidence gathered, possible solutions, tests, decisions, and conclusions.

They can help reconstruct not only what was done, but also what was attempted, what failed, and why a particular approach was adopted.

When investigating an issue, check its current status and any related issues, pull requests, commits, or source files. Distinguish between a proposed solution and one that was actually implemented and tested.

GitHub Projects can help organise and track work across issues. Check the current project status rather than assuming that an item marked as planned has been completed.

## Ask an LLM

The project's documentation, source files, issue discussions, and historical records can add up to a substantial amount of material. Finding the right information can sometimes feel like finding a needle in a haystack.

A large language model (LLM) can help you navigate this material. You can ask specific questions about what has been implemented, how a particular workflow operates, why a decision was made, what went wrong, how it was resolved, or what remains unfinished.

There are two main approaches:

1. **Point the LLM towards the GitHub repository.** This is often the more useful option when the LLM can access the repository directly. It can examine source files, documentation, configuration, scripts, and available version history to help establish what actually exists and how the project works.

2. **Point the LLM towards the published website.** The website can help the LLM explore the published pages and read the project's documentation. However, an LLM may not always be able to access the live website or retrieve all its content. If that happens, use the repository instead.

Ask precise questions and request references to the relevant files, issues, commits, or documentation wherever possible. Do not assume that a proposed implementation is already live or that an explanation is correct simply because an LLM provides it. Verify important conclusions against the actual project records.

{% include navbox-tito.html %}
