import re
import yaml
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(".")

IGNORE_DIRS = {
    ".git",
    "_site",
    ".jekyll-cache",
    "node_modules",
    "vendor",
    "sandbox",
}

SITEMAP_URL = "https://sunilabraham.in/sitemap.xml"

# ------------------------------------------------------------
# Load valid URLs from sitemap
# ------------------------------------------------------------

print("Downloading sitemap...")

response = requests.get(SITEMAP_URL, timeout=30)
response.raise_for_status()

root = ET.fromstring(response.text)

valid_urls = set()

for loc in root.findall(".//{*}loc"):
    url = loc.text.strip()

    parsed = urlparse(url)

    path = parsed.path

    if not path:
        path = "/"

    valid_urls.add(path)

    if path.endswith("/"):
        valid_urls.add(path.rstrip("/"))
    else:
        valid_urls.add(path + "/")

print(f"Loaded {len(valid_urls)} URLs from sitemap")

# ------------------------------------------------------------
# Find internal links
# ------------------------------------------------------------

markdown_link_pattern = re.compile(r"\]\((/[^)#?]+)")

broken_links = []

for file_path in ROOT.rglob("*.md"):

    if any(part in IGNORE_DIRS for part in file_path.parts):
        continue

    try:
        text = file_path.read_text(encoding="utf-8")
    except Exception:
        continue

    for target in markdown_link_pattern.findall(text):

        target = target.split("#")[0]
        target = target.split("?")[0]

        if target.endswith("/"):
            alt = target.rstrip("/")
        else:
            alt = target + "/"

        # File links
        if "." in Path(target).name:

            actual_file = ROOT / target.lstrip("/")

            if not actual_file.exists():
                broken_links.append(
                    {
                        "file": str(file_path),
                        "target": target,
                    }
                )

        # Page links
        else:

            if (
                target not in valid_urls
                and alt not in valid_urls
            ):
                broken_links.append(
                    {
                        "file": str(file_path),
                        "target": target,
                    }
                )

# ------------------------------------------------------------
# Remove duplicates
# ------------------------------------------------------------

seen = set()
clean_links = []

for item in broken_links:

    key = (item["file"], item["target"])

    if key not in seen:
        seen.add(key)
        clean_links.append(item)

# ------------------------------------------------------------
# Write YAML
# ------------------------------------------------------------

output = {
    "broken_links": clean_links
}

with open("_data/broken_links.yml", "w", encoding="utf-8") as f:
    yaml.dump(
        output,
        f,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    )

print(f"Found {len(clean_links)} broken links")
print("Generated _data/broken_links.yml")