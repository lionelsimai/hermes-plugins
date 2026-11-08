---
name: email-reply-draft-planner
description: "Reply Draft Planner for Hermes Agent: apply a score workflow to reply draft work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Reply Draft Planner

Use this skill in Hermes Agent when the task involves email reply draft planner. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: reply draft priority accuracy, reply draft tone fit, reply draft facts supplied only.
2. Run the `email_reply_draft_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: reply draft approval gate, reply draft next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
