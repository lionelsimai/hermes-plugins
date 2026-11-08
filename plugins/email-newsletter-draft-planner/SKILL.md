---
name: email-newsletter-draft-planner
description: "Newsletter Draft Planner for Hermes Agent: apply a classify workflow to newsletter draft work — covers priority accuracy, tone fit and next step clarity, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Email & Calendar, Hermes, Plugins]
    category: email-calendar
---

# Newsletter Draft Planner

Use this skill in Hermes Agent when the task involves email newsletter draft planner. It sits in the Email & Calendar category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: newsletter draft priority accuracy, newsletter draft tone fit, newsletter draft facts supplied only.
2. Run the `email_newsletter_draft_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: newsletter draft approval gate, newsletter draft next step clarity.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
