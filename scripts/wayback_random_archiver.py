#!/usr/bin/env python3
"""
wayback_random_archiver.py

Archive random pages from a Jekyll website (sunilabraham.in) into the
Internet Archive Wayback Machine, one page every 45 seconds, with a
persistent JSON log, graceful Ctrl+C handling and a Markdown report.

The repository at ~/Projects/sunilabraham is treated as strictly READ ONLY.
All runtime data (logs, reports, archive log) lives under
~/Documents/Reports/WaybackMachine/.

External dependencies: requests, PyYAML
"""

from __future__ import annotations

import json
import random
import re
import signal
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import requests
import yaml

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

REPO_ROOT = Path.home() / "Projects" / "sunilabraham"
SITE_BASE_URL = "https://sunilabraham.in"

# Candidate locations for the TSAP build's pages.json, checked in order.
PAGES_JSON_CANDIDATES: tuple[Path, ...] = (
    REPO_ROOT / "pages.json",
    REPO_ROOT / "_data" / "pages.json",
    REPO_ROOT / "assets" / "data" / "pages.json",
    REPO_ROOT / "_site" / "pages.json",
)

DATA_ROOT = Path.home() / "Documents" / "Reports" / "WaybackMachine"
LOGS_DIR = DATA_ROOT / "logs"
REPORTS_DIR = DATA_ROOT / "reports"
ARCHIVE_LOG_FILE = DATA_ROOT / "archive_log.json"

DELAY_SECONDS = 45
RATE_LIMIT_WAIT_SECONDS = 300  # 5 minutes back-off on HTTP 429
MAX_NETWORK_RETRIES = 3
NETWORK_RETRY_BACKOFF_SECONDS = 10
REQUEST_TIMEOUT_SECONDS = 60

WAYBACK_SAVE_URL_TEMPLATE = "https://web.archive.org/save/{url}"
FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

USER_AGENT = "wayback-random-archiver/1.0 (+https://sunilabraham.in)"

# Directories that must never be scanned, regardless of depth.
EXCLUDED_DIR_NAMES: frozenset[str] = frozenset(
    {
        ".git",
        ".github",
        ".venv",
        ".obsidian",
        "venv",
        "node_modules",
        "vendor",
        "_site",
        "Documents",
        "Downloads",
        "cache",
        ".cache",
        "__pycache__",
    }
)


# --------------------------------------------------------------------------
# Data structures
# --------------------------------------------------------------------------

@dataclass
class PageEntry:
    """A single archivable page, either from pages.json or derived from Markdown."""
    url: str
    source_path: Optional[Path] = None


@dataclass
class ArchiveSuccess:
    url: str
    snapshot_url: str
    timestamp: str
    http_status: int


@dataclass
class ArchiveFailure:
    url: str
    reason: str
    timestamp: str


@dataclass
class RunStats:
    """Aggregated statistics for the whole run, used to build the report."""
    start_time: datetime
    finish_time: Optional[datetime] = None
    attempted: int = 0
    successes: list[ArchiveSuccess] = field(default_factory=list)
    failures: list[ArchiveFailure] = field(default_factory=list)
    skipped: int = 0


# --------------------------------------------------------------------------
# Graceful shutdown handling
# --------------------------------------------------------------------------

class GracefulShutdown:
    """Tracks whether the user requested an interrupt (Ctrl+C / SIGTERM)."""

    def __init__(self) -> None:
        self.stop_requested = False
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def _handle_signal(self, signum: int, frame: Any) -> None:
        print("\nInterrupt received. Finishing current request, then exiting cleanly...")
        self.stop_requested = True


# --------------------------------------------------------------------------
# Directory setup (runtime data lives OUTSIDE the repository)
# --------------------------------------------------------------------------

