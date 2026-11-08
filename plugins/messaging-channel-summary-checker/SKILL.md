---
name: messaging-channel-summary-checker
description: "Channel Summary Checker for Hermes Agent: apply a classify workflow to channel summary work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Channel Summary Checker

Use this skill in Hermes Agent when the task involves messaging channel summary checker. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: channel summary audience fit, channel summary tone fit, channel summary length fit.
2. Run the `messaging_channel_summary_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: channel summary approval gate, channel summary platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
