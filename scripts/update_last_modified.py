#!/usr/bin/env python3

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "_data" / "last_modified.yml"

EXCLUDED_DIRS = {
    ".git",
    "_site",
    "node_modules",
    ".sass-cache",
    ".jekyll-cache",
    ".vscode",
}

# Specific commits that should not affect Last Updated dates.
# Abbreviated commit hashes are supported.
IGNORE_COMMITS = {
    "466821e",  # Introduce page_id identifiers across TSAP
}

# Commit-message tags that indicate non-substantive changes.
# A commit is ignored when its summary contains one of these exact tags.
IGNORE_TAGS = {
    "[Minor]",
    "[Minor edit]",
    "[Metadata]",
    "[Batch edit]",
    "[Maintenance]",
}

entries = {}


def should_ignore_commit(commit_hash, commit_subject):
    """Return True if a commit should not affect the Last Updated date."""

    if any(commit_hash.startswith(ignored) for ignored in IGNORE_COMMITS):
        return True

    if any(tag in commit_subject for tag in IGNORE_TAGS):
        return True

    return False


for md_file in sorted(REPO_ROOT.rglob("*.md")):
    rel_path = md_file.relative_to(REPO_ROOT)

    if any(part in EXCLUDED_DIRS for part in rel_path.parts):
        continue

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--format=%H%x09%cs%x09%s",
                "--",
                str(rel_path),
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

        date = ""

        for line in result.stdout.splitlines():
            parts = line.split("\t", 2)

            if len(parts) != 3:
                continue

            commit_hash, commit_date, commit_subject = parts

            if should_ignore_commit(commit_hash, commit_subject):
                continue

            date = commit_date
            break

        if date:
            entries[str(rel_path).replace("\\", "/")] = date

    except subprocess.CalledProcessError:
        continue

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for path, date in sorted(entries.items()):
        f.write(f'"{path}": {date}\n')

print(f"Written {len(entries)} entries to {OUTPUT_FILE}")