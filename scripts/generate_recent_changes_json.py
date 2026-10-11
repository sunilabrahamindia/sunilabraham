#!/usr/bin/env python3
"""Generate a static recent-changes feed from the local Git history.

The feed keeps the newest 300 commits and lists at most 25 changed files per
commit. Commit classification is based on Git file statuses, not message
keywords. The workflow runs this script with the complete Git history.
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import PurePosixPath

REPOSITORY = "sunilabrahamindia/sunilabraham"
MAX_COMMITS = 300
MAX_FILES_PER_COMMIT = 25
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"

# Replace the placeholder email below if Sunil's commits use a known email.
# The email is used only for mapping in this generator; it is not written to
# recent-changes.json.
AUTHOR_MAP = {
    "sunilabrahamindia@gmail.com": {
        "login": "sunilabrahamindia",
        "name": "Tito (TSAP moderator)",
    },
    BOT_EMAIL: {
        "login": "github-actions[bot]",
        "name": "GitHub Actions (automated)",
    },
    "REPLACE_WITH_SUNIL_ABRAHAM_COMMIT_EMAIL": {
        "login": "sunilabrahamayrookhuziel",
        "name": "Sunil Abraham (Owner)",
    },
}


def git(*args):
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout


def parse_commits():
    output = git(
        "log",
        "-z",
        f"--max-count={MAX_COMMITS + 1}",
        "--format=%H%x1f%aI%x1f%an%x1f%ae%x1f%s%x1f%b",
    )
    commits = []
    for record in output.split("\0"):
        if not record.strip():
            continue
        fields = record.split("\x1f", 5)
        if len(fields) < 5:
            continue
        sha, date, author_name, author_email, subject = fields[:5]
        body = fields[5].strip() if len(fields) > 5 else ""
        commits.append({
            "sha": sha.strip(),
            "date": date.strip(),
            "raw_author_name": author_name.strip(),
            "raw_author_email": author_email.strip().lower(),
            "message": subject.strip(),
            "body": body,
        })
    return commits


def file_statuses(sha):
    output = git(
        "diff-tree", "--root", "--no-commit-id", "--name-status",
        "-r", "-M", sha,
    )
    files = []
    for line in output.splitlines():
        fields = line.split("\t")
        if len(fields) < 2:
            continue
        code = fields[0]
        if code.startswith("R") and len(fields) >= 3:
            status, previous, path = "renamed", fields[1], fields[2]
        elif code.startswith("C") and len(fields) >= 3:
            status, previous, path = "copied", fields[1], fields[2]
        else:
            status_code, path = code[:1], fields[-1]
            status = {"A": "added", "M": "modified", "D": "removed", "T": "modified"}.get(status_code, "modified")
            previous = None
        files.append({
            "path": path,
            "status": status,
            "previous_filename": previous,
            "additions": 0,
            "deletions": 0,
        })
    return files


def numstat_for_commit(sha):
    output = git("show", "--format=", "--numstat", "--find-renames", sha)
    totals = {"additions": 0, "deletions": 0}
    by_path = {}
    for line in output.splitlines():
        fields = line.split("\t", 2)
        if len(fields) != 3:
            continue
        try:
            additions = int(fields[0]) if fields[0] != "-" else 0
            deletions = int(fields[1]) if fields[1] != "-" else 0
        except ValueError:
            continue
        path = fields[2]
        by_path[path] = (additions, deletions)
        totals["additions"] += additions
        totals["deletions"] += deletions
    return totals, by_path


def mapped_author(author_name, author_email):
    mapping = AUTHOR_MAP.get(author_email.lower())
    if mapping:
        return mapping["login"], mapping["name"]
    return "", author_name or "Unknown"


def classify(author_login, author_name, author_email, message, files):
    if (
        author_login.endswith("[bot]")
        or author_email.lower() == BOT_EMAIL
        or "github actions" in author_name.lower()
        or message.lower().startswith("update pages index")
        or message.lower().startswith("update generated indexes")
    ):
        return "automated"
    statuses = [item["status"] for item in files]
    if statuses and all(status == "added" for status in statuses):
        return "created"
    if statuses and all(status == "removed" for status in statuses):
        return "removed"
    return "updated"


def build_commit(commit):
    sha = commit["sha"]
    author_login, author_name = mapped_author(
        commit["raw_author_name"], commit["raw_author_email"]
    )
    files = file_statuses(sha)
    stats, numstats = numstat_for_commit(sha)

    for item in files:
        candidates = [item["path"]]
        if item.get("previous_filename"):
            candidates.append(item["previous_filename"])
        for candidate in candidates:
            value = numstats.get(candidate)
            if value is None and " => " in candidate:
                value = numstats.get(candidate.split(" => ")[-1])
            if value is not None:
                item["additions"], item["deletions"] = value
                break

    kind = classify(
        author_login, author_name, commit["raw_author_email"],
        commit["message"], files,
    )
    return {
        "sha": sha,
        "url": f"https://github.com/{REPOSITORY}/commit/{sha}",
        "date": commit["date"],
        "author_login": author_login,
        "author_name": author_name,
        "message": commit["message"],
        "body": commit["body"],
        "type": kind,
        "automated": kind == "automated",
        "file_count": len(files),
        "files_truncated": len(files) > MAX_FILES_PER_COMMIT,
        "files": files[:MAX_FILES_PER_COMMIT],
        "stats": stats,
    }


def main():
    history = parse_commits()
    included = history[:MAX_COMMITS]
    total = int(git("rev-list", "--count", "HEAD").strip() or "0")
    commits = [build_commit(item) for item in included]
    feed = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": REPOSITORY,
        "included_commits": len(commits),
        "total_commits_in_repo": total,
        "history_truncated": total > len(commits),
        "oldest_included_date": commits[-1]["date"] if commits else None,
        "files_per_commit_limit": MAX_FILES_PER_COMMIT,
        "commits": commits,
    }
    with open("recent-changes.json", "w", encoding="utf-8") as handle:
        json.dump(feed, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(
        "Created recent-changes.json with "
        f"{len(commits)} commits ({total} commits in repository history)."
    )


if __name__ == "__main__":
    main()
