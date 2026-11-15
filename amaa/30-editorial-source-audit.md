---
layout: default
title: "Editorial Source Audit: Capitalisation and Italicisation of Indic Words in Essays on Dalits, Religion and Liberation II"
permalink: /amaa/30-editorial-source-audit/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Essay-wise source audit of capitalisation and italicisation of Indic words and terms across the nine essays in Essays on Dalits, Religion and Liberation II."
created: 2026-11-15
---

**Editorial Source Audit** documents the review of capitalisation and italicisation in the nine essays included in *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. The audit responds to the editorial review of the book, which identified inconsistencies in the treatment of terms such as "Dalit" and "Sakti/sakti". These variations may occur within an individual essay as well as across the collection.

The purpose is to establish a consistent and defensible editorial approach while preserving the author's meaning, terminology and argument. This is a source-level exercise: decisions and approved corrections will be made in the individual essay source files, not through `build.py`, the Typst layout or an automated typesetting rule. The decisions will also be recorded in an editorial style-sheet that can guide the preparation of other works by the author.

## Scope

The audit initially covered the nine main essays. It has now been extended to three additional book sections: About the Author, the Foreword by Y. T. Vinayaraj, and the Editor's Note (including its acknowledgement section). The audit therefore covers twelve sections in total. Capitalisation and italicisation are separate workstreams; a decision in one does not automatically determine the other.

## Audit criteria

## Heading-first-word rule (H2-H4)

A separate heading rule applies to every H2, H3 and H4 section heading: the first word must begin with a capital letter, even when that word is normally lowercase in running text. This heading rule takes precedence over the lowercase treatment of generic Indic terms in body text. The rule applies only to the first word of the heading; it does not convert the rest of the heading to title case.

**Nine-essay heading audit:** All H2-H4 headings in the nine essay source files were checked. One heading required correction:

- Essay 3: `#### punyam` changed to `#### Punyam`.
- Essay 9: The subsection labels `a.` and `b.` were inspected and retained exactly as authored. They are structural labels, not heading words, and are exempt from the first-word capitalisation rule.

No other H2-H4 heading in the nine inspected essay files required correction. Essay 1's full-text source contains no Markdown H2-H4 headings. No body-text occurrences were changed as part of this heading pass.

## Heading audit (H2-H4)

A separate heading-italicisation audit was completed for H2, H3 and H4 headings in all nine essay source files. The rule is consistent: an Indic or regional-language term already identified for italicisation in an essay body receives the same treatment when it appears in a heading. The detailed findings and the one print-builder correction are recorded below. This heading pass is separate from the heading-first-word capitalisation rule.

### Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends

**Findings**

- The H2 heading `1. The saktis of the gaps will disappear` contains the Indic term *saktis*, which is included in the Essay 1 italicisation list above.
- The source heading previously used Markdown asterisks inside an HTML heading. That did not provide reliable inline emphasis in the HTML source and the print builder's HTML-heading conversion stripped inline formatting.
- The source heading has now been changed to use `<em>saktis</em>`, so the term is explicitly italicised in the rendered source page.

**Print-build handling**

- The print builder now preserves `<em>` and `<i>` as Typst italics, and `<strong>` and `<b>` as Typst bold, when converting HTML headings.
- This ensures that the italicised *saktis* is retained in the print heading rather than being flattened to roman type.
- Markdown heading emphasis conversion remains unchanged.

**Verification**

- The Essay 1 Markdown source contains explicit HTML emphasis around *saktis* in the H2 heading.
- The print builder's HTML-heading path now translates that emphasis into Typst italic markup.
- The change is confined to the Essay 1 heading and the builder's inline-format preservation for HTML headings. No heading wording, essay body text or other essay source has been changed.
- The generated PDF must be checked after the next build to confirm the final visual output.

**Status:** Source markup and print-builder handling updated for Essay 1. Final PDF visual verification is pending the next successful print build.

## Manual PDF proof checks

The downloaded PDF is also being checked manually in Okular using case-sensitive searches. This is a separate visual proofing step; it does not replace the source-level audit above.

- **Dalit / Dalits:** The case-sensitive searches have been checked across the nine essays. The collection-wide capitalisation decision is uppercase *Dalit* and *Dalits* in the essay text. No lowercase occurrences remain in the essay text. Lowercase forms in URL/permalink slugs are not part of the prose and are intentionally unchanged.
- **Other terminology:** Additional case-sensitive searches are being checked in the PDF. Only terms actually inspected and confirmed will be marked complete here; a suggested search list is not evidence that a term has been checked.


Each occurrence will be examined in its actual sentence and context. The review will apply the following criteria:

### Capitalisation criteria

- Determine whether the term functions as a proper name, common noun, adjective, or another grammatical form.
- Check whether uppercase and lowercase forms carry a contextual or grammatical distinction.
- Compare usage within the essay and across the collection.
- Consider theological, philosophical and historical context.
- Check whether a variation may reproduce the original printed source.
- Standardise only where the evidence supports a consistent editorial form; retain justified variations and record exceptions.

### Italicisation criteria

- Check whether the same Indic word or expression is italicised consistently within an essay and across the collection.
- Consider whether it is being used as an Indic term or has become established in the surrounding English text.
- Examine quotations, titles and other contexts that may affect treatment.
- Compare the source text with the original printed source where necessary.
- Record the preferred treatment before making any source correction.

### Correction and verification criteria

- No blind or bulk find-and-replace operations.
- Record the observed form, context, decision and reason before changing a source.
- Make approved corrections in the individual Markdown essay source only.
- Re-read each corrected passage to ensure that meaning has not changed.
- Record unresolved questions for later review rather than guessing.

## Audit procedure

The review will begin with one essay at a time so that the criteria can be tested against actual usage and context. Once the approach is sufficiently clear, the work can proceed two essays at a time.

For each essay, identify the relevant terms and variations, inspect every occurrence in context, compare with the original print source where relevant, make and record an editorial judgement, apply only approved corrections, and verify the result.

## Audit reports

The following twelve sections form the working report area. Each section has its own findings and decisions. The report distinguishes between observed evidence, editorial judgement, corrections made and items requiring further review.

### 1. The State of Hinduism in 2000 A.D.—Some Emerging Trends

**Full source inspected:** [The State of Hinduism in 2000 A.D.—Some Emerging Trends](/amaa/state-of-hinduism-in-2000-ad-full-text/).

