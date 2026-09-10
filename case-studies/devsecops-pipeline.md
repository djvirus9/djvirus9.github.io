---
title: "Security in the Delivery Pipeline"
permalink: /case-studies/devsecops-pipeline/
layout: single
description: "Designing CI/CD security with Semgrep, Trivy, tuned rules, clear finding ownership, and gradual enforcement based on confidence and risk."
summary: "I integrated SAST and container scanning into delivery workflows, then tuned enforcement and remediation ownership so teams could act on the results."
context: "AppSec · CI/CD · Semgrep · Trivy"
---

## The problem and my role

Security testing varied between services and often arrived late in delivery. Unowned findings and false positives made it harder for developers to distinguish urgent defects from background noise.

I owned tool selection, integration, rule tuning, enforcement thresholds, and the operational handoff to service owners, working with application and platform teams.

## Where the controls run

<figure class="flow-diagram">
  <ol>
    <li><strong>Local commit</strong>Fast checks for secrets and common unsafe patterns provide feedback while the developer is editing.</li>
    <li><strong>Pull request</strong>Semgrep examines code changes with framework-specific rules and actionable remediation messages.</li>
    <li><strong>Container build</strong>Trivy surfaces image and dependency vulnerabilities for contextual review.</li>
    <li><strong>Risk decision</strong>High-confidence findings trigger remediation or an explicit exception with an accountable owner.</li>
  </ol>
  <figcaption>Simplified control placement. Local hooks provide feedback; CI runs checks independently.</figcaption>
</figure>

## Rules and enforcement

I selected Semgrep for readable rules and the ability to express application-specific patterns. Custom rules complemented the default rulesets, with tuning focused on framework misuse and recurring code issues.

Trivy provided container and dependency findings during builds. Severity informed review alongside exploitability and the affected service; indiscriminately blocking every reported CVE would create avoidable friction.

New checks began with visibility and feedback. Enforcement focused on findings with enough confidence and context for developers to understand the required change.

## What an actionable finding contains

The following is an illustrative record format, with example values:

| Field | Example |
|---|---|
| Affected component | A service’s changed source file or container image |
| Detection evidence | Rule ID, location, relevant code, and affected version |
| Risk explanation | The input or dependency condition that makes the issue reachable |
| Owner | The team responsible for the affected service |
| Resolution | Fix guidance, due date, and validation evidence |
| Exception | Named approver, reason, expiry, and compensating control |

The aim was a finding that a service owner could act on without starting a second investigation simply to understand the report.

## Outcomes and measurement

The rollout contributed to an approximately **30% reduction in critical production-bound vulnerabilities**, alongside more consistent security coverage before release.

I also tracked developer fix turnaround, recurring vulnerability classes, and adoption across teams. These indicators helped identify noisy rules and gaps in ownership. Scanner finding counts alone were insufficient to evaluate the program.

## Trade-offs

- Early, reliable feedback helped establish trust before introducing blocking checks.
- Local hooks improved turnaround, but could be bypassed; CI remained an independent control.
- Rule coverage needed ongoing maintenance as frameworks and application patterns changed.
- Exceptions needed accountable ownership to avoid becoming permanent bypasses.

Read the related [pre-commit workflow](/case-studies/pre-commit-hooks/) and [Product Security operating model](/case-studies/licious-product-security/).
