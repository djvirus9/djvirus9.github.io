---
title: "Security Research Methodology"
layout: single
author_profile: true
permalink: /research-methodology/
---

# Security Research Methodology

How I approach independent security research, CVE hunting, and bug bounty work. This page exists because I've found that *how* you hunt matters more than *what tools* you use — and the "how" is rarely documented.

---

## The Two Phases of a Finding

Every finding I ship goes through two distinct phases, and I treat them differently:

### Phase 1 — Discovery

This is the part most researchers focus on: reading code, fuzzing endpoints, identifying the bug. I spend the majority of my time here in **three places**:

- **Codebase audits of widely deployed open-source software.** Mail servers (Dovecot), logging frameworks (Log4j ecosystem), OAuth/OIDC libraries, and browser extensions. High impact because a single bug affects thousands of deployments; high acceptance rate because open-source maintainers generally act fast on well-documented reports.
- **Bug bounty engagements on YesWeHack, Bugcrowd, HackerOne, Intigriti.** I favor programs with open-source components where findings can be responsibly disclosed upstream for CVE credit in addition to the bounty.
- **Targeted research on emerging attack surfaces.** Currently: AI/LLM integrations, browser extension security, algorithmic complexity bugs in parsers.

### Phase 2 — Acceptance

This is where most researchers lose findings, and where I've learned the most over the years. A technically valid bug is not the same as an *accepted* bug. Acceptance depends on:

- **Reachability.** Is it pre-auth or post-auth? Own-session or cross-user? Programs pay for multi-user, reachable impact — not for bugs that crash your own session.
- **Measurable impact.** "DoS" is not an impact claim; "10 requests causing 60 seconds of CPU time per core" is.
- **Concrete exploit chain.** Type confusion with no demonstrated gadget = informative. Type confusion with a PoC that reads a file = critical.
- **Fit with program rules.** Before I spend time on a finding, I verify it's in scope, not excluded by program rules (e.g., MITM-required issues are usually excluded), and not already duplicated.

I make a **GO / NO-GO acceptance probability assessment** before investing in a full writeup. If the probability is below ~40%, I keep hunting rather than writing it up.

---

## What a Good Report Looks Like

The shortest report I can write that gives the triager everything they need to reproduce, validate, and assign severity — in that exact order.

**Standard structure:**

1. **Summary** (one paragraph — what the bug is, what it impacts, why it matters)
2. **Affected versions / configurations** (exact — not "latest")
3. **Reproduction steps** (numbered, copy-pasteable, includes exact commands / requests)
4. **Proof of Concept** (minimal working exploit or curl command)
5. **Impact** (measurable — "X requests cause Y seconds of CPU per core", not "DoS possible")
6. **Suggested fix** (patch, mitigation, or at minimum the class of fix needed)
7. **Credit preference** (researcher handle, whether CVE credit is desired)

No marketing language. No CVSS-score padding. No "this is critical because security is important."

---

## Triager Relationship Management

This is underrated. Triagers see hundreds of reports per week. The ones that get taken seriously tend to be:

- **From researchers with a track record of high-signal reports.** Build this deliberately over time.
- **Written at the triager's level.** Don't over-explain basics; don't under-explain the novel part of the bug.
- **Responsive to clarifying questions within hours, not days.** Momentum matters.
- **Gracious about severity adjustments.** If a triager rates something Medium and I'd argue High, I make the case once with evidence, then I accept the decision. Arguing every severity call erodes trust.

---

## Lessons from Acceptance Patterns

Observations from hundreds of submissions:

- **Pre-auth > post-auth by a wide margin.** Even modest pre-auth bugs typically outpay significant post-auth bugs.
- **Measurable multi-user impact is the dividing line.** A bug that crashes my own session is informative; a bug that crashes every active user's session is payable.
- **Algorithmic complexity (DoS) bugs are under-reported and well-received** when documented with concrete CPU/memory measurements.
- **Browser extension bugs are growing** — sender validation, web-accessible resource exposure, and credential handling in background scripts are all active areas.
- **"Hardcoded credentials in a repo" needs a demonstrated impact path.** A production API key in a public repo is high impact; a dev API key with no prod reachability is informative.

---

## What I Don't Do

- **I don't file duplicate reports.** If I find something and the program has a likely duplicate, I move on.
- **I don't inflate severity.** Programs notice. Triagers notice. It costs future findings.
- **I don't publish PoCs before remediation.** Disclosure timelines exist for a reason.
- **I don't share internal details of employer security work.** There's a clean line between "what I built" (fair for portfolio) and "how their WAF rules are configured" (never).

---

## Related

- [CVE Showcase](/cves/)
- [Exploring LLM Security Risks & OWASP Top 10 for LLMs](/blog/llm-security-owasp-top10/)
- [Bug Bounty Program Governance at Scale](/case-studies/bug-bounty-governance/)