**Capitalisation audit — changes made**

The following approved capitalisation changes have been applied to the essay source:

- **Sakti / sakti:** Changed "Presence of the Sakti" to "Presence of the sakti". The general theological concept is written as lowercase *sakti*; the plural is *saktis*. The word will be capitalised only when used as a proper divine name.
- **Harijan / Harijans:** Changed lowercase "harijan" and "harijans" to "Harijan" and "Harijans" throughout this essay. The author's historical terminology has been retained; it has not been replaced with another term.
- **Brahmin / Brahmins:** Changed lowercase "brahmin" and "brahmins" to "Brahmin" and "Brahmins" throughout this essay.

**Capitalisation decisions retained without change**

- **Bhagavan / bhagavans:** Retained "Bhagavan" and "Bhagavan's" for the singular divine name or title, and lowercase "bhagavans" for the generic plural.
- **God / god / gods:** Retained "God" for a specific divine referent and lowercase "god/gods" for generic references. The compound "god-hypothesis" remains lowercase.
- **Brahman:** Retained "Brahman". It is distinct from "Brahmin" and must not be conflated with it.

These decisions are recorded for Essay 1. Their consistency across the remaining essays will be examined during the collection-wide audit.

**Italicisation audit — changes made**

The italicisation pass has now been completed for the Indic and regional-language vocabulary identified in this essay. Existing italicisation was made consistent by italicising unmarked occurrences of the same terms and expressions.

The terms standardised include:

- *Amman*, *Mata*, *Amman/Mata*, *kop*, *prasad*, *rogi*, *Bheemar*, *rogi/Bheemar*.
- *nagadosam*, *Ezachi*, *Brahmarakshas*, *Gulikan*, *punya nadi*, *Gomata*, *nagam*.
- *andhavisvasam*, *Suryan*, *Chandran*, *Grahangal*, *prakriti saktikal*, *vanangal*.
- *bhagavans*, *Teechamundi teyyam*, *Teechamundi*, *Urachil attam*, *tamasa*.
- *karmaphalam*, *saktibaba*, *parasakti*, *sakti*, *saktis*, *rog*, *potten teyyam*, *suddikarma*.
- *pucca*, *advaitin*, *jivatmans*, *Paramatman*, *sanatandharma*, *lila*, *dharma*.
- *Iswarapuja*, *Deivaseva*, *manasanti*, *bhutas*, *pretas*, *bhayam*, *mantravadis*, *pujaris*, *yakshis*, *pujas*, *sandyavandana*, *mutt*.

This is a consistency pass within Essay 1. The treatment of these terms will be compared with the other essays before the final collection-wide style-sheet is closed.

**Other editorial observations**

- Deferred for a later stage. The present work is limited to capitalisation and italicisation; spelling, transcription, punctuation and other source-verification questions are not being investigated now.

**Verification**

- The capitalisation and italicisation changes have been applied to the Markdown source.
- No wording or spelling has intentionally been changed as part of the italicisation pass.
- The full source should be checked in the rendered page or next proof to confirm the formatting displays as intended.

**Status:** The capitalisation decisions and the Indic-term italicisation pass have both been applied to Essay 1. The source has not been checked against the original printed article as part of this pass.
### 2. Religion, Spirituality and Aspirations of the People

**Full source inspected:** [Religion, Spirituality and Aspirations of the People](/amaa/religion-spirituality-and-aspirations-of-the-people-full-text/).

**Capitalisation audit — changes made**

The following source-level capitalisation corrections have been applied:

- **Sakti / sakti:** Changed generic references to "a non-existent sakti" and "a sakti" to lowercase. This follows the Essay 1 distinction: lowercase *sakti* for the general concept; uppercase only when used as a proper divine name.
- **Brahmin:** Changed "brahmin-high caste dominance" to "Brahmin-high caste dominance", consistent with the treatment of the caste name in Essay 1.
- **Humanism:** Changed "Humanism" to "humanism" where it is used as a generic concept in the phrase "scientific truths, humanism, Marxism".
- **Faiths:** Changed "religious Faiths" to "religious faiths"; the word is a common noun in this context.
- **Struggle:** Changed "our Struggle" to "our struggle"; it is a common noun in the sentence.

No other capitalisation variants were changed. Names, titles, institutional references and contextually distinct forms were retained.

**Italicisation audit — changes made**

The following Indic terms and expressions were italicised where they appeared in roman type:

- *andhamaya visvasam*, *daivasankalpam*, *Suddhi Karmam*, *karma phalam*, *karmavidhi*.
- *yajamananmar*, *vazhipad*, *kaphirangal*, *sandyavandana*.
- *Iswar*, *Karma*, *Dharma*, *Bhutas*, *Samskaras*.
- *matam*, *suddhi*, *pula*, *jati*, *vargiyata*, *Kartav*.
- *bhakti*, *papi*, *samaram*, *vidhi*, *karmam*, *sakti*, *saktis*, *pujas*.

Existing italicisation was retained. The English phrase "Spirituality of Combat" remains in roman type. Proper names, including personal names, were not italicised merely because they are Indian.

**Capitalisation decisions retained without change**

- **Harijan:** Retained the author's historical term and its existing capitalisation.
- **Brahmin:** Existing correctly capitalised uses were retained; only the lowercase compound form noted above was corrected.
- **God / god:** Existing forms were retained according to their specific or generic references.
- **Communism / Marxism:** Retained as names of political ideologies.
- **Church / church:** Retained according to whether the reference is to the specific institution or to churches generally.

These decisions are specific to the contexts inspected in Essay 2 and remain subject to collection-wide comparison.

**Other editorial observations**

- Deferred. The present audit is limited to capitalisation and italicisation. Wording, spelling, transcription, punctuation, references and other source questions have not been edited.

**Verification**

- The source edit was checked by comparing the text before and after the changes. After disregarding Markdown emphasis markers and reversing the listed capitalisation substitutions, the text matched the original exactly.
- This verifies that no wording, spelling, punctuation, paragraph structure, links or other non-formatting content was changed.
- A follow-up correction kept the English phrase "Spirituality of Combat" in roman type.
- The source has not been compared against the original printed article, and the rendered page has not yet been visually checked.

