#!/usr/bin/env python3
"""Render authored project sharing cards; requires the browser-check dependencies."""
import html
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CSS = """
* { box-sizing: border-box; }
body { margin: 0; width: 1200px; height: 630px; padding: 48px 56px; background: #0c1716; color: #edf6f2; font-family: Arial, sans-serif; display: flex; flex-direction: column; }
header { display: flex; align-items: center; gap: 14px; font-size: 21px; }
.mark { display: grid; place-items: center; width: 42px; height: 42px; border: 1px solid #345149; color: #6ee7ce; border-radius: 10px; font-size: 16px; font-weight: 700; }
.category { margin-left: auto; color: #b2c7be; font-size: 15px; letter-spacing: 1px; text-transform: uppercase; }
main { display: grid; grid-template-columns: 1.1fr 1fr; align-items: center; gap: 34px; flex: 1; }
h1 { font-size: 54px; line-height: 1.08; letter-spacing: -2px; margin: 0 0 24px; }
p { font-size: 20px; line-height: 1.5; color: #b2c7be; margin: 0; }
img { display: block; width: 100%; border-radius: 18px; }
footer { display: flex; justify-content: space-between; border-top: 1px solid #345149; padding-top: 22px; font-size: 17px; color: #b2c7be; }
footer span:last-child { color: #6ee7ce; }
"""


def main():
    projects = json.loads((ROOT / "_data/featured_work.json").read_text())
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        for project in projects:
            art = (ROOT / project["art"].lstrip("/")).as_uri()
            source = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(project['title'])}</title><style>{CSS}</style></head>
<body><header><span class="mark">DS</span>Danish Siddiqui<span class="category">Engineering case study</span></header>
<main><div><h1>{html.escape(project['share_title'])}</h1><p>{html.escape(project['share_context'])}</p></div><img src="{art}" alt=""></main>
<footer><span>Product security · Architecture · Engineering</span><span>djvirus9.github.io</span></footer></body></html>"""
            # Use a file origin so Chromium can load the local, authored SVG assets.
            preview = ROOT / "artifacts" / f"{project['anchor']}-social.html"
            preview.parent.mkdir(parents=True, exist_ok=True)
            preview.write_text(source)
            page.goto(preview.as_uri(), wait_until="load")
            page.wait_for_function("Array.from(document.images).every(img => img.complete && img.naturalWidth > 0)")
            output = ROOT / project["share_image"].lstrip("/")
            output.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(output))
            print(f"{output.relative_to(ROOT)}: {output.stat().st_size:,} bytes")
        browser.close()


if __name__ == "__main__":
    main()
