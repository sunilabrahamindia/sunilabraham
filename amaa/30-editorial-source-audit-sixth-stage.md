---
layout: default
title: "Editorial Source Audit: Sixth Stage — Print Proof and Pagination Review"
permalink: /amaa/30-editorial-source-audit-sixth-stage/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Sixth-stage editorial source audit for Essays on Dalits, Religion and Liberation II, documenting print-proof pagination, paragraph and poem leading, and targeted production corrections."
page_id: TSAP-1389
created: 2026-11-20
---

**Editorial Source Audit: Sixth Stage** continues the editorial and print-production review of *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It follows the [first-stage Editorial Source Audit](/amaa/30-editorial-source-audit/), the [second-stage Editorial Source Audit](/amaa/30-editorial-source-audit-second-stage/), the [third-stage Editorial Source Audit](/amaa/30-editorial-source-audit-third-stage/), the [fourth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-fourth-stage/) and the [fifth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-fifth-stage/).

This stage records the latest print-proof work, beginning with the pagination of the Essay 6 festival labels and continuing through the Essay 1 paragraph pagination and the adjustment of poem line leading. The emphasis is on narrowly scoped interventions in the print-production script. The essay manuscript wording is not to be changed when the issue is solely one of page composition or typography.

## Scope and working principles

The work recorded here concerns the print edition generated through `ebook/edrl-ii/print/build.py`. Each intervention is distinguished from a change to the essay source. A successful automated build establishes that the production files compile and the workflow completes; it does not, by itself, establish that every page is visually correct. Visual proof review remains necessary wherever pagination or appearance is the subject of the change.

The following principles apply:

- Make the smallest change that addresses the identified problem.
- Restrict special handling to the exact essay and passage concerned.
- Preserve manuscript wording and source formatting unless a textual correction is specifically required.
- Do not change stanza spacing when the requested adjustment concerns only the leading between poem lines.
- Record failed build attempts and subsequent corrections rather than presenting only the final successful result.
- Treat the PDF as requiring visual inspection even when the workflow succeeds.

## Audit and activity log

### 20 November 2026 — Essay 6: festival labels stranded at page bottoms

**Essay 6 — Religion: A Way of Salvation or an Ideology of Oppression?**

The print proof showed two festival-related labels stranded at the bottoms of pages, separated from the text that followed them:

- `(e) An egalitarian spiritual practice during the Karaga`
- `(c) Dasara`

The correction was made in the print-production script, not in the essay manuscript. Weak page breaks were inserted immediately before these two exact labels so that a label moves to the next page when there is insufficient room for the label and the following content. The intervention was kept specific to these two locations; it was not applied indiscriminately to all nine festival labels.

An initial pagination experiment was found to be too broad and was reverted. The targeted correction was then committed as `b7cce3f541898347af9fe6f8780cd19f070bbdbd`.

