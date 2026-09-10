---
title: "What to Measure Before Blocking with a WAF Rule"
permalink: /blog/waf-count-mode-validation/
layout: single
date: 2026-09-10
article_type: "Engineering note"
description: "A practical evaluation plan for AWS WAF count-mode rollouts: rule matches, legitimate journeys, sampled evidence, enforcement criteria, and rollback."
summary: "Count mode produces observations. A rollout decision needs an explanation of what those observations mean."
---

## Start with the behavior to detect

A proposed WAF rule should have a specific purpose: the request pattern it detects, the endpoint or traffic segment it applies to, and the business behavior it must preserve. That makes the result easier to evaluate than a rule introduced simply to increase coverage.

My [WAF case study](/case-studies/waf-coverage-benchmarking/) describes using count-mode observations before enforcement. The evaluation plan below illustrates how to structure that decision.

## Keep a small evidence record

| Evidence | Decision it supports |
|---|---|
| Representative attack requests | Does the rule detect its intended condition? |
| Sampled matching legitimate requests | Which valid clients or journeys need investigation? |
| Matches by endpoint and client type | Is a broad rule disproportionately affecting one workflow? |
| Matched traffic over relevant business cycles | Is the sample representative of the expected traffic? |
| Checkout, login, and support indicators | What should be monitored when blocking starts? |
| Rollback owner and procedure | Who can respond if enforcement causes unexpected impact? |

Counts alone do not distinguish hostile requests from valid traffic. Aggregate results need representative request-level review, with sensitive information handled through the organization’s normal logging controls.

## Know the limits of the observation

Count mode records matches without itself blocking requests. Other rules may still affect the request, so rule order and the rest of the web ACL matter when interpreting results. AWS recommends testing and tuning protections before relying on enforcement. [AWS WAF testing guidance](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html)

A quiet sample does not establish a zero-false-positive guarantee. It supports a decision for the traffic observed and should be followed by monitoring after rollout.

## Connect the decision to an owner

A useful change record includes the expected behavior, sample evidence, remaining uncertainty, approver, and rollback path. Scoped rollout and observation make it easier to distinguish a rule regression from unrelated application changes.

The proposed matrix is a review aid. It does not describe a new benchmark run or publish production traffic from an employer.
