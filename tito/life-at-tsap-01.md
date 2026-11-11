---
layout: default
title: "Life at TSAP (11 November 2026)"
categories: [Tito Dutta]
description: "A first-person account of a day spent working on paperback production, troubleshooting, inspections, failed builds and recovery at The Sunil Abraham Project."
permalink: /tito/life-at-tsap-01/
authors: [Tito Dutta]
created: 2026-11-12
---

{% include author-date.html %}

{% include under-construction.html %}

I spent a substantial part of Wednesday, 11 November 2026, working on the paperback production of A. M. Abraham Ayrookuzhiel's *Essays on Dalits, Religion and Liberation II*. The work involved troubleshooting the interior layout, investigating paragraph overlaps, correcting the automated PDF inspection process, recovering the print-production workflow after several failed GitHub Actions runs, and examining the generated proofs. The technical chronology is documented in [Print Book Production: Essays on Dalits, Religion and Liberation II](/amaa/30-print-book-production/).

## The paperback production problem

The most frustrating issue was the appearance of overlapping paragraphs in the paperback interior. Consecutive paragraphs were colliding vertically, making parts of the text difficult to read. This was particularly puzzling because more than seventy earlier builds had not exhibited this behaviour.

I initially suspected that the problem might have been introduced during the changes associated with the publication-details revision. However, I could not establish a definitive connection.

I tried several approaches. The global paragraph settings were changed to use `leading: 1.2em` and `spacing: 8pt`. The subsequent build, numbered 88, still showed collisions. Removing the global `#set block(spacing: 0.55em)` rule did not resolve the problem either.

I also experimented with a global `#show par` rule that wrapped paragraphs in blocks and applied spacing below them. That did not produce the desired result, and I eventually removed the rule. Increasing paragraph spacing to 16pt did not establish a reliable solution.

An inspection of the source revealed another complication. The paragraphs were separated by blank lines rather than explicit `#parbreak()` markers. This meant that some of my earlier search-and-replace attempts had been targeting the wrong mechanism.

I experimented with a regular-expression-based post-processing approach to insert `#v(10pt)` between blank-line boundaries. However, this was not verified as a solution. It also carried the risk of affecting headings, lists, quotations, footnotes and poems. I did not treat it as a confirmed fix.

The important point was that the paragraph-overlap problem remained unresolved. I did not want to mistake a change in the source code for proof that the printed pages were correct.

## Correcting the PDF overlap checker

While investigating the layout problem, I also examined the automated PDF overlap checker.

The checker had reported six possible overlaps on pages 176 and 178. On closer inspection, these appeared to be false positives caused by the way the checker measured the vertical distance between text elements. It was flagging elements that were close together without establishing that their bounding boxes actually intersected.

I changed the inspection logic so that it compared both horizontal and vertical bounding-box intersections. The revised check required an overlap of more than one point in both dimensions.

This correction was committed as `728eb658e872364f78c7e77031cf1a0f851638c4`, and workflow run 42970201063 completed successfully.

This was a correction to the automated checker, not a solution to the paragraph-overlap problem in the book. The two issues needed to remain separate. A checker that produces fewer false positives is useful, but it does not certify the visual quality of a PDF.

## The production workflow breaks down

The build workflow became another source of frustration.

The last known successful run before the disruption was run 109, at 13:18 UTC on 11 November. It had generated the interior PDF, front-cover proof, combined review PDF and the associated artefact.

The following runs, numbered 110 to 116, did not produce a usable result. Six failed and one was cancelled.

One failure, in run 115, occurred while GitHub Actions was attempting to install Pandoc, pandoc-data and Linux Libertine fonts through APT. The process could not resolve `azure.archive.ubuntu.com`. The builder itself never ran.

Run 116 failed for a different reason. The Python setup action had pip caching enabled, but the repository did not contain a `requirements.txt` or `pyproject.toml` file for the action to use. The workflow stopped before the builder or system-package installation could run.

These were different failures at different stages. It would have been misleading to attribute all the failed runs to one cause.

There was also a brief mistake involving the builder's location. I edited `ebook/edrl-ii/build.py` instead of the actual print builder at `ebook/edrl-ii/print/build.py`. I restored the unrelated edit.

## Recovering a known working version

At this stage, I decided that the priority should be recovery rather than introducing more changes.

The stable recovery checkpoint was commit `11b45f870dab5c5ef25e826b00fcd270e851b4f7`. I wanted to preserve a known working source state and avoid making the situation harder to diagnose by changing the environment, adding dependencies or modifying the workflow unnecessarily.

The recovery approach was deliberately conservative: freeze the working environment, avoid new dependencies and workflow changes, and make only small, controlled formatting changes in the current print builder.

The next successful attempt came with run 117, attempt 2. It completed under commit `a4cfcba453eddb548226a8a854498adaa64b7955`.

The resulting artefact, `edrl-ii-print-preview-117`, was approximately 7.4 MB. It contained three PDFs:

- `edrl-ii-interior.pdf`
- `edrl-ii-front-cover-proof.pdf`
- `edrl-ii-combined-review.pdf`

The artefact was due to expire on 11 December 2026. I downloaded and opened it. The expected earlier version was present, which confirmed that the recovery had restored a working production output.

That was an important step, but it was not the same as approving the book for print. The paragraph-overlap issue still needed attention, and the generated PDFs still required visual inspection.

## Other interior corrections

The production work also involved several smaller editorial and layout adjustments.

I worked on the spacing in the Foreword and Editor's Note, the use of lowercase Roman numerals for preliminary pages, and the running heads. The intended arrangement was to show the book title on even pages and the essay title on odd pages, except on chapter-opening pages, where running heads should be absent.

The Foreword attribution was right-aligned, and the Editor's attribution was revised. I also worked on the signature line breaks, followed by corrections to the spacing around the signature and the placement of the date.

The approved biography for the About the Author section was inserted after the Editor's Note and before the Contents. The Pambatti Cittar epigraph was added, its refrain restored, and its line breaks corrected.

A portrait plate was added, although its visual verification was still pending. The preliminary-page running heads were removed, and I also noted that the otherwise blank page before the first essay should carry the Roman folio XIII. That still required proofing.

The footer on the preliminary pages needed correction as well. The earlier version used Typst content-block syntax where executable context code was required. Even after the correction, a fresh build and visual inspection were necessary.

The typography also needed to remain proportionate. I wanted to preserve the spacing that had already been corrected and ensure that small text did not fall below the minimum acceptable size of 8pt.

## Keeping the recovery separate from final approval

By the end of the recovery work, I had a successful build and a downloadable set of PDFs again. That was a meaningful improvement over the preceding failed runs.

However, I did not consider the paperback ready for final approval. The paragraph-overlap defect had not been conclusively resolved. The corrected automated checker addressed false positives, but it could not replace visual proofing. The portrait plate, the preliminary-page footer and folio placement also needed further inspection.

I wanted to resist the temptation to keep changing several things at once. The production process had already demonstrated how easily a small workflow or environment change could interrupt the build. Preserving the successful recovery point was therefore more important than rushing into another round of modifications.

## A day of troubleshooting

The day was a reminder that producing a paperback is not simply a matter of converting a manuscript into a PDF. It involves typography, page architecture, automated checks, visual inspection, build environments and careful recovery when the production pipeline fails.

There were several separate problems to investigate, and not all of them were solved. I recovered the build process, corrected a flaw in the overlap checker and restored access to the generated proofs. But the central paragraph-overlap issue remained open.

I ended the day with a working recovery point rather than a finished book. For the moment, that was the more responsible outcome.

{% include navbox-tito.html %}
