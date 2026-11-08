---
name: community-meetup-agenda-summarizer
description: "Meetup Agenda Summarizer for Hermes Agent: apply a plan workflow to meetup agenda work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Meetup Agenda Summarizer

Use this skill in Hermes Agent when the task involves community meetup agenda summarizer. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: meetup agenda member fit, meetup agenda tone fit, meetup agenda approval gate.
2. Run the `community_meetup_agenda_summarizer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: meetup agenda safety check, meetup agenda follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
