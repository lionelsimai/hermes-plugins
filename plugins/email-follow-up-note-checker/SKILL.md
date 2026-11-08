---
name: email-follow-up-note-checker
description: "Follow Up Note Checker for Hermes Agent: apply a plan workflow to follow up note work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Follow Up Note Checker

Use this skill in Hermes Agent when the task involves email follow up note checker. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: follow up note priority accuracy, follow up note tone fit, follow up note facts supplied only.
2. Run the `email_follow_up_note_checker` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: follow up note approval gate, follow up note next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
