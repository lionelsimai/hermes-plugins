---
name: prod-daily-plan-triage-tool
description: "Daily Plan Triage Tool for Hermes Agent: apply a score workflow to daily plan work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Daily Plan Triage Tool

Use this skill in Hermes Agent when the task involves prod daily plan triage tool. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: daily plan priority clarity, daily plan time realism, daily plan next action named.
2. Run the `prod_daily_plan_triage_tool` tool (or follow this procedure manually) — kind: score.
3. Check the output against: daily plan review cadence, daily plan owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
