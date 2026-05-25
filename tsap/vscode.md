---
layout: default
title: "VS Code Workflow"
description: "Guide to using Visual Studio Code (VS Code) for maintaining The Sunil Abraham Project (TSAP), including Git workflow, shortcuts, and practical editing practices."
categories: [TSAP Documentation]
permalink: /tsap/vscode/
created: 2026-05-26
---

**Visual Studio Code (VS Code)** is used within The Sunil Abraham Project (TSAP) primarily for larger or more structured maintenance work. It complements, rather than replaces, browser-based GitHub editing. This page documents the practical TSAP workflow for VS Code rather than explaining VS Code generally.

There are already many tutorials explaining how to use Visual Studio Code (VS Code). This page is not intended to duplicate those guides. Instead, this document explains how VS Code is used specifically within The Sunil Abraham Project (TSAP), including maintaining large numbers of Markdown pages, editing Jekyll front matter safely, reviewing Git changes before publication, and carrying out repository-wide maintenance work.

TSAP is not a software application in the conventional sense. It is closer to a long-term digital archive and publishing infrastructure. Because of this, the workflow emphasises readability, consistency, preservation, and cautious editing practices rather than rapid software deployment.

Many edits may still be easier directly through the GitHub browser interface, especially for quick typo fixes, single-file edits, urgent corrections, mobile edits, and small metadata updates.

VS Code becomes especially useful when the scale of work increases.

## Typical TSAP Workflow

A normal TSAP editing session in VS Code often looks like this:

```text
Open repository
→ Search across multiple pages
→ Edit several related files
→ Save all files
→ Review diffs carefully
→ Commit related edits together
→ Push changes to GitHub
```

This is especially useful when:

- standardising metadata
- repairing internal links
- improving accessibility
- updating templates
- auditing publication pages
- fixing repeated formatting issues

Unlike browser editing, VS Code makes it possible to inspect repository-wide patterns before publishing changes.

## Opening the Repository

The TSAP repository is cloned locally using Git:

```bash
git clone https://github.com/sunilabrahamindia/sunilabraham.git
```

Open the repository in VS Code:

```bash
cd sunilabraham
code .
```

The `.` means "open the current folder".

## Repository Structure

Some folders frequently used in TSAP include:

```text
amaa/
articles/
clusters/
events/
media/
projects/
publications/
resources/
sunil/
tsap/
```

For a broader overview, see [Site Structure](/structure/). Understanding these folders gradually becomes more useful than memorising VS Code features themselves.

## Useful Keyboard Shortcuts

<div class="table-wrapper">

<table class="vscode-shortcuts">
<tr>
<th>Action</th>
<th>Shortcut</th>
</tr>

<tr>
<td>Save current file</td>
<td><code>Ctrl + S</code></td>
</tr>

<tr>
<td>Save all files</td>
<td><code>Ctrl + K then S</code></td>
</tr>

<tr>
<td>Open Source Control</td>
<td><code>Ctrl + Shift + G</code></td>
</tr>

<tr>
<td>Repository-wide search</td>
<td><code>Ctrl + Shift + F</code></td>
</tr>

