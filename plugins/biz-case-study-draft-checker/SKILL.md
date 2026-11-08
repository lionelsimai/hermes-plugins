---
name: biz-case-study-draft-checker
description: "Case Study Draft Checker for Hermes Agent: apply a analyze workflow to case study draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Business & GTM Ops, Hermes, Plugins]
    category: business-gtm-ops
---

# Case Study Draft Checker

Use this skill in Hermes Agent when the task involves biz case study draft checker. It sits in the Business & GTM Ops category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: case study draft facts supplied only, case study draft audience fit, case study draft approval gate.
2. Run the `biz_case_study_draft_checker` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: case study draft next step clarity, case study draft evidence noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
