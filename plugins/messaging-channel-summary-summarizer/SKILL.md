---
name: messaging-channel-summary-summarizer
description: "Channel Summary Summarizer for Hermes Agent: apply a analyze workflow to channel summary work — covers audience fit, tone fit and platform fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Messaging & Gateway, Hermes, Plugins]
    category: messaging-gateway
---

# Channel Summary Summarizer

Use this skill in Hermes Agent when the task involves messaging channel summary summarizer. It sits in the Messaging & Gateway category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: channel summary audience fit, channel summary tone fit, channel summary length fit.
2. Run the `messaging_channel_summary_summarizer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: channel summary approval gate, channel summary platform fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
