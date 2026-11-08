---
name: email-meeting-invite-summarizer
description: "Meeting Invite Summarizer for Hermes Agent: apply a plan workflow to meeting invite work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Meeting Invite Summarizer

Use this skill in Hermes Agent when the task involves email meeting invite summarizer. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: meeting invite priority accuracy, meeting invite tone fit, meeting invite facts supplied only.
2. Run the `email_meeting_invite_summarizer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: meeting invite approval gate, meeting invite next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
