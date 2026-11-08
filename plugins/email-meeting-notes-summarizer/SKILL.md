---
name: email-meeting-notes-summarizer
description: "Meeting Notes Summarizer for Hermes Agent: apply a prioritize workflow to meeting notes work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Meeting Notes Summarizer

Use this skill in Hermes Agent when the task involves email meeting notes summarizer. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: meeting notes priority accuracy, meeting notes tone fit, meeting notes facts supplied only.
2. Run the `email_meeting_notes_summarizer` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: meeting notes approval gate, meeting notes next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
