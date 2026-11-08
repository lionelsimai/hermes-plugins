---
name: biz-pipeline-review-drafter
description: "Pipeline Review Drafter for Hermes Agent: apply a audit workflow to pipeline review work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Pipeline Review Drafter

Use this skill in Hermes Agent when the task involves biz pipeline review drafter. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: pipeline review facts supplied only, pipeline review audience fit, pipeline review approval gate.
2. Run the `biz_pipeline_review_drafter` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: pipeline review next step clarity, pipeline review evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
