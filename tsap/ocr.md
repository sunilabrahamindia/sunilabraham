---
layout: default
title: "Full-Text Creation and OCR Workflows"
description: "Documentation describing the workflows used by The Sunil Abraham Project (TSAP) to create publication-quality full texts from scanned documents, PDFs, and historical source material."
categories: [TSAP Documentation]
permalink: /tsap/ocr/
created: 2026-06-01
---

{% include documentation-notice.html %}

The **Full-Text Creation and OCR Workflow** documents the methods used within The Sunil Abraham Project (TSAP) to convert scanned documents, books, articles, and other source materials into publication-quality digital text.

The primary objective of the workflow is accuracy rather than automation. Many of the documents published by TSAP are historical, academic, religious, legal, or research-oriented sources where preservation of exact wording, footnotes, quotations, poems, section headings, and formatting is important. As a result, workflows are evaluated not only on their ability to recognise text, but also on their ability to preserve structure and minimise editorial errors.

The workflow described here evolved through practical experimentation with a range of OCR and text-extraction methods. The current process reflects observed results rather than theoretical expectations.

## Background

The Sunil Abraham Project (TSAP) frequently works with scanned source material that exists only in printed or image-based form. This has been particularly common while digitising the writings of [A. M. A. Ayrookuzhiel](/amaa/), where many publications are available as scanned journal articles, book chapters, conference papers, photocopies, or ageing printed documents.

Examples include journal articles, book chapters, conference papers, theological publications, historical documents, scanned books, and photocopied source material.

Many of these documents were originally produced decades ago and available through scans of varying quality. Some are professionally typeset, while others are typewritten manuscripts, photocopies, or reproductions of older printed material.

A document may appear perfectly readable to a human reader while producing poor OCR results. In several cases, OCR software successfully recognised large portions of text while simultaneously introducing numerous small errors, omissions, and formatting problems that would have required substantial editorial correction before publication.

As a result, TSAP evaluates text-extraction methods not only on their ability to recognise words, but also on their ability to preserve structure, context, and accuracy. For publication purposes, the central question is not whether text can be extracted from a document, but whether the extracted text is sufficiently reliable to support faithful digital publication.

## Current Workflow

The current workflow prioritises publication accuracy.

### Workflow

```text
PDF
↓
Export pages as JPG images
↓
Upload 2–5 pages at a time
↓
AI-assisted transcription
↓
Human review and audit
↓
Publication
```

Pages are typically exported individually from a PDF and uploaded in small batches. Working with a limited number of pages at a time helps reduce omissions and makes auditing easier.

The resulting transcription is reviewed against the original images before publication.

## Why This Workflow Was Chosen

The current workflow was adopted after repeated experience with OCR systems that successfully recognised large amounts of text but introduced subtle errors that were difficult to detect.

Common OCR problems include dropped words, merged paragraphs, incorrect punctuation, damaged footnotes, formatting loss, character substitutions, and omitted lines.

These errors may not be obvious during casual reading but can become significant when publishing historical or academic material.

By working directly from page images, the transcription process benefits from visual context and can often interpret difficult scans more accurately than conventional OCR systems.

## OCR and Text Extraction Methods Evaluated

Several approaches have been evaluated or considered.

### OCRmyPDF

OCRmyPDF was evaluated during experiments involving scanned academic publications and historical documents. The software successfully created searchable PDF/A files and often reduced file size while preserving the original page images.

The project found OCRmyPDF useful for preservation and archival purposes. However, the quality of the OCR text varied considerably depending on the quality of the original scan. Older documents, typewritten pages, and degraded photocopies frequently produced recognition errors, formatting problems, and damaged footnotes.

As a result, OCRmyPDF is currently regarded as a preservation tool rather than a publication workflow. While the searchable PDFs it produces are valuable for storage and reference, the extracted text generally requires substantial verification before publication.

### pdftotext

The `pdftotext` utility was tested in conjunction with OCRmyPDF. While the tool successfully extracted text from OCR-enabled PDFs, the quality of the output depended entirely on the quality of the OCR layer. In practice, OCR errors present in the source PDF were simply transferred into the extracted text. As a result, the utility proved useful for experimentation and inspection but did not materially improve publication workflows.

### Google Docs OCR

Google Docs OCR has been used and evaluated informally during digitisation work.

While the service can often recognise large amounts of text successfully, it has not performed well on the types of material commonly processed by TSAP. In particular, poems, footnotes, page structure, and other formatting elements were often damaged or simplified during conversion. Footnotes could become detached from their original locations, page breaks could appear within notes, and formatting-sensitive material frequently required extensive correction.

As a result, Google Docs OCR has not been adopted as part of the TSAP publication workflow.

## Other Methods Considered

Other OCR and document-analysis systems have been identified for possible future evaluation, including Marker, Google Document AI, and Azure Document Intelligence. Other OCR and document-analysis systems have been identified for possible future evaluation, including Marker, Google Document AI, and Azure Document Intelligence. These tools have not yet been tested on TSAP source material and therefore no conclusions have been reached regarding their suitability.

## Preservation Workflow

Although OCR output may not always be suitable for publication, searchable archival PDFs remain valuable. The preservation workflow is therefore treated separately from the publication workflow.

### Preservation Workflow

```text
Original PDF
↓
OCRmyPDF
↓
Searchable PDF/A
↓
Archive and storage
```

This workflow improves discoverability and long-term preservation without affecting publication workflows.

## Editorial Review

No OCR or AI-assisted workflow should be assumed to be error-free. Regardless of the extraction method used, publication-quality text should be reviewed against the original source before publication.

This is particularly important for titles, footnotes, quotations, poems, names, dates, citations, and other material where even small transcription errors may affect accuracy or meaning.

Editorial review remains an essential part of the publication process.

## Lessons Learned

Practical testing during the digitisation of A. M. A. Ayrookuzhiel's writings demonstrated that the most automated workflow is not necessarily the most accurate workflow.

For the types of historical and academic material commonly published by TSAP, a slower workflow that incorporates image-based transcription and editorial review may produce substantially better results than fully automated OCR systems.

The project therefore prioritises publication accuracy over automation.

## Future Development

The workflow described here reflects current practice and may evolve as new tools become available. Future evaluations may include additional OCR systems, document-analysis tools, and AI-assisted transcription methods. Any future changes should be assessed against real TSAP source material and judged on the quality of the resulting publication text rather than OCR speed alone.