**Status:** Capitalisation and italicisation audits completed for Essay 2. The Markdown source changes are limited to the recorded capitalisation and italicisation corrections.

### 3. The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue

**Full source inspected:** [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue](/amaa/living-hindu-popular-religious-consciousness-full-text/).

**Capitalisation audit — changes made**

- **Sakti / sakti; Saktis / saktis:** Generic references to the theological concept and its plural have been standardised to lowercase *sakti* and *saktis*. The term is used descriptively throughout the essay, including in the reported speech of interviewees.
- **Parasakti / para sakti:** Lowercase forms have been applied to the generic concept, including the spaced form *para sakti*.
- **Karma / karma; Dharma / dharma:** Generic philosophical and religious concepts have been lowercased.
- **Punyam / punyam:** The generic term is lowercase in running text. The H4 heading `#### Punyam` begins with a capital, in accordance with the heading-first-word rule.
- **Suddhi / suddhi; Asuddhi / asuddhi:** The terms for purity and impurity have been lowercased in the section headings and text.
- **Suddhi / suddhi; Asuddhi / asuddhi:** Both are generic terms and are set in lowercase italics: *suddhi* and *asuddhi*. The essay's existing transliteration is retained for this capitalisation-and-italicisation audit. The variant spelling "assuddhi" in the section heading in section II.1 is recorded for a separate spelling/transliteration review, not silently changed here.
- **Samkalpam / samkalpam:** The generic term has been lowercased.
- **Jivatman, Paramatman, Prakriti, Purusha and Antaryamin:** These philosophical terms have been lowercased where listed as concepts.
- **Avatars / avatars:** The generic plural has been lowercased.
- **Faith / faith:** Generic uses in the introduction, section heading and phrase "faith categories" have been lowercased. The rhetorical heading "That faith is faith's own proof" is retained in its original wording apart from this capitalisation standardisation.

**Capitalisation decisions retained without change**

- **Bhagavan, Iswar, Iswara, Iswaran and Daivam:** Retained as divine names or designations in the contexts in which they occur.
- **Brahman:** Retained as the philosophical name in the quoted account.
- **God:** Retained according to the essay's English theological usage.
- **Harijans:** Retained with the capitalisation established in the earlier essay audit.
- **Names and named traditions:** Personal names, place names, deity names and named philosophical systems were not lowercased.

**Italicisation audit — changes made**

- Added italics to *jivatman*, *paramatman*, *prakriti*, *purusha* and *antaryamin* in the paragraph listing philosophical terms (section II.1).
- Existing italicisation of *sakti*, *saktis*, *parasakti*, *karma*, *dharma*, *punyam*, *suddhi* and other Indic expressions was retained while their capitalisation was standardised where required.
- Existing italics in quoted and explanatory passages were retained. Proper names were not italicised merely because they are Indian.

**Other editorial observations**

- The present audit does not correct spelling, transliteration, grammar, punctuation or factual content. These remain outside scope.

**Verification**

- The source was updated in one commit after both audits.
- The source retained the same 359-line structure.
- A comparison after removing Markdown emphasis markers confirmed that the only textual differences were the explicitly listed capitalisation changes. The only added emphasis markers surround the five philosophical terms listed above.
- No words were added or removed, and no spelling, punctuation, whitespace, paragraph structure, links or front matter were changed.

**Status:** Capitalisation and italicisation audits completed for Essay 3. Source corrections are limited to the recorded case and italic-formatting changes.



**Heading audit (H2-H4) and follow-up italicisation corrections**

**Complete heading re-audit — 15 November 2026**

- All 20 H2-H4 headings in the live Essay 3 source were enumerated and inspected, not just the headings previously flagged.
- Six heading lines were corrected in the source: section C (*parasakti*); the H4 question heading (*papam*, *adharmam*); the H4 headings *Papam* and *Punyam*; the section on God-conception (*suddhi*, *asuddhi*); and section G (*karmam*, *samaya dosam*). The two H4 headings for *Papam* and *Punyam* are counted separately, making six heading lines corrected in total.
- The section D heading already had both *suddhi* and *assuddhi* italicised and was retained. All remaining headings were checked and retained.
- The updated source was fetched again from GitHub. The six corrected heading lines were confirmed to contain the intended Markdown emphasis markers.
- Source commit: `8b3fc61f1b3975c8f0340533339b83866a141720` ("Italicise Indic terms in all Essay 3 headings").

**Status:** Complete H2-H4 heading re-audit and source corrections completed for Essay 3. This verifies the Markdown source markup; rendered-page and print-PDF appearance still require visual checking.


- The complete H2-H4 heading inventory was rechecked directly against the live Essay 3 source. This second, heading-only audit found omissions that the earlier audit had incorrectly reported as already corrected.
- Corrected the H3 heading in section C to italicise *parasakti*.
- Corrected the H4 heading "What is *papam* or *adharmam*?" and the H4 headings "*Papam*" and "*Punyam*".
- Confirmed that the H3 heading in section D already italicised *suddhi* and *assuddhi*; retained it.
- Corrected the H3 heading "God-conception and the traditional practices of purity and pollution" so that *suddhi* and *asuddhi* are individually italicised, while the English conjunction remains roman.
- Corrected the H3 heading in section G so that *karmam* and *samaya dosam* are individually italicised.
- Rechecked every other H2-H4 heading in the essay. No other heading contained an Indic term from the essay's identified italicisation vocabulary that required a further correction.
- The numbered statements (1)–(6) in section I.B are bold paragraph statements, not Markdown H2-H4 headings. The generic term *sakti* is now italicised in these statements wherever it appeared in roman type.
- A full-text follow-up found additional unitalicised occurrences of *sakti* and *saktis* in the opening quoted account, numbered statements, surrounding prose and quotations. All generic occurrences in Essay 3 have now been italicised; existing italics were retained. The spaced expression *para sakti* is italicised as a complete expression where it occurs.

**Essays 4 and 5 — heading audit**

- Essay 4, "The Church and the Study of Religion": all H2-H4 headings were inspected. None contains an Indic term from the essay's italicisation list; no heading correction was required. The terms recorded in the body-text audit, including *avarna jati*, *dharma*, *karma*, *varnashrama*, *papam* and *punyam*, are already italicised in the body text.
- Essay 5, "Religions and the Aspirations of the People": all H2-H4 headings were inspected. None contains an Indic term from the essay's italicisation list; no heading correction was required. The existing body-text italicisation decisions for *puja*, *Nivedyam*, *mantra*, *mantras* and *pujas* remain unchanged.

