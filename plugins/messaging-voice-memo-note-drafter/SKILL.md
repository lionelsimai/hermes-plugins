---
name: messaging-voice-memo-note-drafter
description: "Voice Memo Note Drafter for Hermes Agent: apply a plan workflow to voice memo note work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Voice Memo Note Drafter

Use this skill in Hermes Agent when the task involves messaging voice memo note drafter. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: voice memo note audience fit, voice memo note tone fit, voice memo note length fit.
2. Run the `messaging_voice_memo_note_drafter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: voice memo note approval gate, voice memo note platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
