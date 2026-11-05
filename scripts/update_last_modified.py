#!/usr/bin/env python3

import os
import re
import subprocess
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "_data" / "last_modified.yml"

# Specific commits that should not affect Last Updated dates.
# Abbreviated commit hashes are supported.
IGNORE_COMMITS = {
    "466821e",  # Introduce page_id identifiers across TSAP
}

# Commit-message tags that indicate non-substantive changes.
IGNORE_TAGS = {
    "[Minor]",
    "[Minor edit]",
    "[Metadata]",
    "[Batch edit]",
    "[Maintenance]",
}

COMMIT_HEADER = re.compile(
    r"^([0-9a-f]{40})\t(\d{4}-\d{2}-\d{2})\t(.*)$"
)


def should_ignore_commit(commit_hash, commit_subject):
    """Return True if a commit should not affect the Last Updated date."""

    if any(commit_hash.startswith(ignored) for ignored in IGNORE_COMMITS):
        return True

    if any(tag in commit_subject for tag in IGNORE_TAGS):
        return True

    return False


def get_valid_pages():
    """Return pages using the same front matter rules as generate_pages_json.py."""

    pages = set()

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = sorted(directory for directory in dirs if directory != ".git")
        files.sort()

        for filename in files:
            if not filename.endswith((".md", ".markdown")):
                continue

            md_file = Path(root) / filename
            source_path = md_file.relative_to(REPO_ROOT).as_posix()

            try:
                content = md_file.read_text(encoding="utf-8")

                if not content.startswith("---"):
                    continue

                parts = content.split("---", 2)
                if len(parts) < 3:
                    continue

                front_matter = yaml.safe_load(parts[1])
                if not isinstance(front_matter, dict):
                    continue

                if not front_matter.get("created"):
                    continue

                pages.add(source_path)

            except Exception as error:
                print(f"Skipping {source_path}: {error}")

    return pages


def get_last_modified_dates(pages):
    """Scan Git history once and retain the latest qualifying date per page."""

    result = subprocess.run(
        [
            "git",
            "-c",
            "core.quotePath=false",
            "log",
            "--format=%H%x09%cs%x09%s",
            "--name-only",
            "--",
            "*.md",
            "*.markdown",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    entries = {}
    current_date = None
    ignore_current_commit = True

    for line in result.stdout.splitlines():
        match = COMMIT_HEADER.match(line)

        if match:
            commit_hash, current_date, commit_subject = match.groups()
            ignore_current_commit = should_ignore_commit(
                commit_hash, commit_subject
            )
            continue

        if not line or ignore_current_commit:
            continue

        # Git emits paths relative to the repository root. Only current,
        # valid pages are eligible for the output.
        if line in pages and line not in entries:
            entries[line] = current_date

        if len(entries) == len(pages):
            break

    return entries


def main():
    pages = get_valid_pages()
    entries = get_last_modified_dates(pages)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        for path, date in sorted(entries.items()):
            output.write(f'"{path}": {date}\n')

    print(f"Valid pages found: {len(pages)}")
    print(f"Written {len(entries)} entries to {OUTPUT_FILE}")

    missing = pages - entries.keys()
    if missing:
        print(f"Pages without qualifying Git history: {len(missing)}")


if __name__ == "__main__":
    main()
