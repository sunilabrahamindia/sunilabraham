from pathlib import Path
import re
from datetime import datetime

pages = []

for md_file in Path(".").rglob("*.md"):
    try:
        text = md_file.read_text(encoding="utf-8")

        if not text.startswith("---"):
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            continue

        yaml_text = parts[1]

        if re.search(r"^page_id:\s*", yaml_text, re.MULTILINE):
            continue

        match = re.search(
            r"^created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*$",
            yaml_text,
            re.MULTILINE
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

for i, page in enumerate(pages, start=1):
    page_id = f"TSAP-{i:04d}"

    text = page["path"].read_text(encoding="utf-8")

    text = re.sub(
        r"^(created:\s*[0-9]{4}-[0-9]{2}-[0-9]{2}\s*)$",
        f"page_id: {page_id}\n\\1",
        text,
        count=1,
        flags=re.MULTILINE
    )

    page["path"].write_text(text, encoding="utf-8")

    print(f"{page_id} -> {page['path']}")

print(f"\nUpdated {len(pages)} files.")