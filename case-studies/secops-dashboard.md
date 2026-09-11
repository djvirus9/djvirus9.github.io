---
title: "SecOps Dashboard"
permalink: /case-studies/secops-dashboard/
layout: single
og_title: "From scanner findings to follow-through."
og_image: "/assets/social/secops.png"
og_image_alt: "From scanner findings to follow-through. SecOps Dashboard by Danish Siddiqui, illustrated as findings progressing from import to ownership and resolution."
wide: true
secops: true
open_source: true
toc: false
description: "Explore Danish Siddiqui’s open-source SecOps Dashboard: a real product screenshot, an interactive sample triage workflow, and the engineering decisions behind it."
summary: "A self-hosted workspace for turning scattered scanner findings into investigation, ownership, and follow-through."
context: "Independent project · Open source · MIT License"
---

<div class="so-intro">
  <div>
    <p class="eyebrow">The problem</p>
    <h2>Findings need a workflow after the scan.</h2>
    <p>A report can identify a problem without establishing who will investigate it, whether it duplicates an existing finding, or how the fix will be tracked. I built SecOps Dashboard to connect those steps in one workspace.</p>
    <dl class="so-ownership"><div><dt>My work</dt><dd>Application design, API and frontend implementation, security controls, tests, and deployment tooling.</dd></div><div><dt>What you can inspect</dt><dd>Public source, tagged releases, a threat model, and documented operating procedures.</dd></div></dl>
    <div class="actions"><a class="button button--primary" href="#secops-demo">Try the sample workflow <span aria-hidden="true">↓</span></a><a class="button" href="https://github.com/djvirus9/secops-dashboard">View source <span aria-hidden="true">↗</span></a></div>
  </div>
  <figure class="so-product-shot">
    <a href="{{ '/assets/secops/dashboard.png' | relative_url }}" aria-label="Open the full SecOps Dashboard screenshot"><img src="{{ '/assets/secops/dashboard.png' | relative_url }}" alt="SecOps Dashboard showing eight active sample findings, one critical finding, and three assets, with links to triage and imports." width="1440" height="1000" fetchpriority="high"></a>
    <figcaption>Actual application screenshot from the public repository, using synthetic demo findings. <a href="{{ '/assets/secops/dashboard.png' | relative_url }}">View full image</a>.</figcaption>
  </figure>
</div>

{% include secops-demo.html %}

<section class="so-section" aria-labelledby="secops-architecture">
  <p class="eyebrow">Architecture</p><h2 id="secops-architecture">A visible path from import to follow-up.</h2>
  <div class="so-architecture">
    <div><span class="so-node-label">Interface</span><h3>Next.js</h3><p>Findings, investigation, team workflows, and user sessions.</p></div>
    <div><span class="so-node-label">Application boundary</span><h3>FastAPI</h3><p>Scanner imports, normalization, identity, and project access checks.</p></div>
    <div><span class="so-node-label">Persistent state</span><h3>PostgreSQL</h3><p>Findings, accounts, sessions, activity, and queued notification jobs.</p></div>
    <div><span class="so-node-label">Follow-up</span><h3>Notification worker</h3><p>Deliver Slack and Jira jobs with retries and delivery-state review.</p></div>
  </div>
  <p class="so-caption">Browser requests reach the API through Next.js; scanner reports enter at the API. The worker reads queued jobs from the database. The local quickstart uses SQLite and disables external notifications.</p>
</section>

<section class="so-section" aria-labelledby="secops-decisions">
  <p class="eyebrow">Engineering decisions</p><h2 id="secops-decisions">The choices behind the interface.</h2>
  <div class="so-decisions">
    <article><span>01 / Data quality</span><h3>Make imports explainable.</h3><p>Enable scanner formats backed by representative fixtures, record import outcomes, and use project and component evidence when identifying duplicate findings.</p><p class="so-decision-note">Trade-off: incomplete context can produce a distinct finding. The application avoids guessing how to merge historical records.</p></article>
    <article><span>02 / Access</span><h3>Enforce scope at the API.</h3><p>Use individual accounts, roles, and project grants. Check access on reads and writes, including saved views, exports, and bulk triage.</p><p class="so-decision-note">Trade-off: this is a deployment for one trusted team. Project grants are not isolation between separate organizations.</p></article>
    <article><span>03 / Evidence</span><h3>Treat scanner text as untrusted.</h3><p>Keep administrative credentials out of the frontend, omit raw scan payloads by default, and neutralize formula-like cells in CSV exports.</p><p class="so-decision-note">Trade-off: targeted redaction helps limit exposure, but operators still control access, retention, and backups.</p></article>
    <article><span>04 / Delivery</span><h3>Keep failures reviewable.</h3><p>Persist notification jobs, record delivery state, and provide bounded retries. Apply migrations and document backup, restore, and account recovery.</p><p class="so-decision-note">Trade-off: an interrupted external request can have an uncertain outcome that needs review before retrying.</p></article>
  </div>
</section>

<section class="so-resources" aria-labelledby="secops-evidence">
  <div><p class="eyebrow">Inspect the work</p><h2 id="secops-evidence">Code, decisions, and a way to run it.</h2><p>The case study covers the core workflow and team controls shipped in v0.2.0. The repository tracks subsequent development.</p></div>
  <ul><li><a href="https://github.com/djvirus9/secops-dashboard#try-it-locally">Local quickstart <span aria-hidden="true">↗</span></a><span>Start a local instance and load synthetic findings.</span></li><li><a href="https://github.com/djvirus9/secops-dashboard/releases/tag/v0.2.0">v0.2.0 release <span aria-hidden="true">↗</span></a><span>Published scope and team workflow changes.</span></li><li><a href="https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/docs/threat-model.md">Threat model <span aria-hidden="true">↗</span></a><span>Trust boundaries, abuse cases, and remaining risks.</span></li><li><a href="https://github.com/djvirus9/secops-dashboard/blob/v0.2.0/docs/operations.md">Operations runbook <span aria-hidden="true">↗</span></a><span>Deployment, migrations, backup, and recovery.</span></li></ul>
</section>
