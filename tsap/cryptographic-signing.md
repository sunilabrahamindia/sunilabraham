---
layout: default
title: "TSAP Cryptographic Signing and Verification Policy"
description: "Defines how TSAP uses OpenPGP for signing and verification of important documents."
categories: [TSAP Documentation]
permalink: /tsap/cryptographic-signing/
created: 2026-06-10
---

**Cryptographic signing** in **The Sunil Abraham Project (TSAP)** is used to ensure the authenticity, integrity, and long-term verifiability of selected institutional documents. It provides a mechanism to confirm that a document was explicitly approved at a specific point in time and has not been altered since signing.

Unlike routine communication or day-to-day edits, cryptographic signatures are reserved for materials that carry archival, constitutional, or official significance within TSAP. This ensures that verification remains meaningful, lightweight, and focused only on content where authenticity matters.

## Purpose

This document defines the cryptographic signing and verification practices used within TSAP. It explains how OpenPGP is used to ensure authenticity, integrity, and long-term verifiability of selected TSAP documents.

TSAP does not sign all content. Signing is reserved for documents where authenticity and integrity are important.

## Scope of Signing

TSAP applies cryptographic signing selectively to ensure that only documents requiring long-term authenticity and integrity guarantees are covered. Signed documents include foundational or constitutional materials that define the structure and identity of the project, official announcements or declarations issued on behalf of TSAP, archival snapshots intended to preserve a stable version of the project at a given point in time, datasets or structured releases distributed for public or research use, and other records considered institutionally significant.

Routine communication, including emails and messages, is not signed under this system. Similarly, minor edits or routine updates to existing content, day-to-day operational communication, and non-critical articles or drafts are excluded from cryptographic signing. This ensures that signing remains focused, meaningful, and limited to materials where verifiable authenticity is important rather than being applied to all content indiscriminately.

## Cryptographic Identity Scope

TSAP maintains a cryptographic identity system for ensuring authenticity of selected documents and future institutional processes.

At present, TSAP uses OpenPGP (PGP) as its primary cryptographic signing method. This is used to create verifiable signatures for documents of constitutional, archival, or official significance.

TSAP also reserves the possibility of introducing a dedicated institutional digital signature system in the future. This may include:

- A separate TSAP-managed OpenPGP key distinct from personal identities
- Additional cryptographic signing mechanisms for automation or infrastructure-level verification
- Machine-verifiable trust logs for signed documents

At present, all signatures are issued using a personal OpenPGP key acting on behalf of TSAP. Transition to an institutional key or system, if adopted, will be documented transparently and will not invalidate previously signed records.

## Signed Documents

The following TSAP documents have been cryptographically signed using the TSAP OpenPGP key:

- [TSAP Foundational Principles](/tsap/foundational-principles/)  
  Signed: 10 June 2026  
  Signature: [foundational-principles.md.asc](https://github.com/sunilabrahamindia/sunilabraham/blob/main/tsap/foundational-principles.md.asc)  
  Signatory: Tito Dutta  
  OpenPGP Fingerprint: D8B6 F47B 05BE C620 5884 77CF FC53 BED3 64AC 9AC7  

<!-- TO BE UPDATED AFTER PUBLIC KEY IS UPLOADED
## Public Key

The public key will be published in the TSAP repository and documentation site for verification purposes.

Once published, it will be referenced here as:

- File: `public-key.asc`
- Location: TSAP repository / GitHub / documentation site
-->

<!-- SAME AS ABOVE
## Verification

To verify a TSAP-signed document:

```bash
gpg --import public-key.asc
gpg --verify document.md.asc document.md
```

Verification confirms:

- The document was signed using the TSAP OpenPGP key
- The content has not been modified since the signature was created
-->
