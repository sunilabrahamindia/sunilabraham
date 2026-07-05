#!/usr/bin/env python3
"""
indexnow_submitter.py

Notify IndexNow-participating search engines (Bing, Yandex, Seznam, Naver,
Yep, Amazon) about newly created, updated, or deleted pages on a Jekyll
website (sunilabraham.in), using change detection against a persistent
JSON log rather than random continuous resubmission.

The repository at ~/Projects/sunilabraham is treated as strictly READ ONLY.
All runtime data (logs, reports, submission log) lives under
~/Documents/Reports/IndexNow/.

Design notes (per IndexNow.org documentation):
  - Submissions are batched (up to 10,000 URLs per POST) rather than sent
    one URL per request, since IndexNow explicitly supports bulk submission.
  - Only URLs whose content hash or 'created'/'updated' front matter has
    changed since the last successful submission are queued. Repeatedly
    resubmitting unchanged URLs is discouraged by the protocol and can
    trigger HTTP 422/429 responses.
  - A minimum resubmission interval (5 minutes per the IndexNow FAQ) is
    enforced per URL to avoid spamming.
  - Deleted/removed pages (no longer found on disk or in pages.json) are
    queued separately and submitted so engines can drop them from the index.

External dependencies: requests, PyYAML
"""

from __future__ import annotations

import hashlib
import json
import re
import signal
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import requests
import yaml

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

REPO_ROOT = Path.home() / "Projects" / "sunilabraham"
SITE_HOST = "sunilabraham.in"
SITE_BASE_URL = f"https://{SITE_HOST}"

# Candidate locations for the TSAP build's pages.json, checked in order.
PAGES_JSON_CANDIDATES: tuple[Path, ...] = (
    REPO_ROOT / "pages.json",
    REPO_ROOT / "_data" / "pages.json",
    REPO_ROOT / "assets" / "data" / "pages.json",
    REPO_ROOT / "_site" / "pages.json",
)

# IndexNow key and its public location. The key file itself must already
# be hosted on the live site; this script never writes to the repository.
INDEXNOW_KEY = "6a9765e94ad555b1012ea8ffc66fce4f"
INDEXNOW_KEY_LOCATION = f"{SITE_BASE_URL}/{INDEXNOW_KEY}.txt"

# The global endpoint fans submissions out to all participating engines
# (Bing, Yandex, Seznam, Naver, Yep, Amazon), per IndexNow.org documentation.
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

DATA_ROOT = Path.home() / "Documents" / "Reports" / "IndexNow"
LOGS_DIR = DATA_ROOT / "logs"
REPORTS_DIR = DATA_ROOT / "reports"
SUBMISSION_LOG_FILE = DATA_ROOT / "submission_log.json"

MAX_URLS_PER_BATCH = 10_000  # Documented IndexNow limit per POST request.
MIN_RESUBMIT_INTERVAL = timedelta(minutes=5)  # Documented minimum per IndexNow FAQ.
RATE_LIMIT_WAIT_SECONDS = 300  # 5 minutes back-off on HTTP 429.
MAX_NETWORK_RETRIES = 3
NETWORK_RETRY_BACKOFF_SECONDS = 10
REQUEST_TIMEOUT_SECONDS = 60

FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
USER_AGENT = "indexnow-submitter/1.0 (+https://sunilabraham.in)"

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
    """A single page discovered from pages.json or Markdown scanning."""
    url: str
    content_hash: str
    source_path: Optional[Path] = None


@dataclass
class SubmissionOutcome:
    urls: list[str]
    http_status: int
    timestamp: str
    action: str  # "add_or_update" or "delete"


@dataclass
class SubmissionFailure:
    urls: list[str]
    reason: str
    timestamp: str


@dataclass
class RunStats:
    start_time: datetime
    finish_time: Optional[datetime] = None
    attempted_urls: int = 0
    successes: list[SubmissionOutcome] = field(default_factory=list)
    failures: list[SubmissionFailure] = field(default_factory=list)
    skipped_unchanged: int = 0
    deleted_detected: int = 0


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
        print("\nInterrupt received. Finishing current batch, then exiting cleanly...")
        self.stop_requested = True


