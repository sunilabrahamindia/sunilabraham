---
layout: default
title: "Automatic Last Updated Dates (Documentation)"
description: "Documentation for the Automatic Last Updated Dates system on The Sunil Abraham Project (TSAP), including its purpose, architecture, workflow, and development history."
categories: [TSAP Documentation]
permalink: /tsap/automatic-last-updated-dates-documentation/
created: 2026-06-01
---

{% include documentation-notice.html %}

The **Automatic Last Updated Dates** system is a provenance and maintenance feature used across The Sunil Abraham Project (TSAP). It automatically displays the most recent modification date for pages by extracting information from the repository's Git history and making that information available to the site's Page Data component.

The feature was developed to complement the site's existing page creation date system. Since early 2026, TSAP pages have been required to include a permanent `created:` field in their front matter. While this successfully records when a page first entered the project, it does not indicate when a page was subsequently revised, expanded, corrected, or updated. As the repository continued to grow, manually maintaining a separate `last_updated:` field across hundreds or thousands of pages became increasingly impractical.

The Automatic Last Updated Dates system solves this problem by using Git as the authoritative source of modification history. Rather than storing update dates inside page front matter, a Python script generates a structured YAML data file from repository history. This file is then consumed by the site's Page Data component, allowing modification dates to be displayed automatically.

The implementation was developed with support from ChatGPT. All design decisions, testing, editorial judgement, and final implementation choices were made by the project maintainer.

## Background

The question of how to display page modification dates emerged naturally as TSAP expanded. The project already maintained creation dates, but many pages continued to evolve after publication. Articles were corrected, metadata improved, accessibility issues fixed, internal links updated, photographs added, and supplementary material incorporated over time.

One obvious solution involved adding a manual `last_updated:` field to page front matter. While technically simple, this approach quickly revealed practical limitations. Editors would need to remember to update the field every time a page changed. As the repository grew beyond one thousand Markdown files, the maintenance burden became increasingly undesirable.

Several alternative approaches were considered. One possibility involved using GitHub Actions to generate modification dates automatically during site builds. Another involved using Jekyll plugins capable of exposing Git metadata directly within templates. Other options included external APIs or custom build-time workflows.

Although these approaches were technically feasible, they introduced additional infrastructure, dependencies, or complexity. TSAP generally favours solutions that are transparent, easy to understand, compatible with static hosting, and simple to maintain over long periods of time.

The final design therefore adopted a simpler architecture:

1. Use Git history as the authoritative source.
2. Generate a YAML data file from that history.
3. Display modification dates through existing page templates.

This approach preserved the project's preference for static-site simplicity while avoiding manual maintenance.

## Architecture

The Automatic Last Updated Dates system consists of four components working together.

### Git History

Git serves as the authoritative source for modification dates.

For any tracked page, the most recent modification date can be retrieved using:

```bash
git log -1 --format=%cs -- path/to/file.md
```

This command returns the date of the most recent commit affecting the specified file.

For example:

```bash
git log -1 --format=%cs -- privacy.md
```

returns:

```text
2025-11-22
```

Because all TSAP content already exists within the Git repository, no additional metadata storage mechanism is required.

### Generation Script

The second component is a Python script responsible for generating modification-date data from repository history. The script is located at:

```text
scripts/update_last_modified.py
```

When executed, the script scans Markdown files throughout the repository, retrieves the most recent Git commit date associated with each file, and generates a structured YAML dataset.

The script was intentionally designed as a manual maintenance utility rather than a continuously running automation. This keeps the implementation straightforward while remaining fully compatible with GitHub Pages and static-site workflows.

### Generated Data File

The script produces:

```text
_data/last_modified.yml
```

The file contains page paths mapped to modification dates.

Example:

```yaml
privacy.md: 2025-11-22
media/facebook-free-basics-net-neutrality-debate-indian-express.md: 2026-06-01
publications/example-report.md: 2026-05-15
```

Each key represents a repository path, while each value represents the most recent Git commit date affecting that file.

The file is human-readable, easily audited, and can be regenerated whenever necessary.

### Page Data Integration

The final component is the Page Data section displayed throughout the site.

