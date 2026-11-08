---
name: messaging-dm-triage-planner
description: "Dm Triage Planner for Hermes Agent: apply a score workflow to dm triage work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Dm Triage Planner

Use this skill in Hermes Agent when the task involves messaging dm triage planner. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: dm triage audience fit, dm triage tone fit, dm triage length fit.
2. Run the `messaging_dm_triage_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: dm triage approval gate, dm triage platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
