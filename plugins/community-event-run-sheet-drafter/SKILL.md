---
name: community-event-run-sheet-drafter
description: "Event Run Sheet Drafter for Hermes Agent: apply a prioritize workflow to event run sheet work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Event Run Sheet Drafter

Use this skill in Hermes Agent when the task involves community event run sheet drafter. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: event run sheet member fit, event run sheet tone fit, event run sheet approval gate.
2. Run the `community_event_run_sheet_drafter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: event run sheet safety check, event run sheet follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
