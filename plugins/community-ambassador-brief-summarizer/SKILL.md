---
name: community-ambassador-brief-summarizer
description: "Ambassador Brief Summarizer for Hermes Agent: apply a checklist workflow to ambassador brief work — covers member fit, tone fit and follow up named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Community Ops, Hermes, Plugins]
    category: community-ops
---

# Ambassador Brief Summarizer

Use this skill in Hermes Agent when the task involves community ambassador brief summarizer. It sits in the Community Ops category; the suggested Hermes toolset is `messaging`.

## Workflow
1. Confirm the goal and gather supplied facts about: ambassador brief member fit, ambassador brief tone fit, ambassador brief approval gate.
2. Run the `community_ambassador_brief_summarizer` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: ambassador brief safety check, ambassador brief follow up named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
