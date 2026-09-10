---
title: "Published Vulnerability Research"
permalink: /cves/
layout: single
description: "Selected Traccar and Dovecot CVEs reported by Danish Siddiqui, with precise impact descriptions, publisher severity scores, and public researcher credits."
summary: "Selected public findings across application trust boundaries and server resource consumption."
---

The {{ site.data.cves | size }} advisories below credit my research as **djvirus9** or **djvirus@yeswehack**. Each entry links to the publisher’s description and acknowledgment. This is a selection of public work, rather than a complete inventory of assigned CVEs or private reports.

Scores are the publisher/CNA’s **CVSS 3.1** assessment. Dates refer to publication of the CVE record. References checked on **10 September 2026**.

{% assign groups = site.data.cves | group_by: 'category' %}
{% for group in groups %}
<h2 id="{{ group.name | slugify }}">{{ group.name }}</h2>
<ul class="cve-list">
{% for finding in group.items %}
  <li class="cve-entry" id="{{ finding.id | downcase }}">
    <div class="cve-entry__meta"><strong>{{ finding.id }}</strong><span>{{ finding.product }}</span><span>{{ finding.severity }} · CVSS {{ finding.cvss }}</span></div>
    <h3>{{ finding.title }}</h3>
    <p>{{ finding.impact }}</p>
    <p class="cve-entry__meta"><span>Published <time datetime="{{ finding.published }}">{{ finding.published | date: '%-d %b %Y' }}</time></span><span>Credit: {{ finding.credit }}</span></p>
    <div class="cve-entry__links"><a href="{{ finding.advisory }}" aria-label="Publisher advisory and credit for {{ finding.id }}">Advisory &amp; credit</a><a href="https://www.cve.org/CVERecord?id={{ finding.id }}" aria-label="CVE record for {{ finding.id }}">CVE record</a></div>
  </li>
{% endfor %}
</ul>
{% endfor %}

## Research approach

I combine code review with evidence of reachability and impact, then work with maintainers through disclosure and remediation. Read my [research methodology]({{ '/research-methodology/' | relative_url }}) or the [technical notes behind selected findings]({{ '/blog/' | relative_url }}).

For platform profiles and Hall of Fame references, see [Community & Recognition]({{ '/community/' | relative_url }}).
