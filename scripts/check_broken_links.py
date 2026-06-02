import re
import yaml
from pathlib import Path

ROOT = Path(".")

# Directories to ignore
IGNORE_DIRS = {
    ".git",
    "_site",
    "node_modules",
    ".jekyll-cache",
    "vendor",
}

# ------------------------------------------------------------------
# Build list of valid URLs from front matter permalinks
# ------------------------------------------------------------------

valid_urls = set()

for md_file in ROOT.rglob("*.md"):
    if any(part in IGNORE_DIRS for part in md_file.parts):
        continue

    try:
        text = md_file.read_text(encoding="utf-8")
    except Exception:
        continue

    permalink_match = re.search(
        r"^permalink:\s*['\"]?([^'\"]+)['\"]?",
        text,
        re.MULTILINE,
    )

    if permalink_match:
        valid_urls.add(permalink_match.group(1).strip())

# ------------------------------------------------------------------
# Find internal links
# ------------------------------------------------------------------

broken_links = []

markdown_link_pattern = re.compile(r"\]\((/[^)#]+)\)")

for md_file in ROOT.rglob("*.md"):
    if any(part in IGNORE_DIRS for part in md_file.parts):
        continue

    try:
        text = md_file.read_text(encoding="utf-8")
    except Exception:
        continue

    for target in markdown_link_pattern.findall(text):

        # Ignore anchors
        target = target.split("#")[0]

        # Asset/file link
        if "." in Path(target).name:
            actual_file = ROOT / target.lstrip("/")

            if not actual_file.exists():
                broken_links.append(
                    {
                        "file": str(md_file),
                        "target": target,
                    }
                )

        # Page link
        else:
            if target not in valid_urls:
                broken_links.append(
                    {
                        "file": str(md_file),
                        "target": target,
                    }
                )

# ------------------------------------------------------------------
# Write report
# ------------------------------------------------------------------

output = {
    "broken_links": broken_links
}

with open("_data/broken_links.yml", "w", encoding="utf-8") as f:
    yaml.dump(
        output,
        f,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    )

print(f"Found {len(broken_links)} broken links")
print("Generated _data/broken_links.yml")