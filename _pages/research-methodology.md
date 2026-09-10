---
title: "Security Research Methodology"
permalink: /research-methodology/
layout: single
toc: true
description: "How Danish Siddiqui investigates security findings: establish reachability, demonstrate impact, reproduce the issue, and work with maintainers through remediation."
summary: "A finding becomes useful when its prerequisites, impact, and remediation are clear enough for someone else to validate."
---

## Choose a meaningful boundary

My research includes application authorization, browser and file-handling behavior, and resource consumption in server software. I start by identifying the boundary being tested: one user accessing another user’s data, untrusted content becoming executable, or a small input causing disproportionate processing.

For bounty work, the program’s published scope and exclusions shape which hypotheses I pursue. For open-source work, I check the project’s disclosure process and supported versions.

## Establish reachability and impact

I distinguish the vulnerable code path from the conditions needed to reach it. Authentication, permissions, configuration, user interaction, and the affected version all belong in that explanation.

Impact needs evidence appropriate to the issue: the data or action available across an authorization boundary, the execution context of stored content, or the processing cost of a resource-consumption defect. Severity follows those conditions.

## Make the report reproducible

A useful report contains:

1. A concise explanation of the affected behavior.
2. Exact versions, prerequisites, and relevant configuration.
3. A minimal reproduction with expected and observed results.
4. Evidence of the impact and its limits.
5. A suggested fix or a clear description of the boundary to restore.

I keep the reproduction focused so maintainers can isolate the cause and verify the eventual change.

## Work through remediation

I respond to requests for clarification, retest fixes when available, and coordinate disclosure with the maintainer or program. Public writeups should reflect the final advisory’s classification, prerequisites, and severity assessment.

The [published research collection](/cves/) provides examples with public credit. Related notes explain the [SVG upload boundary](/blog/svg-upload-trust-boundaries/) and [CSV export boundary](/blog/csv-export-trust-boundaries/).
