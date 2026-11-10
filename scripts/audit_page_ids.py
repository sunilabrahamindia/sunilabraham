#!/usr/bin/env python3
"""Read-only integrity audit for TSAP Page IDs."""

from collections import defaultdict
from pathlib import Path
import re
import sys
import yaml

PAGE_EXTENSIONS = {".md", ".markdown", ".svg"}
PAGE_ID_PATTERN = re.compile(r"TSAP-(\d{4,})")


def read_front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None

    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else None


eligible_pages = []
assigned = defaultdict(list)
missing = []
malformed = []
read_errors = []

for path in sorted(Path(".").rglob("*")):
    if not path.is_file() or path.suffix.lower() not in PAGE_EXTENSIONS:
        continue
    if ".git" in path.parts:
        continue

    try:
        metadata = read_front_matter(path)
        if not metadata or not metadata.get("created"):
            continue

        eligible_pages.append(path)
        raw_id = metadata.get("page_id")

        if raw_id is None or str(raw_id).strip() == "":
            missing.append(path)
            continue

        match = PAGE_ID_PATTERN.fullmatch(str(raw_id).strip())
        if not match:
            malformed.append((path, raw_id))
            continue

        number = int(match.group(1))
        assigned[number].append(path)

    except Exception as exc:
        read_errors.append((path, str(exc)))

duplicates = {
    number: paths for number, paths in assigned.items() if len(paths) > 1
}

highest_id = max(assigned, default=0)
gaps = [
    number for number in range(1, highest_id + 1)
    if number not in assigned
]

print("TSAP PAGE ID AUDIT")
print("==================")
print(f"Eligible pages       : {len(eligible_pages)}")
print(f"Pages with valid IDs : {sum(len(paths) for paths in assigned.values())}")
print(f"Pages without IDs    : {len(missing)}")
print(f"Malformed IDs        : {len(malformed)}")
print(f"Duplicate ID values  : {len(duplicates)}")
print(f"Missing sequence IDs : {len(gaps)}")
print(f"Highest valid ID     : TSAP-{highest_id:04d}")
print(f"Next available ID    : TSAP-{highest_id + 1:04d}")

if missing:
    print("\nPAGES WITHOUT IDs")
    for path in missing:
        print(f"  {path}")

if malformed:
    print("\nMALFORMED IDs")
    for path, value in malformed:
        print(f"  {path}: {value!r}")

if duplicates:
    print("\nDUPLICATE IDs")
    for number, paths in sorted(duplicates.items()):
        print(f"  TSAP-{number:04d}")
        for path in paths:
            print(f"    {path}")

if gaps:
    print("\nMISSING SEQUENCE IDs")
    print("  " + ", ".join(f"TSAP-{number:04d}" for number in gaps))

if read_errors:
    print("\nFILES THAT COULD NOT BE READ")
    for path, error in read_errors:
        print(f"  {path}: {error}")

if missing or malformed or duplicates or gaps or read_errors:
    print("\nAUDIT RESULT: ISSUES FOUND")
    sys.exit(1)

print("\nAUDIT RESULT: PASS")
