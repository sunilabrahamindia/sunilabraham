---
layout: default
title: "Indian Website Certificate Expiry Monitor"
description: "An independent public dashboard tracking TLS certificate expiry for selected important Indian websites."
permalink: /tools/india-certificate-expiry/
categories: [Tools, Security]
created: 2026-10-24
---

{% include under-construction.html %}

<p class="lead">**Indian Website Certificate Expiry Monitor** is an independent public-interest project that tracks the expiry dates of TLS certificates presented by selected important Indian websites. The immediate inspiration for this tool is a [tweet by Pranesh Prakash](https://x.com/pranesh/status/2113592458349338640). This tool is at an early stage of development and will be improved gradually.</p>


<style>
/* Indian website certificate expiry dashboard */
.certificate-dashboard { margin: 1.25rem 0 2rem; }
.certificate-controls { display: grid; grid-template-columns: 1fr; gap: .4rem; margin: 1rem 0; max-width: 36rem; }
.certificate-controls input, .certificate-controls select { width: 100%; min-height: 2.75rem; padding: .55rem .7rem; border: 1px solid var(--border-sub, #767676); border-radius: .25rem; background: var(--bg-surface, #fff); color: var(--text-main, #1a1a1a); }
.certificate-summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr)); gap: .75rem; margin: 1rem 0; }
.certificate-summary > div { border: 1px solid var(--border-main, #d8dee4); border-radius: .25rem; padding: .85rem; background: var(--bg-surface, #fff); }
.certificate-summary span, .certificate-summary small { display: block; }
.certificate-summary span { font-size: 1.5rem; font-weight: 700; }
.certificate-summary small, .certificate-domain { color: var(--text-muted, #444); }
.certificate-table-wrap { overflow-x: auto; }
.certificate-table { width: 100%; border-collapse: collapse; }
.certificate-table th, .certificate-table td { padding: .7rem; border: 1px solid var(--table-border, #767676); text-align: left; vertical-align: top; }
.certificate-table th { background: var(--table-th-bg, #f2f2f2); color: var(--table-th-text, #222); }
.certificate-table th button { color: inherit; background: transparent; border: 0; font: inherit; font-weight: 700; text-decoration: underline; cursor: pointer; padding: .15rem; }
.certificate-domain { display: block; font-size: .85rem; overflow-wrap: anywhere; }
.certificate-status { display: inline-block; padding: .2rem .45rem; border: 1px solid currentColor; border-radius: .2rem; font-size: .9rem; font-weight: 600; }
.certificate-status-valid { color: #176534; }
.certificate-status-expiring { color: #8a4b00; }
.certificate-status-expired, .certificate-status-error { color: #a61b1b; }
.certificate-note { font-size: .95rem; }
@media (max-width: 40rem) { .certificate-table { min-width: 42rem; } }

/* Certificate status colours for the site's dark mode */
body.tsap-dark-mode .certificate-status-valid { color: #86efac; }
body.tsap-dark-mode .certificate-status-expiring { color: #fcd34d; }
body.tsap-dark-mode .certificate-status-expired,
body.tsap-dark-mode .certificate-status-error { color: #fca5a5; }
</style>


This independent public-interest project tracks the expiry dates of TLS certificates presented by selected important Indian websites. It is an experimental monitoring resource, not an official government or financial-sector service. Results describe the specific public hostname checked and do not establish the security of an institution's entire network, mobile applications, or payment infrastructure.

The monitor checks the selected websites automatically and records the latest result. A certificate's expiry date is not, by itself, proof of a security incident: a failed check can also result from a network problem, hostname issue, or a service being unavailable. Please verify important findings with the relevant organisation before drawing conclusions.

## Current results

<div class="certificate-dashboard" id="certificate-dashboard">
  <p id="certificate-updated" role="status">Loading the latest monitoring results...</p>
  <div class="certificate-controls">
    <label for="certificate-search">Search websites</label>
    <input id="certificate-search" type="search" placeholder="Search by website, domain or category">
    <label for="certificate-filter">Filter results</label>
    <select id="certificate-filter">
      <option value="all">All results</option>
      <option value="expiring">Expiring within 30 days</option>
      <option value="expired">Expired certificates</option>
      <option value="valid">Valid for more than 30 days</option>
      <option value="error">Could not verify</option>
    </select>
  </div>
  <div class="certificate-summary" aria-live="polite">
    <div><span id="certificate-total">—</span><small>Websites checked</small></div>
    <div><span id="certificate-expiring">—</span><small>Expiring within 30 days</small></div>
    <div><span id="certificate-expired">—</span><small>Expired certificates</small></div>
    <div><span id="certificate-errors">—</span><small>Checks needing review</small></div>
  </div>
  <div class="certificate-table-wrap">
    <table class="certificate-table">
      <thead>
        <tr>
          <th scope="col"><button type="button" data-sort="name">Website / domain</button></th>
          <th scope="col"><button type="button" data-sort="category">Category</button></th>
          <th scope="col"><button type="button" data-sort="expiry">Certificate expiry</button></th>
          <th scope="col"><button type="button" data-sort="days_remaining">Days remaining</button></th>
          <th scope="col">Status</th>
        </tr>
      </thead>
      <tbody id="certificate-rows">
        <tr><td colspan="5">Waiting for the first successful monitoring run.</td></tr>
      </tbody>
    </table>
  </div>
  <p id="certificate-empty" hidden>No websites match these filters.</p>
  <p class="certificate-note">Times are recorded in UTC. "Could not verify" means the check did not produce a reliable certificate result; it does not mean the certificate has expired.</p>
</div>

## Method and limitations

- The checker connects to each listed hostname over HTTPS and reads the certificate presented by that endpoint.
- Results are refreshed by a scheduled GitHub Actions workflow. Scheduled runs can be delayed, so the last-checked timestamp matters.
- Only the hostnames in the curated list are monitored. An organisation may use separate certificates for its subdomains, APIs, applications and other systems.
- This page does not inspect certificates embedded in Android apps, and it does not test UPI, eRupee or any other payment system as a whole.
- A listed expiry date is a technical observation, not a claim that a website is compromised or that users' funds are at risk.

## Sources and corrections

The domain list is curated from publicly identifiable official websites and may be incomplete. If you notice an incorrect domain, an ownership change or a misleading result, please verify it against the organisation's official information before reporting it.

<script>
(function () {
  const dataUrl = '{{ "/assets/data/india-certificate-results.json" | relative_url }}';
  const rows = document.getElementById('certificate-rows');
  const updated = document.getElementById('certificate-updated');
  const search = document.getElementById('certificate-search');
  const filter = document.getElementById('certificate-filter');
  const empty = document.getElementById('certificate-empty');
  let results = [];
  let sortKey = 'days_remaining';
  let sortDirection = 1;

  function safeText(value) {
    return value === null || value === undefined || value === '' ? '—' : String(value);
  }

  function statusFor(item) {
    if (item.status !== 'ok') return { key: 'error', label: 'Could not verify' };
    if (item.days_remaining < 0) return { key: 'expired', label: 'Expired' };
    if (item.days_remaining <= 30) return { key: 'expiring', label: 'Expiring soon' };
    return { key: 'valid', label: 'Valid' };
  }

  function addCell(row, value) {
    const cell = document.createElement('td');
    cell.textContent = safeText(value);
    row.appendChild(cell);
    return cell;
  }

  function render() {
    const term = search.value.trim().toLowerCase();
    const selected = filter.value;
    const visible = results.filter(item => {
      const status = statusFor(item);
      const matchesTerm = [item.name, item.domain, item.category].join(' ').toLowerCase().includes(term);
      return matchesTerm && (selected === 'all' || selected === status.key);
    }).sort((a, b) => {
      let av = a[sortKey], bv = b[sortKey];
      if (sortKey === 'expiry' || sortKey === 'name' || sortKey === 'category') {
        av = String(av || '').toLowerCase();
        bv = String(bv || '').toLowerCase();
        return av < bv ? -sortDirection : av > bv ? sortDirection : 0;
      }
      av = Number.isFinite(av) ? av : Number.MAX_SAFE_INTEGER;
      bv = Number.isFinite(bv) ? bv : Number.MAX_SAFE_INTEGER;
      return (av - bv) * sortDirection;
    });

    rows.replaceChildren();
    visible.forEach(item => {
      const row = document.createElement('tr');
      const website = document.createElement('td');
      const link = document.createElement('a');
      link.href = 'https://' + item.domain + '/';
      link.textContent = item.name;
      website.appendChild(link);
      const domain = document.createElement('small');
      domain.className = 'certificate-domain';
      domain.textContent = item.domain;
      website.appendChild(domain);
      row.appendChild(website);
      addCell(row, item.category);
      addCell(row, item.expiry_utc ? item.expiry_utc.slice(0, 10) : '—');
      addCell(row, item.status === 'ok' ? item.days_remaining : '—');
      const status = statusFor(item);
      const cell = addCell(row, status.label);
      const badge = document.createElement('span');
      badge.className = 'certificate-status certificate-status-' + status.key;
      badge.textContent = status.label;
      cell.textContent = '';
      cell.appendChild(badge);
      if (item.error) row.title = item.error;
      rows.appendChild(row);
    });
    empty.hidden = visible.length !== 0;
    document.getElementById('certificate-total').textContent = results.filter(x => x.status === 'ok').length;
    document.getElementById('certificate-expiring').textContent = results.filter(x => statusFor(x).key === 'expiring').length;
    document.getElementById('certificate-expired').textContent = results.filter(x => statusFor(x).key === 'expired').length;
    document.getElementById('certificate-errors').textContent = results.filter(x => statusFor(x).key === 'error').length;
  }

  search.addEventListener('input', render);
  filter.addEventListener('change', render);
  document.querySelectorAll('[data-sort]').forEach(button => {
    button.addEventListener('click', () => {
      const next = button.dataset.sort;
      sortDirection = sortKey === next ? -sortDirection : 1;
      sortKey = next;
      render();
    });
  });

  fetch(dataUrl, { cache: 'no-store' })
    .then(response => {
      if (!response.ok) throw new Error('Monitoring results are not available yet.');
      return response.json();
    })
    .then(data => {
      results = Array.isArray(data.results) ? data.results : [];
      updated.textContent = data.last_checked_utc
        ? 'Last checked: ' + data.last_checked_utc.replace('T', ' ').replace(/Z$/, ' UTC')
        : 'The first scheduled monitoring run has not completed yet.';
      if (!results.length) updated.textContent = 'No monitoring results are available yet. Check back after the first scheduled run.';
      render();
    })
    .catch(() => {
      updated.textContent = 'Monitoring results could not be loaded. This may be temporary; please try again later.';
      rows.replaceChildren();
      const row = document.createElement('tr');
      const cell = document.createElement('td');
      cell.colSpan = 5;
      cell.textContent = 'Results are temporarily unavailable.';
      row.appendChild(cell);
      rows.appendChild(row);
    });
})();
</script>

