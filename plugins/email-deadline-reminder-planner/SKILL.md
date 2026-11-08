---
name: email-deadline-reminder-planner
description: "Deadline Reminder Planner for Hermes Agent: apply a score workflow to deadline reminder work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Deadline Reminder Planner

Use this skill in Hermes Agent when the task involves email deadline reminder planner. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: deadline reminder priority accuracy, deadline reminder tone fit, deadline reminder facts supplied only.
2. Run the `email_deadline_reminder_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: deadline reminder approval gate, deadline reminder next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
