import os
import json
import yaml

SITE_URL = "https://sunilabraham.in"

pages = []

for root, dirs, files in os.walk("."):
    if ".git" in root:
        continue

    for file in files:
        if not file.endswith((".md", ".markdown")):
            continue

        path = os.path.join(root, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.startswith("---"):
                continue

            parts = content.split("---", 2)

            if len(parts) < 3:
                continue

            front_matter = yaml.safe_load(parts[1])

            if not isinstance(front_matter, dict):
                continue

            title = front_matter.get("title")
            description = front_matter.get("description")
            created = front_matter.get("created")
            date = front_matter.get("date")
            source = front_matter.get("source")
            authors = front_matter.get("authors")
            categories = front_matter.get("categories")

            permalink = front_matter.get("permalink")

            if permalink:
                permalink = SITE_URL.rstrip("/") + permalink
            else:
                permalink = None

            page = {
                "title": title,
                "description": description,
                "created": str(created) if created else None,
                "date": str(date) if date else None,
                "source": source,
                "authors": authors,
                "categories": categories,
                "permalink": permalink
            }

            pages.append(page)

        except Exception as e:
            print("Skipping:", path, e)

pages.sort(
    key=lambda x: x.get("created") or "",
    reverse=True
)

with open("pages.json", "w", encoding="utf-8") as f:
    json.dump(
        pages,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Created pages.json with {len(pages)} pages.")