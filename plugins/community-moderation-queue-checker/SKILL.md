---
name: community-moderation-queue-checker
description: "Moderation Queue Checker for Hermes Agent: apply a score workflow to moderation queue work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Moderation Queue Checker

Use this skill in Hermes Agent when the task involves community moderation queue checker. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: moderation queue member fit, moderation queue tone fit, moderation queue approval gate.
2. Run the `community_moderation_queue_checker` tool (or follow this procedure manually) — kind: score.
3. Check the output against: moderation queue safety check, moderation queue follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
