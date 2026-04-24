---
title: "Building Product Security from Scratch (Licious)"
layout: single
author_profile: true
permalink: /case-studies/licious-product-security/
---

# Building Product Security from Scratch (Licious)

**Role:** SDE-3, Product Security (Founding Security Engineer)  
**Scope:** Application Security • Cloud Security • DevSecOps • Bug Bounty • Governance  
**Context:** First dedicated security hire at a D2C product company serving millions of customers across web, mobile, and API surfaces on AWS.

---

## The Mandate

Establish the Product Security function from zero — covering application security, AWS cloud posture, DevSecOps automation, bug bounty operations, and ISO 27001:2022 readiness — while partnering directly with engineering, platform, and leadership teams.

This meant not just running scans or filing tickets, but designing the **security operating model** for a high-growth engineering org: scope definition, severity taxonomy, SLAs, review gates, and ownership handoffs.

---

## What I Built

### 1. DevSecOps Integration

- Embedded **SAST (Semgrep)** and **SCA / container scanning (Trivy)** into CI/CD pipelines across services.
- Authored **custom Semgrep rules** targeting framework-specific and business-logic patterns — beyond out-of-the-box rulesets — to improve true-positive rate and reduce developer noise.
- **Reduced critical production-bound vulnerabilities by ~30%** via consistent, automated enforcement at the pull-request stage.

### 2. Pre-Commit Security Hooks ("Shift-Left Done Right")

- Built **pre-commit hooks** that run locally on developer machines to catch:
  - Hardcoded secrets (API keys, tokens, credentials)
  - IaC misconfigurations (open Security Groups, public S3, missing encryption)
  - Obvious injection and auth patterns
- Outcome: issues caught **before code ever reaches CI**, cutting down triage cycles and developer context-switching.
- See: [Pre-Commit Hooks case study](/case-studies/pre-commit-hooks/).

### 3. Cloud-Native Security Posture

- Established **CSPM baseline** using Prowler and ScoutSuite, mapped to CIS AWS Foundations Benchmark.
- Deployed **CNAPP (ThreatMapper)** to correlate runtime context with misconfiguration findings and prioritize based on exploitability.
- Led end-to-end **cloud-native security posture improvement program**: IAM hardening, network segmentation review, data-plane access controls, detection coverage.
- See: [Cloud-Native Security Posture case study](/case-studies/cloud-native-posture/).

### 4. WAF Detection Coverage

- Benchmarked existing AWS WAF managed rules against **OWASP Core Rule Set (CRS)** to identify coverage gaps.
- Proposed rule improvements across SQLi, XSS, bot patterns, login/checkout throttling, and country-based anomaly detection.
- Validated all new rules in **COUNT mode** first to prove correctness before promoting to BLOCK.
- See: [WAF Coverage Benchmarking case study](/case-studies/waf-coverage-benchmarking/).

### 5. Bug Bounty Program Governance

- Rebuilt the program end-to-end: defined **scope, severity taxonomy, triage SLAs, and payout governance**.
- Established researcher communication patterns and remediation handoffs to service owners.
- See: [Bug Bounty Program Governance case study](/case-studies/bug-bounty-governance/).

### 6. ISO 27001:2022 Readiness

- Primary security SPOC across **Engineering, IT, HR, and Finance**.
- Established security policies, evidence collection workflows, and audit-readiness controls.
- See: [ISO 27001 Readiness case study](/case-studies/iso27001/).

### 7. Unified Vulnerability Management

- Consolidated findings from SAST, SCA, CSPM, container scanning, bug bounty, and web-level scanning into a **single unified vulnerability matrix** with resource, severity, business impact, owner, SLA, and status.
- Gave leadership a **single source of truth** for security risk rather than tool-by-tool dashboards.

---

## Working Principles

**Developer-first tooling.** Every control I added went through the lens of: *does this help developers ship safely, or does it just generate noise?* Pre-commit hooks, custom Semgrep rules, and CSPM tuning were all shaped by that question.

**Outcome over output.** A CSPM dashboard with 2,000 findings is not security — it's an email list. I prioritized by **business impact and exploitability**, not by raw count.

**Evidence before enforcement.** Every new WAF rule, SG change, or pipeline gate ran in observe-only mode first, with logs reviewed, before moving to enforcement. Zero production impact was a hard constraint, not a goal.

**Ownership as a product.** The most sustainable security outcome wasn't a scan — it was getting engineering teams to own their security findings, backed by clear SLAs and governance.

---

## Related Case Studies

- [DevSecOps Pipeline Security: Semgrep + Trivy](/case-studies/devsecops-pipeline/)
- [Cloud-Native Security Posture](/case-studies/cloud-native-posture/)
- [Pre-Commit Hooks: Shifting Security Left](/case-studies/pre-commit-hooks/)
- [WAF Detection Coverage Benchmarking](/case-studies/waf-coverage-benchmarking/)
- [Bug Bounty Program Governance at Scale](/case-studies/bug-bounty-governance/)
- [ISO 27001 Readiness as Security Ownership](/case-studies/iso27001/)
