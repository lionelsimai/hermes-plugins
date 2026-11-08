---
name: messaging-discord-announcement-drafter
description: "Discord Announcement Drafter for Hermes Agent: apply a analyze workflow to discord announcement work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Discord Announcement Drafter

Use this skill in Hermes Agent when the task involves messaging discord announcement drafter. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: discord announcement audience fit, discord announcement tone fit, discord announcement length fit.
2. Run the `messaging_discord_announcement_drafter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: discord announcement approval gate, discord announcement platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
