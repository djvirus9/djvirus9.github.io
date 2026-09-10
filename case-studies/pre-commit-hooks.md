---
title: "Pre-Commit Hooks: Shifting Security Left"
layout: single
author_profile: false
permalink: /case-studies/pre-commit-hooks/
description: "Added local checks for secrets, IaC configuration, and common code patterns, backed by independent CI enforcement."
summary: "Added local checks for secrets, IaC configuration, and common code patterns, backed by independent CI enforcement."
---

**Focus:** Developer-first security tooling, secrets prevention, IaC safety, feedback-loop design

---

## The feedback problem

Security findings that arrive after a developer has moved to another task create extra investigation and context switching. I added local checks to surface common problems at commit time, alongside independent checks in CI.

## What I Built

A pre-commit hook framework (built on `pre-commit.com`) that runs automatically on `git commit` and catches:

### 1. Hardcoded Secrets
- API keys, access tokens, passwords, private keys
- Custom regex patterns for internal service credentials
- Entropy-based detection for high-randomness strings

### 2. IaC Misconfigurations
- Open Security Groups (`0.0.0.0/0` on sensitive ports)
- Public S3 buckets
- Missing encryption (KMS / SSE)
- IAM policies with `*` actions or resources
- Terraform and CloudFormation covered

### 3. Obvious Vulnerability Patterns
- String-concatenation SQL queries
- Use of deprecated/vulnerable crypto (MD5, SHA1 for auth)
- Hardcoded secrets passed to subprocess calls
- Disabled TLS verification

### 4. Safe Defaults
- `.gitignore` hygiene checks (no `.env`, `.pem`, `.key` files)
- Large file warnings (common vector for accidentally committed databases)

---

## Why It Works (When Most Shift-Left Initiatives Don't)

**1. The feedback loop is instantaneous.**  
The developer sees the security issue *on the command that just broke* — not in a PR comment 15 minutes later. That matters because developers are still in context, still have the code in their head, and fix it in seconds rather than minutes.

**2. Setup is part of repository onboarding.**

Installed via a single `pre-commit install` during repo setup. No dashboard to log into. No tickets to triage. It's either green or red.

**3. False positives cost credibility, not just time.**  
I tuned each rule aggressively before rollout. A hook that blocks a commit for a legitimate reason builds trust. A hook that blocks a commit for the wrong reason gets added to `--no-verify` and stays there forever.

**4. CI remains the enforcement boundary.**

A local hook cannot reliably observe its own bypass through `git commit --no-verify`. Required CI checks run independently, and any CI exception needs a documented reason and owner.

**5. Hooks complement CI, they don't replace it.**  
CI still runs full SAST/SCA on every PR. Pre-commit catches the obvious stuff locally; CI catches the harder stuff with more time and compute. They're layers, not substitutes.

---

## Lessons Learned

- **Start small.** Two rules developers don't hate is better than twenty rules that all get bypassed.
- **Ship a "why this fired" message with every rule.** Don't just say "secret detected" — say "this looks like an AWS access key because `AKIA` + 16 alphanumerics". Developers will respect hooks that respect their time.
- **Track CI exceptions and time to fix.** These provide observable feedback on enforcement and developer friction; local hook bypasses cannot be counted reliably by the hook itself.
- **Pair pre-commit hooks with a "what to do if this fires" wiki page.** The developer shouldn't have to DM security to get unblocked.

---

## Related

- [DevSecOps Pipeline Security: Semgrep + Trivy](/case-studies/devsecops-pipeline/)
- [Building Product Security from Scratch (Licious)](/case-studies/licious-product-security/)