**Verification:** EDRL II print-proof workflow [#44665273688](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44665273688) completed successfully. The successful build confirms that the production script ran; the final placement of both labels must be judged from the generated PDF.

**Status:** Targeted print-builder correction committed; PDF placement remains subject to visual proof confirmation.

### 20 November 2026 — Essay 1: prevent subsection 3 from being stranded at the bottom of a page

**Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**

The print proof showed the bold, multi-line subsection 3 paragraph at the bottom of page 6, with the prose belonging to it beginning on page 7:

> 3. In the process of reinterpretation and reconstruction of the concept of God or Supreme Self, there will be greater interaction between the God of play and the God of history.

A weak page break was added immediately before this exact bold paragraph in the Essay 1 processing within `ebook/edrl-ii/print/build.py`. A weak break allows the paragraph to move when the remaining page space is insufficient; it does not impose an unconditional page break. The essay source text was not changed.

The first implementation attempt did not produce a successful build. A subsequent attempt exposed an incorrectly matched Essay 1 subsection 6 expression in the same Essay 1-specific processing. That matcher was corrected without changing the subsection 6 wording or the intended heading treatment.

**Verification:** The corrected implementation was committed in `1fc11ce6a981a8914cdce35d3b91d4d40f60df3c`. EDRL II print-proof workflow [#44666946399](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44666946399) completed successfully. The resulting PDF still requires inspection around subsections 3, 4, 5 and 6 to ensure that the adjustment has not created a new pagination problem nearby.

**Status:** Corrected production script and successful build; neighbouring-page visual review remains necessary.

### 20 November 2026 — Essay 1: preserve subsection 6 heading indentation

The Essay 1-specific processing also retains the existing treatment of subsection 6, **"Will the sacred cow return?"**. The heading is emitted with the intended 12.1pt horizontal indentation after its page-break intervention, so that its position remains consistent with the other indented subsection headings.

The subsection 6 matcher had to be corrected during the subsection 3 pagination work. The final correction is included in commit `1fc11ce6a981a8914cdce35d3b91d4d40f60df3c`.

**Verification:** The print-proof workflow for that commit, [#44666946399](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44666946399), completed successfully. The heading's visual alignment should be checked against the preceding subsection headings in the PDF.

**Status:** Matcher correction committed and build successful; visual alignment remains part of proof review.

### 20 November 2026 — Poem line leading matched to the main text

**Production file:** `ebook/edrl-ii/print/build.py`

The poem lines in the print edition had a different line leading from the main essay text. The requested adjustment was limited to the leading between lines within poem stanzas. The poem paragraph setting was changed from 12.65pt to 9pt, matching the 9pt leading used for the main body text.

The change was made only in the poem stanza-rendering rule inside `convert_post_poem_prose()`. It did not alter the spacing between stanzas or the space surrounding the poem:

- Leading within poem stanzas: changed from 12.65pt to 9pt.
- Gap between stanzas: retained at 12pt.
- Space above and below the poem block: retained at 16pt.
- Paragraph spacing within a stanza: retained at 0pt.
- Festival-label leading: left unchanged.
- Main body paragraph settings: left unchanged.

No poem wording or essay manuscript source was changed. In particular, this was not a request to reduce or otherwise alter the stanza gaps or the space before and after the poem.

**Commit:** `7c31e77cab6cac6e05355b8280f332f8e4cc13d0` — "Match poem line leading to body text".

**Verification:** EDRL II print-proof workflow [#44667723333](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44667723333) completed successfully. The commit diff confirms that the only change in the file was the poem stanza leading value. The generated PDF still needs visual review to assess the appearance of poem lines and check for any resulting pagination changes.

**Status:** Exact print-builder change committed; automated build successful; visual PDF review pending.

### 20 November 2026 — Print footnote marker size reduced to 12pt

**Production file:** `ebook/edrl-ii/print/build.py`

The superscript footnote reference marker in the print edition was set to **12pt**, reduced from 14pt. The change is limited to the Typst rule that controls the size of the superscript marker:

```typst
#show footnote: it => super(text(size: 12pt)[#it])
```

No other footnote settings were changed. In particular, the footnote text size remains 8.5pt, and the main body text remains 11pt. No essay manuscript text, footnote content, footnote-entry typography, spacing or other print settings were altered.

**Commit:** `c0888069b1a9d62bb76210b342861cb6558d3d0` — "Set print footnote markers to 12pt".

**Verification:** The commit diff confirms a single-line change from 14pt to 12pt in `ebook/edrl-ii/print/build.py`. The resulting print-proof build and PDF still need to be checked.

**Status:** Source change committed and diff verified; print build and visual inspection pending.

### 20 November 2026 — Essay 1: standardise subsection heading alignment and restore paragraph indents

**Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**

The print proof showed inconsistent indentation across subsection headings 1–6. The agreed formatting correction was:

- Subsection headings 1–6: flush-left, following the existing position of heading 3.
- First line of the paragraph following each heading: retain the normal 12.1pt first-line indent.
- Subsequent paragraph lines: retain the normal body margin.
- Subsection 6: keep its heading on a separate line from the paragraph beginning "I am not here referring..."; indent only that paragraph's first line.
- Preserve the existing weak page break before subsection 3.

The essay manuscript wording was not changed. The correction is confined to the Essay 1 processing in `ebook/edrl-ii/print/build.py`.

During proofing, an earlier paragraph-wide Typst setting unintentionally affected the first line of the following prose. A later attempt also exposed a build-script error because it called an undefined converter. Those attempts were not accepted as final. The final correction uses a paragraph-local `#par(first-line-indent: 0pt)` for each heading, rather than a paragraph-wide `#set par` rule. This keeps the flush-left heading treatment local and leaves the normal 12.1pt body paragraph indent in force.

**Final source commit:** `26fa7af5e11fe05c24eaeca9bc9326ec27b51000` — "Scope flush-left formatting to Essay 1 headings only".

**Verification:** EDRL II print-proof workflow [#601](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44677085731) completed successfully. The user has made an initial inspection and reported that the affected formatting looks correct. A full-book scan is still in progress; this is therefore a provisional proof approval, not final sign-off.

**Status:** Targeted formatting correction committed; build #601 successful; initial visual check positive; full-book review pending.

### 20 November 2026 — Essay 1: audit of subsection soft page-break rules and paragraph spacing

**Essay 1 — The State of Hinduism in 2000 A.D.—Some Emerging Trends**

The six bold subsection paragraphs (1–6) were reviewed in `ebook/edrl-ii/print/build.py` to establish which ones have an explicit weak page break before them. The current rule is:

| Subsection | Explicit weak page break before it |
|---|---|
| 1 | No |
| 2 | No |
| 3 | Yes |
| 4 | No |
| 5 | No |
| 6 | No |

The existing weak page break before subsection 3 was preserved. No additional soft page breaks were added to the other subsection paragraphs.

The paragraph-spacing adjustment went through two incorrect implementations before being corrected:

1. An explicit `#block(above: 12pt)` was tried. It did not give the intended visible spacing because the block spacing interacted with the surrounding paragraph spacing.
2. That was replaced with an explicit `#v(12pt, weak: false)`, and then reduced to `#v(10pt, weak: false)`. This added extra vertical space on top of the normal paragraph spacing and made the gap too large.
3. The extra vertical-space command was then removed. The current Essay 1 heading conversion is paragraph-local:

   ```typst
   #par(first-line-indent: 0pt)[...]
   ```

   This keeps the bold subsection paragraph flush-left without adding a separate vertical-space command. It inherits the existing body paragraph settings: **9pt leading and 10pt paragraph spacing**. The following prose retains its normal **12.1pt first-line indent**.

The relevant global setting in `build.py` remains:

```python
BODY_PAR = "#set par(justify: true, justification-limits: (spacing: (min: 85%, max: 120%), tracking: (min: 0pt, max: 0.01em)), leading: 9pt, first-line-indent: 12.1pt, hanging-indent: 0pt, spacing: 10pt)"
```

No change was made to the essay manuscript wording. The H1, H2, H3 and H4 heading rules were not changed. The weak page break before subsection 3 was not changed. No separate spacing was added after the bold subsection paragraphs.

**Commits and builds:**

- `bc2aab0` — first attempt to add 12pt above the bold paragraphs; the implementation did not produce the intended result.
- `5251332` — replaced the block spacing with explicit 12pt vertical space; print-proof workflow [#44693794342](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44693794342) completed successfully.
- `6a33392` — changed the explicit vertical space to 10pt; print-proof workflow [#44695242882](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44695242882) completed successfully.
- `e15fe97` — removed the additional vertical-space command, leaving the heading-local first-line-indent setting; print-proof workflow [#44695962008](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44695962008) completed successfully.

A successful build confirms compilation only. The final visual appearance of the bold paragraph spacing remains subject to the user's proof review.

**Status:** The current script has no additional explicit vertical gap before or after the bold subsection paragraphs. It uses the normal body paragraph spacing. The only explicit weak page break among subsections 1–6 remains the one before subsection 3.

## Outstanding proof checks

1. Inspect Essay 6 around both festival labels and confirm that each label stays with the material it introduces.
2. Inspect Essay 1 around subsections 3–6, including the pages immediately before and after each affected passage. Confirm that subsection 3 is not stranded and that the movement has not created an orphan or awkward break in subsections 4 or 5.
3. Compare the indentation of Essay 1 subsection 6 with the other subsection headings.
4. Inspect the poem in the latest PDF. Confirm that line leading has changed while the 12pt stanza gap and 16pt outer spacing remain visually intact.
5. Review any pagination changes caused by the revised poem leading before treating the print proof as final.

The latest successful workflow is a production-build result, not a declaration that the PDF has passed all visual checks. The outstanding items above should be marked complete only after the relevant pages have been inspected.

{% include navbox-amaa.html %}
