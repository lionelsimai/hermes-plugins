---
name: biz-follow-up-plan-checker
description: "Follow Up Plan Checker for Hermes Agent: apply a plan workflow to follow up plan work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Follow Up Plan Checker

Use this skill in Hermes Agent when the task involves biz follow up plan checker. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: follow up plan facts supplied only, follow up plan audience fit, follow up plan approval gate.
2. Run the `biz_follow_up_plan_checker` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: follow up plan next step clarity, follow up plan evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
