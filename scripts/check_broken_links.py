import re
import yaml
from pathlib import Path

ROOT = Path(".")

IGNORE_DIRS = {
    ".git",
    "_site",
    ".jekyll-cache",
    "node_modules",
    "vendor",
    "sandbox",
}

# ------------------------------------------------------------
# Build list of valid URLs
# ------------------------------------------------------------

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
        url = permalink_match.group(1).strip()

        valid_urls.add(url)

        if url.endswith("/"):
            valid_urls.add(url.rstrip("/"))
        else:
            valid_urls.add(url + "/")

    else:
        rel = md_file.relative_to(ROOT)

        if rel.name == "index.md":
            url = "/" + str(rel.parent).replace("\\", "/") + "/"
        else:
            url = "/" + str(rel.with_suffix("")).replace("\\", "/") + "/"

        url = re.sub(r"/+", "/", url)

        valid_urls.add(url)

        if url.endswith("/"):
            valid_urls.add(url.rstrip("/"))
        else:
            valid_urls.add(url + "/")

# ------------------------------------------------------------
# Find internal links
# ------------------------------------------------------------

markdown_link_pattern = re.compile(r"\]\((/[^)#?]+)")

broken_links = []

for md_file in ROOT.rglob("*.md"):
    if any(part in IGNORE_DIRS for part in md_file.parts):
        continue

    try:
        text = md_file.read_text(encoding="utf-8")
    except Exception:
        continue

    for target in markdown_link_pattern.findall(text):

        target = target.split("#")[0]
        target = target.split("?")[0]

        if target.endswith("/"):
            target_alt = target.rstrip("/")
        else:
            target_alt = target + "/"

        # Asset/file links
        if "." in Path(target).name:
            actual_file = ROOT / target.lstrip("/")

            if not actual_file.exists():
                broken_links.append(
                    {
                        "file": str(md_file),
                        "target": target,
                    }
                )

        # Page links
        else:
            if (
                target not in valid_urls
                and target_alt not in valid_urls
            ):
                broken_links.append(
                    {
                        "file": str(md_file),
                        "target": target,
                    }
                )

# ------------------------------------------------------------
# Remove duplicates
# ------------------------------------------------------------

seen = set()
unique_broken_links = []

for item in broken_links:
    key = (item["file"], item["target"])

    if key not in seen:
        seen.add(key)
        unique_broken_links.append(item)

# ------------------------------------------------------------
# Write YAML
# ------------------------------------------------------------

output = {
    "broken_links": unique_broken_links
}

with open("_data/broken_links.yml", "w", encoding="utf-8") as f:
    yaml.dump(
        output,
        f,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    )

print(f"Found {len(unique_broken_links)} broken links")
print("Generated _data/broken_links.yml")