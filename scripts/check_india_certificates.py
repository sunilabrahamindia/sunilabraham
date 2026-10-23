#!/usr/bin/env python3
"""Check the TLS certificates presented by a curated list of Indian websites."""
from __future__ import annotations

import json
import socket
import ssl
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOMAINS_FILE = ROOT / "_data" / "india-certificate-domains.json"
RESULTS_FILE = ROOT / "assets" / "data" / "india-certificate-results.json"
TIMEOUT_SECONDS = 12


def parse_cert_date(value: str) -> datetime:
    # OpenSSL's getpeercert() commonly returns e.g. 'Oct 24 12:00:00 2026 GMT'.
    return datetime.strptime(value, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)


def check_website(item: dict, now: datetime) -> dict:
    domain = item["domain"]
    result = {
        "name": item["name"],
        "domain": domain,
        "category": item.get("category", "Other"),
        "status": "error",
        "expiry_utc": None,
        "days_remaining": None,
        "issuer": None,
        "last_checked_utc": now.isoformat().replace("+00:00", "Z"),
        "error": None,
    }
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=TIMEOUT_SECONDS) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as tls_sock:
                cert = tls_sock.getpeercert()
        not_after = cert.get("notAfter")
        if not not_after:
            raise ValueError("The server did not provide a readable certificate expiry.")
        expiry = parse_cert_date(not_after)
        result.update({
            "status": "ok",
            "expiry_utc": expiry.isoformat().replace("+00:00", "Z"),
            "days_remaining": (expiry.date() - now.date()).days,
            "issuer": dict(x[0] for x in cert.get("issuer", [])),
        })
    except (OSError, ssl.SSLError, ValueError, TimeoutError) as exc:
        result["error"] = f"{type(exc).__name__}: {str(exc)[:240]}"
    return result


def main() -> None:
    now = datetime.now(timezone.utc)
    config = json.loads(DOMAINS_FILE.read_text(encoding="utf-8"))
    results = [check_website(item, now) for item in config["websites"]]
    payload = {
        "last_checked_utc": now.isoformat().replace("+00:00", "Z"),
        "results": sorted(
            results,
            key=lambda item: (
                item["days_remaining"] is None,
                item["days_remaining"] if item["days_remaining"] is not None else 999999,
                item["domain"],
            ),
        ),
    }
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ok = sum(item["status"] == "ok" for item in results)
    print(f"Checked {len(results)} hostnames: {ok} certificate results, {len(results) - ok} checks needing review.")
    for item in results:
        print(f'{item["domain"]}: {item["status"]}; expiry={item["expiry_utc"]}; days={item["days_remaining"]}; error={item["error"]}')


if __name__ == "__main__":
    main()
