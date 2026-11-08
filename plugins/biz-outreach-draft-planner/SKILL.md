---
name: biz-outreach-draft-planner
description: "Outreach Draft Planner for Hermes Agent: apply a prioritize workflow to outreach draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Outreach Draft Planner

Use this skill in Hermes Agent when the task involves biz outreach draft planner. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: outreach draft facts supplied only, outreach draft audience fit, outreach draft approval gate.
2. Run the `biz_outreach_draft_planner` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: outreach draft next step clarity, outreach draft evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