**Verification and status**

- Essay 3 source formatting was updated without changing wording, spelling, punctuation, paragraph order or metadata.
- Essays 4 and 5 required no heading changes in this pass.
- The next EDRL II print build will render the updated Essay 3 source. The generated PDF still requires visual inspection to confirm the printed italic treatment.

**Status:** Essay 3 body-text and H2-H4 italicisation corrections applied. Essay 4 and Essay 5 heading audits completed; no corrections required.

### 4. The Church and the Study of Religion

**Full source inspected:** [The Church and the Study of Religion](/amaa/the-church-and-the-study-of-religion/). The complete essay is embedded in the article's "Full text" section; no separate full-text page exists.

**Capitalisation audit — findings and decisions**

- **Indic terms:** The generic terms *avarna jati*, *dharma*, *karma*, *varnashrama*, *papam* and *punyam* are already lowercase.
- **Teyyam / Teyyams:** Retained capitalisation as the name of the North Malabar religious tradition and its associated ritual figures in this article.
- **Proper names and designations:** Personal names, caste/community names, place names and institutional names were retained.
- No capitalisation correction was required in the inspected essay text.

**Italicisation audit — findings and decisions**

- The Indic expressions *avarna jati*, *homas*, *yagnas*, *mutts*, *ashrams*, *dharma*, *karma*, *varnashrama*, *papam* and *punyam* are already italicised in the article's full-text section.
- Existing italicisation in the notes, including *Sthalamahatyama*, *namas*, *ex jure* and *op. cit.*, was retained.
- **Teyyam / Teyyams:** Retained in roman type as the name of a named religious tradition and its ritual figures, rather than treated as ordinary untranslated vocabulary.
- No italicisation correction was required in the inspected essay text.

**Verification**

- The complete article source, including the embedded full text and notes, was inspected.
- No source changes were made: the existing capitalisation and italicisation were consistent with the decisions recorded above.
- Front matter, article summary, contents, publication details, notes, links, styling and all other content remain untouched.

**Status:** Both audits completed for Essay 4. No source correction was necessary.

### 5. Religions and the Aspirations of the People

**Full source inspected:** [Religions and the Aspirations of the People](/amaa/religions-and-the-aspirations-of-the-people/). The full essay is embedded in the article's "Full text" section.

**Capitalisation audit — findings and decisions**

- **Brahmin / Brahmins:** The caste name is consistently capitalised in the inspected essay and notes; no correction was required.
- **Dalit / Dalits:** The terms are capitalised consistently in the author's usage; retained.
- **Harijan:** Retained in the historical quotation and discussion. It has not been replaced.
- **God / god:** Specific references to God and generic references to a god were retained according to context.
- **Bhakti:** Retained in "Bhakti movement" as the name of a historical religious movement.
- No source-level capitalisation correction was made. Capitalised words in quotations, titles and named institutions were retained.

**Italicisation audit — changes made**

- The generic Indic term *puja* was italicised in its previously unmarked occurrence(s).
- Existing italicisation of *Nivedyam*, *mantra*, *mantras* and *pujas* was retained. The unmarked generic *puja* was italicised, and the expression *Namaskara puja* was kept together as one italicised phrase wherever it occurs.
- *Channer lahala* and the title *Social Justice and Ashrams* were already italicised and were retained.
- Personal names, deity names, institutional names and English expressions were not italicised merely because they occur in an Indian context.

**Verification**

- The full embedded essay, publication details and notes were inspected.
- The source update was checked against the previous version. After removing Markdown emphasis markers, the text matched exactly; no words, spelling, punctuation, paragraph structure, links, metadata or other content were changed.
- The source has not been compared against the original printed article, and the rendered page has not yet been visually checked.

**Status:** Both audits completed for Essay 5. The only source correction was the recorded italicisation of *puja*.

### 6. Religion: A Way of Salvation or an Ideology of Oppression?

**Full source inspected:** [Religion: A Way of Salvation or an Ideology of Oppression?](/amaa/religion-way-salvation-ideology-oppression-full-text/).

**Capitalisation audit — findings and decisions**

- **Brahmin / Brahmins:** Retained uppercase for the caste name throughout the prose and tables.
- **Brahminical / brahminical:** Both forms occur. Lowercase is used in running prose, while uppercase appears in heading-style contexts. No blanket replacement was made; the distinction will be checked against the printed source before any standardisation.
- **Autochthonous:** The term appears in heading-style and running-text contexts. Existing forms were retained pending comparison with the original print source.
- **Devasthanam / Devasthanams:** Retained as used in the essay. Whether these are being treated as a generic institutional term or a named category requires confirmation from the printed source.
- **God / god:** Specific and generic references were retained according to context.
- **Names and named festivals:** Personal names, deity names, caste/community names and festival names were retained.
- No capitalisation corrections were made in this pass. Ambiguous forms have been recorded rather than standardised by assumption.

**Italicisation audit — changes made**

The following Indic terms were italicised where they appeared in roman type:

- *Devasthanam*, *Devasthanams*, *gudi*, *gudis*, *Purohit*, *Mudi*.
- *puja*, *kumkum*, *udubathi*, *agarbathi*, *Jathra*, *prasadam*.

Existing italicisation was retained for terms and expressions including *rache*, *Ur habba*, *utsava moorti*, *garbagudi*, *kumbalakayee*, *Anna Chatra*, *Panaka*, *mora*, *moras*, *Siddha* and *Dhare*. Proper names and named festivals were not italicised merely because they are Indian.

**Verification**

- The complete 371-line Markdown source, including tables, the full essay and notes, was inspected.
- The source update was checked against the previous version. After removing Markdown emphasis markers, the text matched exactly; no words, spelling, punctuation, paragraph structure, links, metadata, tables or other content were changed.
- The source has not been compared against the original printed article, and the rendered page has not yet been visually checked.
- Capitalisation questions listed above remain deliberately unresolved; no spelling or transliteration corrections were made.

**Status:** Both audits completed for Essay 6. Source changes are limited to the recorded Indic-term italicisation corrections.

### 7. Dalit Theology: A Movement of Counter-Culture

