---
name: biz-partner-shortlist-drafter
description: "Partner Shortlist Drafter for Hermes Agent: apply a plan workflow to partner shortlist work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Partner Shortlist Drafter

Use this skill in Hermes Agent when the task involves biz partner shortlist drafter. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: partner shortlist facts supplied only, partner shortlist audience fit, partner shortlist approval gate.
2. Run the `biz_partner_shortlist_drafter` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: partner shortlist next step clarity, partner shortlist evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
