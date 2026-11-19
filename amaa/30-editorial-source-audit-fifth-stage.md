---
layout: default
title: "Editorial Source Audit: Fifth Stage — Remaining Checks and Work Log"
permalink: /amaa/30-editorial-source-audit-fifth-stage/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Fifth-stage editorial source audit for Essays on Dalits, Religion and Liberation II, recording remaining checks, corrections, print-proof reviews and production verification."
created: 2026-11-19
---

**Editorial Source Audit: Fifth Stage** continues the editorial preparation of *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It follows the work documented in the [first-stage Editorial Source Audit](/amaa/30-editorial-source-audit/), the [second-stage Editorial Source Audit](/amaa/30-editorial-source-audit-second-stage/), the [third-stage Editorial Source Audit](/amaa/30-editorial-source-audit-third-stage/) and the [fourth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-fourth-stage/).

The earlier stages recorded the collection-wide capitalisation and italicisation review, comparisons with the original printed sources, heading consistency work, the development of editorial conventions and subsequent source-editing and production checks. This fifth stage will provide the working record for the remaining checks and follow-up work required before the volume is ready for publication.

The work will be recorded as it is undertaken. Each entry should distinguish the material examined, the issue identified, the decision taken, any source or production change made and the verification completed. An item must not be described as complete unless the relevant check has actually been carried out.

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

## Purpose and scope

This stage will provide a working record of:

- Remaining editorial and source-verification matters carried forward from the earlier stages.
- Further checks of the nine essays, including their text, headings, notes, references and internal consistency.
- Review of print proofs for layout, pagination, typography, footnotes, quotations, tables and other elements that may affect readability or fidelity to the source.
- Further corrections approved during the present review, with a clear distinction between manuscript-source changes and print-production changes.
- Checks of the Foreword, Editor's Note, About the Author, credit page and other book matter where required.
- Verification of changes and a record of matters that remain unresolved.

The scope is not limited to the nine essays. Where relevant, it may include the complete print-production workflow and the files used to generate the e-book and print editions. Any production intervention will be identified separately from a change to the essay source.

## Relationship with the earlier stages

The earlier audit pages remain the records of the work completed and decisions made in their respective stages. This fifth-stage page does not replace or retrospectively rewrite those records.

- [First stage — Capitalisation and italicisation audit](/amaa/30-editorial-source-audit/)
- [Second stage — Source verification against original publications](/amaa/30-editorial-source-audit-second-stage/)
- [Third stage — Heading consistency and Manual of Style](/amaa/30-editorial-source-audit-third-stage/)
- [Fourth stage — Source editing, final checks and style review](/amaa/30-editorial-source-audit-fourth-stage/)

Where a matter has already been examined, the earlier entry should be consulted. This stage will record any new review, follow-up decision or additional verification rather than duplicating the earlier account.

## Working method

For each activity, record, where applicable:

1. The essay, section, production file or other material examined.
2. The check or editorial question undertaken.
3. The finding, including any discrepancy or uncertainty.
4. The decision and its rationale.
5. The source or production change made, if authorised.
6. The verification performed and its result.
7. Any outstanding action.

Source corrections should be made only after the relevant passage has been examined in context. Avoid broad or automatic changes where individual judgement is required. Preserve the author's meaning, wording and argument unless a specific correction has been established and approved.

## Audit and activity log

### 19 November 2026 — Essay 1, subsection 6: heading indentation after weak page break

**Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**

The print proof showed an indentation inconsistency at subsection 6, "Will the sacred cow return?". Subsections 1–5 use an indented heading position, whereas subsection 6 began further to the left after the weak page-break intervention that moved it to a new page.

The existing weak page break was retained. The Essay 1-specific processing in `ebook/edrl-ii/print/build.py` was adjusted so that the subsection 6 heading is emitted with a 12.1pt horizontal indent immediately after the weak page break. The intervention remains restricted to the exact subsection 6 heading in Essay 1. No wording or formatting was changed in the essay manuscript source, and no other essay or section was targeted.