**Full source inspected:** [Dalit Theology: A Movement of Counter-Culture](/amaa/dalit-theology-movement-counter-culture-full-text/).

**Capitalisation audit — changes made**

- **Dalit / Dalit; Dalits / Dalits:** Standardised the author's narrative references to *Dalit* and *Dalits*, including the derived term *Dalitism*, with uppercase initial letters. The quoted occurrence discussed as a term was also changed to "Dalit" in accordance with the collection-wide decision. No lowercase `dalit` or `dalits` remains in the essay text; the lowercase permalink slug is intentionally unchanged.
- **Karma / karma:** Changed the generic philosophical concept from "Karma" to lowercase "karma", consistent with the treatment of generic Indic concepts in the earlier essays.
- **Brahmin / Brahmins; Brahmanical / Brahmanic:** Existing capitalisation was retained. These forms refer to caste identity, cultural/religious traditions or related designations in the contexts in which they occur.
- **God / god:** Existing forms were retained according to context, including the quoted phrase "the people of God".
- **Named texts, traditions, communities and people:** Existing capitalisation was retained. No spelling or transliteration was changed.

**Italicisation audit — changes made**

- Added italics to the generic Indic terms *trivikrama*, *rakshasas* and *amrita*.
- Set the generic philosophical term *karma* in lowercase italics.
- Existing italicisation of *colony*, *cheri*, *palli* and *onavil* was retained.
- Indic terms appearing inside direct quotations, including "shamkara" and "atman", were left as they appeared in the quotation. Names and titles were not italicised merely because they are Indian.
- The compound *Dharmasastras* was retained intact and was not split or partially italicised.

**Verification**

- The complete 405-line Markdown source, including the essay and notes, was inspected.
- The source was updated only for the listed capitalisation and italic-formatting changes. A comparison with the pre-edit source confirmed that, after removing Markdown emphasis markers and reversing the recorded capitalisation substitutions, the text matched exactly.
- No words were added or removed; no spelling, punctuation, paragraph structure, links, front matter, notes or other content was rewritten or corrected.
- The source was fetched again after the update. Its 405-line structure remains unchanged.
- The source has not been compared against the original printed article, and the rendered page has not yet been visually checked.

**Status:** Capitalisation and italicisation audits completed for Essay 7. Source changes are limited to the recorded case and italic-formatting corrections.

### 8. Dalit Liberation — Some Reflections on Their Ideological Predicament

**Full source inspected:** [Dalit Liberation — Some Reflections on Their Ideological Predicament](/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament/). The complete essay is embedded in the article's "Full text" section.

**Capitalisation audit — findings and decisions**

- **Dalit / Dalits:** The terms are consistently capitalised in the author's narrative. No correction was required.
- **Harijan / Harijans:** Retained with initial capitals in the historical discussion and in the cited account of the Kerala study. The author's historical terminology has not been replaced.
- **Brahmin / Brahminical:** Retained with initial capitals for the caste name and the adjective describing its religious authority and value system.
- **Aryas:** Retained as capitalised in the reported statement quoted in the opening section.
- No source-level capitalisation correction was necessary. Capitalisation within direct quotations was retained.

**Italicisation audit — findings and decisions**

- The essay contains no unitalicised Indic expression for which a source correction was judged necessary in this pass.
- *Religion and Society* and the other publication titles are already italicised where required.
- Terms such as "Vedas", "Sastras" and "smritis" occur within a direct quotation attributed to Ambedkar. Their treatment within the quotation has been retained rather than editorially reformatted.
- "Hartal" and "laddus" occur as words used in the English narrative and are retained in roman type.
- No source-level italicisation correction was made.

**Verification**

- The complete 105-line article source, including the embedded full text and publication details, was inspected.
- No source changes were necessary. The existing capitalisation and italicisation were retained.
- The front matter, article summary, text, quotations, publication details, links, notes and styling remain untouched.

**Status:** Both audits completed for Essay 8. No source correction was required.

### 9. The Ideological Nature of the Emerging Dalit Consciousness

**Full source inspected:** [The Ideological Nature of the Emerging Dalit Consciousness](/amaa/the-ideological-nature-of-the-emerging-dalit-consciousness/). The complete essay is embedded in the article's "Full text" section.

**Capitalisation audit — changes made**

The following source-level capitalisation corrections have been applied in the author's narrative:

- **Dalit / Dalits:** Lowercase generic occurrences of "dalit" were standardised to "Dalit" in "Dalit movement", "Dalit ideology", "Dalit identity", "Dalit nationality", "Dalit organisations", "Dalit politics", "Dalit religion", "Dalit demands", "Dalit party workers", "Dalit classes" and "Dalit liberation".
- **Non-Dalit:** Changed "non-dalit castes" to "non-Dalit castes", retaining the original compound and its meaning.
- **Brahminical / Brahminic:** Standardised lowercase "brahminical" and "brahminic" to "Brahminical" and "Brahminic" in the author's narrative. Existing "Brahminism" and other correctly capitalised forms were retained.
- **Vedic / Puranic:** Changed generic adjectives "vedic" and "puranic" to "Vedic" and "Puranic" in references to Vedic and Puranic myths and civilisation.

**Capitalisation decisions retained without change**

- The lowercase "dalit" in the permalink slug remains unchanged.
- The wording "the Dalit Nationality" is capitalised inside the quoted passage under the collection-wide standardisation decision. This was an explicit editorial decision, not an automatic normalisation.
- Names, titles, institutional names, and the existing capitalisation of Dalit/Dalits in the rest of the article were retained.
- No wording or spelling correction was made, including in passages whose grammar or phrasing may warrant separate editorial attention.

**Italicisation audit — findings and decisions**

- The Indic expression *Mardhita Desiyata* is already italicised and was retained.
- The Kannada slogan *jati bidi, mota bidi, manavatage jiva kodi* is already italicised and was retained as one expression.
- Existing italicisation of *Dalitaru Barvaru*, *Mahasammate the Great Elect*, *Homo hierarchicus* and *homo democraticus* was retained.
- Titles of books, journals, poems and publications in the notes were already italicised where required.
- Indic terms appearing in quoted poetry and other direct quotations were not reformatted. No additional italicisation correction was judged necessary.

**Verification**

