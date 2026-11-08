---
name: email-meeting-agenda-planner
description: "Meeting Agenda Planner for Hermes Agent: apply a checklist workflow to meeting agenda work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Meeting Agenda Planner

Use this skill in Hermes Agent when the task involves email meeting agenda planner. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: meeting agenda priority accuracy, meeting agenda tone fit, meeting agenda facts supplied only.
2. Run the `email_meeting_agenda_planner` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: meeting agenda approval gate, meeting agenda next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
