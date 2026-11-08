---
name: email-calendar-conflict-drafter
description: "Calendar Conflict Drafter for Hermes Agent: apply a score workflow to calendar conflict work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Calendar Conflict Drafter

Use this skill in Hermes Agent when the task involves email calendar conflict drafter. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: calendar conflict priority accuracy, calendar conflict tone fit, calendar conflict facts supplied only.
2. Run the `email_calendar_conflict_drafter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: calendar conflict approval gate, calendar conflict next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
