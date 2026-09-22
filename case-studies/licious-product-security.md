---
title: "Building Product Security from Scratch"
permalink: /case-studies/licious-product-security/
layout: single
og_title: "Building product security from scratch."
og_image: "/assets/social/licious.png"
og_image_alt: "Building product security from scratch at Licious. A case study by Danish Siddiqui, with an illustration connecting application, cloud, and governance controls."
description: "How Danish Siddiqui established Product Security at Licious: AppSec, AWS controls, DevSecOps, bug bounty governance, and ISO 27001 readiness."
summary: "As Licious’s first dedicated security engineer, I established a shared operating model for application security, cloud controls, vulnerability management, and governance."
context: "Licious · SDE-3, Product Security · May 2025–Present"
---

## The starting point

A growing consumer product needed security ownership across web, mobile, APIs, and AWS. The mandate included technical controls and the processes that turn findings into fixes: a defined scope, severity criteria, service owners, remediation expectations, and escalation paths.

I owned the security function and worked with application, platform, and leadership teams to put those pieces into day-to-day engineering workflows.

## The operating model

<figure class="flow-diagram">
  <ol>
    <li><strong>Find and validate</strong>Combine code, dependency, cloud, and researcher findings. Confirm reachability and impact.</li>
    <li><strong>Prioritize and assign</strong>Record the affected service, severity, business context, accountable owner, and fix expectation.</li>
    <li><strong>Remediate and verify</strong>Work with engineering on the change, then retest the original condition.</li>
    <li><strong>Prevent recurrence</strong>Feed recurring patterns into rules, architecture reviews, developer guidance, and control evidence.</li>
  </ol>
  <figcaption>A simplified view of the vulnerability lifecycle used to connect security tooling with engineering ownership.</figcaption>
</figure>

## Controls and delivery

| Area | My contribution | Supporting case study |
|---|---|---|
| Secure delivery | Integrated Semgrep and Trivy into CI/CD and tuned custom rules | [Pipeline security](/case-studies/devsecops-pipeline/) |
| Developer feedback | Added local checks for secrets, IaC, and common code patterns | [Pre-commit hooks](/case-studies/pre-commit-hooks/) |
| AWS posture | Validated CSPM findings and reviewed IAM, network, and data access | [Cloud posture](/case-studies/cloud-native-posture/) |
| Edge controls | Compared WAF coverage and evaluated rules before blocking | [WAF coverage](/case-studies/waf-coverage-benchmarking/) |
| External research | Defined scope, triage, researcher communication, and remediation handoffs | [Bug bounty operations](/case-studies/bug-bounty-governance/) |
| Governance | Coordinated control ownership and evidence across Engineering, IT, HR, and Finance | [ISO 27001 readiness](/case-studies/iso27001/) |

## Decisions that shaped the program

**Give every finding an owner.** I consolidated SAST, SCA, container, cloud, and bug bounty findings into a common vulnerability matrix. Resource, severity, business impact, owner, SLA, and status made it possible to follow work across tools.

**Validate before enforcement.** New checks and controls needed evidence that they detected the intended condition and worked with legitimate application behavior. WAF rules were evaluated in count mode before promotion to blocking.

**Use context when prioritizing.** Exploitability and exposure on login, checkout, and payment surfaces shaped sequencing. Raw scanner severity was an input to that decision.

## Outcomes

The security function gained defined ownership, a repeatable finding lifecycle, and shared engineering controls. CI/CD integration and custom rule tuning contributed to an approximately **30% reduction in critical production-bound vulnerabilities**.

The detailed [DevSecOps case study](/case-studies/devsecops-pipeline/) explains the controls and trade-offs behind that result. The [experience timeline](/#experience) provides the wider role and employment history.
