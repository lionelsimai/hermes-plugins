---
name: biz-lead-list-check-scorer
description: "Lead List Check Scorer for Hermes Agent: apply a classify workflow to lead list check work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Lead List Check Scorer

Use this skill in Hermes Agent when the task involves biz lead list check scorer. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: lead list check facts supplied only, lead list check audience fit, lead list check approval gate.
2. Run the `biz_lead_list_check_scorer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: lead list check next step clarity, lead list check evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