# --------------------------------------------------------------------------
# Directory setup (runtime data lives OUTSIDE the repository)
# --------------------------------------------------------------------------

def ensure_runtime_directories() -> None:
    """Create the runtime data directories under Documents if missing."""
    for directory in (DATA_ROOT, LOGS_DIR, REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    if not SUBMISSION_LOG_FILE.exists():
        SUBMISSION_LOG_FILE.write_text(json.dumps({"entries": {}}, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------
# Persistent submission log: url -> {content_hash, last_submitted, status}
# --------------------------------------------------------------------------

def load_submission_log() -> dict[str, dict[str, Any]]:
    """Load the persistent per-URL submission log."""
    try:
        raw = json.loads(SUBMISSION_LOG_FILE.read_text(encoding="utf-8"))
        entries = raw.get("entries", {})
        return entries if isinstance(entries, dict) else {}
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Warning: could not read submission log ({exc}). Starting with an empty log.")
        return {}


def save_submission_log(entries: dict[str, dict[str, Any]]) -> None:
    """Persist the per-URL submission log back to disk."""
    payload = {"entries": entries}
    SUBMISSION_LOG_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def was_recently_submitted(entries: dict[str, dict[str, Any]], url: str) -> bool:
    """Check whether a URL was submitted within the minimum resubmit interval."""
    record = entries.get(url)
    if not record or "last_submitted" not in record:
        return False
    last_submitted = datetime.fromisoformat(record["last_submitted"])
    return datetime.now(timezone.utc) - last_submitted < MIN_RESUBMIT_INTERVAL


def content_unchanged(entries: dict[str, dict[str, Any]], url: str, content_hash: str) -> bool:
    """Check whether a URL's content hash matches what was last submitted."""
    record = entries.get(url)
    return bool(record) and record.get("content_hash") == content_hash


def record_submission(
    entries: dict[str, dict[str, Any]],
    url: str,
    content_hash: str,
    timestamp: str,
    action: str,
) -> None:
    """Update the in-memory log entry for a URL after a successful submission."""
    entries[url] = {
        "content_hash": content_hash,
        "last_submitted": timestamp,
        "last_action": action,
    }


# --------------------------------------------------------------------------
# Source 1: pages.json (single source of truth, when available)
# --------------------------------------------------------------------------

def load_pages_from_json() -> Optional[list[PageEntry]]:
    """
    Attempt to load pages from the TSAP build's pages.json, computing a
    stable content hash per entry so changes can be detected on later runs.
    Returns None if unavailable, signalling fallback to Markdown scanning.
    """
    for candidate in PAGES_JSON_CANDIDATES:
        if not candidate.exists():
            continue
        try:
            raw_text = candidate.read_text(encoding="utf-8")
            raw = json.loads(raw_text)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: found {candidate} but could not parse it ({exc}). Trying next candidate.")
            continue

        pages = extract_pages_from_json(raw)
        if pages:
            print(f"Using pages.json as the URL source:\n{candidate}\n")
            return pages

    return None


def extract_pages_from_json(raw: Any) -> list[PageEntry]:
    """
    Normalise pages.json into PageEntry objects. Each entry's content hash
    is derived from its own JSON representation, so any field change
    (title, updated date, body summary, etc.) is detected as a change.
    """
    items: list[Any]
    if isinstance(raw, dict) and "pages" in raw:
        items = raw["pages"]
    elif isinstance(raw, list):
        items = raw
    else:
        return []

    pages: list[PageEntry] = []
    for item in items:
        if isinstance(item, str):
            candidate = item
            hash_source = item
        elif isinstance(item, dict):
            candidate = item.get("url") or item.get("permalink") or ""
            hash_source = json.dumps(item, sort_keys=True)
        else:
            continue

        if not candidate:
            continue

        if candidate.startswith("http://") or candidate.startswith("https://"):
            url = candidate
        else:
            path_part = candidate if candidate.startswith("/") else f"/{candidate}"
            url = SITE_BASE_URL.rstrip("/") + path_part

        content_hash = hashlib.sha256(hash_source.encode("utf-8")).hexdigest()
        pages.append(PageEntry(url=url, content_hash=content_hash))

    return pages


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
    """Recreate the default Jekyll permalink when no explicit 'permalink' is set."""
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
    excluded/hidden/backup/cache directories. The content hash is derived
    from the file's full text, so any edit is detected as a change.
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
        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        pages.append(PageEntry(url=url, content_hash=content_hash, source_path=md_file))

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
# Change detection
# --------------------------------------------------------------------------

def classify_pages(
    current_pages: list[PageEntry],
    log_entries: dict[str, dict[str, Any]],
) -> tuple[list[PageEntry], list[str], int]:
    """
    Split current pages into those that need submission (new or changed)
    and detect URLs that vanished (previously logged, no longer present),
    which are treated as deletions. Returns (to_submit, deleted_urls, skipped_count).
    """
    current_urls = {p.url for p in current_pages}
    to_submit: list[PageEntry] = []
    skipped = 0

    for page in current_pages:
        if content_unchanged(log_entries, page.url, page.content_hash):
            skipped += 1
            continue
        if was_recently_submitted(log_entries, page.url):
            skipped += 1
            continue
        to_submit.append(page)

    deleted_urls = [
        url for url in log_entries
        if url not in current_urls and log_entries[url].get("last_action") != "delete"
    ]

    return to_submit, deleted_urls, skipped


# --------------------------------------------------------------------------
# IndexNow submission
# --------------------------------------------------------------------------

def submit_batch(
    urls: list[str],
    session: requests.Session,
) -> tuple[bool, int, str]:
    """
    Submit a batch of up to MAX_URLS_PER_BATCH URLs to the IndexNow global
    endpoint via a single JSON POST request.

    Returns (success, http_status_code, message). Raises requests.RequestException
    on network-level failures so the caller can apply its own retry policy.
    """
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": urls,
    }

    response = session.post(
        INDEXNOW_ENDPOINT,
        json=payload,
        headers={"User-Agent": USER_AGENT, "Content-Type": "application/json; charset=utf-8"},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    status_code = response.status_code

    if status_code == 429:
        return False, status_code, "Rate limited by IndexNow (HTTP 429)"
    if status_code == 403:
        return False, status_code, "Key not valid or key file not found (HTTP 403)"
    if status_code == 422:
        return False, status_code, "URLs do not belong to host or key mismatch (HTTP 422)"
    if status_code == 400:
        return False, status_code, "Bad request: invalid format (HTTP 400)"
    if status_code >= 400:
        return False, status_code, f"IndexNow returned HTTP {status_code}"

    # 200 = accepted immediately, 202 = accepted, key validation pending.
    return True, status_code, "Batch accepted by IndexNow"


def submit_with_retries(
    urls: list[str],
    session: requests.Session,
    shutdown: GracefulShutdown,
) -> tuple[bool, int, str]:
    """
    Wrap submit_batch with retry logic for HTTP 429 (long back-off, retries
    indefinitely) and transient network errors (short back-off, 3 retries).
    """
    network_attempts = 0

    while True:
        if shutdown.stop_requested:
            return False, 0, "Aborted before completion due to user interrupt"

        try:
            success, status_code, message = submit_batch(urls, session)
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


def chunk_urls(urls: list[str], size: int) -> list[list[str]]:
    """Split a list of URLs into batches no larger than the documented limit."""
    return [urls[i:i + size] for i in range(0, len(urls), size)]


# --------------------------------------------------------------------------
# Progress display and countdown
# --------------------------------------------------------------------------

def countdown_sleep(total_seconds: int, shutdown: GracefulShutdown) -> None:
    """Sleep for total_seconds, printing a live countdown, abortable via Ctrl+C."""
    remaining = total_seconds
    while remaining > 0 and not shutdown.stop_requested:
        print(f"  Waiting {remaining:>4}s before next action...", end="\r", flush=True)
        time.sleep(1)
        remaining -= 1
    print(" " * 50, end="\r")


def print_batch_progress(
    batch_index: int,
    total_batches: int,
    batch_size: int,
    status_code: int,
    action: str,
) -> None:
    """Print a single block of progress info for one submitted batch."""
    print(f"[batch {batch_index}/{total_batches}] {action} : {batch_size} URL(s)")
    print(f"    HTTP status : {status_code}")


# --------------------------------------------------------------------------
# Report generation
# --------------------------------------------------------------------------

def write_report(stats: RunStats, report_path: Path) -> Path:
    """Generate the Markdown report summarising the run and save it to disk."""
    finish_time = stats.finish_time or datetime.now(timezone.utc)
    elapsed = finish_time - stats.start_time

    lines: list[str] = []
    lines.append("# IndexNow Submission Report")
    lines.append("")
    lines.append(f"- Start time: {stats.start_time.isoformat()}")
    lines.append(f"- Finish time: {finish_time.isoformat()}")
    lines.append(f"- Elapsed time: {elapsed}")
    lines.append(f"- Attempted URLs: {stats.attempted_urls}")
    lines.append(f"- Successful batches: {len(stats.successes)}")
    lines.append(f"- Failed batches: {len(stats.failures)}")
    lines.append(f"- Skipped (unchanged or recently submitted): {stats.skipped_unchanged}")
    lines.append(f"- Deletions detected and submitted: {stats.deleted_detected}")
    lines.append("")

    if stats.successes:
        lines.append("## Successful submissions")
        lines.append("")
        lines.append("| Action | URLs in batch | Timestamp | HTTP Status |")
        lines.append("|---|---|---|---|")
        for item in stats.successes:
            url_preview = ", ".join(item.urls[:3])
            if len(item.urls) > 3:
                url_preview += f", … (+{len(item.urls) - 3} more)"
            lines.append(f"| {item.action} | {url_preview} | {item.timestamp} | {item.http_status} |")
        lines.append("")

    if stats.failures:
        lines.append("## Failures")
        lines.append("")
        lines.append("| URLs in batch | Reason | Timestamp |")
        lines.append("|---|---|---|")
        for item in stats.failures:
            url_preview = ", ".join(item.urls[:3])
            if len(item.urls) > 3:
                url_preview += f", … (+{len(item.urls) - 3} more)"
            lines.append(f"| {url_preview} | {item.reason} | {item.timestamp} |")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def build_report_filename() -> str:
    """Build the report filename in indexnow-report-YYYY-MM-DD-HHMMSS.md format."""
    now = datetime.now()
    return f"indexnow-report-{now.strftime('%Y-%m-%d-%H%M%S')}.md"


# --------------------------------------------------------------------------
# Key file health check (documented best practice)
# --------------------------------------------------------------------------

def verify_key_file(session: requests.Session) -> bool:
    """
    Confirm the hosted key file returns exactly the configured key, since
    a broken key file silently causes all IndexNow submissions to fail
    ownership verification (HTTP 403). This only performs a GET request
    against the live site; it never touches the local repository.
    """
    try:
        response = session.get(INDEXNOW_KEY_LOCATION, timeout=REQUEST_TIMEOUT_SECONDS)
    except requests.RequestException as exc:
        print(f"Warning: could not verify key file ({exc}). Proceeding anyway.")
        return False

    if response.status_code != 200:
        print(f"Warning: key file returned HTTP {response.status_code} at {INDEXNOW_KEY_LOCATION}.")
        return False

    body = response.text.strip()
    if body != INDEXNOW_KEY:
        print("Warning: key file content does not match the configured INDEXNOW_KEY.")
        return False

    print("Key file verified successfully.")
    return True


# --------------------------------------------------------------------------
# Main orchestration
# --------------------------------------------------------------------------

def run() -> None:
    ensure_runtime_directories()
    log_entries = load_submission_log()
    shutdown = GracefulShutdown()

    session_timestamp_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_log_path = LOGS_DIR / f"session_{session_timestamp_tag}.log"
    report_path = REPORTS_DIR / build_report_filename()

    def log_line(text: str) -> None:
        print(text)
        with session_log_path.open("a", encoding="utf-8") as handle:
            handle.write(text + "\n")

    stats = RunStats(start_time=datetime.now(timezone.utc))

    with requests.Session() as session:
        verify_key_file(session)

        current_pages = load_pages_with_fallback()
        log_line(f"Discovered {len(current_pages)} candidate page(s).")

        current_pages = list({p.url: p for p in current_pages}.values())
        to_submit, deleted_urls, skipped = classify_pages(current_pages, log_entries)
        stats.skipped_unchanged = skipped

        log_line(f"New or changed pages to submit: {len(to_submit)}")
        log_line(f"Deleted/removed pages detected: {len(deleted_urls)}")

        add_or_update_urls = [p.url for p in to_submit]
        batches = chunk_urls(add_or_update_urls, MAX_URLS_PER_BATCH)
        delete_batches = chunk_urls(deleted_urls, MAX_URLS_PER_BATCH)

        total_batches = len(batches) + len(delete_batches)
        batch_counter = 0

        for batch in batches:
            if shutdown.stop_requested:
                log_line("Stopping before next batch due to user interrupt.")
                break

            batch_counter += 1
            stats.attempted_urls += len(batch)
            log_line(f"[batch {batch_counter}/{total_batches}] Submitting {len(batch)} add/update URL(s).")

            success, status_code, message = submit_with_retries(batch, session, shutdown)
            now_iso = datetime.now(timezone.utc).isoformat()

            if success:
                print_batch_progress(batch_counter, total_batches, len(batch), status_code, "add_or_update")
                stats.successes.append(
                    SubmissionOutcome(urls=batch, http_status=status_code, timestamp=now_iso, action="add_or_update")
                )
                page_by_url = {p.url: p for p in to_submit}
                for url in batch:
                    page = page_by_url[url]
                    record_submission(log_entries, url, page.content_hash, now_iso, "add_or_update")
                save_submission_log(log_entries)
                log_line(f"    Success -> {message}")
            else:
                log_line(f"    Failed  -> HTTP {status_code}: {message}")
                stats.failures.append(SubmissionFailure(urls=batch, reason=message, timestamp=now_iso))

            if shutdown.stop_requested:
                break

        if not shutdown.stop_requested:
            for batch in delete_batches:
                if shutdown.stop_requested:
                    log_line("Stopping before next batch due to user interrupt.")
                    break

                batch_counter += 1
                stats.attempted_urls += len(batch)
                log_line(f"[batch {batch_counter}/{total_batches}] Submitting {len(batch)} deleted URL(s).")

                success, status_code, message = submit_with_retries(batch, session, shutdown)
                now_iso = datetime.now(timezone.utc).isoformat()

                if success:
                    print_batch_progress(batch_counter, total_batches, len(batch), status_code, "delete")
                    stats.successes.append(
                        SubmissionOutcome(urls=batch, http_status=status_code, timestamp=now_iso, action="delete")
                    )
                    stats.deleted_detected += len(batch)
                    for url in batch:
                        record_submission(log_entries, url, "deleted", now_iso, "delete")
                    save_submission_log(log_entries)
                    log_line(f"    Success -> {message}")
                else:
                    log_line(f"    Failed  -> HTTP {status_code}: {message}")
                    stats.failures.append(SubmissionFailure(urls=batch, reason=message, timestamp=now_iso))

                if shutdown.stop_requested:
                    break

    stats.finish_time = datetime.now(timezone.utc)
    write_report(stats, report_path)
    save_submission_log(log_entries)
    log_line(f"Report written to: {report_path}")
    log_line(f"Submission log saved to: {SUBMISSION_LOG_FILE}")


if __name__ == "__main__":
    try:
        run()
    except FileNotFoundError as exc:
        print(f"Fatal error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001 - top-level safety net, never crash silently
        print(f"Unexpected fatal error: {exc}", file=sys.stderr)
        sys.exit(1)