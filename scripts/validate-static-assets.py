#!/usr/bin/env python3
"""Validate local image assets before deploying the static Loupe-8 site."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
EXPECTED_ASSETS = {
    "assets/loupe-favicon.png": b"\x89PNG\r\n\x1a\n",
    "assets/loupe-icon.webp": b"RIFF",
    "assets/loupe-wordmark-light.webp": b"RIFF",
    "assets/loupe-wordmark-dark.webp": b"RIFF",
    "assets/loupe-lockup-light.webp": b"RIFF",
    "assets/loupe-lockup-dark.webp": b"RIFF",
    "assets/amash-brand-ribbon.webp": b"RIFF",
}
MAX_HTML_BYTES = 100_000
MAX_ASSET_BYTES = 1_000_000


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


if not HTML_PATH.is_file():
    fail("index.html is missing")

html_bytes = HTML_PATH.stat().st_size
html = HTML_PATH.read_text(encoding="utf-8")
if html_bytes >= MAX_HTML_BYTES:
    fail(f"index.html exceeds {MAX_HTML_BYTES:,} bytes ({html_bytes:,})")
if "data:image/" in html:
    fail("index.html contains embedded image data; keep large images as external assets")

references = set(
    re.findall(r"\b(?:src|href|srcset)=[\"'](assets/[^\"']+)[\"']", html)
)
missing_references = sorted(references - {
    path for path in EXPECTED_ASSETS if (ROOT / path).is_file()
})
if missing_references:
    fail("referenced asset files are missing: " + ", ".join(missing_references))

unreferenced = sorted(set(EXPECTED_ASSETS) - references)
if unreferenced:
    fail("expected optimized assets are not referenced: " + ", ".join(unreferenced))

asset_total = 0
for relative_path, signature in EXPECTED_ASSETS.items():
    path = ROOT / relative_path
    if not path.is_file():
        fail(f"required asset is missing: {relative_path}")
    data = path.read_bytes()
    if not data.startswith(signature):
        fail(f"invalid file signature: {relative_path}")
    if path.suffix == ".webp" and data[8:12] != b"WEBP":
        fail(f"invalid WebP container: {relative_path}")
    asset_total += len(data)

if asset_total >= MAX_ASSET_BYTES:
    fail(f"optimized asset set exceeds {MAX_ASSET_BYTES:,} bytes ({asset_total:,})")

print(
    "PASS: static asset checks passed "
    f"(HTML {html_bytes:,} bytes; assets {asset_total:,} bytes; "
    f"{len(references)} local references)."
)
