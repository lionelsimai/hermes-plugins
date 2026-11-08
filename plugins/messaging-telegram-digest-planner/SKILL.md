---
name: messaging-telegram-digest-planner
description: "Telegram Digest Planner for Hermes Agent: apply a template workflow to telegram digest work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Telegram Digest Planner

Use this skill in Hermes Agent when the task involves messaging telegram digest planner. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: telegram digest audience fit, telegram digest tone fit, telegram digest length fit.
2. Run the `messaging_telegram_digest_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: telegram digest approval gate, telegram digest platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
