---
name: api-api-change-review-auditor
description: "Api Change Review Auditor for Hermes Agent: apply a template workflow to api change review work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Api Change Review Auditor

Use this skill in Hermes Agent when the task involves api api change review auditor. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: api change review contract fit, api change review auth handled safely, api change review error cases covered.
2. Run the `api_api_change_review_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: api change review rate limits respected, api change review verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
