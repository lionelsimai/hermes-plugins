---
name: api-integration-spec-checker
description: "Integration Spec Checker for Hermes Agent: apply a classify workflow to integration spec work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Integration Spec Checker

Use this skill in Hermes Agent when the task involves api integration spec checker. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: integration spec contract fit, integration spec auth handled safely, integration spec error cases covered.
2. Run the `api_integration_spec_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: integration spec rate limits respected, integration spec verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