<tr>
<td>Open terminal</td>
<td><code>Ctrl + `</code></td>
</tr>

<tr>
<td>Open Extensions panel</td>
<td><code>Ctrl + Shift + X</code></td>
</tr>

<tr>
<td>Open Command Palette</td>
<td><code>Ctrl + Shift + P</code></td>
</tr>

<tr>
<td>Quick file search</td>
<td><code>Ctrl + P</code></td>
</tr>

<tr>
<td>Find within current file</td>
<td><code>Ctrl + F</code></td>
</tr>

<tr>
<td>Replace within current file</td>
<td><code>Ctrl + H</code></td>
</tr>

<tr>
<td>Multi-file replace</td>
<td><code>Ctrl + Shift + H</code></td>
</tr>

<tr>
<td>Toggle sidebar</td>
<td><code>Ctrl + B</code></td>
</tr>

</table>

</div>

## Repository-Wide Search

One of the biggest advantages of VS Code for TSAP is repository-wide search.

Shortcut:

```text
Ctrl + Shift + F
```

Useful for:

- locating internal links
- finding outdated metadata
- auditing repeated phrases
- checking CSS class usage
- identifying inconsistent formatting
- locating missing fields
- reviewing YAML structures

As TSAP grows, this becomes increasingly important.

## Reviewing Changes Safely

Before committing changes:

1. Open the Source Control panel
2. Click changed files individually
3. Review the visual diff
4. Confirm no accidental edits exist

VS Code highlights:

- additions in green
- deletions in red
- modified lines visually

This review step becomes especially important during:

- batch edits
- metadata cleanup
- accessibility fixes
- CSS modifications
- template changes

## Git Workflow

One important difference between browser editing and VS Code editing is that VS Code exposes the underlying Git workflow directly.

The workflow usually has three stages:

```text
Edit files
→ Commit locally
→ Push to GitHub
```

This can initially feel intimidating, but it provides important advantages:

- changes can be reviewed before publication
- mistakes are easier to detect
- edits remain reversible
- maintenance history becomes transparent
- large-scale changes become safer

For TSAP, Git history also functions as a kind of editorial and preservation log.

### Common Git Commands

Pull latest repository changes:

```bash
git pull
```

Stage changes:

```bash
git add .
```

Create commit:

```bash
git commit -m "Commit message"
```

Push changes to GitHub:

```bash
git push
```

## Commit Messages

Commit messages should briefly describe the purpose of the changes.

Examples:

```text
[vscode] Add internal links and metadata cleanup
```

```text
[a11y] Improve colour contrast in article template
```

```text
[cleanup] Standardise publication metadata
```

Useful tags may include:

- `[vscode]`
- `[a11y]`
- `[cleanup]`
- `[metadata]`
- `[css]`
- `[portal]`
- `[infra]`

## Browser Editing vs VS Code

TSAP currently uses a hybrid workflow.

Neither method replaces the other.

### Browser Editing

Browser-based GitHub editing remains extremely useful for:

- correcting typos
- fixing one page quickly
- updating a single date or link
- making emergency edits
- editing while travelling
- quick publishing tasks

For lightweight work, browser editing is often faster.

### VS Code

VS Code becomes valuable when work expands beyond isolated edits.

Examples include:

- editing many related pages together
- repository-wide search
- accessibility audits
- metadata standardisation
- reviewing diffs carefully before publishing
- editing layouts, includes, or CSS
- restructuring sections across multiple pages

Over time, both workflows naturally complement each other.

## Recommended Extensions

### Essential

- YAML by Red Hat
- markdownlint
- Jekyll Syntax Support

### Useful

- GitLens
- Error Lens
- Todo Tree

Extensions should support readability and maintainability rather than unnecessary visual complexity.

## Accessibility Considerations

When editing in VS Code:

- prioritise readable formatting
- use semantic HTML where appropriate
- maintain high colour contrast
- avoid unnecessary visual clutter
- preserve meaningful alt text
- check heading hierarchy carefully
- favour clean Markdown over excessive HTML

Accessibility remains a core TSAP priority.

## Good Editing Practices

- Save files frequently
- Review diffs before committing
- Group related edits into meaningful commits
- Avoid massive unrelated commits
- Keep Markdown readable in raw form
- Preserve consistent formatting
- Use relative internal links where possible
- Prefer incremental improvements over unnecessary rewrites

## Notes

- VS Code does not replace browser editing; both remain useful.
- Git history provides long-term transparency and reversibility.
- Repository-wide search becomes increasingly important as TSAP grows.
- Local editing reduces the fragility of browser-only workflows for large archival projects.

## External Links

- [Visual Studio Code Official Website](https://code.visualstudio.com/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
- [GitHub CLI](https://cli.github.com/)

<style>
.table-wrapper {
  overflow-x: auto;
  margin: 1rem 0;
}

.vscode-shortcuts {
  width: 100%;
  border-collapse: collapse;
  min-width: 320px;
}

.vscode-shortcuts th,
.vscode-shortcuts td {
  border: 1px solid #ccc;
  padding: 0.5rem 0.75rem;
  text-align: left;
  vertical-align: top;
}

.vscode-shortcuts th {
  background: #f2f2f2;
}

.vscode-shortcuts code {
  white-space: nowrap;
  background: #f8f8f8;
  padding: 2px 4px;
  border-radius: 4px;
}

@media (max-width: 600px) {
  .vscode-shortcuts {
    font-size: 0.9rem;
  }

  .vscode-shortcuts th,
  .vscode-shortcuts td {
    padding: 0.45rem 0.6rem;
  }
}
</style>
