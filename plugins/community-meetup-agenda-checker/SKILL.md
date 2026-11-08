---
name: community-meetup-agenda-checker
description: "Meetup Agenda Checker for Hermes Agent: apply a prioritize workflow to meetup agenda work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Meetup Agenda Checker

Use this skill in Hermes Agent when the task involves community meetup agenda checker. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: meetup agenda member fit, meetup agenda tone fit, meetup agenda approval gate.
2. Run the `community_meetup_agenda_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: meetup agenda safety check, meetup agenda follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
