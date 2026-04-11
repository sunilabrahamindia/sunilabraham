---
layout: default
title: "Templates"
description: "An overview of reusable Jekyll include templates used across The Sunil Abraham Project (TSAP)."
categories: [TSAP Documentation]
permalink: /tsap/templates/
created: 2026-04-11
---

**Templates** are reusable snippets of HTML used across **The Sunil Abraham Project** (TSAP) to maintain visual and structural consistency. On TSAP, templates are implemented as Jekyll include files, which are small, self-contained files stored in the `_includes` directory at the root of the project repository. They are inserted into any page using the Liquid tag `{% raw %}{% include filename.html %}{% endraw %}`, and some accept parameters to customise their output. The full list of include files is available on [**GitHub**](https://github.com/sunilabrahamindia/sunilabraham/tree/main/_includes).

## Content Templates

### Main Article

Displays a styled callout linking to a main or parent article on a related topic.

```liquid
{% raw %}{% include main-article.html link="/page-url/" title="Page Title" %}{% endraw %}
```

### Notice

Displays a warning or important notice to the reader. Accepts a `message` parameter.

```liquid
{% raw %}{% include notice.html message="Your message here." %}{% endraw %}
```

### Stub

Displays a notice indicating that the page is short and incomplete and will be expanded over time. Takes no parameters.

```liquid
{% raw %}{% include stub.html %}{% endraw %}
```

### Under Construction

Displays a notice indicating that the page is actively being worked on. Takes no parameters.

```liquid
{% raw %}{% include under-construction.html %}{% endraw %}
```

### Outdated

Displays a notice indicating that some information on the page may no longer be current. Takes no parameters.

```liquid
{% raw %}{% include outdated.html %}{% endraw %}
```

### Disputed

Displays a notice indicating that the accuracy or neutrality of some information is disputed. Takes no parameters.

```liquid
{% raw %}{% include disputed.html %}{% endraw %}
```

### Cleanup

Displays a notice indicating that the page requires editorial cleanup. Takes no parameters.

```liquid
{% raw %}{% include cleanup.html %}{% endraw %}
```

### Copy Edit

Displays a notice indicating that the page requires copy editing for grammar, style, cohesion, tone, or spelling. Takes no parameters.

```liquid
{% raw %}{% include copyedit.html %}{% endraw %}
```

### Expert Needed

Displays a notice indicating that the page deals with a specialised subject and may benefit from expert review. Takes no parameters.

```liquid
{% raw %}{% include expert-needed.html %}{% endraw %}
```

### Current Event

Displays a notice indicating that the page documents a current or ongoing event. Takes no parameters.

```liquid
{% raw %}{% include current.html %}{% endraw %}
```

### Expand

Displays a notice indicating that the article as a whole needs expansion. Takes no parameters.

```liquid
{% raw %}{% include expand.html %}{% endraw %}
```

### Expand Section

Displays a notice indicating that a specific section needs expansion. Place immediately below the relevant `##` or `###` heading. Takes no parameters.

```liquid
{% raw %}{% include expand-section.html %}{% endraw %}
```

### Did You Know

Displays the "Did You Know" facts grid, used on the TSAP main page.

```liquid
{% raw %}{% include dyk.html %}{% endraw %}
```

### Event Infobox

Displays a structured event data table with Schema.org markup. Reads automatically from the page's front matter fields such as `event_type`, `date`, `location`, `sunils_role`, `organisers`, and `website`. Takes no parameters.

```liquid
{% raw %}{% include event-infobox.html %}{% endraw %}
```

### Mentions List

Displays a list of external mentions of TSAP pages, sourced from `_data/mentions`. Sorted by access date, newest first. Takes no parameters.

```liquid
{% raw %}{% include mentions-list.html %}{% endraw %}
```

## Page Metadata Templates

### Author

Displays the author or authors of a page, reading from the `authors` front matter field. Takes no parameters.

```liquid
{% raw %}{% include author.html %}{% endraw %}
```

### Categories

Displays a Wikipedia-style category box using the `categories` front matter field. Takes no parameters.

```liquid
{% raw %}{% include categories.html %}{% endraw %}
```

### Page Data

Displays the page creation date with links to its GitHub commit history, file preview, and raw source. Reads from the `created` front matter field. Takes no parameters.

```liquid
{% raw %}{% include page-data.html %}{% endraw %}
```

### Back to Top

Displays a right-aligned "Back to Top" link. Takes no parameters.

```liquid
{% raw %}{% include back-to-top.html %}{% endraw %}
```

<style>
pre {
  overflow-x: auto;
  white-space: pre;
}
</style>
