# Compact homepage and project sharing cards

The homepage now leads with a larger portrait, a concise introduction, and direct work, email, résumé, LinkedIn, and GitHub links. Three flagship projects show contribution, delivery, and a clear route to the full case study: Licious, SecOps Dashboard, and CyberShield360.

The CyberShield explorer and captioned video remain on their case-study and tour pages. The SecOps sample workflow remains on its case study. Their scripts, styles, and media do not load on the homepage. The DevSecOps Roadmap, writing, community, résumé, and full case-study index remain discoverable.

Experience and certifications use native expandable sections, including without JavaScript. Existing homepage anchors for experience, credentials, selected work, research, open source, and CyberShield still resolve. Old CyberShield stage anchors lead to its project card, which links to the full workflow; stage-specific URLs on the case study retain their original behavior.

## Content and images

- Contributions and outcomes come from the existing case studies and résumé; no new quantified results or customer claims were added.
- The credibility section links directly to the existing Traccar and Dovecot publisher acknowledgments. The count is explicitly selected CVE advisories, not a lifetime total.
- Certification names remain résumé-backed. Personal verification URLs and publishable colleague recommendations were requested but not supplied, so no verification badges, quotations, or placeholders were added.
- The approximately 30% result remains in the detailed Licious and pipeline case studies. It was not promoted to the homepage without a baseline and measurement period.
- The existing portrait is unchanged; responsive image selection uses the existing 224- and 747-pixel assets.
- Three original SVG illustrations distinguish the projects. They are decorative previews of the work, not representations of private product interfaces. The actual SecOps screenshot remains on its case study.
- Each flagship case study has an individual 1200 × 630 PNG, headline, and image description for Open Graph and Twitter sharing. `scripts/render_project_previews.py` regenerates these using local Chromium and the authored SVGs.

## Review and validation

At a 390 × 844 viewport, the default homepage is 2,663 pixels high, down from 6,880 pixels (about 61% shorter). The introduction, all three projects, research evidence, and contact panel end at 2,075 pixels, approximately 2.5 screens. Expanded experience and credentials add optional reading below that point.

The default page has no horizontal overflow at 320, 390, 768, or 1440 pixels. Light and dark previews were reviewed. The homepage remains usable with JavaScript disabled; keyboard activation expands the background sections and all three project links reach their case studies.

Local checks passed for all 22 generated pages and both Chromium browser suites: 32 viewport/theme/page scenarios and 54 automated accessibility checks, plus video playback, captions, seeking, modal focus handling, triage updates, keyboard controls, and no-JavaScript fallbacks. CI runs the same suites in Chromium and WebKit before deployment.

Preview images:

- [Mobile homepage](previews/home-refined-mobile.png)
- [Desktop homepage](previews/home-refined-desktop.png)
- [Dark mobile homepage](previews/home-refined-dark.png)
