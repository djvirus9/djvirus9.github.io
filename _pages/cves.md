---
title: "CVE Showcase"
layout: single
author_profile: false
classes: wide portfolio-subpage
permalink: /cves/
---

# CVE Showcase

A curated list of CVEs credited to my research across open-source and commercial software. Findings span pre-authentication denial-of-service conditions, authentication/authorization flaws, injection bugs, and security misconfigurations in widely deployed software.

**Profiles:** [NVD](https://nvd.nist.gov/vuln/search) • [YesWeHack](https://yeswehack.com/hunters/djvirus) • [Bugcrowd](https://bugcrowd.com/djvirus) • [HackerOne](https://hackerone.com/djvirus)

---

## Denial of Service (CWE-400 / CWE-407)

Algorithmic complexity and resource exhaustion bugs in widely deployed server software — the kind of issues that are easy to miss in code review but become catastrophic at scale.

| CVE | Impact | Notes |
|-----|--------|-------|
| [CVE-2026-27859](https://nvd.nist.gov/vuln/detail/CVE-2026-27859) | Pre-auth O(n^2) CPU DoS in Dovecot/Pigeonhole | Identified in the RFC 2231 MIME parameter parser. Pre-authentication, reachable over standard IMAP/SMTP. Severity 5.3 (Medium). |
| [CVE-2026-27644](https://nvd.nist.gov/vuln/detail/CVE-2026-27644) | Resource exhaustion | — |
| [CVE-2026-27693](https://nvd.nist.gov/vuln/detail/CVE-2026-27693) | Resource exhaustion | — |
| [CVE-2026-27694](https://nvd.nist.gov/vuln/detail/CVE-2026-27694) | Resource exhaustion | — |

---

## Authentication & Authorization (CWE-287 / CWE-345 / CWE-749)

Missing validation, improper state management, and exposure of sensitive operations — common patterns I hunt for in auth flows and browser extensions.

| CVE | Impact | Notes |
|-----|--------|-------|
| [CVE-2026-40202](https://nvd.nist.gov/vuln/detail/CVE-2026-40202) | Authentication/authorization flaw | — |
| [CVE-2026-40016](https://nvd.nist.gov/vuln/detail/CVE-2026-40016) | Authentication/authorization flaw | — |
| [CVE-2026-40017](https://nvd.nist.gov/vuln/detail/CVE-2026-40017) | Authentication/authorization flaw | — |
| [CVE-2026-40014](https://nvd.nist.gov/vuln/detail/CVE-2026-40014) | Authentication/authorization flaw | — |
| [CVE-2026-25648](https://nvd.nist.gov/vuln/detail/CVE-2026-25648) | Authorization bypass | — |
| [CVE-2026-25649](https://nvd.nist.gov/vuln/detail/CVE-2026-25649) | Authorization bypass | — |
| [CVE-2026-23521](https://nvd.nist.gov/vuln/detail/CVE-2026-23521) | Missing validation | — |

---

## Injection & Input Handling (CWE-74 / CWE-79 / CWE-89)

| CVE | Impact | Notes |
|-----|--------|-------|
| [CVE-2025-29074](https://nvd.nist.gov/vuln/detail/CVE-2025-29074) | Injection / input handling | — |
| [CVE-2025-29075](https://nvd.nist.gov/vuln/detail/CVE-2025-29075) | Injection / input handling | — |
| [CVE-2025-29076](https://nvd.nist.gov/vuln/detail/CVE-2025-29076) | Injection / input handling | — |
| [CVE-2025-29077](https://nvd.nist.gov/vuln/detail/CVE-2025-29077) | Injection / input handling | — |
| [CVE-2025-29078](https://nvd.nist.gov/vuln/detail/CVE-2025-29078) | Injection / input handling | — |

---

## Other Findings

| CVE | Notes |
|-----|-------|
| [CVE-2024-57459](https://nvd.nist.gov/vuln/detail/CVE-2024-57459) | Security misconfiguration / exposure |

---

## Approach

My CVE research typically follows one of three paths:

1. **Codebase audits of widely deployed open-source software** — mail servers (Dovecot), logging frameworks (Log4j ecosystem), OAuth/OIDC libraries, and browser extensions. I look for algorithmic complexity issues, missing validation, and authentication edge cases.

2. **Bug bounty engagements on YesWeHack, Bugcrowd, HackerOne, and Intigriti** — especially programs with open-source components, where findings can be responsibly disclosed upstream and receive CVE credit.

3. **Targeted research** on emerging attack surfaces — currently focused on AI/LLM integrations (see [OWASP LLM Top 10 writeup](/blog/llm-security-owasp-top10/)) and browser extension security.

See [Security Research Methodology](/research-methodology/) for how I approach acceptance probability, triager communication, and report quality.

---

## Beyond CVEs — Hall of Fame & Program Rankings

- **160+ Hall of Fame acknowledgements** from Atlassian, Google, Mastercard, SoundCloud, Paytm, Achmea, and others
- **Top 3 Bug Hunter** on Convertkit (Bugcrowd)
- **Synack Red Team member** — invite-only private vulnerability research network (<10% acceptance rate)

*This list is kept intentionally concise. Additional CVEs, Hall of Fame acknowledgements, and private bug bounty findings are available on request.*
