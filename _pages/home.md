---
title: "Danish Siddiqui"
permalink: /
layout: single
wide: true
home: true
description: "I build security programs and the tools that make them work. Explore Danish Siddiqui’s work at Licious, SecOps Dashboard, CyberShield360, and published vulnerability research."
---

<section class="home-intro" aria-labelledby="intro-title">
  <div class="home-intro__identity">
    <p class="eyebrow">Senior Product Security Engineer</p>
    <h1 id="intro-title">Danish Siddiqui<span class="home-intro__dot" aria-hidden="true">.</span></h1>
  </div>
  <img class="home-intro__portrait" src="{{ '/assets/avatar-224.jpg' | relative_url }}" srcset="{{ '/assets/avatar-224.jpg' | relative_url }} 224w, {{ '/assets/avatar.jpg' | relative_url }} 747w" sizes="(max-width: 672px) 108px, 224px" alt="Danish Siddiqui" width="747" height="1024" fetchpriority="high">
  <p class="home-intro__lead">I build security programs and the tools that make them work.</p>
  <p class="home-intro__context"><strong>Founding security engineer at Licious.</strong><br>AppSec, cloud security, and DevSecOps.</p>
  <div class="actions home-intro__actions">
    <a class="button button--primary" href="#selected-work">Explore my work <span aria-hidden="true">↓</span></a>
    <a class="button" href="mailto:danishismyname1@gmail.com">Email me <span aria-hidden="true">↗</span></a>
  </div>
  <div class="home-intro__details">
    <p>Bengaluru · Open to global opportunities</p>
    <nav aria-label="Profile links"><a href="https://www.linkedin.com/in/djvirus9">LinkedIn</a><a href="https://github.com/djvirus9">GitHub</a></nav>
  </div>
</section>

<section class="home-work" aria-labelledby="selected-work">
  <div class="section-heading">
    <div><p class="eyebrow">Selected work / 01–03</p><h2 id="selected-work">Built, shipped, and put to work.</h2></div>
    <a href="{{ '/case-studies/' | relative_url }}">All case studies <span aria-hidden="true">→</span></a>
  </div>
  <div class="flagship-grid">
    {% for project in site.data.featured_work %}
    <article class="flagship" id="{{ project.anchor }}">
      {% if project.anchor == 'cybershield' %}<span id="cybershield-discover"></span><span id="cybershield-enrich"></span><span id="cybershield-prioritize"></span><span id="cybershield-report"></span>{% endif %}
      <div class="flagship__visual"><img src="{{ project.art | relative_url }}" alt="" width="660" height="360" loading="lazy" decoding="async"></div>
      <div class="flagship__body">
        <p class="eyebrow">{{ project.category | escape }}</p>
        <h3>{{ project.title | escape }}</h3>
        <p class="flagship__contribution">{{ project.contribution | escape }}</p>
        <p class="flagship__outcome"><span>Delivered</span>{{ project.outcome | escape }}</p>
        <a class="flagship__link" href="{{ project.url | relative_url }}">{{ project.link_label | escape }} <span aria-hidden="true">→</span></a>
      </div>
    </article>
    {% endfor %}
  </div>
</section>

<section class="home-proof" aria-labelledby="research">
  <div><p class="eyebrow">Research with public credit</p><h2 id="research">{{ site.data.cves | size }} selected CVE advisories.</h2><p>Research acknowledged by Traccar and Dovecot’s publisher.</p><a href="{{ '/cves/' | relative_url }}">Explore findings and acknowledgments <span aria-hidden="true">→</span></a></div>
  <div class="home-proof__sources">
    <a href="https://github.com/traccar/traccar/security/advisories/GHSA-mc2g-mjqh-8x78"><span>Traccar</span>SVG upload · CVE-2026-25648 <span aria-hidden="true">↗</span></a>
    <a href="https://documentation.open-xchange.com/dovecot/security/advisories/csaf/2026/oxdc-adv-2026-0001.json"><span>Dovecot</span>MIME parsing · CVE-2026-27859 <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section class="contact-panel home-contact" id="contact" aria-labelledby="contact-title">
  <div><p class="eyebrow">Let’s work together</p><h2 id="contact-title">Building a product security function?</h2><p>I’m open to senior security engineering and technical leadership opportunities.</p></div>
  <div class="actions"><a class="button button--primary" href="mailto:danishismyname1@gmail.com">Email Danish <span aria-hidden="true">↗</span></a></div>
</section>

<section class="home-background" aria-labelledby="background-title">
  <h2 id="background-title">A little more background</h2>
  <details id="experience" class="home-details">
    <summary><span>Experience <small>Licious · Halodoc · Invia · FireCompass</small></span></summary>
    <ol class="experience-list">
      {% for job in site.data.experience %}
      <li><span class="period">{{ job.period }}</span><div><h3>{% if job.url %}<a href="{{ job.url | relative_url }}">{{ job.company }}</a>{% else %}{{ job.company }}{% endif %}</h3><span class="role">{{ job.role }}</span><p>{{ job.summary }}</p></div></li>
      {% endfor %}
    </ol>
  </details>
  <details id="credentials" class="home-details">
    <summary><span>Certifications <small>CKA · CKS · AWS Security – Specialty</small></span></summary>
    <ul class="home-credentials"><li><strong>CKS</strong> · Linux Foundation · 2026</li><li><strong>CKA</strong> · Linux Foundation · 2026</li><li><strong>AWS Certified Security – Specialty</strong></li></ul>
  </details>
  <div class="home-more" id="open-source">
    <a href="https://github.com/djvirus9/awesome-devsecops-mastery-2026"><span>Open-source learning</span>DevSecOps Roadmap <span aria-hidden="true">↗</span></a>
    <a href="{{ '/blog/' | relative_url }}"><span>Research &amp; writing</span>Practical security lessons <span aria-hidden="true">→</span></a>
    <a href="{{ '/community/' | relative_url }}"><span>Beyond the day job</span>Community &amp; recognition <span aria-hidden="true">→</span></a>
  </div>
</section>
