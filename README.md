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
- `_data/case_studies.json`: case-study card titles, descriptions, and featured selection.
- `case-studies/`: detailed accounts of engineering work.
- `_data/cves.json`: selected public CVEs, publication dates, publisher scores, and direct acknowledgment links.
- `_data/writing.json` and `blog/`: article index and technical notes.
- `_sass/custom.scss`: shared layout, typography, and light/dark color variables.
- `_layouts/` and `_includes/`: semantic layouts, navigation, and metadata.

The site uses system fonts and local JavaScript. Mobile navigation works without JavaScript; theme preference storage is optional. The empty search interface, search downloads, external icon font, and visible empty feed link have been removed.

Read [content provenance and outstanding details](docs/content-notes.md) before adding new quantitative claims or credential links. The `docs`, `scripts`, and `artifacts` directories are excluded from the public build.

See the [CyberShield360 showcase review](docs/showcase-review.md) for the interactive feature and the [original redesign review](docs/review.md) for the wider site refresh.

## Validation and deployment

Pull requests build the site and check generated headings, descriptions, social images, local assets, links, anchors, and CVE data. The interactive showcase is also checked in Chromium and WebKit for navigation, accessibility, media loading, and captions. Pull-request workflows do not deploy.

The existing GitHub Pages deployment runs after a change reaches `main`, or through a manual workflow on `main`. Build dependencies are locked for macOS and Linux.

## CyberShield360 showcase

The homepage and CyberShield360 case study share `_includes/cybershield-showcase.html`. Content, stages, and the tour transcript live in `_data/cybershield.json`. Diagrams have dedicated desktop and phone layouts in `_includes/cybershield-diagram.html`.

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

The social preview source is `scripts/social-preview.html`. To regenerate its 1200 × 630 PNG with Playwright:

```sh
playwright screenshot --browser chromium --viewport-size '1200,630' file:///absolute/path/to/repository/scripts/social-preview.html assets/social-preview.png
```

## Contact

[LinkedIn](https://www.linkedin.com/in/djvirus9) · [GitHub](https://github.com/djvirus9) · [Email](mailto:danishismyname1@gmail.com)
