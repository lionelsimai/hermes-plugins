---
name: prod-shopping-list-reviewer
description: "Shopping List Reviewer for Hermes Agent: apply a checklist workflow to shopping list work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Shopping List Reviewer

Use this skill in Hermes Agent when the task involves prod shopping list reviewer. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: shopping list priority clarity, shopping list time realism, shopping list next action named.
2. Run the `prod_shopping_list_reviewer` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: shopping list review cadence, shopping list owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
