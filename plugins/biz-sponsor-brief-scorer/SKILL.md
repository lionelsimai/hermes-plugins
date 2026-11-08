---
name: biz-sponsor-brief-scorer
description: "Sponsor Brief Scorer for Hermes Agent: apply a plan workflow to sponsor brief work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Sponsor Brief Scorer

Use this skill in Hermes Agent when the task involves biz sponsor brief scorer. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: sponsor brief facts supplied only, sponsor brief audience fit, sponsor brief approval gate.
2. Run the `biz_sponsor_brief_scorer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: sponsor brief next step clarity, sponsor brief evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
