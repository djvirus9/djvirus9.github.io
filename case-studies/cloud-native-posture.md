---
title: "Cloud-Native Security Posture: From Baseline to Hardened"
layout: single
author_profile: false
classes: wide portfolio-subpage
permalink: /case-studies/cloud-native-posture/
---

# Cloud-Native Security Posture: From Baseline to Hardened

**Focus:** AWS cloud posture, network segmentation, IAM hardening, detection coverage  
**Scope:** Production cloud environment supporting a high-growth consumer product

---

## The Problem

Most cloud security programs start with a CSPM tool running wild — thousands of findings, no ownership, no prioritization, and engineering teams tuning out. The goal here wasn't a bigger finding count; it was a **defensible cloud posture** that a CISO, an auditor, and a hiring manager would each look at and conclude the same thing: this is owned.

---

## The Approach

### 1. CSPM Baseline (Tool-Agnostic)

Ran baseline scans using **Prowler** and **ScoutSuite**, mapped findings against the **CIS AWS Foundations Benchmark**. Chose open-source CSPM deliberately — gives full control over rule customization, and the output is reproducible without a vendor seat.

Generated a first-pass misconfiguration inventory across:

- S3 public access, bucket policies, encryption
- IAM: users, roles, policies, access keys, MFA posture
- Security Group and NACL exposure
- CloudTrail, Config, GuardDuty coverage
- KMS key usage, rotation, cross-account access
- Encryption at rest (EBS, RDS, S3)
- Publicly reachable resources

### 2. CSPM Validation (The Step Most Teams Skip)

Raw CSPM output is noise until it's validated. Every finding went through:

- **False positive removal** (e.g., intentional public endpoints like ALB health check paths)
- **Business impact mapping** — findings on checkout, login, and payment paths get prioritized over internal admin tools
- **Owner assignment** — no unassigned findings
- **Severity recalibration** based on actual exploitability, not generic CVSS

The validated output was dramatically shorter than the raw output — which is the point.

### 3. Network Security Hardening

Structured as a layered review:

**Security Groups (primary control):**
- Inventory of all production SGs across EC2, ALB, EKS, RDS, Redis
- Identification of broad inbound rules (0.0.0.0/0), broad outbound, port reuse, orphan SGs
- Proposal of hardened rules: SG-to-SG references instead of CIDRs, port-level least privilege, explicit egress restrictions on sensitive workloads
- Phased rollout: non-prod → shadow prod → full prod, with traffic validation at each step

**NACLs (subnet-level control):**
- Complementary to SGs, not duplicative
- Tier-based subnet segmentation (ALB / App / DB)
- Validation via VPC Flow Logs

**Routing & exposure review:**
- Route table review for unnecessary 0.0.0.0/0 routes and NAT misuse
- Identification of services bypassing ALB/WAF
- Direct public IP exposure audit

**East-West / lateral movement:**
- Service-to-service traffic analysis
- Micro-segmentation strategy using SG + NACL + EKS NetworkPolicy

### 4. Data-Plane Access Controls

Review of access patterns on:

- S3 buckets (private endpoints, IAM-based access, block public access policies)
- RDS / Aurora (IAM auth, encryption, private endpoints)
- Redis / OpenSearch (network isolation, auth)

Cross-account exposure mapping to ensure no data store was accessible from unintended principals.

### 5. Detection & Visibility

Validated logging for:

- SG and NACL denies via VPC Flow Logs
- WAF block events
- IAM authentication events via CloudTrail
- GuardDuty finding coverage

Identified blind spots and proposed alerting improvements rather than dumping more logs into a SIEM nobody reads.

### 6. Control Effectiveness Testing

Actively tested:

- SG blocks via attempted unauthorized access
- NACL deny rules
- WAF + SG interaction
- Simulated direct IP access bypassing ALB
- Lateral movement attempts inside the VPC

Every control had to demonstrably block unintended traffic **with evidence in logs**. "Configured correctly" was not the bar; "observably effective" was.

---

## Working Principles

**Defense in depth, not defense by duplication.** SGs and NACLs serve different purposes. NACLs aren't just "SGs at the subnet level" — they give you a stateless, tier-based boundary that complements SGs without duplicating them.

**Change management is part of the control.** Every production network change went through documented review and approval before deployment, with rollback plans. Zero production impact was non-negotiable.

**Evidence-based prioritization.** Business-critical paths (checkout, login, payments) got the first pass. Internal tools came later. This is not "risk appetite" — it's engineering reality.

**Standards before scale.** Documented "do's and don'ts" for SG creation, NACL usage, subnet design, and routing patterns. A security engineer can't review every SG change; the org needs defaults that make the secure path the easy path.

---

## Outcomes

- **Validated, prioritized CSPM inventory** replacing the raw finding dump
- **Hardened production network posture** with demonstrably effective controls
- **Detection coverage** validated end-to-end for network and access events
- **Security design standards** for SGs, NACLs, subnets, and routing — ready for org-wide adoption
- **KT sessions with DevOps** on standards, common misconfig patterns, and review checklists

---

## Related

- [AWS Attack Path Analysis & Risk Prioritization](/case-studies/aws-attack-paths/)
- [DevSecOps Pipeline Security: Semgrep + Trivy](/case-studies/devsecops-pipeline/)
- [Building Product Security from Scratch (Licious)](/case-studies/licious-product-security/)
