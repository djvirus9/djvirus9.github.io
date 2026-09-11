#!/usr/bin/env python3
"""Check the sample triage workflow, accessibility, and browser-only state."""
import argparse
import functools
import json
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright
from check_showcase import QuietHandler, assert_axe


def check_workflow(page, axe_path, report):
    root = page.locator('[data-secops-demo]')
    assert root.locator('[data-finding-id]').count() == 5
    assert root.locator('[data-count="open"]').inner_text() == '3'
    root.locator('#sample-severity').select_option('high')
    assert root.locator('[data-finding-id]').count() == 2
    root.locator('#sample-search').fill('worker')
    assert root.locator('[data-finding-id]').count() == 1
    root.locator('[data-finding-id="DEMO-002"]').click()
    assert root.locator('[data-detail="id"]').inner_text() == 'DEMO-002'
    root.locator('#sample-new-status').select_option('investigating')
    root.locator('#sample-assignee').select_option('Application team')
    root.locator('[data-triage-form] button').click()
    assert root.locator('[data-count="open"]').inner_text() == '2'
    assert root.locator('[data-count="investigating"]').inner_text() == '2'
    assert 'Investigating' in root.locator('[data-finding-id="DEMO-002"]').inner_text()
    assert root.locator('#sample-assignee').input_value() == 'Application team'
    if axe_path:
        assert_axe(page, axe_path, report)

    root.locator('[data-reset-demo]').click()
    assert root.locator('[data-finding-id]').count() == 5
    assert root.locator('[data-count="open"]').inner_text() == '3'
    root.locator('#sample-filter-status').select_option('open')
    root.locator('[data-finding-id="DEMO-001"]').click()
    root.locator('#sample-new-status').select_option('resolved')
    root.locator('[data-triage-form] button').click()
    assert root.locator('[data-finding-id]').count() == 2
    assert root.locator('[data-finding-id="DEMO-001"]').count() == 0
    assert root.locator('[data-count="resolved"]').inner_text() == '2'
    assert 'DEMO-001 updated to Resolved' in root.locator('[data-demo-feedback]').inner_text()
    root.locator('#sample-filter-status').select_option('all')
    root.locator('[data-finding-id="DEMO-001"]').click()
    assert root.locator('#sample-new-status').input_value() == 'resolved'
    if axe_path:
        assert_axe(page, axe_path, report)

    root.locator('#sample-search').fill('<sample that has no matching findings>')
    assert root.locator('[data-empty]').is_visible()
    assert not root.locator('[data-finding-detail]').is_visible()
    assert root.locator('[data-result-count]').inner_text() == '0 of 5 sample findings'
    if axe_path:
        assert_axe(page, axe_path, report)
    root.locator('[data-reset-demo]').click()
    root.locator('[data-finding-id="DEMO-003"]').focus()
    page.keyboard.press('Enter')
    assert page.evaluate('document.activeElement.id') == 'sample-finding-title'
    assert root.locator('[data-detail="id"]').inner_text() == 'DEMO-003'
    root.locator('#sample-new-status').select_option('closed')
    root.locator('[data-triage-form] button').click()
    assert root.locator('[data-count="resolved"]').inner_text() == '2'
    page.reload(wait_until='networkidle')
    assert root.locator('[data-count="open"]').inner_text() == '3'
    assert root.locator('[data-count="resolved"]').inner_text() == '1'
    report['workflow_checks'] += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    parser.add_argument('--browsers', nargs='+', default=['chromium'])
    parser.add_argument('--axe', type=Path)
    parser.add_argument('--output', type=Path, default=Path('artifacts/secops-checks.json'))
    args = parser.parse_args()
    if args.axe and not args.axe.is_file():
        parser.error('The axe-core script must exist locally.')
    handler = functools.partial(QuietHandler, directory=str(args.build.resolve()))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}'
    path = '/case-studies/secops-dashboard/'
    report = {'scenarios': [], 'accessibility_checks': 0, 'workflow_checks': 0, 'fallback_checks': 0, 'errors': []}
    try:
        with sync_playwright() as p:
            for name in args.browsers:
                browser = getattr(p, name).launch()
                for width in [320, 390, 768, 1440]:
                    for theme in ['light', 'dark']:
                        context = browser.new_context(viewport={'width': width, 'height': 1000}, color_scheme=theme)
                        page = context.new_page()
                        errors, requests = [], []
                        page.on('pageerror', lambda error: errors.append(str(error)))
                        page.on('request', lambda request: requests.append(request.url))
                        page.on('response', lambda response: errors.append(f'{response.status} {response.url}') if response.status >= 400 else None)
                        case = {'browser': name, 'width': width, 'theme': theme}
                        try:
                            response = page.goto(base + path, wait_until='networkidle')
                            assert response.status == 200
                            assert page.locator('h1').count() == 1
                            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Horizontal overflow'
                            assert page.locator('[data-demo-app]').is_visible()
                            if args.axe:
                                assert_axe(page, args.axe, report)
                            if width in (390, 1440):
                                check_workflow(page, args.axe, report)
                            external = [url for url in requests if urlsplit(url).scheme in ('http', 'https') and urlsplit(url).netloc != urlsplit(base).netloc]
                            assert not external, external
                            assert not errors, errors
                            case['status'] = 'passed'
                        except Exception as error:
                            case.update(status='failed', error=str(error))
                            report['errors'].append(case)
                            print(json.dumps(case), flush=True)
                        finally:
                            report['scenarios'].append(case)
                            context.close()
                context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 900})
                page = context.new_page()
                page.goto(base + path, wait_until='load')
                assert not page.locator('[data-demo-app]').is_visible()
                assert page.locator('.sd-fallback-finding').count() == 5
                page.locator('.sd-fallback-finding summary').first.click()
                assert page.locator('.sd-fallback-finding').first.locator('p').first.is_visible()
                page.goto(base, wait_until='load')
                assert page.locator('#open-source .os-card').count() == 2
                report['fallback_checks'] += 1
                context.close()
                context = browser.new_context(reduced_motion='reduce')
                context.add_init_script("Object.defineProperty(window, 'localStorage', {get() {throw new Error('Storage unavailable');}})")
                page = context.new_page()
                page.goto(base + path, wait_until='networkidle')
                check_workflow(page, None, report)
                report['fallback_checks'] += 1
                context.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2))
    print(json.dumps({'scenarios': len(report['scenarios']), 'accessibility_checks': report['accessibility_checks'], 'workflow_checks': report['workflow_checks'], 'fallback_checks': report['fallback_checks'], 'failures': len(report['errors'])}))
    if report['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