def ensure_runtime_directories() -> None:
    """Create the runtime data directories under Documents if missing."""
    for directory in (DATA_ROOT, LOGS_DIR, REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE_LOG_FILE.exists():
        ARCHIVE_LOG_FILE.write_text(json.dumps({"entries": []}, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------
# Persistent archive log (previously archived URLs, with full detail)
# --------------------------------------------------------------------------

def load_archive_log() -> list[dict[str, Any]]:
    """Load the list of archive-log entries from the persistent JSON log."""
    try:
        raw = json.loads(ARCHIVE_LOG_FILE.read_text(encoding="utf-8"))
        entries = raw.get("entries", [])
        return entries if isinstance(entries, list) else []
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Warning: could not read archive log ({exc}). Starting with an empty log.")
        return []


def archived_url_set(entries: list[dict[str, Any]]) -> set[str]:
    """Extract the set of already-archived URLs from log entries."""
    return {entry["url"] for entry in entries if "url" in entry}


def save_archive_log(entries: list[dict[str, Any]]) -> None:
    """Persist the archive-log entries back to the JSON log file."""
    payload = {"entries": entries}
    ARCHIVE_LOG_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def append_success_to_log(
    entries: list[dict[str, Any]],
    success: ArchiveSuccess,
) -> None:
    """Append a successful archive record to the in-memory log entries."""
    entries.append(
        {
            "url": success.url,
            "snapshot_url": success.snapshot_url,
            "timestamp": success.timestamp,
            "http_status": success.http_status,
        }
    )


# --------------------------------------------------------------------------
# Source 1: pages.json (single source of truth, when available)
# --------------------------------------------------------------------------

def load_pages_from_json() -> Optional[list[PageEntry]]:
    """
    Attempt to load the list of page URLs from the TSAP build's pages.json.

    Returns None if no candidate file is found or none could be parsed,
    signalling the caller to fall back to Markdown scanning. This function
    only reads files, never writes to the repository.
    """
    for candidate in PAGES_JSON_CANDIDATES:
        if not candidate.exists():
            continue
        try:
            raw = json.loads(candidate.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: found {candidate} but could not parse it ({exc}). Trying next candidate.")
            continue

        urls = extract_urls_from_pages_json(raw)
        if urls:
            print(f"Using pages.json as the URL source:\n{candidate}\n")
            return [PageEntry(url=url) for url in urls]

    return None


def extract_urls_from_pages_json(raw: Any) -> list[str]:
    """
    Normalise the various shapes pages.json might take into a flat list
    of absolute URLs. Supports a bare list of strings, a list of objects
    with a 'url' or 'permalink' key, or a dict with a 'pages' key.
    """
    items: list[Any]
    if isinstance(raw, dict) and "pages" in raw:
        items = raw["pages"]
    elif isinstance(raw, list):
        items = raw
    else:
        return []

    urls: list[str] = []
    for item in items:
        if isinstance(item, str):
            candidate = item
        elif isinstance(item, dict):
            candidate = item.get("url") or item.get("permalink") or ""
        else:
            continue

        if not candidate:
            continue

        if candidate.startswith("http://") or candidate.startswith("https://"):
            urls.append(candidate)
        else:
            path_part = candidate if candidate.startswith("/") else f"/{candidate}"
            urls.append(SITE_BASE_URL.rstrip("/") + path_part)

    return urls


# --------------------------------------------------------------------------
# Source 2: Markdown scanning (fallback only)
# --------------------------------------------------------------------------

def is_excluded_directory(path: Path) -> bool:
    """Check whether any path component matches an excluded or hidden directory name."""
    for part in path.parts:
        if part in EXCLUDED_DIR_NAMES:
            return True
        if part.startswith(".") and part not in (".", ".."):
            return True
        if part.lower().endswith("backup") or part.lower().endswith("_bak"):
            return True
    return False


def extract_front_matter(md_text: str) -> Optional[dict[str, Any]]:
    """Extract and parse the YAML front matter block from a Markdown file."""
    match = FRONT_MATTER_PATTERN.match(md_text)
    if not match:
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def derive_default_permalink(relative_path: Path) -> str:
    """
    Recreate the default Jekyll permalink for a page when no explicit
    'permalink' front matter field is present.

    Default Jekyll behaviour for regular pages mirrors the file path,
    stripping the extension, and treats 'index.md' as the directory's
    own URL.
    """
    parts = list(relative_path.parts)
    stem = relative_path.stem

    if stem == "index":
        directory_parts = parts[:-1]
        url_path = "/".join(directory_parts)
    else:
        directory_parts = parts[:-1]
        url_path = "/".join(directory_parts + [stem])

    url_path = url_path.strip("/")
    return f"/{url_path}/" if url_path else "/"


def build_page_url(front_matter: dict[str, Any], relative_path: Path) -> str:
    """Build the absolute public URL for a page, honouring an explicit permalink."""
    explicit_permalink = front_matter.get("permalink")
    if explicit_permalink:
        path_part = str(explicit_permalink).strip()
        if not path_part.startswith("/"):
            path_part = "/" + path_part
        if not path_part.endswith("/") and "." not in Path(path_part).name:
            path_part += "/"
    else:
        path_part = derive_default_permalink(relative_path)

    return SITE_BASE_URL.rstrip("/") + path_part


def is_page_eligible(front_matter: dict[str, Any]) -> bool:
    """A page qualifies only if it has a 'created' field and is not unpublished."""
    if "created" not in front_matter:
        return False
    if front_matter.get("published", True) is False:
        return False
    return True


def scan_repository_for_pages(repo_root: Path) -> list[PageEntry]:
    """
    Recursively scan the repository for eligible .md files, skipping all
    excluded/hidden/backup/cache directories, and turn them into PageEntry
    objects. This function only reads files; it never writes anything.
    """
    pages: list[PageEntry] = []

    if not repo_root.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo_root}")

    for md_file in sorted(repo_root.rglob("*.md")):
        relative_path = md_file.relative_to(repo_root)

        if is_excluded_directory(relative_path.parent):
            continue

        try:
            text = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"Warning: skipping unreadable file {md_file}: {exc}")
            continue

        front_matter = extract_front_matter(text)
        if front_matter is None:
            continue
        if not is_page_eligible(front_matter):
            continue

        url = build_page_url(front_matter, relative_path)
        pages.append(PageEntry(url=url, source_path=md_file))

    return pages


def load_pages_with_fallback() -> list[PageEntry]:
    """Load pages from pages.json if possible, otherwise fall back to scanning Markdown."""
    pages_from_json = load_pages_from_json()
    if pages_from_json is not None:
        return pages_from_json

    print("pages.json unavailable or empty.")
    print("Falling back to Markdown scanning.\n")

    return scan_repository_for_pages(REPO_ROOT)


# --------------------------------------------------------------------------
# Wayback Machine archiving
# --------------------------------------------------------------------------

def archive_url(url: str, session: requests.Session) -> tuple[bool, int, str]:
    """
    Submit a single URL to the Wayback Machine 'save' endpoint without
    following redirects and without downloading the archived page body.

    Returns (success, http_status_code, snapshot_or_error_text).
    Raises requests.RequestException on network-level failures.
    """
    save_url = WAYBACK_SAVE_URL_TEMPLATE.format(url=url)
    response = session.get(
        save_url,
        headers={"User-Agent": USER_AGENT},
        timeout=REQUEST_TIMEOUT_SECONDS,
        allow_redirects=False,
        stream=True,
    )
    response.close()  # Discard body; we only need status and headers.

    status_code = response.status_code

    if status_code == 429:
        return False, status_code, "Rate limited by Wayback Machine (HTTP 429)"

    if status_code >= 400:
        return False, status_code, f"Wayback Machine returned HTTP {status_code}"

    # The snapshot location is exposed via Content-Location, or via
    # Location on a redirect response (since redirects are not followed).
    snapshot_path = response.headers.get("Content-Location") or response.headers.get("Location")
    if snapshot_path:
        if snapshot_path.startswith("http://") or snapshot_path.startswith("https://"):
            snapshot_url = snapshot_path
        else:
            snapshot_url = "https://web.archive.org" + snapshot_path
    else:
        snapshot_url = save_url

    return True, status_code, snapshot_url


def archive_with_retries(
    url: str,
    session: requests.Session,
    shutdown: GracefulShutdown,
) -> tuple[bool, int, str]:
    """
    Wrap archive_url with retry logic for HTTP 429 (long back-off, retries
    indefinitely) and transient network errors (short back-off, 3 retries).
    """
    network_attempts = 0

    while True:
        if shutdown.stop_requested:
            return False, 0, "Aborted before completion due to user interrupt"

        try:
            success, status_code, message = archive_url(url, session)
        except requests.RequestException as exc:
            network_attempts += 1
            if network_attempts > MAX_NETWORK_RETRIES:
                return False, 0, f"Network error after {MAX_NETWORK_RETRIES} retries: {exc}"
            print(
                f"Network error ({exc}). Retrying in {NETWORK_RETRY_BACKOFF_SECONDS}s "
                f"(attempt {network_attempts}/{MAX_NETWORK_RETRIES})..."
            )
            countdown_sleep(NETWORK_RETRY_BACKOFF_SECONDS, shutdown)
            continue

        if not success and status_code == 429:
            print(
                f"Rate limited (HTTP 429). Waiting {RATE_LIMIT_WAIT_SECONDS // 60} "
                "minutes before retrying (indefinitely, until success or interrupt)..."
            )
            countdown_sleep(RATE_LIMIT_WAIT_SECONDS, shutdown)
            if shutdown.stop_requested:
                return False, status_code, message
            continue

        return success, status_code, message


# --------------------------------------------------------------------------
# Progress display and countdown
# --------------------------------------------------------------------------

def countdown_sleep(total_seconds: int, shutdown: GracefulShutdown) -> None:
    """Sleep for total_seconds, printing a live countdown, abortable via Ctrl+C."""
    remaining = total_seconds
    while remaining > 0 and not shutdown.stop_requested:
        print(f"  Waiting {remaining:>4}s until next request...", end="\r", flush=True)
        time.sleep(1)
        remaining -= 1
    print(" " * 50, end="\r")


def print_progress(
    index: int,
    total: int,
    url: str,
    status_code: int,
    snapshot_url: str,
) -> None:
    """Print a single block of progress info for one archived page."""
    print(f"[{index}/{total}] {url}")
    print(f"    HTTP status : {status_code}")
    print(f"    Snapshot    : {snapshot_url}")


# --------------------------------------------------------------------------
# Report generation
# --------------------------------------------------------------------------

def write_report(stats: RunStats, report_path: Path) -> Path:
    """Generate the Markdown report summarising the run and save it to disk."""
    finish_time = stats.finish_time or datetime.now(timezone.utc)
    elapsed = finish_time - stats.start_time

    lines: list[str] = []
    lines.append("# Wayback Random Archiver Report")
    lines.append("")
    lines.append(f"- Start time: {stats.start_time.isoformat()}")
    lines.append(f"- Finish time: {finish_time.isoformat()}")
    lines.append(f"- Elapsed time: {elapsed}")
    lines.append(f"- Attempted: {stats.attempted}")
    lines.append(f"- Successful: {len(stats.successes)}")
    lines.append(f"- Failed: {len(stats.failures)}")
    lines.append(f"- Skipped (already archived): {stats.skipped}")
    lines.append("")

    if stats.successes:
        lines.append("## Successful archives")
        lines.append("")
        lines.append("| Original URL | Snapshot URL | Timestamp | HTTP Status |")
        lines.append("|---|---|---|---|")
        for item in stats.successes:
            lines.append(f"| {item.url} | {item.snapshot_url} | {item.timestamp} | {item.http_status} |")
        lines.append("")

    if stats.failures:
        lines.append("## Failures")
        lines.append("")
        lines.append("| Original URL | Reason | Timestamp |")
        lines.append("|---|---|---|")
        for item in stats.failures:
            lines.append(f"| {item.url} | {item.reason} | {item.timestamp} |")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def build_report_filename() -> str:
    """Build the report filename in the required wayback-report-YYYY-MM-DD-HHMMSS.md format."""
    now = datetime.now()
    return f"wayback-report-{now.strftime('%Y-%m-%d-%H%M%S')}.md"


# --------------------------------------------------------------------------
# Main orchestration
# --------------------------------------------------------------------------

def run() -> None:
    ensure_runtime_directories()
    log_entries = load_archive_log()
    archived_urls = archived_url_set(log_entries)
    shutdown = GracefulShutdown()

    session_timestamp_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_log_path = LOGS_DIR / f"session_{session_timestamp_tag}.log"
    report_path = REPORTS_DIR / build_report_filename()

    def log_line(text: str) -> None:
        print(text)
        with session_log_path.open("a", encoding="utf-8") as handle:
            handle.write(text + "\n")

    all_pages = load_pages_with_fallback()
    log_line(f"Discovered {len(all_pages)} candidate page(s).")

    pending_pages = [p for p in all_pages if p.url not in archived_urls]
    already_skipped = len(all_pages) - len(pending_pages)

    pending_pages = list({p.url: p for p in pending_pages}.values())

    random.shuffle(pending_pages)

    stats = RunStats(start_time=datetime.now(timezone.utc))
    stats.skipped = already_skipped

    total = len(pending_pages)
    if total == 0:
        log_line("Nothing new to archive. All eligible pages were already archived.")

    with requests.Session() as session:
        for index, page in enumerate(pending_pages, start=1):
            if shutdown.stop_requested:
                log_line("Stopping before next request due to user interrupt.")
                break

            stats.attempted += 1
            log_line(f"[{index}/{total}] Archiving: {page.url}")

            success, status_code, message = archive_with_retries(page.url, session, shutdown)
            now_iso = datetime.now(timezone.utc).isoformat()

            if success:
                print_progress(index, total, page.url, status_code, message)
                success_record = ArchiveSuccess(
                    url=page.url,
                    snapshot_url=message,
                    timestamp=now_iso,
                    http_status=status_code,
                )
                stats.successes.append(success_record)
                append_success_to_log(log_entries, success_record)
                archived_urls.add(page.url)
                save_archive_log(log_entries)  # Persist immediately after every success.
                log_line(f"    Success -> {message}")
            else:
                log_line(f"    Failed  -> HTTP {status_code}: {message}")
                stats.failures.append(ArchiveFailure(url=page.url, reason=message, timestamp=now_iso))

            if shutdown.stop_requested:
                log_line("Interrupt detected after completing current request. Exiting.")
                break

            if index < total:
                countdown_sleep(DELAY_SECONDS, shutdown)

    stats.finish_time = datetime.now(timezone.utc)
    write_report(stats, report_path)
    save_archive_log(log_entries)  # Final save, guaranteed even if loop exited early.
    log_line(f"Report written to: {report_path}")
    log_line(f"Archive log saved to: {ARCHIVE_LOG_FILE}")


if __name__ == "__main__":
    try:
        run()
    except FileNotFoundError as exc:
        print(f"Fatal error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001 - top-level safety net, never crash silently
        print(f"Unexpected fatal error: {exc}", file=sys.stderr)
        sys.exit(1)