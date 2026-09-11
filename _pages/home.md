---
title: "Danish Siddiqui"
permalink: /
layout: single
wide: true
cybershield: true
description: "Founding security engineer at Licious. Explore Danish Siddiqui’s work in AppSec, AWS, Kubernetes, DevSecOps, and published vulnerability research."
---

<section class="hero" aria-labelledby="intro-title">
  <div>
    <p class="eyebrow">Senior Product Security Engineer</p>
    <h1 id="intro-title">Danish Siddiqui</h1>
    <p class="hero__lead">I build product security programs—from the first control to engineering-wide adoption.</p>
    <p class="hero__focus">AppSec &nbsp;·&nbsp; AWS &amp; Kubernetes &nbsp;·&nbsp; DevSecOps</p>
    <div class="actions">
      <a class="button button--primary" href="{{ '/case-studies/' | relative_url }}">Explore my work <span aria-hidden="true">→</span></a>
      <a class="button" href="{{ '/assets/Danish_Siddiqui_Security_Engineer_Resume.pdf' | relative_url }}">Résumé PDF</a>
      <a class="button" href="mailto:danishismyname1@gmail.com">Get in touch</a>
    </div>
  </div>
  <div class="hero__profile">
    <img class="hero__avatar" src="{{ '/assets/avatar-224.jpg' | relative_url }}" alt="Danish Siddiqui" width="112" height="112" fetchpriority="high">
    <p><strong>Founding security engineer at Licious.</strong><br>Bengaluru, India. Open to global opportunities.</p>
    <div class="hero__links"><a href="https://www.linkedin.com/in/djvirus9">LinkedIn</a><a href="https://github.com/djvirus9">GitHub</a></div>
  </div>
</section>

<div class="proof-strip" aria-label="Experience and research">
  <a href="#experience"><strong>6+ years</strong><span>Across product and offensive security</span></a>
  <a href="{{ '/cves/' | relative_url }}"><strong>{{ site.data.cves | size }} advisories</strong><span>Selected CVEs with public credit</span></a>
  <a href="#credentials"><strong>CKA + CKS</strong><span>Kubernetes administration and security</span></a>
</div>

{% include cybershield-showcase.html home=true %}

<section class="home-section" aria-labelledby="selected-work">
  <div class="section-heading">
    <div><p class="eyebrow">More selected work</p><h2 id="selected-work">Security systems I’ve built</h2></div>
    <a href="{{ '/case-studies/' | relative_url }}">All case studies <span aria-hidden="true">→</span></a>
  </div>
  <div class="card-grid card-grid--pair">
    {% for study in site.data.case_studies %}{% if study.featured and study.slug != 'cybershield360' %}{% include work-card.html study=study featured=true %}{% endif %}{% endfor %}
  </div>
</section>

<section class="home-section" aria-labelledby="experience">
  <div class="section-heading"><div><p class="eyebrow">Experience</p><h2 id="experience">From research to security ownership</h2></div></div>
  <ol class="experience-list">
    {% for job in site.data.experience %}
    <li><span class="period">{{ job.period }}</span><div><h3>{% if job.url %}<a href="{{ job.url | relative_url }}">{{ job.company }}</a>{% else %}{{ job.company }}{% endif %}</h3><span class="role">{{ job.role }}</span><p>{{ job.summary }}</p></div></li>
    {% endfor %}
  </ol>
  <div class="credentials" id="credentials" aria-label="Certifications">
    <span><strong>CKS</strong> · Linux Foundation · 2026</span>
    <span><strong>CKA</strong> · Linux Foundation · 2026</span>
    <span><strong>AWS Certified Security – Specialty</strong></span>
  </div>
</section>

<section class="home-section home-research" aria-labelledby="research">
  <div>
    <p class="eyebrow">Research &amp; writing</p><h2 id="research">Public findings, practical lessons</h2>
    <p>Published research on Traccar and Dovecot, plus notes on the trust boundaries behind the bugs.</p>
    <a href="{{ '/cves/' | relative_url }}">Browse advisories and credits <span aria-hidden="true">→</span></a>
  </div>
  <ul class="research-links">
    <li><a href="{{ '/blog/svg-upload-trust-boundaries/' | relative_url }}">When an image upload becomes executable content</a><small>Traccar · Stored XSS · CVE-2026-25648</small></li>
    <li><a href="{{ '/blog/csv-export-trust-boundaries/' | relative_url }}">The trust boundary in a CSV export</a><small>Traccar · Formula injection · CVE-2026-27644</small></li>
    <li><a href="{{ '/blog/llm-security-owasp-top10/' | relative_url }}">LLM security risks and the OWASP Top 10</a><small>Published on the Halodoc engineering blog</small></li>
    <li><a href="{{ '/community/' | relative_url }}">Community and recognition</a><small>Conference volunteering and researcher profiles</small></li>
  </ul>
</section>

<section class="contact-panel" aria-labelledby="contact-title">
  <p class="eyebrow">Let’s work together</p><h2 id="contact-title">Building a product security function?</h2>
  <p>I’m interested in senior Product Security, AppSec, Cloud Security, and security engineering lead opportunities.</p>
  <div class="actions"><a class="button button--primary" href="mailto:danishismyname1@gmail.com">Email Danish</a><a class="button" href="{{ '/assets/Danish_Siddiqui_Security_Engineer_Resume.pdf' | relative_url }}">Read my résumé</a></div>
</section>
