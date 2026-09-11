# Danish Siddiqui’s security portfolio

Live site: [djvirus9.github.io](https://djvirus9.github.io/).

A Jekyll portfolio with engineering case studies, a résumé-backed experience timeline, published vulnerability research, and technical notes. Existing public page and résumé URLs are preserved.

## Local preview

Use Ruby 3.2 and Bundler, then run:

```sh
bundle install
bundle exec jekyll build
python3 scripts/check_site.py _site
python3 scripts/serve_site.py _site --port 4173
```

Open `http://127.0.0.1:4173/`.

## Editing content

- `_pages/home.md`: homepage narrative and section order.
- `_data/experience.json`: employment history sourced from the résumé.
- `_data/case_studies.json`: the full case-study index.
- `_data/featured_work.json`: the three homepage projects, illustrations, and sharing-card content.
- `assets/css/home.css`: the compact homepage layout.
- `case-studies/`: detailed accounts of engineering work.
- `_data/cves.json`: selected public CVEs, publication dates, publisher scores, and direct acknowledgment links.
- `_data/writing.json` and `blog/`: article index and technical notes.
- `_data/open_source.json` and `_includes/open-source.html`: reusable open-source project cards from the earlier homepage.
- `case-studies/secops-dashboard.md`: the SecOps Dashboard case study and source references.
- `_data/secops_demo.json`, `_includes/secops-demo.html`, and `assets/js/secops-demo.js`: the synthetic, in-memory sample triage workflow.
- `_sass/custom.scss`: shared layout, typography, and light/dark color variables.
- `_layouts/` and `_includes/`: semantic layouts, navigation, and metadata.

The site uses system fonts and local JavaScript. Mobile navigation works without JavaScript; theme preference storage is optional. The empty search interface, search downloads, external icon font, and visible empty feed link have been removed.

Read [content provenance and outstanding details](docs/content-notes.md) before adding new quantitative claims or credential links. The `docs`, `scripts`, and `artifacts` directories are excluded from the public build.

See the [homepage refinement review](docs/homepage-review.md) for the compact layout and project sharing cards, the [CyberShield360 showcase review](docs/showcase-review.md) for the interactive feature and the [original redesign review](docs/review.md) for the wider site refresh.

## Validation and deployment

Pull requests build the site and check generated headings, descriptions, social images, local assets, links, anchors, and CVE data. The interactive showcase is also checked in Chromium and WebKit for navigation, accessibility, media loading, and captions. Pull-request workflows do not deploy.

The sample triage workflow also runs through Chromium and WebKit checks for filtering, selection, status/owner updates, counts, reset, keyboard navigation, accessibility, and no-JavaScript fallbacks.

The existing GitHub Pages deployment runs after a change reaches `main`, or through a manual workflow on `main`. Build dependencies are locked for macOS and Linux.

## Open-source projects and sample triage

The homepage links the SecOps Dashboard and DevSecOps Roadmap to their public repositories. The dashboard case study uses its actual v0.2.0 repository screenshot and links to the release, threat model, and operating procedures. See [the content and validation review](docs/open-source-review.md).

The embedded sample is a simplified portfolio interaction, not the full application. It uses five synthetic findings, makes no API calls, and retains changes only in memory until reset or reload. Without JavaScript, expandable examples remain readable. The screenshot and sample use different synthetic datasets and are labeled separately.

After building, run:

```sh
python3 scripts/check_secops.py _site --browsers chromium --axe /path/to/axe.min.js
```

Use `--browsers chromium webkit` to match CI. Both browser suites run before deployment. `assets/css/open-source.css` and the sample's JavaScript load only on the SecOps case-study page.

## CyberShield360 showcase

The CyberShield360 case study uses `_includes/cybershield-showcase.html`. The homepage links to this full experience through a compact project preview. Content, stages, and the tour transcript live in `_data/cybershield.json`. Diagrams have dedicated desktop and phone layouts in `_includes/cybershield-diagram.html`.

The diagrams are explicitly illustrated workflows using example data. Invia’s public links are promotional launch videos, and are attributed as such. The feature does not present them as interface screen recordings.

The 75-second video, poster, and English captions are committed in `assets/cybershield/`. Video data is loaded after the visitor chooses to play; JavaScript-disabled browsers use a standalone player and transcript page. To regenerate the authored tour after changing its data or diagrams:

```sh
python3 -m venv /tmp/portfolio-browser-env
/tmp/portfolio-browser-env/bin/pip install -r scripts/requirements-browser.txt
/tmp/portfolio-browser-env/bin/playwright install chromium
bundle exec jekyll build
/tmp/portfolio-browser-env/bin/python scripts/render_cybershield_tour.py _site
bundle exec jekyll build
```

Rendering requires `ffmpeg`. Browser checks run against a temporary local server:

```sh
/tmp/portfolio-browser-env/bin/python scripts/check_showcase.py _site
```

Use `--browsers chromium webkit` after installing both engines, and `--axe /path/to/axe.min.js` for the same axe-core 4.10.3 accessibility checks used in CI. The test dependencies and render scripts are excluded from the public site.

Project sharing cards use the authored illustrations in `assets/projects/` and content in `_data/featured_work.json`. Regenerate their 1200 × 630 PNGs with `python3 scripts/render_project_previews.py`, then rebuild the site. Each flagship case study defines its own `og_title`, `og_image`, and `og_image_alt`. These illustrations describe the work; they are not product screenshots.

The default social preview source is `scripts/social-preview.html`. To regenerate its 1200 × 630 PNG with Playwright:

```sh
playwright screenshot --browser chromium --viewport-size '1200,630' file:///absolute/path/to/repository/scripts/social-preview.html assets/social-preview.png
```

## Contact

[LinkedIn](https://www.linkedin.com/in/djvirus9) · [GitHub](https://github.com/djvirus9) · [Email](mailto:danishismyname1@gmail.com)