The Page Data component retrieves the current page's repository path using:

```liquid
{{ page.path }}
```

It then looks for a corresponding entry inside:

```liquid
site.data.last_modified
```

The implementation uses conditional logic:

{% raw %}
```liquid
{% assign last_updated = site.data.last_modified[page.path] %}
{% if last_updated %}
  Last updated on {{ last_updated | date: "%-d %B %Y" }}.
{% endif %}
```
{% endraw %}

This ensures that pages with available data display a modification date, while pages without a matching entry simply omit the information.

As a result, newly created pages continue to render correctly even if the YAML file has not yet been regenerated.

## Development History

### 1 June 2026

The first implementation of the Automatic Last Updated Dates system was developed on 1 June 2026.

Development followed an incremental testing methodology rather than attempting to build the entire system at once. Individual assumptions were tested separately before proceeding to the next stage.

The first step confirmed that Git could reliably return modification dates for individual files.

Example:

```bash
git log -1 --format=%cs -- privacy.md
```

Once Git history retrieval had been verified, testing shifted to Jekyll's data-loading capabilities. A temporary YAML file was created within the `_data` directory containing a single test entry.

```yaml
privacy.md: 2025-11-22
```

This entry was then displayed through the Page Data component to confirm that Jekyll could successfully load and expose the data.

Additional testing verified that:

- `_data` files loaded correctly.
- Liquid templates could access the data.
- `page.path` matched repository paths.
- Conditional display logic functioned correctly.
- Missing entries did not create empty placeholders.
- Newly created pages degraded gracefully.

A temporary debugging phase involved displaying raw `page.path` values on live pages in order to confirm that repository paths matched YAML keys. This confirmed that the architecture was viable and that no additional path translation layer would be required.

Once the architecture had been validated, a Python script was developed to automate generation of modification-date data for the repository as a whole.

The resulting implementation successfully avoided GitHub Actions, Jekyll plugins, database storage, and manual front-matter maintenance.

## Maintenance Workflow

The system is designed around periodic regeneration rather than continuous automation.

Whenever significant content changes occur, the following workflow is recommended:

1. Create, edit, move, or rename content.
2. Run:

   ```bash
   python3 scripts/update_last_modified.py
   ```

3. Verify that `_data/last_modified.yml` has been regenerated successfully.
4. Review unexpected additions or removals.
5. Commit updated files.
6. Push changes to GitHub.

Once deployed, pages automatically display updated modification dates.

The script may be run weekly, fortnightly, monthly, or before major releases. The system is intended to provide useful maintenance information rather than real-time modification tracking.

## Advantages

The selected architecture provides several important advantages.

Because modification dates are derived from Git history, editors do not need to maintain additional front-matter fields. The implementation remains fully compatible with GitHub Pages and does not depend upon custom plugins or build infrastructure. The generated YAML file remains transparent and human-readable, allowing manual inspection whenever necessary.

The system also scales naturally. Whether the repository contains one hundred pages or several thousand, the underlying workflow remains largely unchanged.

Perhaps most importantly, the implementation is easy to reverse. Removing the feature simply requires deleting the generated YAML file and removing the corresponding Liquid template code.

## Known Limitations

The system reflects Git commit history rather than editorial significance. A minor formatting correction, metadata adjustment, accessibility fix, or spelling correction may update a page's modification date even when the substantive content remains unchanged.

Pages created after the most recent regeneration will not display a Last Updated date until the script is run again. This behaviour is intentional and avoids introducing unnecessary automation complexity.

The implementation also assumes that repository history accurately reflects page evolution. Files introduced outside the normal Git workflow may require regeneration before appearing correctly.

These limitations are considered acceptable given the project's emphasis on simplicity, transparency, maintainability, and static-site compatibility.

## Future Improvements

Several enhancements may be considered in the future.

Potential improvements include excluding selected directories from generation, suppressing modification dates when they match creation dates, expanding maintenance reporting, integrating modification information into additional editorial tools, and refining presentation within the Page Data component.

Any future improvements should continue to prioritise transparency, maintainability, and compatibility with TSAP's long-term static-site architecture.
