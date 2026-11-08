---
name: messaging-signal-note-summarizer
description: "Signal Note Summarizer for Hermes Agent: apply a classify workflow to signal note work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Signal Note Summarizer

Use this skill in Hermes Agent when the task involves messaging signal note summarizer. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: signal note audience fit, signal note tone fit, signal note length fit.
2. Run the `messaging_signal_note_summarizer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: signal note approval gate, signal note platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
