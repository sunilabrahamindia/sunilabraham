---
layout: default
title: "Does TSAP Use a Wiki Engine?"
description: "An explanation of how TSAP is built without a conventional wiki engine, and how Jekyll, Markdown, YAML, Git, GitHub, and custom TSAP scripts provide many wiki-like capabilities."
categories: [TSAP Documentation]
permalink: /tsap/wiki-engine/
created: 2026-08-24
---

{% include documentation-notice.html %}

**Does The Sunil Abraham Project (TSAP) use a wiki engine such as MediaWiki?** This is a question we have received a few times. Some of TSAP's features are inspired by Wikipedia's functionality (please see our [acknowledgement](/tsap/acknowledgement/#wikipedia)), so it may appear that TSAP is built using a wiki engine. However, it is not.

TSAP uses a GitHub repository, GitHub Pages and Jekyll. Together, these form a static site publishing system, which we have extended with our own scripts, templates and other custom functionality. Many features that may look wiki-like are therefore implemented through this combination rather than through a conventional wiki engine.

This page explains how TSAP works, what we use instead of a wiki engine, and how we have built wiki-like functionality into the project.

## What Is a Wiki Engine?

A wiki engine is software designed to manage a collection of interconnected pages. MediaWiki, for example, is the software used by Wikipedia. A wiki engine provides the underlying systems for creating and editing pages, maintaining revisions, organising content into categories, linking pages, using templates, searching content and managing other aspects of a wiki.

TSAP does not use a wiki engine. Instead, its content and functionality are built from the GitHub repository, Jekyll, GitHub Pages and a number of scripts, templates, includes and other components developed for the project.

## How Are TSAP Pages Created?

In a wiki, a page is normally created and maintained through the wiki engine. In TSAP, the primary source of a page is a Markdown file in the GitHub repository. The file contains the article content and can also contain YAML front matter with information such as its title, description, categories, dates, permalink and other metadata.

Jekyll processes these source files and generates the corresponding website pages. This means that the web page visitors see is generated from the source material rather than being a page stored inside a wiki application.

## How Are Categories and Other Metadata Handled?

TSAP uses YAML front matter together with Jekyll templates and our own scripts to associate information with pages. Categories, dates and other metadata can then be used to generate navigation, indexes and other parts of the site.

Our scripts can also read and process this information when a particular task requires it. This allows the same metadata to be used by different parts of the project rather than being limited to the display of an individual page.

## How Are Pages Linked?

Pages in TSAP can link to one another using ordinary Markdown and HTML links. Jekyll's site structure and page metadata can be used when generating those links, while our templates and scripts can support particular navigation and relationship features.

This provides interconnected pages without a wiki engine maintaining a separate database of page relationships.

## How Are Templates and Reusable Elements Handled?

TSAP uses Jekyll layouts and includes for reusable structures and common elements. We have also developed custom includes, templates and other components for features specific to TSAP.

This allows common elements to be maintained separately from individual articles. A change to a shared component can therefore be reflected across the pages that use it when the site is generated.

## How Is Revision History Handled?

The source files are maintained in Git, so changes to articles, metadata, templates, scripts and other files are recorded in the repository's history.

This is different from having a separate wiki revision system, because the history belongs to the Git repository containing the source material. The history of the generated website can therefore be understood through the history of the files from which it is produced.

## How Are Search and Indexes Created?

Search and indexing can be based on the content and metadata contained in the source files. TSAP uses generated data and custom scripts where required to process this information and support particular search and indexing functions.

This also allows different types of information in the archive to be processed for different purposes. An index does not have to be part of an individual article; it can be generated from the wider collection of source files.

## What Do Our Custom Scripts Do?

The custom scripts are an important part of TSAP's architecture. They perform tasks that go beyond the basic operation of Jekyll, including processing content and metadata, generating or maintaining data, automating repetitive operations and supporting tools developed specifically for the project.

As TSAP develops, additional functionality can therefore be implemented through these scripts and other custom components without requiring the underlying content to be moved into a wiki engine.

## What About Features Inspired by Wikipedia?

Some TSAP features are inspired by functionality familiar from Wikipedia. We acknowledge this in our [acknowledgement](/tsap/acknowledgement/#wikipedia).

This influence concerns ideas and functionality, not the software used to operate the site. Wikipedia uses MediaWiki, while TSAP uses GitHub, Jekyll, GitHub Pages and our own scripts, templates, includes and other custom components.

## What Could Be Added in the Future?

The absence of a wiki engine does not prevent TSAP from developing additional interconnected and knowledge-oriented features. Further work could include richer backlinks, related-page systems, automatically generated indexes, structured information about people and organisations, timelines, entity relationships, knowledge graphs and more advanced search and discovery tools.

Such features can be implemented using the existing source material, Jekyll, Git and additional TSAP scripts and components as required.

## In Summary

TSAP does not use a wiki engine. Its pages are maintained as source files in the GitHub repository, processed by Jekyll and published through GitHub Pages, with Git providing version history and our own scripts, templates, includes and other components providing additional functionality.

Some of the resulting features may be familiar from wikis, including interconnected pages, categories, structured metadata, reusable components, indexes and revision history. These features are implemented through TSAP's own architecture rather than through a conventional wiki engine.

## See also

- [YAML Front Matter](/tsap/yaml/), how we structure our YAML and use YAML front matter
- [Site structure](/tsap/structure/), an overview of our site structure and repositories
- [Templates](/tsap/templates/), the various templates we use across TSAP
