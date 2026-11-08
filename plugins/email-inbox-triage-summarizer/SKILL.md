---
name: email-inbox-triage-summarizer
description: "Inbox Triage Summarizer for Hermes Agent: apply a classify workflow to inbox triage work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Inbox Triage Summarizer

Use this skill in Hermes Agent when the task involves email inbox triage summarizer. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: inbox triage priority accuracy, inbox triage tone fit, inbox triage facts supplied only.
2. Run the `email_inbox_triage_summarizer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: inbox triage approval gate, inbox triage next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
