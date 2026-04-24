---
title: "WAF Detection Coverage: Benchmarking Against OWASP CRS"
layout: single
author_profile: true
permalink: /case-studies/waf-coverage-benchmarking/
---

# WAF Detection Coverage: Benchmarking Against OWASP CRS

**Focus:** Rule coverage analysis, safe rule rollout, count-mode validation, false-positive discipline

---

## Why Managed Rules Aren't Enough

AWS WAF's managed rule groups are a sensible default — but relying entirely on them leaves gaps. Managed rules are updated on AWS's cadence, tuned for generic traffic, and don't know anything about your application's business logic. For a consumer-facing product with checkout, auth, and payment surfaces, "generic" is not good enough.

The approach here was to **benchmark AWS WAF's existing coverage against the OWASP Core Rule Set (CRS)** — the industry-standard open-source ruleset used by ModSecurity — and close the gaps with custom rules.

---

## The Process

### 1. Gap Analysis

Mapped current AWS WAF managed rules against OWASP CRS categories:

- **SQLi** — where were the SQL injection patterns we'd miss?
- **XSS** — was reflected / stored / DOM-based XSS equally covered?
- **Request smuggling, path traversal, LFI/RFI** — CRS staples, often under-covered in managed rules
- **Bot patterns** — beyond AWS BotControl's built-in categories
- **Country-based anomaly detection** — business-specific geographic patterns
- **Login/checkout throttling** — rate limits tuned to actual user behavior, not generic thresholds

The output was a **coverage matrix** with every CRS category rated: covered / partially covered / gap.

### 2. Rule Proposal

For each identified gap, proposed a specific AWS WAF rule with:

- **Rule logic** (regex, string match, rate-based, or custom)
- **Expected true-positive pattern** (what real attack this catches)
- **Expected false-positive risk** (what legitimate traffic might trip it)
- **Severity and business impact**

This turned the WAF into a **documented detection surface** rather than a black box of "whatever AWS ships by default."

### 3. COUNT Mode First

Every new rule went into **COUNT mode** before enforcement. Count mode logs matches without blocking — giving you real production traffic data to validate against.

Minimum 7 days of count-mode observation per rule, checking:

- Did the rule fire on actual attack traffic? (look at request patterns, sources, user-agents)
- Did it fire on legitimate traffic? (checkout flows, login, session validation)
- Did the firing rate change with daily/weekly business cycles?

Only after a clean count-mode period did a rule move to **BLOCK**.

### 4. Impact Study

For rules promoted to BLOCK:

- Checkout conversion rate monitored pre- and post-enforcement
- Customer support ticket volume tracked for "site is broken" reports
- WAF log patterns reviewed for unexpected blocks

A WAF rule that breaks a single real checkout costs more than the rule catches in value. Zero false positives during peak business hours was the hard bar.

### 5. Bot Control Tuning

Beyond the CRS ruleset, tuned AWS WAF BotControl specifically. A common issue: legitimate mobile clients using generic HTTP library user-agents get classified as bots by `CategoryHttpLibrary` rules, creating unnecessary CAPTCHAs on critical `/api/` paths. The fix was surgical — not disabling BotControl, but creating scoped exceptions with ongoing monitoring.

---

## Working Principles

**Benchmark before you build.** Every custom rule should be justified against an external standard (OWASP CRS, OWASP API Top 10). Custom rules invented from scratch tend to duplicate managed rules or miss well-known patterns entirely.

**Count mode is not optional.** Any rule going straight to BLOCK in production is a bet with customer revenue. Count mode is the cost of doing business safely.

**The WAF is a detection layer, not a prevention layer.** Treat it like an IDS with enforcement capability. Application-level controls (auth, input validation, CSRF, rate limiting in the app) are the real defense. The WAF catches the obvious stuff and buys time when an app-level bug ships.

**Document every rule's intent.** A WAF rule without a written reason for existing will be deleted the first time it causes a support ticket. Rules with clear "this catches X, its expected FPR is Y" documentation survive incidents.

---

## Outcomes

- **Documented CRS coverage map** for AWS WAF — every category rated, every gap tracked
- **Rule improvement backlog** with clear priority and expected impact
- **COUNT-mode validation discipline** before any BLOCK promotion
- **Bot control tuning** reducing false-positive CAPTCHA load on legitimate API traffic
- **Zero production conversion impact** across the rollout

---

## Related

- [Cloud-Native Security Posture](/case-studies/cloud-native-posture/)
- [Building Product Security from Scratch (Licious)](/case-studies/licious-product-security/)
