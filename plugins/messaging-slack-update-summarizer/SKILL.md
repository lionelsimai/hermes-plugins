---
name: messaging-slack-update-summarizer
description: "Slack Update Summarizer for Hermes Agent: apply a template workflow to slack update work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Slack Update Summarizer

Use this skill in Hermes Agent when the task involves messaging slack update summarizer. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: slack update audience fit, slack update tone fit, slack update length fit.
2. Run the `messaging_slack_update_summarizer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: slack update approval gate, slack update platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
