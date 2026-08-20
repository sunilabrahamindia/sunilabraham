---
layout: default
title: "GitHub Multi-Account Identity and Authentication Incident (July–August 2026)"
description: "Documentation of two GitHub multi-account authentication, Git identity, and commit attribution incidents involving two GitHub accounts on Tito Dutta's laptop."
categories: [TSAP Documentation, TSAP Incidents]
permalink: /tsap/github-multi-account-identity/
created: 2026-08-21
---

{% include documentation-notice.html %}

Two GitHub accounts are used on Tito Dutta's laptop for different purposes: one for The Sunil Abraham Project and related work, and another for personal projects. This arrangement resulted in two separate instances of confusion around GitHub authentication, Git commit identity, and commit attribution.

The first instance occurred in July 2026 while working on the [Swapna Dutta website](https://swapnadutta.pages.dev/). A second instance occurred in August 2026 while developing a [hobby game dashboard](https://unitedclan.pages.dev/). Both instances were identified and corrected after only a small number of edits, but the second incident provided a clearer understanding of the distinction between the GitHub account used for authentication and the identity recorded in a Git commit.

This document records what happened, the approaches that were attempted, the eventual diagnosis, and the resulting workflow.

## Background

Two GitHub accounts are used on Tito Dutta's laptop:

- `sunilabrahamindia` — used for The Sunil Abraham Project and related work.
- `titodutta` — used for personal projects, including the Swapna Dutta website and United Clan Dashboard.

Both accounts are used from the same Ubuntu terminal environment.

## First Instance: Swapna Dutta

The first significant experience occurred in July 2026 while working on the Swapna Dutta website.

The same laptop was being used for both the personal repository and The Sunil Abraham Project. This created confusion around which GitHub account was being used for Git operations.

One attempted solution was to use different editors for the two accounts:

- VS Code for `sunilabrahamindia`
- VSCodium for `titodutta`

This was abandoned because the editor does not determine Git identity or GitHub authentication.

Git repositories, Git configuration, credentials, and GitHub authentication operate independently of the editor being used.

## GitHub CLI Account Switching

The next approach was to use GitHub CLI account switching.

The active account can be changed with:

    gh auth switch

The active account can be checked with:

    gh auth status

This provided a much cleaner way to change the authenticated GitHub account from the terminal.

However, the later United Clan Dashboard incident showed that this does not automatically change the Git identity configured inside a repository.

## Second Instance: United Clan Dashboard

The same problem appeared again in August 2026 while developing:

    titodutta/unitedclan-dashboard

The active GitHub CLI account had been correctly switched to `titodutta` and verified with:

    gh auth status

The repository accepted the pushes normally.

However, new commits appeared in GitHub as being attributed to `sunilabrahamindia`, even though that account did not have access to the repository.

The local Git identity was then checked:

    cd ~/Projects/unitedclan-dashboard
    git config user.name
    git config user.email

The repository was still configured with the Git identity associated with `sunilabrahamindia`.

This explained the apparent contradiction.

## What Actually Happened

There were two separate identities involved:

- **Authentication:** `titodutta` was the account authorised to push to the repository.
- **Commit identity:** Git was still creating commits using the `sunilabrahamindia` identity.

The sequence was therefore:

1. Git created a commit using the locally configured Git identity.
2. The commit contained the project account's author information.
3. The push was authenticated using the personal GitHub account.
4. GitHub accepted the push because the personal account had repository access.
5. GitHub attributed the commit to the account matching the author information.

Therefore, `sunilabrahamindia` did not need access to the repository and did not perform the push.

The important distinction is between "authentication" and "authorship".

## Resolution

The Git identity was corrected specifically for the United Clan Dashboard repository:

    cd ~/Projects/unitedclan-dashboard
    git config user.name "titodutta"
    git config user.email "[email associated with the personal GitHub account]"

The configuration was deliberately repository-local and did not use `--global`.

The actual email address is intentionally not recorded in this documentation.

The existing incorrectly attributed commits were left unchanged. The corrected identity applies to future commits.

## Lessons Learned

1. **`gh auth switch` and Git identity are separate.** Switching the active GitHub account does not automatically change the name and email configured for Git commits.

2. **Authentication and authorship are separate.** One GitHub account can authenticate a push while another account is shown as the commit author.

3. **Different editors are not account boundaries.** Using VS Code and VSCodium for different accounts does not reliably separate GitHub identities.

4. **Check both identities when using multiple accounts.** Before important work, verify:

       gh auth status
       git remote -v
       git config user.name
       git config user.email

## Current Workflow

Repositories belonging to The Sunil Abraham Project continue to use the `sunilabrahamindia` Git identity.

Personal repositories such as the United Clan Dashboard use the `titodutta` Git identity.

The repositories and project folders do not need to be renamed or reorganised.

The July 2026 Swapna Dutta experience and the August 2026 United Clan Dashboard incident together provide a record of how the issue was discovered and resolved.
