---
layout: default
title: "Externalised Memory"
description: "Documentation describing the externalised memory methodology used within The Sunil Abraham Project (TSAP) to preserve project knowledge across time, sessions, and AI systems."
categories: [TSAP Documentation]
permalink: /tsap/externalised-memory/
created: 2026-05-29
---

{% include documentation-notice.html %}

The **Externalised Memory** methodology is a documentation and knowledge-preservation practice used within The Sunil Abraham Project (TSAP). The aim is to ensure that important project knowledge does not become dependent on human recollection, individual AI conversations, or temporary working notes.

As TSAP has grown in size and complexity, it has become increasingly important to preserve not only content and source material, but also the reasoning behind technical decisions, workflows, editorial standards, and implementation choices. The externalised memory approach seeks to capture that knowledge in durable records that can be understood by future maintainers, contributors, and AI systems.

The methodology is based on a simple principle: conversation memory is not project memory. Conversations are temporary. Project knowledge should instead be preserved in structured documentation that remains available regardless of changes in software, personnel, devices, or AI systems.

## Background

Many AI-assisted workflows depend heavily on conversation history. As discussions become longer, important decisions can become difficult to locate, reconstruct, or verify. Context windows may be exceeded, conversations may become unwieldy, and valuable project knowledge can become fragmented across multiple sessions.

TSAP addresses this problem by creating dedicated records that preserve implementation history, workflows, design decisions, maintenance procedures, lessons learned, and other forms of institutional knowledge.

The goal is not merely documentation. The goal is continuity.

## Public Documentation and Workflow Records

The externalised memory system distinguishes between two forms of documentation.

### Public Documentation

Public documentation explains what a system is, why it exists, and how it is intended to be used.

Examples include:

* project documentation pages
* methodology pages
* style guides
* implementation summaries

These pages are written primarily for readers, contributors, and maintainers.

### Workflow Documentation and Implementation Records

Workflow records are internal project-memory documents.

Their purpose is to preserve:

* implementation history
* development decisions
* architectural reasoning
* maintenance workflows
* lessons learned
* constraints and assumptions

These records are intended primarily for future maintainers and future AI-assisted work.

They serve as portable project memory.

## Why

The approach offers several advantages.

### Continuity Across Conversations

Important project knowledge remains available even when original conversations are no longer accessible.

### Continuity Across AI Systems

Workflow records can be read by different AI systems, allowing project context to be reconstructed without relying on the memory of a particular model.

### Reduced Rediscovery

Future work can build upon existing decisions instead of repeatedly rediscovering information that has already been established.

### Improved Maintainability

Workflows, commands, filenames, URLs, and architectural decisions remain documented and verifiable.

### Institutional Memory

Knowledge becomes part of the project itself rather than remaining dependent on individuals.

## Workflow Records

A workflow documentation and implementation record is typically created when a project involves:

* significant development effort
* multiple design decisions
* long-term maintenance requirements
* complex workflows
* reusable architectural patterns
* future AI-assisted work

Workflow records are intentionally detailed.

Where relevant, they may include:

* exact URLs
* filenames
* scripts
* commands
* workflows
* implementation history
* discovered problems
* future considerations

The intention is to minimise future ambiguity.

## Examples Within TSAP

Examples of systems that have used this approach include:

* the A. M. A. Ayrookuzhiel Citations Catalogue
* the What Links Here tool
* structured data systems
* maintenance workflows

As TSAP evolves, additional systems may be documented using the same methodology.

## Cross-Model Reconstruction

One useful test of an externalised memory record is whether a different AI model can successfully reconstruct the project context from the record alone.

A successful record should allow a future reader to understand:

* what was built
* why it was built
* how it works
* how it is maintained
* what constraints exist
* what decisions should not be changed casually

without requiring access to the original development conversation.

This approach has been tested within TSAP using multiple AI systems and has proved useful for transferring project knowledge between sessions and models.

## Limitations

Externalised memory is not intended to replace source code, version control, public documentation, or human judgement.

Workflow records may become outdated if they are not maintained. They may also reflect the understanding available at a particular point in time rather than a complete historical account.

For this reason, workflow records should be treated as living documents that may be expanded as systems evolve.

## Relationship to TSAP

The Sunil Abraham Project places a strong emphasis on preservation, documentation, transparency, and long-term accessibility. The externalised memory methodology extends those principles beyond content and into project workflows, implementation history, and institutional knowledge.

The objective is simple: important knowledge should survive changes in conversations, software, devices, AI systems, and time itself.
