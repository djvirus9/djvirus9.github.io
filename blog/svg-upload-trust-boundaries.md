---
title: "When an Image Upload Becomes Executable Content"
permalink: /blog/svg-upload-trust-boundaries/
layout: single
date: 2026-09-10
article_type: "Research note"
description: "Lessons from CVE-2026-25648 in Traccar: SVG content, browser execution contexts, and how to validate an upload’s behavior when another user retrieves it."
summary: "An upload review needs to follow the file all the way to the browser that consumes it."
---

## The published finding

[CVE-2026-25648](https://github.com/traccar/traccar/security/advisories/GHSA-mc2g-mjqh-8x78), credited to my account, concerns stored XSS through Traccar’s SVG device-image uploads. An authenticated uploader could store active content that executes in another user’s browser when opened in an executable context.

The significant boundary is between the user who supplies a file and the user who later consumes it. A legitimate upload permission does not establish that the uploaded document is safe to execute.

## Follow the retrieval path

A review should cover both ends of the workflow:

1. Which file formats does the application need, and how does it validate their contents?
2. What content type and response headers does the retrieval endpoint send?
3. Does the browser receive the file as an image resource, a document, or an embedded object?
4. Does that document share an origin with an authenticated application?

An SVG loaded through an image element has different execution behavior from an SVG opened as a document. [MDN documents the restrictions for SVG used as an image](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image). A test should record the exact retrieval and rendering path instead of treating every display of the same file as equivalent.

## A useful verification matrix

| Scenario | What to verify |
|---|---|
| Normal image upload | Supported images remain usable |
| Unsupported active format | The upload policy rejects it consistently |
| Direct navigation to a stored file | Untrusted content cannot execute with application privileges |
| A second user retrieves the file | The cross-user boundary remains intact |
| Replacement or renamed file | Content validation and serving behavior stay consistent |

These are proposed regression checks, not a claim that every path was affected in Traccar.

## Defensive choices

Keep the accepted formats tied to the product’s actual needs. For raster-only features, reject active document formats. If active formats are essential, review sanitization and isolate untrusted content from authenticated application origins. Validate file contents rather than trusting an upload’s supplied MIME type. These choices align with [OWASP’s upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

The [publisher advisory](https://github.com/traccar/traccar/security/advisories/GHSA-mc2g-mjqh-8x78) contains the affected-version information, severity assessment, and researcher credit.
