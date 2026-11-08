---
name: biz-proposal-outline-checker
description: "Proposal Outline Checker for Hermes Agent: apply a prioritize workflow to proposal outline work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Proposal Outline Checker

Use this skill in Hermes Agent when the task involves biz proposal outline checker. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: proposal outline facts supplied only, proposal outline audience fit, proposal outline approval gate.
2. Run the `biz_proposal_outline_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: proposal outline next step clarity, proposal outline evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
