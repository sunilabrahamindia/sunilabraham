#!/usr/bin/env python3

from pathlib import Path
import re
from datetime import datetime

PAGE_ID_PATTERN = re.compile(r"^page_id:\s*(TSAP-(\d{4}))\s*$", re.MULTILINE)

pages = []
highest_id = 0

for md_file in Path(".").rglob("*.md"):
    try:
        text = md_file.read_text(encoding="utf-8")

        if not text.startswith("---"):
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            continue

        yaml_text = parts[1]

        # Find existing Page IDs
        match = PAGE_ID_PATTERN.search(yaml_text)
        if match:
            highest_id = max(highest_id, int(match.group(2)))
            continue

        # Skip pages without a created date
        match = re.search(
            r"^created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*$",
            yaml_text,
            re.MULTILINE,
        )

        if not match:
            continue

        created = datetime.strptime(
            match.group(1),
            "%Y-%m-%d"
        ).date()

        pages.append({
            "path": md_file,
            "created": created
        })

    except Exception as e:
        print(f"Skipping {md_file}: {e}")

pages.sort(key=lambda x: (x["created"], str(x["path"])))

next_id = highest_id + 1

for page in pages:
    page_id = f"TSAP-{next_id:04d}"

    text = page["path"].read_text(encoding="utf-8")

    text = re.sub(
        r"^(created:\s*[0-9]{4}-[0-9]{2}-[0-9]{2}\s*)$",
        f"page_id: {page_id}\n\\1",
        text,
        count=1,
        flags=re.MULTILINE,
    )

    page["path"].write_text(text, encoding="utf-8")

    print(f"{page_id} -> {page['path']}")

    next_id += 1

print(f"\nHighest existing Page ID : TSAP-{highest_id:04d}")
print(f"Assigned new Page IDs    : {len(pages)}")
print(f"Next available Page ID   : TSAP-{next_id:04d}")