---
layout: default
title: "TSAP Domain Expiry Monitor (Documentation)"
description: "Documentation for the TSAP Domain Expiry Monitor, including its architecture, monitoring workflow, renewal detection, and automated reminder system."
categories: [TSAP Documentation, TSAP Tools]
permalink: /tsap/domain-expiry-monitor/
created: 2026-07-13
---

{% include documentation-notice.html %}

The **TSAP Domain Expiry Monitor** automatically monitors the registration expiry date of the primary domain used by The Sunil Abraham Project (TSAP). It periodically retrieves authoritative registration information from the official NIXI RDAP service, detects domain renewals, and sends reminder notifications before expiry.

The monitoring system was intentionally designed to remain lightweight, dependable, and inexpensive while avoiding third-party monitoring services and manual calendar reminders.

## Background

The primary domain represents one of the most important pieces of infrastructure supporting The Sunil Abraham Project. Although domain registrars provide renewal reminders, relying exclusively on external notifications introduces unnecessary risk.

The Domain Expiry Monitor was therefore developed as an independent reminder system that remains under the project's own control.

Rather than relying on WHOIS lookups or commercial APIs, the monitor retrieves registration information directly from the official NIXI RDAP service, ensuring that reminder calculations are based upon authoritative registry data.

The monitor currently supervises the primary domain used by TSAP while being designed so that support for additional domains can be added in the future with only minor changes.

## Objectives

The monitoring system was designed to:

- Monitor the expiry date of the primary TSAP domain.
- Retrieve registration information from an authoritative source.
- Send reminder notifications before domain expiry.
- Detect when a domain has been renewed.
- Prevent duplicate reminder notifications.
- Operate automatically without manual intervention.
- Remain lightweight and inexpensive to maintain.
- Provide simple manual testing facilities.

## Architecture

The monitoring system consists of several independent components.

```text
      Google Apps Script Trigger
                 │
                 ▼
     TSAP Domain Expiry Monitor
                 │
                 ▼
       Official NIXI RDAP Service
                 │
                 ▼
      Domain Registration Data
         │                │
         ▼                ▼
 Script Properties     Gmail Service
         │                │
         └────────► Reminder Emails
```

Each component performs a single responsibility. Google Apps Script performs the monitoring, the NIXI RDAP service provides authoritative registration information, Script Properties preserve monitoring state between executions, and Gmail delivers reminder notifications.

Separating these responsibilities keeps the monitoring logic simple while making future maintenance considerably easier.

## Components

### Google Apps Script

Google Apps Script serves as the monitoring engine.

A time-driven trigger executes the monitoring script once each morning. During every execution the script retrieves the current registration information from the official RDAP service, calculates the remaining validity period, checks for renewal events, and determines whether reminder notifications should be sent.

The monitoring logic intentionally contains no presentation layer and performs only monitoring, comparison, and notification.

### Official NIXI RDAP Service

Registration information is retrieved directly from the official NIXI RDAP service.

Using RDAP avoids the need for HTML scraping or unofficial WHOIS services while providing structured registration information in a standardised format.

The monitor retrieves information including:

- Domain name.
- Registration expiry date.
- Registrar information.
- Nameserver information.

The expiry date serves as the authoritative reference for all reminder calculations.

### Script Properties

The monitoring system stores a small amount of persistent state using Google Apps Script Script Properties.

This information includes:

- The previously recorded expiry date.
- Reminder thresholds that have already generated notifications.

Using Script Properties avoids the need for an additional spreadsheet while allowing the monitor to remember previous executions.

### Gmail

Reminder notifications are delivered using Gmail.

The monitoring script generates plain-text notification emails containing the current registration information together with the remaining validity period.

Separate notification messages are generated for:

- Manual testing.
- Domain renewal detection.
- Scheduled expiry reminders.

## Monitoring Workflow

Each monitoring cycle follows a simple sequence.

