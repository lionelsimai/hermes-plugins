---
name: api-rate-limit-review-checker
description: "Rate Limit Review Checker for Hermes Agent: apply a template workflow to rate limit review work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Rate Limit Review Checker

Use this skill in Hermes Agent when the task involves api rate limit review checker. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: rate limit review contract fit, rate limit review auth handled safely, rate limit review error cases covered.
2. Run the `api_rate_limit_review_checker` tool (or follow this procedure manually) — kind: template.
3. Check the output against: rate limit review rate limits respected, rate limit review verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
