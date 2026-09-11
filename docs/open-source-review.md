# Open-source portfolio additions

## Scope

- Add a SecOps Dashboard case study with an actual product screenshot, a sample triage workflow, architecture, design decisions, and public evidence links.
- Add visual cards for SecOps Dashboard and the DevSecOps Roadmap to the homepage.
- Move the existing Licious and DevSecOps cards ahead of the interactive showcases so current engineering work is easier to discover.
- Preserve the complete CyberShield360 explorer, its media, existing page URLs, and résumé.
- Coordinate a separate GitHub profile README refresh with the same project and contact links.

## Content provenance

The case study describes the core workflow and team controls in the public [v0.2.0 release](https://github.com/djvirus9/secops-dashboard/releases/tag/v0.2.0). It links the matching [threat model](https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/docs/threat-model.md) and [operations runbook](https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/docs/operations.md). Development on main is newer; it is not presented as part of the reviewed release.

`assets/secops/dashboard.png` is copied unchanged from [the v0.2.0 repository image](https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/docs/images/dashboard.png). The project is owned by Danish Siddiqui and published under the [MIT License](https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/LICENSE). The screenshot's eight active findings are synthetic, not an adoption or production security metric.

The portfolio demo is independently implemented for the static site. Its five findings are invented examples on `example.com` subdomains. Status values mirror the product's open / investigating / resolved / closed workflow. The owner choices are deliberately simplified. The demo does not exercise the real API, import engine, authentication, authorization, database, or integrations, and does not claim to validate those controls.

The roadmap description is based on its [public README](https://github.com/djvirus9/awesome-devsecops-mastery-2026). No live star counts, customer numbers, testimonials, or unverified outcomes were added.

## Validation

- Jekyll and the existing static checks pass for 22 pages.
- Local Chromium: existing showcase passes 24 scenarios and 44 axe checks; SecOps passes eight scenarios, 20 axe checks, five workflow checks, and two fallback checks.
- Sample checks exercise combined search/severity filters, updates to status and owner, counts, filtered-out updates, empty results, reset, keyboard selection, reload, blocked storage, and JavaScript-disabled examples.
- Both browser suites run in Chromium and WebKit in GitHub Actions before publication.
- GitHub's Markdown renderer accepts the separate profile README. Its new case-study link is published after the portfolio deployment.

## Previews

- [Homepage open-source section](previews/open-source-home.png)
- [Desktop sample](previews/secops-demo-desktop.png)
- [Phone sample](previews/secops-demo-mobile.png)
- [Case study in dark mode](previews/secops-case-dark.png)
