---
name: prod-daily-plan-tracker
description: "Daily Plan Tracker for Hermes Agent: apply a template workflow to daily plan work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Daily Plan Tracker

Use this skill in Hermes Agent when the task involves prod daily plan tracker. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: daily plan priority clarity, daily plan time realism, daily plan next action named.
2. Run the `prod_daily_plan_tracker` tool (or follow this procedure manually) — kind: template.
3. Check the output against: daily plan review cadence, daily plan owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
