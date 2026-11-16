---
layout: default
title: "Editorial Source Audit: Second Stage — Source Verification for Essays on Dalits, Religion and Liberation II"
permalink: /amaa/30-editorial-source-audit-second-stage/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Second-stage editorial source audit for Essays on Dalits, Religion and Liberation II, recording further source checks, verification findings, corrections and the temporary suspension of automatic print builds on essay edits."
created: 2026-11-16
---

**Editorial Source Audit: Second Stage** records the further source-verification work being undertaken for *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It continues the work documented in the [first-stage Editorial Source Audit](/amaa/30-editorial-source-audit/), which recorded the collection-wide review of capitalisation, italicisation, heading treatment and quotation punctuation.

The first-stage audit dealt primarily with consistency and presentation within the available manuscript sources. The second stage provides a separate working record for further checking of the essays against their source material. Findings, uncertainties, decisions and any approved corrections will be recorded here as the work proceeds. No source should be changed merely because a difference is noticed; each case must be examined and its significance established first.

## The nine essays under review

1. [The State of Hinduism in 2000 A.D.—Some Emerging Trends](https://sunilabraham.in/amaa/state-of-hinduism-in-2000-ad-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/state-of-hinduism-in-2000-ad-full-text.md))
2. [Religion, Spirituality and Aspirations of the People](https://sunilabraham.in/amaa/religion-spirituality-and-aspirations-of-the-people-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religion-spirituality-and-aspirations-of-the-people-full-text.md))
3. [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue](https://sunilabraham.in/amaa/living-hindu-popular-religious-consciousness-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/living-hindu-popular-religious-consciousness-full-text.md))
4. [The Church and the Study of Religion](https://sunilabraham.in/amaa/the-church-and-the-study-of-religion/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/the-church-and-the-study-of-religion.md))
5. [Religions and the Aspirations of the People](https://sunilabraham.in/amaa/religions-and-the-aspirations-of-the-people/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religions-and-the-aspirations-of-the-people.md))
6. [Religion: A Way of Salvation or an Ideology of Oppression?](https://sunilabraham.in/amaa/religion-way-salvation-ideology-oppression-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religion-way-salvation-ideology-oppression-full-text.md))
7. [Dalit Theology: A Movement of Counter-Culture](https://sunilabraham.in/amaa/dalit-theology-movement-counter-culture-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/dalit-theology-movement-counter-culture-full-text.md))
8. [Dalit Liberation—Some Reflections on Their Ideological Predicament](https://sunilabraham.in/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament.md))
9. [The Ideological Nature of the Emerging Dalit Consciousness](https://sunilabraham.in/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness.md))

## Purpose

The purpose of this stage is to carry out further source checking across the essays and maintain a clear record of:

- The source material examined and the essay or passage to which it relates.
- Differences, omissions, inconsistencies or uncertainties identified during comparison.
- Whether a difference is a source variation, a transcription issue, an editorial decision or an unresolved question.
- The evidence supporting a decision.
- Any correction approved and applied to the relevant source file.
- The verification carried out after a correction.

This is a source-verification exercise. It is distinct from the print-layout work documented in [Print Book Production](/amaa/30-print-book-production/) and from the capitalisation, italicisation and punctuation work already recorded in the first-stage audit.

## Relationship with the first-stage audit

The [first-stage audit](/amaa/30-editorial-source-audit/) remains the record of the earlier editorial work, including the nine-essay capitalisation and italicisation review, the H2-H4 heading checks, and the quotation and sentence-ending punctuation audit.

This second-stage page is not intended to replace or rewrite that record. It will document additional source checks and any new decisions arising from them. Where a finding belongs to an earlier audit, the relevant first-stage entry should be referred to rather than duplicated.

## Scope and working method

The work will proceed through the relevant essay sources and source materials. Each item will be examined in context. A difference will not automatically be treated as an error: the original publication, the available manuscript and the intended edited text may contain legitimate variations.

For each check, the record should identify, where available:

1. The essay and precise passage, page, section or other locator.
2. The manuscript text currently held in the repository.
3. The corresponding source text or other evidence examined.
4. The exact difference or question observed.
5. The assessment and reason for the decision.
6. Whether a source correction was approved and made.
7. The subsequent source comparison or other verification.

If the available evidence is insufficient, the item will remain open. Unverified assumptions must not be recorded as established facts.

## Source-editing and build policy

During this stage, the essay sources may require repeated small edits as the checks progress. Automatically building the complete EDRL II print preview after every essay edit would create unnecessary builds while the source review is in progress.

For that reason, the automatic essay-edit triggers in the EDRL II print workflow have been temporarily suspended.

### Temporary suspension recorded — 16 November 2026

The workflow file `.github/workflows/build-edrl-ii-print.yml` has been changed so that edits to the nine essay source files no longer trigger an automatic print build on every push.

The following nine essay paths have been removed from the workflow's `push.paths` trigger:

- `amaa/state-of-hinduism-in-2000-ad-full-text.md`
- `amaa/religion-spirituality-and-aspirations-of-the-people-full-text.md`
- `amaa/living-hindu-popular-religious-consciousness-full-text.md`
- `amaa/the-church-and-the-study-of-religion.md`
- `amaa/religions-and-the-aspirations-of-the-people.md`
- `amaa/religion-way-salvation-ideology-oppression-full-text.md`
- `amaa/dalit-theology-movement-counter-culture-full-text.md`
- `amaa/dalit-liberation-some-reflections-on-their-ideological-predicament.md`
- `amaa/the-ideological-nature-of-the-emerging-dalit-consciousness.md`

**The print workflow itself remains enabled.** The following triggers remain in place:

- Manual execution through GitHub Actions using `workflow_dispatch`.
- Pushes to `main` that change `ebook/edrl-ii/manifest.yml`.
- Pushes that change `ebook/edrl-ii/front-matter.md` or `ebook/edrl-ii/foreword.md`.
- Pushes that change files under `ebook/edrl-ii/print/`, including `build.py`.
- Changes to `.github/workflows/build-edrl-ii-print.yml` itself.

This is a temporary change to the path filters, not a disabling of GitHub Actions, the print workflow, or manual proof generation. A print build can still be started manually whenever a fresh PDF is required. The essay paths can be restored to the trigger after this source-checking period is over.

**Workflow change:** The path-filter change was committed and fetched again from GitHub to verify that the nine essay paths had been removed while the manual and production-file triggers remained. The change is therefore confirmed in the repository.

**Reinstatement:** The automatic essay-edit triggers are to be restored when the source-checking work has reached a suitable stopping point. Until then, a manual build should be requested when a sufficiently coherent set of source changes is ready for print proofing.

## Audit log

This section will be updated as individual source checks are undertaken. Each entry should distinguish what was examined, what was found, what decision was made and what remains unresolved. No finding is considered complete merely because a possible difference has been noticed.

### Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends

**Source compared:** The original *Indian Journal of Theology*, Vol. 26, No. 2 (April–June 1977), pp. 86–91, against the current full-text source, `amaa/state-of-hinduism-in-2000-ad-full-text.md`. The comparison was carried out page by page using supplied PDF screenshots. The first-stage Editorial Source Audit was consulted before deciding whether a visible difference required correction.

**Source corrections made**

- **Page 86:** Changed `rogi` to `rog` in the expression *rog/Bheemar*. The word *Bheemar* was retained. The line-break form "small-pox" in the PDF was not adopted; it is a line-break hyphenation of "smallpox".
- **Page 87:** Added italics to *a corresponding decrease in his sense of dependence* and *deprived of a certain sense of mystery*.
- **Page 89:** Added italics to *natural* in "as merely natural without significance", and to *Ganapathy* in "offered in homage to Ganapathy".
- **Page 90:** Italicised *Bhagavan's lila* in full, *puja* in "the true puja", and the complete four-part series of explanatory quotations beginning "bhutas and pretas were created by bhayam (fear)" and ending "thought of as yakshi".
- **Page 91:** No source correction was required.

**Other source adjustments recorded during this review**

- Changed the six existing numbered subsection headings following "The Secular Option" from H2 to H3. The headings' wording and identifiers were retained.
- Italicised all three standalone occurrences of *karma* in the essay.
- The heading and body structure, wording and identifiers were otherwise preserved during these edits.

**Differences examined but not changed**

- The PDF's line-break hyphenation "small-pox" on page 86 was retained as the single word "smallpox" in the essay.
- The heading-level italics visible on page 89 were not applied to entire headings. The first-stage audit requires only identified Indic terms in headings to receive italics; it does not require whole headings to be italicised.
- Capitalisation differences involving *Harijan/Harijans*, *Brahmin/Brahmins* and generic *sakti* were not changed during this second-stage comparison, because the first-stage audit already records the collection's editorial decisions for these forms.
- The title-case treatment of the page 87 subsection heading and the capitalisation of *Sakti* noted on page 88 were not changed during this comparison.
- The page 90 headings and the page 91 heading were not changed.

**Verification and status**

- The essay source was fetched again before each approved update. Each edit was limited to the approved formatting or word correction.
- The changes above were committed in separate source updates and the current file was re-fetched after editing.
- The page-by-page comparison of the supplied original pages 86–91 is recorded here. This entry records the changes made and the principal differences deliberately left unchanged; it does not claim that spelling, transcription or all other aspects of the essay have been comprehensively proofread.

**Status:** Pages 86–91 compared. Approved corrections applied to the Essay 1 source; no changes were made to the print builder or to other essay files.


### Essay 5 — Religions and the Aspirations of the People

**Source compared:** The original *Religion and Society*, Vol. XXX, Nos. 3 & 4 (September–December 1983), pp. 102–108, against `amaa/religions-and-the-aspirations-of-the-people.md`. The supplied page images were reviewed in sequence: 102, 103–104, 105, 106–107 and 108. No page in the supplied sequence was missing.

**Source correction made**

- **Page 105:** Extended the italics to the complete sentence beginning “When a religion attaches itself to concrete power interests in a society...” and ending “...the power interests of a particular section.” This sentence continues the italicised passage across the page break from page 104.

**Other findings**

- No other source-text correction was made during this comparison.
- The author footnote on the opening page is not part of the essay text and was not added.
- Footnotes 1 and 2 (pages 103–104) and footnote 3 (page 107) have corresponding entries in the essay's Notes section. Their presence and placement were checked. The exact wording of footnote 3 has not yet been certified by a complete word-for-word transcription comparison; do not treat this entry as closing the collection-wide footnote verification alert above.

**Status:** Pages 102–108 reviewed. One approved italicisation correction applied on page 105. No other edits made to Essay 5.

### Current status — 16 November 2026

- The second-stage audit page has been created as a separate record linked to the first-stage audit.
- Further source checking is the next workstream; individual findings will be entered here as they are examined and verified.
- Automatic print builds triggered by edits to the nine essay source files have been temporarily suspended.
- Manual print builds and the other specified production-file triggers remain available.
- The suspension is temporary and must be reviewed and reversed when the source-checking period is complete.

## Footnote verification alert — pending collection-wide check

**Important: this is a temporary working alert, not a confirmed finding.**

There is a concern that, in at least one essay, material that should have remained a footnote may have been incorporated into the main text as an ordinary paragraph. This may have happened during transcription or formatting. The affected essay and passage have not yet been identified conclusively.

**Action required:** Check the footnotes in all nine essays against their original published sources. For every footnote, verify that:

- The footnote marker appears at the correct place in the main text.
- The footnote wording is preserved accurately and remains a footnote, rather than appearing as an ordinary body paragraph.
- The note is placed in the correct notes/footnotes area and is not missing, duplicated, or merged into the conclusion or another paragraph.
- The sequence and numbering of footnotes match the source.

**Essay 5 — Religions and the Aspirations of the People:** Pages 103–104 contain footnotes 1 and 2, and page 107 contains footnote 3. These notes are present in the current essay's Notes section. Their presence has been checked, but this does not replace a complete footnote-placement audit across all nine essays.

Keep this alert open until the collection-wide check is completed. Record each essay checked and any correction made here, then remove this temporary alert only when the concern has been resolved.

## See also

- [Editorial Source Audit — First Stage](/amaa/30-editorial-source-audit/)
- [Print Book Production: Essays on Dalits, Religion and Liberation II](/amaa/30-print-book-production/)

{% include navbox-amaa.html %}
