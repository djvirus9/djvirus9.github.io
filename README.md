# Danish Siddiqui’s security portfolio

Live site: [djvirus9.github.io](https://djvirus9.github.io/).

A Jekyll portfolio with engineering case studies, a résumé-backed experience timeline, published vulnerability research, and technical notes. Existing public page and résumé URLs are preserved.

## Local preview

Use Ruby 3.2 and Bundler, then run:

```sh
bundle install
bundle exec jekyll build
python3 scripts/check_site.py _site
python3 -m http.server 4173 --bind 127.0.0.1 --directory _site
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

See the [update review and screenshots](docs/review.md) for the current design and validation coverage.

## Validation and deployment

Pull requests build the site and check generated headings, descriptions, social images, local assets, links, anchors, and CVE data. Pull-request workflows do not deploy.

The existing GitHub Pages deployment runs after a change reaches `main`, or through a manual workflow on `main`. Build dependencies are locked for macOS and Linux.

The social preview source is `scripts/social-preview.html`. To regenerate its 1200 × 630 PNG with Playwright:

```sh
playwright screenshot --browser chromium --viewport-size '1200,630' file:///absolute/path/to/repository/scripts/social-preview.html assets/social-preview.png
```

## Contact

[LinkedIn](https://www.linkedin.com/in/djvirus9) · [GitHub](https://github.com/djvirus9) · [Email](mailto:danishismyname1@gmail.com)
