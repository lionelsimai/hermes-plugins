---
name: messaging-whatsapp-broadcast-draft-drafter
description: "Whatsapp Broadcast Draft Drafter for Hermes Agent: apply a audit workflow to whatsapp broadcast draft work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Whatsapp Broadcast Draft Drafter

Use this skill in Hermes Agent when the task involves messaging whatsapp broadcast draft drafter. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: whatsapp broadcast draft audience fit, whatsapp broadcast draft tone fit, whatsapp broadcast draft length fit.
2. Run the `messaging_whatsapp_broadcast_draft_drafter` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: whatsapp broadcast draft approval gate, whatsapp broadcast draft platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
