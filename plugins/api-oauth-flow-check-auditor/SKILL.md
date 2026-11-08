---
name: api-oauth-flow-check-auditor
description: "Oauth Flow Check Auditor for Hermes Agent: apply a plan workflow to oauth flow check work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Oauth Flow Check Auditor

Use this skill in Hermes Agent when the task involves api oauth flow check auditor. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: oauth flow check contract fit, oauth flow check auth handled safely, oauth flow check error cases covered.
2. Run the `api_oauth_flow_check_auditor` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: oauth flow check rate limits respected, oauth flow check verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
