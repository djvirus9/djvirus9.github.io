---
title: "Case Studies"
permalink: /case-studies/
layout: single
wide: true
description: "Engineering case studies from Danish Siddiqui: SecOps Dashboard, Product Security at Licious, DevSecOps pipelines, AWS controls, and CyberShield360."
summary: "The problems, decisions, and operating models behind my work in product security."
---

<div class="card-grid">
{% for study in site.data.case_studies %}{% include work-card.html study=study level=2 %}{% endfor %}
</div>
