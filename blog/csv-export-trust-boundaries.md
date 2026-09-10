---
title: "The Trust Boundary in a CSV Export"
permalink: /blog/csv-export-trust-boundaries/
layout: single
date: 2026-09-10
article_type: "Research note"
description: "How CVE-2026-27644 in Traccar illustrates the difference between valid CSV serialization and safe interpretation by spreadsheet software."
summary: "A value that is harmless in a database can acquire a new meaning when a spreadsheet opens it."
---

## The published finding

[CVE-2026-27644](https://github.com/traccar/traccar/security/advisories/GHSA-745r-9qgj-x7m7), credited to my account, affects Traccar’s position-data CSV exports. User-controlled fields could become formulas when a manager or administrator exported the data and opened it in spreadsheet software.

The exporter sits between two trust contexts: lower-privilege users can influence data, while a different user opens the resulting file in a more capable interpreter.

## Serialization and interpretation

A CSV library can correctly quote commas, newlines, and quotation marks while preserving a value that a spreadsheet interprets as a formula. Correct file structure and literal cell interpretation therefore need separate validation.

For example, the harmless text `=1+1` may become a calculation when opened in a spreadsheet. That is a useful local demonstration of the interpretation boundary; it does not establish command execution or data theft.

The effect of a malicious formula depends on the spreadsheet application, its configuration, available functions, and user interaction. A report should state those prerequisites explicitly.

## Review the whole route

| Stage | Review question |
|---|---|
| Input | Which users can influence exported fields? |
| Storage | Can an attacker’s value reach a record shared with another user? |
| Export | Are delimiters escaped and formula interpretation addressed? |
| Consumption | Which spreadsheet applications and import settings are supported? |
| Regression | Do legitimate numbers, names, and multiline values survive the fix? |

[OWASP’s CSV injection testing guidance](https://wstg.owasp.org/latest/4-Web_Application_Security_Testing/07-Injection/21-CSV_Injection/) discusses formula-triggering values and spreadsheet-specific pitfalls. Mitigations need validation against the consumers the product supports, including relevant save-and-reopen behavior.

## What this changes in code review

Export code deserves a trust-boundary review alongside HTML rendering, file upload, and API authorization. A field’s safety depends on the consumer interpreting it, so input validation alone cannot settle whether an export is safe.

Use the [publisher advisory](https://github.com/traccar/traccar/security/advisories/GHSA-745r-9qgj-x7m7) for affected versions, the remediation release, and the final severity assessment.
