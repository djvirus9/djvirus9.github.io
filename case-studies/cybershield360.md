---
title: "Building CyberShield360"
permalink: /case-studies/cybershield360/
layout: single
description: "Danish Siddiqui’s role in building CyberShield360 at Invia: attack surface discovery, enrichment, prioritization, reporting, and public product demonstrations."
summary: "At Invia, I designed and helped launch an attack surface management product that turns external asset discovery into prioritized exposure information."
context: "Invia · Senior Security Engineer · September 2022–November 2023"
---

<div class="demo-links">
  <a class="button button--primary" href="https://www.youtube.com/watch?v=a-o99XjxkMw">Watch the walkthrough <span aria-hidden="true">↗</span></a>
  <a class="button" href="https://www.youtube.com/watch?v=4FVeZtl4WZs">Watch the second demo <span aria-hidden="true">↗</span></a>
</div>

## The problem

Security teams needed a repeatable view of their internet-facing assets and changing exposure. Periodic assessments and manually maintained inventories made it difficult to keep that view current across multiple customer environments.

CyberShield360 brought discovery, analysis, and reporting into a product workflow that teams could use for ongoing triage.

## My ownership

I owned product architecture and security design, defined the discovery and analysis pipeline, and worked with engineering and leadership to scope and launch the product.

This included translating security requirements into product priorities and deciding how findings should be presented to the people responsible for remediation.

## From assets to decisions

<figure class="flow-diagram">
  <ol>
    <li><strong>Discover</strong>Identify external assets and exposed services within the assessment scope.</li>
    <li><strong>Enrich</strong>Attach service information and correlate relevant vulnerability data.</li>
    <li><strong>Prioritize</strong>Use exposure and risk context to identify findings that need investigation.</li>
    <li><strong>Report</strong>Present the affected assets and supporting evidence for triage and remediation.</li>
  </ol>
  <figcaption>Conceptual product pipeline. The public walkthroughs show the delivered interface and workflow.</figcaption>
</figure>

## Design priorities

**Repeatability:** discovery and enrichment needed to support continuing assessment across environments.

**Useful signal:** service identification and CVE correlation are starting points for validation; a matched version alone should not be presented as proof of exploitability.

**Actionable output:** asset context and prioritization needed to help a security team decide what to investigate or fix next.

## Delivery and public evidence

The product reached launch and was demonstrated publicly. The walkthroughs above provide a view of its functionality, while the [Invia product page](https://www.invia.com.au/CyberShield360) provides the product context.

This work extended my role from conducting assessments to building the system through which teams discover, understand, and track exposure.
