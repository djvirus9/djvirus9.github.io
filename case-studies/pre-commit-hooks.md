---
title: "Pre-Commit Hooks: Shifting Security Left"
layout: single
author_profile: false
classes: wide portfolio-subpage
permalink: /case-studies/pre-commit-hooks/
---

# Pre-Commit Hooks: Shifting Security Left

**Focus:** Developer-first security tooling, secrets prevention, IaC safety, feedback-loop design

---

## The Problem with "Shift-Left"

"Shift-left security" is one of the most overused phrases in the industry. In practice, most organizations interpret it as: *run the same scans, just earlier in the pipeline*. That's not shift-left — that's shift-slightly-left. The security signal still reaches the developer via a Jenkins comment 20 minutes after they've context-switched to the next task.

**True shift-left** means the developer gets feedback *before* they push code. That's what pre-commit hooks solve.

---

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

**2. It's opt-in-by-default-on.**  
Installed via a single `pre-commit install` during repo setup. No dashboard to log into. No tickets to triage. It's either green or red.

**3. False positives cost credibility, not just time.**  
I tuned each rule aggressively before rollout. A hook that blocks a commit for a legitimate reason builds trust. A hook that blocks a commit for the wrong reason gets added to `--no-verify` and stays there forever.

**4. Bypass is allowed — and tracked.**  
`git commit --no-verify` exists for a reason. Emergency hotfixes happen. But bypasses are logged centrally, so a pattern of bypassing by a specific developer or service is visible without requiring heavy enforcement.

**5. Hooks complement CI, they don't replace it.**  
CI still runs full SAST/SCA on every PR. Pre-commit catches the obvious stuff locally; CI catches the harder stuff with more time and compute. They're layers, not substitutes.

---

## Lessons Learned

- **Start small.** Two rules developers don't hate is better than twenty rules that all get bypassed.
- **Ship a "why this fired" message with every rule.** Don't just say "secret detected" — say "this looks like an AWS access key because `AKIA` + 16 alphanumerics". Developers will respect hooks that respect their time.
- **Measure bypass rate, not block rate.** A high block rate with low bypass rate is a successful rollout. A low block rate with high bypass rate is theater.
- **Pair pre-commit hooks with a "what to do if this fires" wiki page.** The developer shouldn't have to DM security to get unblocked.

---

## Related

- [DevSecOps Pipeline Security: Semgrep + Trivy](/case-studies/devsecops-pipeline/)
- [Building Product Security from Scratch (Licious)](/case-studies/licious-product-security/)
