# Content provenance and follow-ups

This file is excluded from the generated website.

## Sources used

- Existing portfolio source at commit `83dc252`.
- The owner's résumé, previously hosted on the site, for roles, employment dates, certifications, and reported outcomes.
- Traccar publisher advisories for CVE classifications, CVSS scores, and `djvirus9` reporter credit.
- Open-Xchange CSAF advisories for Dovecot classifications and `djvirus@yeswehack` credit.
- CVE Program records for CVE publication dates and CNA severity data.
- OWASP, MDN, and AWS documentation for the educational notes. Each note links its references.

## CVE presentation

The public showcase now contains 10 selected, published records with independently checked acknowledgments. Its homepage count is generated from `_data/cves.json`. The number is explicitly a selected-public-advisory count, not a replacement claim about the total number of CVEs ever assigned.

Six IDs from the former page did not resolve through the public CVE API during review: CVE-2026-40202 and CVE-2025-29074 through CVE-2025-29078. This does not establish that they are invalid or reserved. They have been omitted from the public showcase until publication status and supporting links are confirmed.

CVE-2024-57459 is a published SQL injection issue in CloudClassroom. The public record links a different researcher handle; a connection to Danish’s credit was not established. Restore this entry when the relevant attribution is supplied.

The source résumé’s overall 22-CVE claim was not edited during the portfolio review. Both résumé PDFs and all public résumé download links were removed from the site on 23 September 2026 at the owner's request.

## Details that need the owner’s input

- The ~30% reduction remains in the Licious and DevSecOps case studies with the résumé’s original scope: critical production-bound vulnerabilities. No period, baseline, absolute counts, or measurement method was invented. Add those details when supplied. The metric is no longer a context-free homepage tile.
- CKA, CKS, and AWS certification names are preserved. CKA and CKS years are supported by the résumé. Personal verification URLs were not available; the page does not present generic issuer links as credential verification.
- The 160+ recognition claim is retained from the résumé and linked to selected public profiles, explicitly described as an incomplete sample.
- Employment dates and titles on the homepage follow the résumé. The original general availability for global opportunities is preserved; relocation, remote-only preferences, and visa status were not inferred.
- No conference year, speaking engagement, testimonial, certificate identifier, production screenshot, benchmark result, or employer configuration was invented.

## Case studies and writing

Workflow figures summarize the existing accounts and are labelled as simplified or conceptual. The finding-record table is explicitly illustrative. CyberShield360 walkthroughs are the existing public links, now positioned near the introduction.

Three new notes are dated 10 September 2026. They discuss published research and propose verification approaches. They do not claim new experiments, publication history, or results that were not present in the sources.

Technical corrections include distinguishing SVG image rendering from document execution, treating CSV formula interpretation separately from CSV serialization, narrowing WAF XSS coverage to server-visible patterns, and acknowledging that local pre-commit hooks cannot reliably observe their own bypass.
