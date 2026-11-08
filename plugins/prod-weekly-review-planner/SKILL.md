---
name: prod-weekly-review-planner
description: "Weekly Review Planner for Hermes Agent: apply a plan workflow to weekly review work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Weekly Review Planner

Use this skill in Hermes Agent when the task involves prod weekly review planner. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: weekly review priority clarity, weekly review time realism, weekly review next action named.
2. Run the `prod_weekly_review_planner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: weekly review review cadence, weekly review owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
