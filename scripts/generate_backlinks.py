import os
import re
import yaml

BACKLINKS = {}

ROOT_DIRS = [
    "ai",
    "amaa",
    "articles",
    "cis",
    "clusters",
    "events",
    "ideas-and-opinions",
    "projects",
    "publications",
    "resources",
    "sunil",
    "tsap",
    "videos"
]

LINK_PATTERN = re.compile(r'\((/[^)#?]+/?)(?:[#?][^)]+)?\)')

def get_permalink(content, filepath, root_dir):
    match = re.search(r'permalink:\s*([^\n]+)', content)
    if match:
        permalink = match.group(1).strip()
        if not permalink.endswith('/'):
            permalink += '/'
        return permalink

    relative = os.path.relpath(filepath, root_dir)
    relative = os.path.splitext(relative)[0]
    return "/" + relative.replace("\\", "/") + "/"

for root_dir in ROOT_DIRS:
    if not os.path.exists(root_dir):
        continue

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.endswith((".md", ".markdown")):
                continue

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            if "exclude_from_backlinks: true" in content:
                continue

            source_url = get_permalink(content, filepath, root_dir)

            matches = LINK_PATTERN.findall(content)

            for target_url in matches:
                if not target_url.startswith("/"):
                    continue

                if target_url == source_url:
                    continue

                BACKLINKS.setdefault(target_url, [])

                if source_url not in BACKLINKS[target_url]:
                    BACKLINKS[target_url].append(source_url)

with open("_data/backlinks.yml", "w", encoding="utf-8") as f:
    yaml.dump(BACKLINKS, f, allow_unicode=True, sort_keys=True)

print("Backlinks generated successfully.")
