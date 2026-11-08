---
name: prod-travel-plan-tracker
description: "Travel Plan Tracker for Hermes Agent: apply a audit workflow to travel plan work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Travel Plan Tracker

Use this skill in Hermes Agent when the task involves prod travel plan tracker. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: travel plan priority clarity, travel plan time realism, travel plan next action named.
2. Run the `prod_travel_plan_tracker` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: travel plan review cadence, travel plan owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
