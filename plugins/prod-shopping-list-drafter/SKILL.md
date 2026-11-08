---
name: prod-shopping-list-drafter
description: "Shopping List Drafter for Hermes Agent: apply a analyze workflow to shopping list work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Shopping List Drafter

Use this skill in Hermes Agent when the task involves prod shopping list drafter. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: shopping list priority clarity, shopping list time realism, shopping list next action named.
2. Run the `prod_shopping_list_drafter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: shopping list review cadence, shopping list owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
