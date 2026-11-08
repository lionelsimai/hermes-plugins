---
name: api-webhook-plan-auditor
description: "Webhook Plan Auditor for Hermes Agent: apply a template workflow to webhook plan work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Webhook Plan Auditor

Use this skill in Hermes Agent when the task involves api webhook plan auditor. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: webhook plan contract fit, webhook plan auth handled safely, webhook plan error cases covered.
2. Run the `api_webhook_plan_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: webhook plan rate limits respected, webhook plan verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
