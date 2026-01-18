---
title: "Building Product Security from Scratch (Licious)"
permalink: /case-studies/licious-product-security/
layout: single
---

# Flagship Case Study: Building Product Security from Scratch at a High-Growth Product Company

## Context
Licious is a high-growth consumer product company with rapidly evolving web, mobile, API, and cloud infrastructure. At the time I joined, there was no centralized product security function, limited visibility into security risk, and no consistent security ownership across engineering teams.

I joined as the first dedicated Product Security Engineer, with the mandate to establish, scale, and operationalize product security end-to-end without slowing engineering velocity.

## Problem Statement
The core challenges were not tool gaps, but structural security risks:
- No single owner for product security decisions
- Security findings scattered across teams with inconsistent triage
- Limited proactive detection of application and cloud misconfigurations
- No standardized vulnerability lifecycle or severity model
- Increasing external attack surface and bug bounty signal without governance
- Compliance expectations (ISO 27001) without a mature security baseline

The risk was not theoretical: vulnerabilities were reaching late stages of delivery, remediation cycles were slow, and security decisions were reactive rather than preventative.

## My Role and Ownership
As the first and sole Product Security owner, I was responsible for:
- Defining the product security strategy across AppSec, Cloud Security, and DevSecOps
- Making security architecture and tooling decisions
- Embedding security into the SDLC with minimal developer friction
- Acting as the single point of accountability for vulnerabilities, bug bounty, and compliance readiness
- Partnering directly with engineering, platform, IT, HR, and leadership teams

This role required both hands-on execution and decision-making authority.

## Approach and Strategy
### 1. Establishing Security Ownership and Baselines
I started by defining clear security ownership, risk classification, and remediation expectations across teams. This included:
- A unified vulnerability severity and prioritization model
- Clear ownership mapping for services and infrastructure
- A standard vulnerability lifecycle from discovery to closure

This shifted security from "best effort" to measurable accountability.

### 2. Embedding Security into the SDLC (Shift-Left)
Rather than relying on periodic testing, I focused on early, automated detection:
- Integrated SAST (Semgrep) into CI/CD to catch code-level issues early
- Added container and dependency scanning (Trivy) for build-time risk visibility
- Tuned findings to reduce noise and improve developer trust in results

The goal was not maximum findings, but actionable signal that developers would actually fix.

### 3. Cloud Security and Attack Path Visibility
To address cloud risk at scale, I designed and operated a lightweight AWS cloud security posture program:
- Used CSPM tools (Prowler, ScoutSuite) to continuously assess AWS configurations
- Identified real attack paths, not just isolated misconfigurations
- Prioritized fixes based on exploitability and business impact, not checklist compliance

This allowed teams to focus on high-risk paths rather than chasing low-impact alerts.

### 4. Bug Bounty Program Design and Governance
I revamped and operated the bug bounty program end-to-end, including:
- Defining scope boundaries aligned with business risk
- Creating a consistent severity taxonomy and triage workflow
- Establishing payout governance to balance researcher engagement and signal quality
- Acting as the primary triager, coordinating remediation with engineering teams

This transformed bug bounty from a reactive inbox into a controlled external signal.

### 5. Compliance Enablement (ISO 27001:2022)
Alongside technical controls, I acted as the primary security SPOC for ISO 27001 readiness, working across:
- Engineering (technical controls and evidence)
- IT and HR (access control, policies, processes)
- Leadership (risk acceptance and prioritization)

Rather than treating compliance as a checklist, I aligned controls with actual security posture to avoid "paper security".

## Impact and Outcomes
- ~30% reduction in critical production-bound vulnerabilities through early detection
- Established a repeatable product security operating model
- Improved remediation speed and developer security adoption
- Enabled proactive identification of high-risk cloud attack paths
- Brought structure and governance to external vulnerability reporting
- Created a security baseline that supported ISO 27001:2022 readiness

Most importantly, security shifted from a reactive function to a trusted engineering partner.

## Key Skills Demonstrated
Product Security Strategy and Ownership • Application and API Security • AWS Cloud Security and Attack Path Analysis • DevSecOps and Security Automation • Bug Bounty Operations and Governance • Security Risk Management and Compliance Enablement

**Skills & Signals:** Secure SDLC · OWASP Top 10 · OWASP API Top 10 · Vulnerability Management Lifecycle · CSPM · Stakeholder Management

## Why This Matters
This engagement demonstrates my ability to build security programs from zero, make pragmatic security decisions, and operate as a senior individual contributor with ownership mindset -- not just execute tools or assessments.