The first build attempt (#523) exposed a Typst syntax error in the heading-emission expression. That expression was corrected, and the subsequent print-proof workflow completed successfully.

**Verification:** GitHub Actions build #524 completed successfully and uploaded the `edrl-ii-print-preview-524` artifact. The source change is recorded in commit `df7aa83d2c64570f81ae8f853688a1e07c5f68e6`. The generated PDF is available for visual confirmation of the heading alignment; the final visual comparison against subsection 5 remains to be made.

**Status:** Print-builder correction committed and print build successful. Final visual confirmation of the indentation remains pending.


### 19 November 2026 — Essay 3: English translation added to Poonthanam quotation and footnotes renumbered

**Essay 3 — The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue**

The quotation attributed to Punthanam in Part I, Section B, point (2), was present in the source as two Romanised Malayalam lines, without an English translation. An English translation has now been added immediately below the original lines, retaining the existing Romanised text unchanged and presenting the translation across two corresponding lines:

> Within just two or four days, You have a man carried on a bier;  
> You place a burden on the shoulders of a king who has risen to the heights of his palace.

A footnote has been added to clarify the editorial provenance of the translation: it was not included in the original journal publication and has been added for the present publication.

Because this new note occurs before the essay's existing notes, the footnotes were renumbered sequentially throughout the source. The new translation note is now note 1; the eight pre-existing notes have moved to notes 2–9. All in-text reference anchors, note IDs, citation targets and return backlinks were updated to match. This preserves the order in which the notes occur in the essay and avoids a numbering sequence that would be incorrect in the printed book.

**Verification:** The main source, `amaa/living-hindu-popular-religious-consciousness-full-text.md`, was updated in commit `affb508901565f9c942f997a6982a3c9ddf4706f`. The nine note IDs and nine reference anchors were checked for sequential numbering, and the corresponding citation targets and backlinks were checked for consistency. No duplicate IDs were found.

**Status:** Source updated and footnote sequence and links validated. Print-proof review of the translated quotation and its footnote remains part of the production checks.

### 19 November 2026 — Essay 3, Section B: numbered-point spacing and blockquote presentation

**Essay 3 — The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue**

#### Numbered-point spacing

The print proof showed inconsistent spacing after the numbered labels in Section B. Some points appeared correctly as `(1) A sense...`, while others ran directly into the following text, for example `(2)Another...` and `(6)Experience...`.

The original Markdown source was checked. It contains the expected space after each numbered label, so the problem was in the Essay 3-specific transformation in `ebook/edrl-ii/print/build.py`. For points (2), (6), (7), (10) and (11), the script replaces the source label with an inline Typst spacing command and number. The replacement had omitted the space after the closing parenthesis.

The replacement was corrected to retain that space. No change was made to the Essay 3 manuscript, global paragraph settings, line leading or other indentation rules. The correction is limited to the five numbered points handled by this print-only transformation.

**Verification:** The change was committed on the test branch `test/blockquote-curly-quote-20261119` in commit `d790a2042445ef317d010c558368fd15c6b7b5a4`. GitHub Actions print build #538 completed successfully and uploaded the print-preview artifact. Visual confirmation of the corrected gaps in the resulting PDF remains pending. The `main` branch was not changed.

**Status:** Print-builder correction committed on the test branch; build successful. Final visual confirmation remains pending.

#### Blockquote presentation

The Essay 3 print proof was also reviewed for the visual distinction of blockquotes. The existing Typst blockquote treatment was retained, including its 12pt spacing above and below, 22pt left and right insets, 10.5pt text size, 9pt leading and 10pt paragraph spacing. No vertical rule or background was introduced.

An initial attempt to add the opening and closing curly quotation marks as separate Typst layout elements produced an incorrectly positioned closing mark and was withdrawn. A subsequent attempt inserted the marks into the Markdown text before conversion. Build #537 completed successfully, but inspection of the generated PDF's extracted text showed that the curly quotation marks had not appeared. The intended visual treatment is therefore not yet achieved.

The blockquote investigation and its changes remain confined to the same test branch. The main branch and the Essay 3 manuscript source were not changed for this experiment.

**Verification:** Build #537 completed successfully and uploaded the print-preview artifact. The extracted PDF text did not contain the intended curly quotation marks. The result is not accepted as a completed correction.

**Status:** Unresolved. Further investigation is required at the Markdown-to-Typst conversion stage. No further blockquote change has been made as part of the numbered-point spacing correction.

## Outstanding work

Remaining checks will be added here as they are identified and undertaken. Each item should retain its context and should be marked complete only after the relevant source check, build or visual verification has been carried out.

An item should be removed or marked complete only after its outcome has been verified. Matters carried forward from earlier stages should retain their original context and should not be treated as new findings without a fresh check.

{% include navbox-amaa.html %}
