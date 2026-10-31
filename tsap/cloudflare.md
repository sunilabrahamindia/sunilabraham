---
layout: default
title: "Cloudflare Services (Documentation)"
description: "Documentation of Cloudflare services used by The Sunil Abraham Project (TSAP), including their purpose, implementation, and the reasons for selecting them."
categories: [TSAP Documentation]
permalink: /tsap/cloudflare/
created: 2026-10-31
---

{% include documentation-notice.html %}

The Sunil Abraham Project (TSAP) uses Cloudflare and a range of its services as part of the project's website infrastructure, service delivery, monitoring, and experimental search systems. This page documents Cloudflare services that are currently in use, as well as services or configurations used in the past, explaining how they have been used and, where the available record establishes it, why they were selected. Like the project's other documentation pages, this is an evolving record of implementation and design decisions rather than a general guide to Cloudflare.

## Cloudflare Pages

### Purpose

Cloudflare Pages hosts a secondary deployment of the TSAP website. The primary public website remains hosted through GitHub Pages at [sunilabraham.in](https://sunilabraham.in/). The mirror serves two related purposes: it provides an independent deployment against which the GitHub Pages deployment can be compared, and it offers a fallback access route if the primary hosting arrangement or custom domain becomes unavailable.

### Deployment and access

The mirror is deployed from the same Git repository as the primary website. Its Cloudflare Pages address is:

- `https://sunilabraham.pages.dev/`

The mirror is intentionally not promoted through the primary website's navigation or ordinary public links. This keeps it as a secondary infrastructure route rather than a competing public entry point. Anyone who knows the address may still be able to access it.

### Search engine exclusion

A root-level `_headers` file configures the following response header for the Pages mirror:

```text
https://sunilabraham.pages.dev/*
  X-Robots-Tag: noindex, nofollow, noarchive
```

This instructs compliant search engines not to index, follow links from, or retain an archive of the mirror's pages. The purpose is to reduce duplicate indexing while retaining the independently hosted copy. The `_headers` file is intended for Cloudflare Pages; GitHub Pages does not process it as a hosting configuration file.

### Rationale and limitations

An important operational use of the mirror is deployment diagnosis. When a recent change appears on Cloudflare Pages but not on GitHub Pages, the comparison provides evidence that the source change can build and deploy successfully in at least one environment. This can help narrow the investigation towards a GitHub Pages-specific build, deployment, caching, or serving issue instead of immediately assuming that the source change itself is at fault. It is a diagnostic indicator, not conclusive proof: the two hosting platforms may use different build environments or configurations, and a successful deployment does not guarantee that every part of the site is correct.

The mirror also provides domain and hosting resilience. It offers another route to the content if the custom domain cannot be renewed, is suspended, experiences a DNS problem, or becomes inaccessible through the primary hosting service. A separate hosting platform reduces dependence on a single deployment provider.

The mirror is not a complete solution to every failure scenario. Both deployments use the same source repository, so a damaging commit or repository-level problem could affect both copies. Cloudflare Pages is an additional access route, not a substitute for independent repository backups and archival copies.

## Cloudflare DNS and CDN

### DNS management

DNS management for `sunilabraham.in` was moved from BigRock DNS to Cloudflare DNS. BigRock remains the domain registrar, responsible for domain registration and renewal; Cloudflare is responsible for authoritative DNS management. The migration involved auditing the existing records, verifying the imported configuration, restoring records that had been omitted during import, deploying the Cloudflare nameservers, and testing the active configuration.

Centralising DNS management in Cloudflare also provides a more convenient interface for maintaining and verifying records, including CNAME records and other changes needed for services connected to the domain. This is a practical operational benefit: DNS changes are easier to review and manage from the Cloudflare dashboard than they were through the previous interface.

### CDN and performance

The domain also uses Cloudflare's network in front of the website. Depending on the DNS record's proxy status and the resource being requested, Cloudflare can provide edge delivery, caching, and other network-level optimisations. The aim is to improve delivery and reduce dependence on a direct connection to the origin service, although the actual effect varies by request, cache status, location, and the service being accessed.

Some observed response-time measurements appeared modestly better after the migration, but small differences in individual measurements are not enough to establish a reliable site-wide speed improvement. DNS lookup time, time to first byte, and total page-load time measure different parts of the request and should not be treated as interchangeable. Performance claims should be based on repeated, comparable measurements rather than a single reading.

## Cloudflare Email Routing

Cloudflare Email Routing is configured for the `sunilabraham.in` domain to forward incoming messages sent to configured domain addresses to a destination mailbox. This makes it possible to use addresses at the project's custom domain without treating Cloudflare Email Routing as a standalone mailbox or outbound email service.

The configuration was tested with incoming messages, including a message containing Bengali text, to check that forwarding worked. Email Routing depends on the relevant DNS records and verified destination address remaining correctly configured. Any future changes to the domain's DNS should preserve the records required for email delivery.

## Cloudflare Workers

### TSAP Status Monitoring System

Cloudflare Workers is used to serve the public TSAP Status Monitoring System dashboard. The Worker retrieves monitoring information from a JSON endpoint provided by Google Apps Script and renders the dashboard for visitors. Google Apps Script performs the monitoring and Google Sheets stores the results; the Worker handles the presentation layer.

The dashboard is available at:

- [status.sunilabraham.in](https://status.sunilabraham.in/)
- [Cloudflare Workers fallback address](https://status.sunilabrahamindia.workers.dev/)

Separating the dashboard from the monitoring and storage components allows the presentation layer to be changed independently. The fallback Workers address also provides another route if the custom status domain experiences a DNS-related problem. Further details are documented in the [TSAP Status Monitoring System documentation](/tsap/status-monitoring-system/).

## Cloudflare AI Search

Cloudflare AI Search has been explored as a search and retrieval backend for selected TSAP content. One documented use is the knowledge-search interface for A. M. A. Ayrookuzhiel, available at [A. M. A. Ayrookuzhiel — Knowledge Engine](/amaa/search/).

The search interface and its indexing configuration are separate parts of the system: the interface provides the visitor-facing experience, while the search backend indexes selected content for retrieval. The implementation and scope of indexing may change as the feature develops. This page records the use of Cloudflare AI Search as a project component; it does not imply that every TSAP page is indexed by it.

## Cloudflare Observability pricing notice

On 29 October 2026, an email notice about upcoming Cloudflare Observability pricing changes was received at the project's administrative mailbox. A similar notice had been received at a personal mailbox on 27 October 2026. This entry records the substance of the notice without reproducing mailbox addresses, account identifiers, or other private information.

The notice states that the new pricing is due to take effect on 1 December 2026. Observability usage will be measured by the volume of log and trace data ingested and stored, rather than by the number of events. The notice describes these possible outcomes:

- **Workers Paid:** the account will automatically receive a paid Observability subscription. Usage will be billed at the existing pricing until 1 December 2026; after that date, usage beyond included allowances will be billed under the new Observability pricing.
- **No Workers Paid plan or Enterprise contract:** the account will remain on the Free Observability plan, with no Observability charge under the notice. Ingestion will pause when the daily limit is reached and resume when the limit resets.
- **Enterprise:** existing contract terms apply until renewal, after which the new pricing applies.

The notice says that no action is required merely to transition to the new pricing. It recommends reviewing usage and the pricing details before 1 December 2026. It also says that sampling can be adjusted to manage the volume of data ingested. The account's plan and actual Observability usage must be checked in the Cloudflare dashboard; the email alone does not establish which outcome applies to TSAP.

### Action points before 1 December 2026

1. Check the account's Workers plan and whether a paid Observability subscription will apply.
2. Review Observability usage, including log and trace ingestion and stored data, in the Cloudflare dashboard.
3. Read the pricing details linked in the notice and compare them with the account's actual usage and included allowances.
4. If usage could exceed the relevant allowance, decide whether to adjust logging, tracing, or sampling before the new pricing takes effect.
5. Recheck the account before the effective date. The absence of a saved payment card, by itself, does not establish which plan or billing outcome applies.

No account settings have been changed as part of documenting this notice. The pricing change and its effect on the project's account remain to be verified.

## Design considerations

Cloudflare services have been used for specific operational purposes rather than as a replacement for TSAP's static-site architecture. The main website remains a Git-based static site, while Cloudflare services provide additional hosting, a serverless presentation layer, and experimental search infrastructure where useful.

The project's reasons for choosing a service should be documented only where they can be supported by the implementation or a recorded decision. Where the historical reason for a choice is not established, it should remain undocumented rather than be inferred retrospectively.

## Maintenance record

This page should be updated when a Cloudflare service is introduced, substantially reconfigured, retired, or replaced. Entries should distinguish current use from experiments and past use, and should record the service's role, relevant public endpoints, dependencies, limitations, and documented reasons for selection where known.

{% include navbox-tsap.html %}
