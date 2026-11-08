---
name: email-calendar-conflict-planner
description: "Calendar Conflict Planner for Hermes Agent: apply a template workflow to calendar conflict work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Calendar Conflict Planner

Use this skill in Hermes Agent when the task involves email calendar conflict planner. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: calendar conflict priority accuracy, calendar conflict tone fit, calendar conflict facts supplied only.
2. Run the `email_calendar_conflict_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: calendar conflict approval gate, calendar conflict next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
