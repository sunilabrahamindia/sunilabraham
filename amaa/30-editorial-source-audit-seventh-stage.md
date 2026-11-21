---
layout: default
title: "Editorial Source Audit: Seventh Stage — Chapter Title and Publication-Note Layout"
permalink: /amaa/30-editorial-source-audit-seventh-stage/
categories: [A. M. A. Ayrookuzhiel, 30th Death Anniversary Commemoration]
description: "Seventh-stage editorial source audit for Essays on Dalits, Religion and Liberation II, recording chapter-title line balancing, original-publication label layout and print-build verification."
created: 2026-11-21
---

**Editorial Source Audit: Seventh Stage** continues the editorial and print-production review of *Essays on Dalits, Religion and Liberation II* by A. M. Abraham Ayrookuzhiel. It follows the [first-stage Editorial Source Audit](/amaa/30-editorial-source-audit/), the [second-stage Editorial Source Audit](/amaa/30-editorial-source-audit-second-stage/), the [third-stage Editorial Source Audit](/amaa/30-editorial-source-audit-third-stage/), the [fourth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-fourth-stage/), the [fifth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-fifth-stage/) and the [sixth-stage Editorial Source Audit](/amaa/30-editorial-source-audit-sixth-stage/).

This stage records the print-layout work undertaken on 21 November 2026. The work concerns the chapter-opening title and original-publication note presentation. All changes described here were made in the print-generation script, `ebook/edrl-ii/print/build.py`. The nine essay manuscripts and their original chapter-title text were not edited.

## Scope and working principles

The interventions in this stage are presentation-only adjustments to the generated print edition:

- Preserve the exact wording of every chapter title and publication note.
- Use deliberate line breaks only in the print rendering of the two identified chapter titles.
- Keep the original-publication block left-aligned, with its label on a separate line from the publication details.
- Do not edit the original essay Markdown files.
- Treat a successful automated build as confirmation that the production files compile, not as a substitute for visual inspection of the PDF.

## Audit and activity log

### 21 November 2026 — Original-publication label placed on its own line

**Production file:** `ebook/edrl-ii/print/build.py`

The original-publication note below each chapter title was adjusted so that the label **ORIGINAL PUBLICATION:** appears on its own line, with the publication details beginning on the following line. The block is left-aligned.

This is a print-layout change applied to the publication-note block generated for the chapters. It does not alter the publication details in the manifest or any essay manuscript.

**Status:** Print-generation rule updated. The resulting layout should be checked in the generated PDF, including whether any publication details wrap onto three lines.

### 21 November 2026 — Chapter 2 title line break balanced

**Chapter 2 — Religion, Spirituality and Aspirations of the People**

The title was appearing with the short second line **"the People"**. For the print display, a deliberate line break was introduced after **"and"**, producing the following two-line arrangement:

> Religion, Spirituality and  
> Aspirations of the People

The chapter title itself remains unchanged. The line break is applied only by the print-rendering rule in `build.py`; it does not alter the manifest title, contents entry or essay source.

### 21 November 2026 — Chapter 5 title line break balanced

**Chapter 5 — Religions and the Aspirations of the People**

The title was appearing with only **"People"** on its second line. For the print display, a deliberate line break was introduced after **"the"**, producing this arrangement:

> Religions and the  
> Aspirations of the People

As with Chapter 2, the original title text remains unchanged. The adjustment affects only the rendered chapter heading in the print edition.

### 21 November 2026 — Initial build failure and correction

The first build following the two title-display adjustments failed during Typst compilation. The generated Typst source reported:

```text
error: unknown variable: display-title
```

The cause was a missing Typst content marker before the local variable declaration. The declaration was corrected from `let display-title` to `#let display-title` in `ebook/edrl-ii/print/build.py`. No manuscript or title text was changed as part of this correction.

**Initial failed print build:** [EDRL II print proof #621](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44877671230).

**Corrected print build:** [EDRL II print proof #622](https://github.com/sunilabrahamindia/sunilabraham/actions/runs/44877799358) completed successfully.

**Status:** Typst compilation and the automated print-proof workflow succeeded after the correction. The generated PDF still requires visual inspection to confirm the two title breaks, the left-aligned original-publication blocks and the line wrapping of all nine publication details.

## Outstanding proof checks

1. Inspect Chapter 2 and confirm that its title breaks after "and" as intended.
2. Inspect Chapter 5 and confirm that its title breaks after "the" as intended.
3. Check all nine original-publication blocks: confirm that the label is on its own line, the block is left-aligned, and no publication details spill awkwardly into three lines.
4. Review the surrounding chapter-opening spacing and divider ornaments to ensure that the adjustments have not introduced unwanted crowding or imbalance.

A successful build confirms that the Typst source compiles and the workflow completes. The seventh-stage print review should be considered visually verified only after these pages have been inspected in the generated PDF.

{% include navbox-amaa.html %}
