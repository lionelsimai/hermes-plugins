---
name: community-speaker-brief-reporter
description: "Speaker Brief Reporter for Hermes Agent: apply a prioritize workflow to speaker brief work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Speaker Brief Reporter

Use this skill in Hermes Agent when the task involves community speaker brief reporter. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: speaker brief member fit, speaker brief tone fit, speaker brief approval gate.
2. Run the `community_speaker_brief_reporter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: speaker brief safety check, speaker brief follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