- The source update was limited to the recorded capitalisation changes.
- The source remains 334 lines. A case-insensitive comparison confirmed that the text is lexically identical before and after the update. The GitHub commit diff was inspected and showed only the recorded capitalisation changes.
- No words were added or removed. Spelling, punctuation, paragraph structure, links, front matter, quotations, notes and styling were not otherwise changed.
- The quoted phrase "the Dalit Nationality" was checked and capitalised. The lowercase permalink slug remains unchanged by design.

**Status:** Capitalisation and italicisation audits completed for Essay 9. Only the recorded capitalisation changes were applied to the Markdown source.


### 10. About the Author

**Source inspected:** The About the Author text in the paperback print source, `ebook/edrl-ii/print/build.py`. The same biographical text is reproduced in the print build; the e-book front matter currently does not contain this section.

**Capitalisation audit — findings and decisions**

- **A. M. Abraham Ayrookuzhiel:** Personal name retained in its existing form throughout.
- **Dalit / Dalits:** Retained with initial capitals when referring to the communities and their identity.
- **Christian Institute for the Study of Religion and Society (CISRS):** Institutional name and acronym retained.
- **Anglican Church, St. Paul High Anglican Church, United Kingdom, Rome, Kerala, Chengannur, Puthenkavu, Thiruvananthapuram, Pune, Bangalore, Wokingham and Berkshire:** Proper names and institutional designations retained.
- No capitalisation correction was made.

**Italicisation audit — findings and decisions**

- The titles *The Sacred in Popular Hinduism: An Empirical Study in Chirakkal, North Malabar*, *Swami Anand Thirth: Untouchability, Gandhian Solution on Trial* and *The Dalit Desiyata: The Kerala Experience in Development and Class Struggle* are already italicised.
- No other Indic word or expression requiring italics was identified in the biographical text.
- No italicisation correction was made.

**Verification**

- The complete biographical text was inspected in its print source.
- No source changes were made. The wording, dates, names, punctuation and paragraph structure remain untouched.

**Status:** Capitalisation and italicisation review completed for About the Author. No source correction was required.

### 11. Foreword

**Source inspected:** `ebook/edrl-ii/foreword.md`, the shared source used by the e-book and paperback print build. The Foreword is by Y. T. Vinayaraj.

**Capitalisation audit — findings and decisions**

- **Dalit / Dalits:** Retained with initial capitals when referring to the communities and their identity.
- **CISRS:** The full institutional name, Christian Institute for the Study of Religion and Society, and its acronym are retained.
- **Navayana / Navayana Christianity:** Retained as capitalised in the author's discussion of the Buddhist tradition and the proposed Christian path.
- **B. R. Ambedkar, P. D. Devanandan, M. M. Thomas, Giorgio Agamben, Kerala, Bengaluru, India and Rome:** Personal and place names retained.
- **Potten Theyyam / Theyyam:** Retained as capitalised in the named Dalit counter-religious tradition and the discussion of the song and performance tradition.
- **Daivam:** Retained with an initial capital in the sentence explaining the term's etymology and meaning.
- No capitalisation correction was made.

**Italicisation audit — findings and decisions**

- *Essays on Dalits, Religion and Liberation*, *Religion & Society*, *The Sacred in Popular Hinduism*, *Swami Anand Thirth: Untouchability, Gandhian Solution on Trial*, *The Dalit Deśiyata: The Kerala Experience in Development and Class Struggle*, *Dalit Kavithakal: Oru Padanam*, *Dalit Sahityam* and *Sacrafanations* are italicised as publication or book titles.
- *shakti* is italicised in its Indic sense in the phrase describing immanent energy.
- The source was subsequently corrected to italicise *Potten Theyyam* in both identified occurrences, and *Potten* and *Theyyam* in the explanatory phrase where the terms are individually quoted. *Daivam* is italicised in its explanatory sentence. The verse line is formatted as *Yes, we planted a Tulasi*, so *Tulasi* receives italics within the complete italicised line. *Navayana* was also italicised in both occurrences. These are formatting corrections only; no wording was changed.
- The two numbered references and their bibliographic entries were inspected as part of the source. Book titles in the notes are italicised.
- No italicisation correction was made.

**Other editorial observations**

- The poem is marked with italics line by line in the source. This is preserved as supplied and is not treated as an Indic-term italicisation decision.
- The quoted expressions and the source's existing transliteration have been retained. Spelling, transliteration, factual and stylistic questions are outside this audit.

**Verification**

- The complete 10,972-character shared Foreword source was inspected, including the poem, signature and both notes.
- The Foreword source was corrected in two commits: `decd2aad685ea581218d4d40ca00f7c3e9d78be6` (initial term italicisation) and `d1b5386fbdd4ef315c20b704acfa437061f31779` (correction of term and verse markup). The follow-up source inspection confirmed the intended emphasis and found no malformed nested emphasis in the corrected verse. The changes are limited to Markdown emphasis markup; wording and punctuation were not intentionally changed.

**Status:** Capitalisation review completed with no case changes. The identified Foreword italicisation corrections have been applied and the source re-fetched for verification.

### 12. Editor's Note

**Source inspected:** The Editor's Note and its Acknowledgement section in `ebook/edrl-ii/print/build.py`. The e-book front matter currently contains only a placeholder for this section; the print source contains the full draft.

**Capitalisation audit — findings and decisions**

- **A. M. Abraham Ayrookuzhiel:** Personal name retained in its existing form.
- **Dalit:** Retained with an initial capital when referring to Dalit experience and identity.
- **Asian Trading Corporation, Christian Institute for the Study of Religion and Society (CISRS), Indian Journal of Theology, Towards a Dalit Theology, Religion and Society, Raja Rammohun Roy National Agency for ISBN (RRRNA), United Theological College and Swami Anandatirtha Trust:** Institutional and publication names retained.
- **Bangalore / Bengaluru:** Both forms occur in distinct source contexts. They have not been standardised in this capitalisation-and-italicisation pass.
- Personal names and honorifics in the acknowledgement, including Dr. Y. T. Vinayaraj, Dr. K. C. Abraham, Prabu P., Pranesh Prakash, M. Kunhikrishnan, Sangram Keshari Senapati, Mrs Ponnamma Abraham, Sunil Abraham, Matthew Abraham and Jacob Abraham, are retained.
- No capitalisation correction was made.

**Italicisation audit — findings and decisions**

