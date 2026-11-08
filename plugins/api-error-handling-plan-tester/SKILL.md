---
name: api-error-handling-plan-tester
description: "Error Handling Plan Tester for Hermes Agent: apply a audit workflow to error handling plan work — covers contract fit, auth handled safely and verification call, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [APIs & Integrations, Hermes, Plugins]
    category: apis-integrations
---

# Error Handling Plan Tester

Use this skill in Hermes Agent when the task involves api error handling plan tester. It sits in the APIs & Integrations category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: error handling plan contract fit, error handling plan auth handled safely, error handling plan error cases covered.
2. Run the `api_error_handling_plan_tester` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: error handling plan rate limits respected, error handling plan verification call.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
