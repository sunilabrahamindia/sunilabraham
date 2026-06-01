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

entries = {}

for md_file in sorted(REPO_ROOT.rglob("*.md")):
    rel_path = md_file.relative_to(REPO_ROOT)

    if any(part in EXCLUDED_DIRS for part in rel_path.parts):
        continue

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "-1",
                "--format=%cs",
                "--",
                str(rel_path)
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

        date = result.stdout.strip()

        if date:
            entries[str(rel_path).replace("\\", "/")] = date

    except subprocess.CalledProcessError:
        continue

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for path, date in sorted(entries.items()):
        f.write(f'"{path}": {date}\n')

print(f"Written {len(entries)} entries to {OUTPUT_FILE}")