- *Essays on Dalits, Religion and Liberation*, *Religion and Society*, *Indian Journal of Theology* and *Towards a Dalit Theology* are italicised as book, journal or publication titles.
- No Indic word or expression requiring italicisation was identified in the Editor's Note or Acknowledgement text.
- No italicisation correction was made.

**Other editorial observations**

- The heading **Acknowledgement** is retained as it appears in the source. This audit does not make spelling or house-style changes.
- The wording, grammar, punctuation, acknowledgement sequence and signature block are outside the scope of this capitalisation-and-italicisation pass.

**Verification**

- The complete Editor's Note and Acknowledgement text in the print source were inspected, including the editor's signature attribution and date.
- No source changes were made. Wording, spelling, punctuation, names, paragraph structure and signature content remain untouched.

**Status:** Capitalisation and italicisation review completed for the Editor's Note. No source correction was required.

## Follow-up tests and corrections (November 2026)

The two editorial audits prompted additional checks beyond the original essay-by-essay review. These checks address consistency between body text, headings, front matter and the paperback print conversion. They do not expand the editorial scope to spelling, transliteration, grammar or factual correction.

### 5. Quotation and sentence-ending punctuation audit

**Objective**

To check the punctuation at the end of quoted sentences throughout the nine essay sources, particularly quotations attributed to interviewees and other people whose words are reproduced in the essays. The audit follows the editorial instruction that sentence-ending punctuation should appear before the closing quotation mark in these quotations. Each occurrence must be read in context: punctuation belonging to the surrounding sentence, rather than to the quoted words, should not be moved inside the quotation marks. The review is carried out in the individual Markdown source files identified through `ebook/edrl-ii/manifest.yml`; it is not a typesetting-only correction.

**Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**

**Source inspected:** [The State of Hinduism in 2000 A.D.—Some Emerging Trends](/amaa/state-of-hinduism-in-2000-ad-full-text/).

- Two quoted sentences ended with a full stop outside the closing single quotation mark.
- Both were corrected so that the full stop appears before the closing quotation mark.
- No wording was changed.

**Essay 2 — Religion, Spirituality and Aspirations of the People**

**Source inspected:** [Religion, Spirituality and Aspirations of the People](/amaa/religion-spirituality-and-aspirations-of-the-people-full-text/).

- Three quoted statements ended with punctuation outside the closing single quotation mark: the statement ending "I am in a veritable prison", the statement ending "I do not know much about Christians", and the statement ending "all men are children of God".
- All three were corrected so that the full stop appears before the closing quotation mark.
- A separate sentence containing a quoted phrase followed by a comma was inspected and retained: the comma belongs to the surrounding sentence, not to the quoted words.

**Essay 3 — The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue**

**Source inspected:** [The Living Hindu Popular Religious Consciousness and Some Reflections on It in the Context of Hindu-Christian Dialogue](/amaa/living-hindu-popular-religious-consciousness-full-text/).

- One complete statement attributed to a Pulaya ended with the full stop outside the closing double quotation mark.
- The full stop was moved inside the closing quotation mark.
- Other quoted expressions and lists were inspected. Punctuation outside quotation marks was retained where the quotation was only a phrase or list item within the author's sentence.

**Essay 4 — The Church and the Study of Religion**

**Source inspected:** [The Church and the Study of Religion](/amaa/the-church-and-the-study-of-religion/).

- Four complete quoted passages or sentences had their full stops outside the closing single quotation mark: the statement on the theological task in India; the quoted recommendation to study religion from the perspective of the poor; the quotation ending "let noble thoughts come to me from every side"; and Prof. Saral Chatterji's quoted passage on religion as a medium of expression.
- All four full stops were moved inside their respective closing quotation marks.
- A quoted phrase embedded within the author's sentence ("in their total task of witness and service") was inspected and retained with the full stop outside, because the punctuation belongs to the surrounding sentence.

**Essay 5 — Religions and the Aspirations of the People**

**Source inspected:** [Religions and the Aspirations of the People](/amaa/religions-and-the-aspirations-of-the-people/).

- The full source was checked for sentence-ending punctuation around quotations, including the Chief Minister's reported statement.
- No correction was required. The full stop at the end of the Chief Minister's statement is already inside the closing quotation mark.
- The comma after the quoted words "Hare Rama, Hare Krishna" was retained because the quotation is integrated into the author's sentence.

**Essay 6 — Religion: A Way of Salvation or an Ideology of Oppression?**

**Source inspected:** [Religion: A Way of Salvation or an Ideology of Oppression?](/amaa/religion-way-salvation-ideology-oppression-full-text/).

- The full source was checked for sentence-ending punctuation placed outside closing quotation marks.
- No corrections were required.

**Essay 7 — Dalit Theology: A Movement of Counter-Culture**

**Source inspected:** [Dalit Theology: A Movement of Counter-Culture](/amaa/dalit-theology-movement-counter-culture-full-text/).

- Eight complete quoted statements had their full stops outside the closing quotation mark.
- All eight full stops were moved inside the closing quotation mark. These included quotations from the Commission for Scheduled Castes and Tribes, Sri Jayendra Saraswathi, the Backward Classes Commission, R.S. Khare, J.T. Appavoo, Jyoti Sahi and Tirumular.
- Nested quotation marks in the passage attributed to R.S. Khare were preserved; the sentence-ending full stop was placed inside the outer quotation mark.
- Quoted expressions such as "no people" and "the people of God" were retained as phrases within the author's sentences; their punctuation belongs to the surrounding sentences.

**Essay 8 — Dalit Liberation—Some Reflections on Their Ideological Predicament**

**Source inspected:** [Dalit Liberation—Some Reflections on Their Ideological Predicament](/amaa/dalit-liberation-some-reflections-on-their-ideological-predicament/).

- Four corrections were made: the full stops were moved inside the closing quotation marks in the quoted passage ending "caste-class associations", the quotation ending "the religion of the smritis", the quoted answer "No", and Ambedkar's statement "Beware of Gandhi and the Congress".
- The long quotation from Dr. P. Sivanandan was already punctuated correctly and was left unchanged.
- The first part of the paired statement "Beware of socialist Brahmins" was retained with its comma outside the quotation marks because it is integrated into the surrounding sentence.

**Verification and status**

