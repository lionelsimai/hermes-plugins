---
name: api-api-key-checklist-mapper
description: "Api Key Checklist Mapper for Hermes Agent: apply a plan workflow to api key checklist work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Api Key Checklist Mapper

Use this skill in Hermes Agent when the task involves api api key checklist mapper. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: api key checklist contract fit, api key checklist auth handled safely, api key checklist error cases covered.
2. Run the `api_api_key_checklist_mapper` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: api key checklist rate limits respected, api key checklist verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
