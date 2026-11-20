---
layout: default
title: "Editorial Source Audit: Sixth Stage — Print Proof and Pagination Review"
permalink: /amaa/30-editorial-source-audit-sixth-stage/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Sixth-stage editorial source audit for Essays on Dalits, Religion and Liberation II, documenting print-proof pagination, paragraph and poem leading, and targeted production corrections."
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

## Outstanding proof checks

1. Inspect Essay 6 around both festival labels and confirm that each label stays with the material it introduces.
2. Inspect Essay 1 around subsections 3–6, including the pages immediately before and after each affected passage. Confirm that subsection 3 is not stranded and that the movement has not created an orphan or awkward break in subsections 4 or 5.
3. Compare the indentation of Essay 1 subsection 6 with the other subsection headings.
4. Inspect the poem in the latest PDF. Confirm that line leading has changed while the 12pt stanza gap and 16pt outer spacing remain visually intact.
5. Review any pagination changes caused by the revised poem leading before treating the print proof as final.

The latest successful workflow is a production-build result, not a declaration that the PDF has passed all visual checks. The outstanding items above should be marked complete only after the relevant pages have been inspected.

{% include navbox-amaa.html %}