- All three source files were fetched again after the corrections.
- Essay 6 was checked and required no change.
- The eight corrections in Essay 7 and four corrections in Essay 8 were confirmed in the current source files.
- Remaining quotation marks followed by punctuation were reviewed in context and retained where the quotation was a phrase within the author's sentence, or where the punctuation belonged to the surrounding sentence.
- No wording was changed.
- **Status:** Quotation and sentence-ending punctuation audit completed for Essays 1-8. Essay 9 remains to be checked.


### 1. Collection-wide H2-H4 italicisation check

- H2, H3 and H4 headings were checked in all nine essay source files against the Indic-term italicisation decisions already recorded for each essay.
- Essay 1: the H2 term *saktis* was explicitly marked with HTML `<em>` in the source. The print-builder handling for inline emphasis in HTML headings was also corrected.
- Essay 2: no H2-H4 heading contained an identified Indic term requiring an additional italicisation correction.
- Essay 3: *parasakti* in an H3 heading and *papam*, *adharmam*, *Papam* and *Punyam* in H4 headings were checked and formatted consistently. The H3/H4 headings containing *suddhi*, *assuddhi*, *karmam* and *samaya dosam* already carried italics and were retained.
- Essays 4 and 5: no H2-H4 heading required an additional correction.
- Essay 6: *Devasthanams* and *Mudi* were already italicised in headings; no further correction was needed.
- Essays 7 and 8: no H2-H4 heading required an additional correction.
- Essay 9: the lettered subsection labels were retained as authored; the relevant heading terms were already italicised.

**Result:** The heading-italicisation check was completed for all nine essays. This is distinct from the heading-first-word capitalisation check above.

### 2. Essay 3 full-text emphasis and markup checks

- A follow-up full-text search found generic occurrences of *sakti* and *saktis* that had not been included in the initial heading-only pass. These were checked in their sentences, numbered statements and quotations, and the remaining generic occurrences were italicised.
- The numbered statements (1)-(6) in section I.B were confirmed to be bold paragraphs, not H2-H4 headings. Their formatting was therefore handled as body text, not reported as heading corrections.
- A subsequent markup review found two quotations with nested Markdown emphasis around *sakti*. The nested markers were removed while keeping each complete quotation italicised. This avoids malformed or ambiguous emphasis markup.
- The final correction was committed as `f5f99ccec2abc8b3ffbaeee2bb6683d223cad99e` ("Fix nested italics in Essay 3 quoted phrases"). The earlier full-text italicisation pass was committed as `dff1cd59325999c0afeb0d60fa1ecd5ccc71139a`.

### 3. Print-conversion checks

- The Essay 1 heading uses HTML `<em>` because the previous Markdown emphasis form inside the HTML heading did not survive the print-builder conversion reliably.
- The print builder's HTML-heading conversion was updated to translate `<em>` and `<i>` to Typst emphasis, and `<strong>` and `<b>` to Typst bold. The relevant builder change is recorded in commit `4e0bfad7c03ec4504c63125132db7d48dfb3daa9` ("Render HTML heading italics explicitly in Typst").
- The Foreword is read from `ebook/edrl-ii/foreword.md`; its Markdown emphasis is converted through Pandoc to Typst. The Editor's Note and About the Author are hardcoded in `ebook/edrl-ii/print/build.py`, rather than read from `front-matter.md`.
- The current Editor's Note and About the Author text in `build.py` was inspected. Publication titles were already italicised; no additional Indic-language term requiring italics was identified. No changes were made to these two sections or to `build.py` during this follow-up.

### 4. Source-integrity and proof limitations

- Where source corrections were made, comparisons were used to distinguish formatting changes from wording changes. For Essay 3, a comparison after removing emphasis markers and reversing the recorded capitalisation substitutions confirmed that the text remained lexically unchanged apart from the approved formatting and case changes.
- The corrected Foreword was fetched again and inspected for the specific terms and verse markup.
- The print builder's conversion logic was inspected, but this is not equivalent to a successful print build or visual PDF proof.
- A new successful print build and visual inspection of the resulting PDF are still required before the print typography can be marked as visually verified. The earlier downloadable preview predates the latest Essay 3 nested-emphasis correction.
- These source audits do not establish fidelity against the original printed articles. Original-print comparison remains a separate verification task.

**Follow-up status:** The additional heading checks, source-markup checks and identified source corrections are recorded. Final PDF visual verification and comparison with the original printed sources remain outstanding.

## Change-volume overview

Based on the recorded source corrections and the breadth of the capitalisation and italicisation passes, the three essays with the largest volume of changes are:

1. **Essay 7 — Dalit Theology: A Movement of Counter-Culture**: extensive Dalit/Dalitism capitalisation standardisation, a generic Karma correction, and several Indic-term italicisation changes.
2. **Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**: capitalisation standardisation of Sakti, Harijan and Brahmin, alongside the broadest recorded Indic and regional-language italicisation pass.
3. **Essay 9 — The Ideological Nature of the Emerging Dalit Consciousness**: numerous Dalit/Dalits, non-Dalit, Brahminical/Brahminic and Vedic/Puranic capitalisation corrections.

This is a qualitative ranking of the documented change volume, not a verified count of individual character-level edits.

## Editorial decision record and style-sheet

The style-sheet will be built from decisions made during the audit, rather than written in advance of examining the essays. For each term or expression, the record will capture:

- The term and its observed variants.
- The essay and the context in which it occurs.
- The capitalisation decision and its reason.
- The italicisation decision and its reason.
- The preferred editorial form, where standardisation is appropriate.
- Any qualification or exception.
- Whether the decision has been applied to the source file and checked.

The style-sheet will serve as the reference for maintaining consistency across this volume and, where applicable, for editing other works by A. M. Abraham Ayrookuzhiel.

## Progress

An essay will be marked complete only after both audits have been examined, findings and decisions have been recorded, and approved source corrections have been checked. The audit report sections above will be updated as the work proceeds.

**Working principle: Examine in context → apply the criteria → make an editorial judgement → record the decision → correct the source → verify the result.**

## See also

- [Print Book Production: Essays on Dalits, Religion and Liberation II](/amaa/30-print-book-production/)
- [Word Frequency Analysis and Subject Index Research: Essays on Dalits, Religion and Liberation II](/amaa/30-print-book-production-index-research/)

{% include navbox-amaa.html %}
