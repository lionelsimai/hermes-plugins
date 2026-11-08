---
name: community-member-spotlight-planner
description: "Member Spotlight Planner for Hermes Agent: apply a checklist workflow to member spotlight work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Member Spotlight Planner

Use this skill in Hermes Agent when the task involves community member spotlight planner. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: member spotlight member fit, member spotlight tone fit, member spotlight approval gate.
2. Run the `community_member_spotlight_planner` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: member spotlight safety check, member spotlight follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
