---
name: api-rest-endpoint-test-planner
description: "Rest Endpoint Test Planner for Hermes Agent: apply a analyze workflow to rest endpoint test work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Rest Endpoint Test Planner

Use this skill in Hermes Agent when the task involves api rest endpoint test planner. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: rest endpoint test contract fit, rest endpoint test auth handled safely, rest endpoint test error cases covered.
2. Run the `api_rest_endpoint_test_planner` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: rest endpoint test rate limits respected, rest endpoint test verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
