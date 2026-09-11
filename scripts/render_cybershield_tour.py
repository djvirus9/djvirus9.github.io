#!/usr/bin/env python3
"""Render the authored workflow tour from the site's data and SVG illustrations.

Requires Playwright with Chromium and ffmpeg. Build Jekyll first, then pass the
build directory. No original Invia footage or customer screenshots are used.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright


def timestamp(seconds):
    return f"00:{seconds // 60:02d}:{seconds % 60:02d}.000"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path, help="Jekyll output directory")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / "_data/cybershield.json").read_text())
    rendered = (args.build / "index.html").read_text()
    diagrams = re.findall(r'<svg class="cs-diagram".*?</svg>', rendered, flags=re.S)
    if len(diagrams) != len(data["stages"]):
        raise SystemExit("Build the homepage before rendering the tour.")
    stages = {stage["id"]: (stage, diagrams[index]) for index, stage in enumerate(data["stages"])}
    destination = root / "assets/cybershield"
    destination.mkdir(parents=True, exist_ok=True)
    captions = ["WEBVTT", ""]
    for segment in data["tour"]:
        captions.extend([f'{timestamp(segment["start"])} --> {timestamp(segment["end"])}', segment["caption"], ""])
    (destination / "workflow-tour.vtt").write_text("\n".join(captions))

    with tempfile.TemporaryDirectory(prefix="cybershield-tour-") as temp:
        temp = Path(temp)
        frames = []
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
            for index, segment in enumerate(data["tour"]):
                stage, svg = stages[segment["stage"]]
                steps = "".join(f'<span class="{"selected" if item["id"] == stage["id"] else ""}">{i + 1:02d} {html.escape(item["label"])}</span>' for i, item in enumerate(data["stages"]))
                document = f'''<!doctype html><html lang="en"><meta charset="utf-8">
<link rel="stylesheet" href="{(root / 'assets/css/cybershield.css').as_uri()}">
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; width: 1280px; height: 720px; overflow: hidden; background: #102b28; color: #edf9f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
header {{ display: flex; align-items: center; justify-content: space-between; padding: 35px 48px 26px; border-bottom: 1px solid #34544f; }}
.brand {{ font-size: 29px; font-weight: 750; letter-spacing: -1px; }}
.meta {{ color: #b5d8c9; font-size: 17px; }}
main {{ display: grid; grid-template-columns: 350px 1fr; gap: 25px; align-items: center; padding: 22px 35px 0 48px; }}
.eyebrow {{ color: #8af0c7; letter-spacing: 2px; font-size: 15px; font-weight: 700; text-transform: uppercase; }}
h1 {{ font-size: 43px; line-height: 1.14; letter-spacing: -1.4px; margin: 20px 0 26px; }}
.output {{ font-size: 21px; line-height: 1.5; color: #c1ded4; margin: 0; max-width: 300px; }}
.graphic {{ width: 100%; max-width: 600px; justify-self: center; border: 1px solid #507c6c; border-radius: 18px; overflow: hidden; }}
.steps {{ display: flex; justify-content: space-between; gap: 8px; padding: 10px 48px; color: #b5d8c9; font-size: 18px; border-bottom: 1px solid #34544f; }}
.steps span {{ border-radius: 6px; padding: 8px 20px; }}
.steps .selected {{ color: #102b28; background: #b1f3db; font-weight: 700; }}
</style>
<header><span class="brand">CyberShield360</span><span class="meta">Illustrated workflow · Example data</span></header>
<div class="steps">{steps}</div>
<main><div><div class="eyebrow">{html.escape(segment['heading'].split(' / ')[0] if index < 4 else 'Product ownership')}</div><h1>{html.escape(segment['heading'].split(' / ')[-1])}</h1><p class="output">{html.escape(stage['output'] if index < 4 else 'Architecture, security design, and delivery at Invia.')}</p></div><div class="graphic">{svg}</div></main>
</html>'''
                source = temp / f"scene-{index}.html"
                source.write_text(document)
                page.goto(source.as_uri(), wait_until="load")
                frame = temp / f"scene-{index}.png"
                page.screenshot(path=str(frame))
                frames.append(frame)
            browser.close()
        shutil.copy2(frames[0], destination / "workflow-poster.png")
        command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
        for frame, segment in zip(frames, data["tour"]):
            command.extend(["-loop", "1", "-framerate", "12", "-t", str(segment["end"] - segment["start"]), "-i", str(frame)])
        inputs = "".join(f"[{index}:v]" for index in range(len(frames)))
        command.extend(["-filter_complex", f"{inputs}concat=n={len(frames)}:v=1:a=0,format=yuv420p[v]", "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-movflags", "+faststart", "-t", str(data["duration"]), "-an", str(destination / "workflow-tour.mp4")])
        subprocess.run(command, check=True)
    print(f"Rendered {data['duration']}-second video, poster, and English captions in {destination}")


if __name__ == "__main__":
    main()
