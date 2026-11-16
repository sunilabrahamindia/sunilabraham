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

1. [The State of Hinduism in 2000 A.D.—Some Emerging Trends](https://sunilabraham.in/amaa/state-of-hinduism-in-2000-ad-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/state-of-hinduism-in-2000-ad-full-text.md)) ✅
2. [Religion, Spirituality and Aspirations of the People](https://sunilabraham.in/amaa/religion-spirituality-and-aspirations-of-the-people-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religion-spirituality-and-aspirations-of-the-people-full-text.md))
3. [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue](https://sunilabraham.in/amaa/living-hindu-popular-religious-consciousness-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/living-hindu-popular-religious-consciousness-full-text.md))
4. [The Church and the Study of Religion](https://sunilabraham.in/amaa/the-church-and-the-study-of-religion/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/the-church-and-the-study-of-religion.md)) ✅
5. [Religions and the Aspirations of the People](https://sunilabraham.in/amaa/religions-and-the-aspirations-of-the-people/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religions-and-the-aspirations-of-the-people.md)) ✅
6. [Religion: A Way of Salvation or an Ideology of Oppression?](https://sunilabraham.in/amaa/religion-way-salvation-ideology-oppression-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/religion-way-salvation-ideology-oppression-full-text.md)) ✅
7. [Dalit Theology: A Movement of Counter-Culture](https://sunilabraham.in/amaa/dalit-theology-movement-counter-culture-full-text/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/dalit-theology-movement-counter-culture-full-text.md))
8. [Dalit Liberation—Some Reflections on Their Ideological Predicament](https://sunilabraham.in/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament.md))
9. [The Ideological Nature of the Emerging Dalit Consciousness](https://sunilabraham.in/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness/) ([repository source](https://github.com/sunilabrahamindia/sunilabraham/blob/main/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness.md)) ✅

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


### Essay 4 — The Church and the Study of Religion

**Source compared:** The original *Religion and Society*, Vol. XXVIII, No. 3 (September 1981), pp. 36–41, against `amaa/the-church-and-the-study-of-religion.md`. The supplied page images were reviewed in sequence: 36, 37, 38–39 and 40–41. No page in the supplied sequence was missing.

**Source corrections made**

- **Page 39:** Italicised *liberation and oppression* in the sentence describing the role of structural factors in religion.
- **Page 40:** Removed italics from *God* in the list “dharma, karma, varnashrama, God, papam, punyam”. The word *God* appears in roman type in the original; the surrounding Indic terms remain italicised.

**Differences examined but not changed**

- The italicised appearance of the heading “The Structural factor in Religion” on page 37 and “The realm of meanings and symbols” on page 39 was not reproduced as whole-heading italics. The first-stage editorial rules do not require entire headings to be italicised.
- The apparent underline beneath the phrase “a human historical reality subjected to the psychological and sociological laws...” on page 38 was identified as a reader's handwritten mark on the scanned copy, not original print formatting. No change was made.
- The author-identification footnote on the opening page was not added to the essay text.

**Footnote check**

- Footnotes 1 and 2 (page 36), 3 (page 37), 4 (page 38), 5 (page 39) and 6 (page 40) were checked against the corresponding entries in the essay's Notes section. Their markers and note texts correspond to the supplied source pages.
- The page 37 footnote 3 includes *ex jure*, which is italicised in the essay.
- The author's biographical footnote on page 36 remains excluded, consistent with the treatment of author footnotes in this project.

**Status:** Pages 36–41 reviewed. Two approved italicisation corrections applied, on pages 39 and 40. No other essay-text changes made.

### Essay 5 — Religions and the Aspirations of the People

**Source compared:** The original *Religion and Society*, Vol. XXX, Nos. 3 & 4 (September–December 1983), pp. 102–108, against `amaa/religions-and-the-aspirations-of-the-people.md`. The supplied page images were reviewed in sequence: 102, 103–104, 105, 106–107 and 108. No page in the supplied sequence was missing.

**Source correction made**

- **Page 105:** Extended the italics to the complete sentence beginning “When a religion attaches itself to concrete power interests in a society...” and ending “...the power interests of a particular section.” This sentence continues the italicised passage across the page break from page 104.

**Other findings**

- No other source-text correction was made during this comparison.
- The author footnote on the opening page is not part of the essay text and was not added.
- Footnotes 1 and 2 (pages 103–104) and footnote 3 (page 107) have corresponding entries in the essay's Notes section. Their presence and placement were checked. The exact wording of footnote 3 has not yet been certified by a complete word-for-word transcription comparison; do not treat this entry as closing the collection-wide footnote verification alert above.

**Status:** Pages 102–108 reviewed. One approved italicisation correction applied on page 105. No other edits made to Essay 5.


### Essay 6 — Religion: A Way of Salvation or an Ideology of Oppression?

**Source compared:** The original *Religion and Society*, Vol. XXXII, No. 1 (March 1985), against `amaa/religion-way-salvation-ideology-oppression-full-text.md`. The supplied source pages reviewed in this sequence were printed pages 1 and 4–23. Pages 2–3 were not supplied in this review sequence and remain unchecked. Page 23, the final page, was checked against the closing paragraphs in the essay file.

**Source corrections and editorial changes made**

- **Page 9:** Corrected `Kumbara` to `Kuruba` in the passage identifying the priests of certain *Devasthanams*, following the printed source.
- **Page 10, footnote 1, item (h):** Corrected “To do any announcing or auctioning of any property by the Government” to “To do any announcing of auctioning of any property by the Government”, following the printed source.
- **Pages 11–12:** Italicised the Kannada festival names *Agate Male Ungalu*, *Hasta Malai* and *Pongalu*, and the term *tappa*. The relevant festival subsection heading was also italicised.
- **Pages 13–14:** Italicised the non-English terms identified during the page comparison, including *Ur habba*, *utsava moorti* and *garbagudi*. The relevant festival and subsection headings were brought into line with the essay's heading-italics treatment.
- **Pages 15–16:** Italicised *Makara Sankranti* in its subsection heading and regularised italics across the festival headings, including the headings for Sri Ramanavami, Naga Panchami, Dasara, Deepavali and Basava Jayanti. The spelling and wording of the body text were otherwise retained except for the specific correction recorded below.
- **Page 15:** Corrected the description of *Panaka* from “jaggery and pepper” to “jaggery and green gram”, matching the printed source.
- **Page 17:** Italicised the subsection heading “Birth and naming of the Child” and regularised the italics in the headings for *Mudi* and Marriage. Corrected the transcription of the Lingayat religious consultant from `Siddha` to `Sastri`.
- **Page 19:** Italicised the subsection heading “Death”. Corrected `Kumbara` to `Kurubas` in the list of communities from which the Dasaiahs come, matching the printed source.
- **Page 21, conclusion:** Corrected the opening sentence to read that the Reddy-Vokkaliga-Shetty landlord communities “are the real power in the villages”, matching the printed source. Restored the omitted clause: “nor their power any threat to the status of Brahmins.”
- **Pages 21–22, conclusion references:** Added the missing superscript markers 5, 6 and 7 at the corresponding quotations and passages, and added the matching notes: K. Damodaran, *Indian Thought* (notes 5 and 6), and Gail Omvedt's article in *Economic and Political Weekly* (note 7). Return links were added for all three notes.

**Footnote check**

- **Page 10:** Footnote 1, including its lettered duties (a)–(j), was compared with the source. Item (h) was corrected as recorded above.
- **Page 11:** Footnote 2 was checked against the source.
- **Page 12:** Footnote 3 was checked against the source.
- **Page 13:** Footnote 4 was checked against the source.
- **Page 21:** The two printed references to K. Damodaran were restored as notes 5 and 6, including the *Ibid.* reference.
- **Page 22:** The printed Gail Omvedt reference was restored as note 7.
- The note markers, sequence and corresponding Notes entries for notes 1–7 were checked. The added references have working return links.

**Final page check — page 23**

The final page's two closing paragraphs were compared with the essay file. The continuation of the paragraph beginning on page 22 and the final paragraph beginning “We have come across some empirical evidence...” are present in the correct order. No text correction was required on page 23.

**Pages not yet checked**

Pages 2–3 of the printed essay were not supplied during this review sequence. They must be checked before the page-by-page source comparison can be described as complete.

**Status:** Supplied pages 1 and 4–23 reviewed; approved corrections and formatting changes applied; footnotes 1–7 checked and the missing conclusion references restored. Pages 2–3 remain outstanding.
### Current status — 16 November 2026

- The second-stage audit page has been created as a separate record linked to the first-stage audit.
- Further source checking is the next workstream; individual findings will be entered here as they are examined and verified.
- Automatic print builds triggered by edits to the nine essay source files have been temporarily suspended.
- Manual print builds and the other specified production-file triggers remain available.
- The suspension is temporary and must be reviewed and reversed when the source-checking period is complete.

### Essay 9 — pages 22–23

**Source compared:** Printed pages 22 and 23 of *The Ideological Nature of the Emerging Dalit Consciousness* against the current essay source, `amaa/the-ideological-nature-of-the-emerging-dalit-consciousness.md`.

**Capitalisation differences examined on page 22**

- The printed source uses lowercase *vedic*; the digital text uses *Vedic*. The digital form is retained in accordance with the established capitalisation convention.
- The printed source uses lowercase *brahminic*; the digital text uses *Brahminic*. The digital form is retained in accordance with the established convention recorded in the first-stage audit.
- The printed source uses lowercase *anti-brahminical*; the digital text uses *anti-Brahminical*. The digital form remains unchanged for now. The capitalisation of *Brahminical* is still an open question recorded under "Manual check / future consideration"; this comparison does not close that question or authorise a change.

**Other findings**

- Pages 22 and 23 follow pages 20 and 21 in the supplied sequence; no page number is missing.
- No further wording, omission, or footnote discrepancy requiring correction was identified in this comparison.
- No changes were made to the Essay 9 source for pages 22–23. The existing digital capitalisation was retained; the *Brahminical* decision remains open.

**Status:** Pages 22–23 compared. Audit recorded; no source correction required or applied.

### Essay 3 — pages 23–25

**Source compared:** Printed pages 23–25 of *The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue* against `amaa/living-hindu-popular-religious-consciousness-full-text.md`.

**Findings**

- **Page 23:** The continuation from page 22, the paragraphs on differing Hindu moral and social values, Christian social discrimination, and the socially conditioned experience of religious concepts, and the beginning of the paragraph on dialogue all correspond to the digital text.
- **Page 24:** The continuation of the dialogue paragraph and the discussion of *anubhava*, *pramana*, the point of growth in the living present, and the sacred-profane division correspond to the digital text. The Indic and Latin terms checked for italics, including *anubhava*, *pramana*, *garbha grha* and *versus*, are represented in italics in the digital text.
- **Page 25:** The paragraphs on the Catholic and Protestant traditions, their different treatment of sacred and profane divisions, and the concluding comparison correspond to the digital text.
- The supplied page sequence is continuous: 23, 24 and 25. No footnote marker or footnote text appears on these three pages requiring a separate note check.

**Corrections and status**

No definite omission, wording discrepancy, or footnote discrepancy was identified on pages 23–25. No change was made to the Essay 3 source.

**Status:** Pages 23–25 compared. No source correction required or applied.

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

## Manual check / future consideration

### Brahminical — capitalisation to be reviewed

The capitalisation of *Brahminical* in Essay 9, *The Ideological Nature of the Emerging Dalit Consciousness*, requires a further manual decision.

The first-stage Editorial Source Audit records the form **Brahminical** as the standardised form in the author's narrative. However, the question of whether *Brahminical* should ultimately be uppercase or lowercase is being left open for reconsideration. No change to the essay source is authorised on this point at this stage.

**Status:** Open — manual review and editorial decision pending.

### Essay 9 — page 21: capitalisation of "Vedic" and "Puranic"

The printed source uses lowercase *vedic* and *puranic* in the phrase "vedic and puranic myths" (page 21). The current digital text uses *Vedic* and *Puranic*. This difference is recorded for manual editorial consideration. It is not being treated as an automatic transcription correction, and no change to the essay source is authorised at this stage.

**Status:** Open — retain the current capitalisation pending a manual decision.

### Essay 3 — pages 13–14: capitalisation variations for review

The comparison of printed pages 13–14 of *The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue* identified the following capitalisation differences between the printed source and the current digital text:

- **Page 13:** The printed source uses *Potten teyyam*; the digital text uses *Potten Teyyam*.
- **Page 14:** The printed section heading uses *Suddhi* and *Assuddhi*; the digital heading uses lowercase *suddhi* and *assuddhi*.
- **Page 14:** The printed source uses *Avatars* in item (i); the digital text uses *avatars*.
- **Page 14:** The printed source uses *Sakti* in the phrase "the Sakti of Bhagavan"; the digital text uses *sakti*.

These are recorded as capitalisation variations for later editorial review only. The user has confirmed that none of these forms should be changed at this stage. No changes to the Essay 3 source were made for these points.

**Status:** Recorded for manual capitalisation review. No source changes authorised or applied.

### Essay 3 — page 16: *suddhi* and *asuddhi* in the section heading

The printed heading uses initial capitals in *Suddhi* and *Asuddhi*, while the digital heading uses lowercase *suddhi* and *asuddhi*. The digital form is intentional and follows the first-stage editorial decision that these are generic terms and remain lowercase, including in headings. The heading's first-word capitalisation rule does not require these terms to be capitalised because they occur within the parenthetical phrase, not as the first word of the heading.

This is a record of the already-established editorial decision, not a new inconsistency or a request for further review. No change to the Essay 3 source is required.

**Status:** Decision reaffirmed and recorded. No source change required.


## See also

- [Editorial Source Audit — First Stage](/amaa/30-editorial-source-audit/)
- [Print Book Production: Essays on Dalits, Religion and Liberation II](/amaa/30-print-book-production/)

{% include navbox-amaa.html %}
