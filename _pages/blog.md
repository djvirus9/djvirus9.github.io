---
title: "Writing & Research"
permalink: /blog/
layout: single
description: "Technical notes by Danish Siddiqui on published Traccar CVEs, WAF validation, and practical security risks in LLM integrations."
summary: "Research notes and engineering decisions, with links to the underlying advisories and references."
---

<div class="writing-list">
{% for post in site.data.writing %}
  <article class="work-card">
    <p class="eyebrow">{{ post.type }}{% if post.date %} · <time datetime="{{ post.date }}">{{ post.date | date: '%-d %b %Y' }}</time>{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p>{{ post.summary }}</p>
    <a class="work-card__link" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title | escape }}">Read article <span aria-hidden="true">→</span></a>
  </article>
{% endfor %}
</div>
