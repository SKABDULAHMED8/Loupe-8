#!/usr/bin/env python3
"""Validate Loupe-8 static assets, SEO metadata, guide pages and sitemap."""

from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
SITEMAP_PATH = ROOT / "sitemap.xml"
README_PATH = ROOT / "README.md"
BASE_URL = "https://skabdulahmed8.github.io/Loupe-8/"
SOCIAL_IMAGE = "https://skabdulahmed8.github.io/Loupe-8/LOUPE_Home_Logo1.png"
GUIDE_PATHS = (
    "guides/passport-photo-for-online-forms/index.html",
    "guides/signature-image-for-online-forms/index.html",
    "guides/compress-image-to-20kb-or-50kb/index.html",
    "guides/resize-image-to-exact-pixels/index.html",
    "guides/profile-photo-resizer/index.html",
    "guides/resize-and-compress-image-for-online-form/index.html",
    "guides/convert-image-to-jpg-png-webp/index.html",
)
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
    print("ERROR: " + message, file=sys.stderr)
    raise SystemExit(1)


def check(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def check_json_ld(html: str, relative_path: str) -> None:
    blocks = re.findall(
        r'<script\s+type="application/ld\+json">([\s\S]*?)</script>',
        html,
        re.I,
    )
    check(bool(blocks), relative_path + " needs valid JSON-LD structured data")
    for block in blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            fail(relative_path + " contains invalid JSON-LD: " + str(exc))


def check_page(path: Path, canonical: str, *, guide: bool = False) -> str:
    check(path.is_file(), "required page is missing: " + str(path.relative_to(ROOT)))
    html = path.read_text(encoding="utf-8")
    check(path.stat().st_size < MAX_HTML_BYTES, path.name + " is too large")
    check(len(re.findall(r"<h1\b", html, re.I)) == 1,
          str(path.relative_to(ROOT)) + " must contain exactly one H1")
    check(len(re.findall(r"<title>[^<]+</title>", html, re.I)) == 1,
          str(path.relative_to(ROOT)) + " must contain exactly one title")
    descriptions = re.findall(r'<meta\s+name="description"\s+content="([^"]+)"', html, re.I)
    check(len(descriptions) == 1 and len(descriptions[0]) >= 90,
          str(path.relative_to(ROOT)) + " needs one useful meta description")
    check('<link rel="canonical" href="' + canonical + '">' in html,
          str(path.relative_to(ROOT)) + " canonical URL is incorrect")
    check('<meta property="og:url" content="' + canonical + '">' in html,
          str(path.relative_to(ROOT)) + " Open Graph URL must match the canonical URL")
    check('name="robots" content="index, follow' in html,
          str(path.relative_to(ROOT)) + " must be indexable")
    check("og:image" in html and "twitter:card" in html,
          str(path.relative_to(ROOT)) + " needs social metadata")
    check(SOCIAL_IMAGE in html,
          str(path.relative_to(ROOT)) + " must reference the verified first-party brand image")
    check("aggregateRating" not in html,
          str(path.relative_to(ROOT)) + " must not publish browser-local review aggregates")
    image_tags = re.findall(r"<img\b[^>]*>", html, re.I)
    check(all(re.search(r"\balt\s*=", tag, re.I) for tag in image_tags),
          str(path.relative_to(ROOT)) + " image elements must have alt attributes")
    check_json_ld(html, str(path.relative_to(ROOT)))
    if guide:
        # Do not impose a fixed word-count target. Validate useful page structure instead.
        check('href="' + BASE_URL + '#app"' in html,
              str(path.relative_to(ROOT)) + " must link back to the editor")
        check('"@type":"Article"' in html or '"@type": "Article"' in html,
              str(path.relative_to(ROOT)) + " needs Article schema")
    return html


html = check_page(HTML_PATH, BASE_URL)
check("image.pi7.org" not in html.casefold(), "homepage must not direct visitors to an unrelated third-party image service")
check("unhandledrejection" not in html, "do not show the site-wide standby notice for unrelated rejected promises")
readme = README_PATH.read_text(encoding="utf-8")
check("edgeone" not in readme.casefold(), "README must not advertise an EdgeOne backup host")
check("edgeone" not in html.casefold(), "homepage must not reference an EdgeOne backup host")
check(HTML_PATH.stat().st_size < MAX_HTML_BYTES, "index.html exceeds the size limit")
check("data:image/" not in html, "keep image assets outside index.html")
check("<h1>Free online image resizer for exact pixels and KB limits</h1>" in html,
      "homepage H1 does not target general image-resizing intent")
check("<title>Free Online Image Resizer &amp; Compressor | Loupe-8</title>" in html,
      "homepage title does not describe the image-resizer category")
check('id="tool-summary"' in html,
      "homepage needs an answer-first tool summary")
check('<table class="capability-table">' in html,
      "homepage needs a capability and limitation comparison table")
for required_limit in (
    "Exact output file size, such as exactly 20 KB",
    "An animated GIF is processed as a single still image",
    "It does not remove or replace backgrounds",
    "It does not draw or create a digital signature",
):
    check(required_limit in html,
          "homepage capability table is missing: " + required_limit)

check('guides/resize-and-compress-image-for-online-form/' in html and
      'guides/convert-image-to-jpg-png-webp/' in html,
      "homepage must link to both new task guides")
check('name="twitter:card" content="summary_large_image"' in html,
      "homepage Twitter card must use summary_large_image")
check('og:image:width" content="2146"' in html and 'og:image:height" content="733"' in html,
      "homepage social image dimensions must match the existing 2146 x 733 PNG")
check('href="guides/' in html, "homepage must link to its guide cluster")
check('href="#faq"' in html, "FAQ navigation must target the real FAQ anchor")
check(len(re.findall(r'<article class="faq-item">', html)) >= 13,
      "homepage needs at least thirteen visible FAQ answers")
check('"@type":"WebApplication"' in html and '"applicationCategory":"MultimediaApplication"' in html,
      "WebApplication schema is missing")
check("FAQPage" not in html, "do not add retired FAQ rich-result markup")

references = set(re.findall(
    r"""\b(?:src|href|srcset|content)=["'](assets/[^"']+)["']""", html
))
missing = sorted(path for path in references if not (ROOT / path).is_file())
if missing:
    fail("referenced assets are missing: " + ", ".join(missing))
unreferenced = sorted(set(EXPECTED_ASSETS) - references)
if unreferenced:
    fail("expected assets are not referenced: " + ", ".join(unreferenced))

asset_total = 0
for relative, signature in EXPECTED_ASSETS.items():
    path = ROOT / relative
    check(path.is_file(), "required asset is missing: " + relative)
    data = path.read_bytes()
    check(data.startswith(signature), "invalid file signature: " + relative)
    if path.suffix == ".webp":
        check(data[8:12] == b"WEBP", "invalid WebP file: " + relative)
    asset_total += len(data)
check(asset_total < MAX_ASSET_BYTES, "optimized static assets exceed 1 MB")

for relative in GUIDE_PATHS:
    canonical = BASE_URL + relative.removesuffix("index.html")
    guide_html = check_page(ROOT / relative, canonical, guide=True)
    check("edgeone" not in guide_html.casefold(), relative + " must not reference an EdgeOne backup host")

guide_index = ROOT / "guides/index.html"
check(guide_index.is_file(), "guides/index.html is missing")
guide_index_html = check_page(guide_index, BASE_URL + "guides/")
check("edgeone" not in guide_index_html.casefold(), "guide index must not reference an EdgeOne backup host")
check("CollectionPage" in guide_index_html, "guide index needs CollectionPage schema")

# Title links and snippets should describe each page, not duplicate another page.
all_page_paths = [HTML_PATH, guide_index] + [ROOT / path for path in GUIDE_PATHS]
page_titles = []
page_descriptions = []
for page_path in all_page_paths:
    page_source = page_path.read_text(encoding="utf-8")
    page_titles.extend(re.findall(r"<title>([^<]+)</title>", page_source, re.I))
    page_descriptions.extend(
        re.findall(r'<meta\s+name="description"\s+content="([^"]+)"', page_source, re.I)
    )
check(len(page_titles) == len(set(page_titles)),
      "every indexable page must have a unique title")
check(len(page_descriptions) == len(set(page_descriptions)),
      "every indexable page must have a unique meta description")
for relative in GUIDE_PATHS:
    target = BASE_URL + relative.removesuffix("index.html")
    check(target in guide_index_html,
          "guide index must link to " + target)

try:
    sitemap_tree = ET.parse(SITEMAP_PATH)
except (ET.ParseError, OSError) as exc:
    fail("sitemap.xml is missing or invalid: " + str(exc))
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_url_nodes = [node.text for node in sitemap_tree.findall(".//sm:loc", ns)]
sitemap_urls = set(sitemap_url_nodes)
check(len(sitemap_url_nodes) == len(sitemap_urls), "sitemap must not contain duplicate URLs")
check(all(url and url.startswith(BASE_URL) for url in sitemap_urls),
      "sitemap must contain only URLs under the canonical GitHub Pages project path")
required = {BASE_URL, BASE_URL + "guides/"} | {
    BASE_URL + path.removesuffix("index.html") for path in GUIDE_PATHS
}
missing_urls = sorted(required - sitemap_urls)
if missing_urls:
    fail("sitemap is missing canonical URLs: " + ", ".join(missing_urls))
check(sitemap_urls == required,
      "sitemap URLs must match the exact set of published canonical pages")
robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
check("Allow: /" in robots, "project robots.txt must allow crawling")
check("Sitemap: " + BASE_URL + "sitemap.xml" in robots,
      "project robots.txt must point to the canonical sitemap URL")

print(
    "PASS: Loupe-8 SEO, guide, sitemap and asset validation "
    + "(homepage " + str(HTML_PATH.stat().st_size) + " bytes; "
    + str(len(GUIDE_PATHS)) + " article guides; "
    + str(len(sitemap_urls)) + " sitemap URLs; "
    + str(asset_total) + " asset bytes)."
)
