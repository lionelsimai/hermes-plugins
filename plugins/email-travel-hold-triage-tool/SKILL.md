---
name: email-travel-hold-triage-tool
description: "Travel Hold Triage Tool for Hermes Agent: apply a score workflow to travel hold work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Travel Hold Triage Tool

Use this skill in Hermes Agent when the task involves email travel hold triage tool. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: travel hold priority accuracy, travel hold tone fit, travel hold facts supplied only.
2. Run the `email_travel_hold_triage_tool` tool (or follow this procedure manually) — kind: score.
3. Check the output against: travel hold approval gate, travel hold next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
