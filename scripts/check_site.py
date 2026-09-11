#!/usr/bin/env python3
"""Check the generated portfolio without making network requests."""
import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.assets = []
        self.h1s = 0
        self.meta = {}
        self.title = ""
        self.in_title = False
        self.canonical = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1s += 1
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property"))] = attrs.get("content")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("img", "script", "video", "source", "track"):
            if attrs.get("src", attrs.get("data-src")):
                self.assets.append(attrs.get("src", attrs.get("data-src")))
            if attrs.get("poster", attrs.get("data-poster")):
                self.assets.append(attrs.get("poster", attrs.get("data-poster")))
        if tag == "link" and attrs.get("href"):
            if attrs.get("rel") == "canonical":
                self.canonical = attrs["href"]
            elif attrs.get("rel") in ("stylesheet", "icon"):
                self.assets.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title += text


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not root.is_dir():
        raise SystemExit(f"Build directory does not exist: {root}")
    pages = {p: Page(p.read_text()) for p in root.rglob("*.html")}
    errors = []
    descriptions = {}
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        if page.h1s != 1:
            errors.append(f"{relative}: expected one h1, got {page.h1s}")
        for element_id, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f"{relative}: duplicate id {element_id}")
        if not page.title.strip() or not page.canonical:
            errors.append(f"{relative}: missing title or canonical URL")
        description = page.meta.get("description")
        if not description:
            errors.append(f"{relative}: missing description")
        elif description in descriptions:
            errors.append(f"{relative}: duplicate description from {descriptions[description]}")
        else:
            descriptions[description] = relative
        if page.meta.get("twitter:card") != "summary_large_image":
            errors.append(f"{relative}: missing social card")
        social = page.meta.get("og:image")
        if not social:
            errors.append(f"{relative}: missing social image")
        for href in page.links + page.assets + ([social] if social else []):
            resolved = urlsplit(urljoin("https://djvirus9.github.io/" + relative, href))
            if resolved.scheme not in ("http", "https") or resolved.netloc != "djvirus9.github.io":
                continue
            target = root / unquote(resolved.path).lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{relative}: missing target {href}")
            elif resolved.fragment and target in pages and unquote(resolved.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing anchor {href}")
    source_root = Path(__file__).resolve().parents[1]
    cves = json.loads((source_root / "_data/cves.json").read_text())
    if len({cve["id"] for cve in cves}) != len(cves):
        errors.append("CVE data contains duplicate IDs")
    for cve in cves:
        for field in ("id", "product", "title", "impact", "published", "advisory", "credit", "cvss_version"):
            if not cve.get(field):
                errors.append(f"{cve.get('id')}: missing {field}")
        if not 0 <= float(cve["cvss"]) <= 10:
            errors.append(f"{cve['id']}: invalid CVSS score")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Checked {len(pages)} HTML pages: headings, metadata, assets, internal links, anchors, and {len(cves)} CVE records passed.")


if __name__ == "__main__":
    main()