1. The daily trigger starts the monitoring script.
2. The script retrieves the latest registration information from the official NIXI RDAP service.
3. The expiry date is extracted from the returned RDAP data.
4. The remaining number of days until expiry is calculated.
5. The current expiry date is compared with the previously stored value.
6. Renewal detection is performed.
7. Reminder thresholds are evaluated.
8. Notification emails are sent when appropriate.
9. Monitoring state is updated for the next execution.

Each execution is independent while retaining only the small amount of state necessary for duplicate prevention and renewal detection.

## Reminder Schedule

Reminder notifications are currently generated when the remaining validity period reaches:

- 60 days
- 30 days
- 15 days
- 7 days
- 3 days
- 1 day

Each reminder is sent only once for a particular registration cycle.

If the monitoring script executes multiple times during the same reminder window, duplicate notifications are automatically suppressed.

## Renewal Detection

One of the principal features of the monitoring system is its ability to detect when the monitored domain has been renewed.

During every execution, the newly retrieved expiry date is compared with the expiry date stored from the previous successful execution.

If the two dates differ, the system assumes that the domain registration has been renewed.

When a renewal is detected, the monitor automatically:

- Stores the new expiry date.
- Clears the reminder history for the previous registration cycle.
- Sends a confirmation notification indicating that a renewal has been detected.
- Begins monitoring against the new expiry date.

This process requires no manual intervention and ensures that reminder notifications always correspond to the current registration period.

## Duplicate Prevention

Reminder notifications are intended to be sent only once for each configured reminder threshold.

To achieve this, the monitoring system maintains a record of reminder thresholds that have already generated notifications during the current registration cycle.

Before sending a reminder, the script checks whether that threshold has already been recorded.

If a reminder has already been issued, no additional notification is generated.

When a domain renewal is detected, the reminder history is automatically cleared, allowing reminders for the next registration period to be generated normally.

## Manual Testing

The monitoring system provides dedicated functions for testing and maintenance.

These functions allow the monitoring workflow to be verified without waiting for scheduled executions or approaching reminder thresholds.

Available testing functions include:

- Sending a trial notification email.
- Creating a draft notification email.
- Running the monitoring process manually.
- Creating the scheduled trigger.
- Removing existing triggers.

These facilities simplify testing during development while ensuring that normal reminder history remains unaffected.

## Scheduled Execution

The monitoring script operates automatically using a Google Apps Script time-driven trigger.

The trigger currently executes once every morning.

During each scheduled execution, the monitor retrieves the latest RDAP information, evaluates the configured reminder thresholds, performs renewal detection, and generates notifications where appropriate.

No user interaction is required after the monitoring system has been configured.

## Reliability and Error Handling

The monitoring system has been designed to continue operating even when temporary problems occur.

The script includes error handling for situations such as:

- Temporary network failures.
- Unavailable RDAP services.
- Invalid or unexpected responses.
- JSON parsing failures.
- Email delivery errors.

Whenever an error occurs, the execution terminates gracefully without corrupting the stored monitoring state.

The next scheduled execution continues normally without requiring manual recovery.

## Design Philosophy

The Domain Expiry Monitor follows the same architectural principles used throughout The Sunil Abraham Project.

The system was intentionally designed to remain:

- Lightweight.
- Easy to understand.
- Easy to maintain.
- Independent of commercial monitoring platforms.
- Inexpensive to operate.
- Built using widely available cloud services.

Rather than implementing unnecessary complexity, the monitor focuses on performing a single task reliably over long periods with minimal maintenance.

## Future Development

The current implementation monitors a single domain.

The underlying architecture, however, has been designed so that support for multiple domains can be introduced in the future with relatively small modifications.

Potential future enhancements include:

- Monitoring multiple domains.
- Supporting different reminder schedules for individual domains.
- Recording historical monitoring events in a database.
- Publishing a public monitoring dashboard.
- Additional notification channels.
- Administrative reporting and monitoring statistics.

These enhancements can be introduced without fundamentally changing the existing monitoring architecture.
