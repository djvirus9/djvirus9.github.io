#!/usr/bin/env python3
"""Exercise the built showcase, accessible controls, and video in real browsers."""
import argparse
import functools
import json
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright
from serve_site import SiteHandler


class QuietHandler(SiteHandler):
    def log_message(self, *args):
        pass


def assert_axe(page, axe_path, report):
    if not page.evaluate("Boolean(window.axe)"):
        page.add_script_tag(path=str(axe_path))
    violations = page.evaluate("""async () => {
      const result = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice']}});
      return result.violations.map(item => ({id: item.id, nodes: item.nodes.map(node => ({target: node.target, message: node.failureSummary}))}));
    }""")
    report["accessibility_checks"] += 1
    assert not violations, json.dumps(violations)


def check_media(page):
    page.wait_for_function("""() => {
      const video = document.querySelector('video');
      return video.readyState >= 2 && video.textTracks.length === 1 && video.textTracks[0].cues && video.textTracks[0].cues.length === 5;
    }""", timeout=30000)
    state = page.locator("video").evaluate("""video => ({duration: video.duration, width: video.videoWidth, mode: video.textTracks[0].mode, end: video.textTracks[0].cues[4].endTime})""")
    assert state == {"duration": 75, "width": 1280, "mode": "showing", "end": 75}, state
    page.locator("video").evaluate("video => { video.pause(); video.currentTime = 34; }")
    page.wait_for_function("document.querySelector('video').currentTime >= 34")
    page.wait_for_function("""() => {
      const cues = document.querySelector('video').textTracks[0].activeCues;
      return cues.length === 1 && cues[0].text.includes('Consider exposure');
    }""")
    assert "Consider exposure" in page.locator("video").evaluate("video => video.textTracks[0].activeCues[0].text")


def check_controls(page, axe_path, report):
    for index, stage in enumerate(["discover", "enrich", "prioritize", "report"]):
        tab = page.locator(f'[data-stage-tab="{stage}"]')
        tab.click()
        assert page.locator('[role="tabpanel"]:visible').count() == 1
        assert page.locator(f'#cybershield-{stage}').is_visible()
        assert tab.get_attribute("aria-selected") == "true"
        assert page.url.endswith("#cybershield-" + stage)
        if axe_path:
            assert_axe(page, axe_path, report)
    page.locator('[data-stage-tab="report"]').focus()
    page.keyboard.press("ArrowRight")
    assert page.locator('[data-stage-tab="discover"]').get_attribute("aria-selected") == "true"
    page.keyboard.press("End")
    assert page.locator('[data-stage-tab="report"]').get_attribute("aria-selected") == "true"
    page.keyboard.press("Home")
    assert page.locator('[data-stage-tab="discover"]').get_attribute("aria-selected") == "true"
    page.keyboard.press("ArrowRight")
    assert page.evaluate('document.activeElement.dataset.stageTab') == "enrich"
    page.reload(wait_until="networkidle")
    assert page.locator('#cybershield-enrich').is_visible()

    page.locator('[data-open-tour]').click()
    assert page.locator('[data-tour-dialog]').evaluate("dialog => dialog.open")
    check_media(page)
    if axe_path:
        assert_axe(page, axe_path, report)
    page.locator('.cs-tour-close').focus()
    page.keyboard.press("Escape")
    assert not page.locator('[data-tour-dialog]').evaluate("dialog => dialog.open")
    assert page.locator('video').evaluate("video => video.paused")
    assert page.evaluate('document.activeElement.matches("[data-open-tour]")')
    page.locator('[data-open-tour]').click()
    assert page.locator('video source').count() == 1
    page.locator('.cs-tour-close').click()
    report["control_checks"] += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--browsers", nargs="+", default=["chromium"])
    parser.add_argument("--axe", type=Path, help="Local axe-core 4.10.3 script")
    parser.add_argument("--output", type=Path, default=Path("artifacts/showcase-checks.json"))
    args = parser.parse_args()
    handler = functools.partial(QuietHandler, directory=str(args.build.resolve()))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    report = {"scenarios": [], "accessibility_checks": 0, "control_checks": 0, "fallback_checks": 0, "errors": []}
    paths = ["/", "/case-studies/cybershield360/", "/case-studies/cybershield360/tour/"]
    try:
        with sync_playwright() as p:
            for name in args.browsers:
                browser = getattr(p, name).launch()
                for width in [320, 390, 768, 1440]:
                    for theme in ["light", "dark"]:
                        for path in paths:
                            case = {"browser": name, "width": width, "theme": theme, "path": path}
                            context = browser.new_context(viewport={"width": width, "height": 900}, color_scheme=theme)
                            page = context.new_page()
                            errors, requests = [], []
                            page.on("pageerror", lambda error: errors.append(str(error)))
                            page.on("request", lambda request: requests.append(request.url))
                            page.on("response", lambda response: errors.append(f"{response.status} {response.url}") if response.status >= 400 else None)
                            try:
                                response = page.goto(base + path, wait_until="networkidle")
                                assert response.status == 200
                                assert page.locator("h1").count() == 1
                                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), "Horizontal overflow"
                                assert not any(urlsplit(url).path.endswith(".mp4") for url in requests), "Video downloaded before interaction"
                                assert all(urlsplit(url).netloc == urlsplit(base).netloc for url in requests), "Unexpected third-party request"
                                if args.axe:
                                    assert_axe(page, args.axe, report)
                                if not path.endswith("/tour/"):
                                    assert page.locator('[role="tabpanel"]:visible').count() == 1
                                    assert page.locator('.cs-panel:not([hidden]) .cs-diagram:visible').count() == 1
                                    if width in (390, 1440) and theme == "light":
                                        check_controls(page, args.axe, report)
                                elif width == 390 and theme == "light":
                                    page.locator("video").evaluate("video => video.play()")
                                    check_media(page)
                                assert not errors, errors
                                case["status"] = "passed"
                            except Exception as error:
                                case["status"] = "failed"
                                case["error"] = str(error)
                                report["errors"].append(case)
                            finally:
                                report["scenarios"].append(case)
                                context.close()
                for path in paths[:2]:
                    context = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 900})
                    page = context.new_page()
                    page.goto(base + path, wait_until="load")
                    assert page.locator("[data-stage-panel]:visible").count() == 4
                    page.locator('[data-stage-tab="report"]').click()
                    assert page.url.endswith("#cybershield-report")
                    page.locator('[data-open-tour]').click()
                    assert page.url.endswith("/cybershield360/tour/")
                    assert page.locator("video source").get_attribute("src").endswith(".mp4")
                    assert page.locator("#tour-transcript").is_visible()
                    report["fallback_checks"] += 1
                    context.close()
                context = browser.new_context(reduced_motion="reduce")
                context.add_init_script("Object.defineProperty(window, 'localStorage', {get() {throw new Error('Storage unavailable');}})")
                page = context.new_page()
                page.goto(base, wait_until="networkidle")
                page.locator('[data-stage-tab="report"]').click()
                assert page.locator('#cybershield-report').is_visible()
                assert page.locator('#cybershield-report').evaluate("element => getComputedStyle(element).animationName") == "none"
                report["fallback_checks"] += 1
                context.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2))
    print(json.dumps({"scenarios": len(report["scenarios"]), "accessibility_checks": report["accessibility_checks"], "control_checks": report["control_checks"], "fallback_checks": report["fallback_checks"], "failures": len(report["errors"])}))
    if report["errors"]:
        raise SystemExit(json.dumps(report["errors"], indent=2))


if __name__ == "__main__":
    main()
