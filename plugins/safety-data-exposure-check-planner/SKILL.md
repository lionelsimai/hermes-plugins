---
name: safety-data-exposure-check-planner
description: "Data Exposure Check Planner for Hermes Agent: apply a plan workflow to data exposure check work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Data Exposure Check Planner

Use this skill in Hermes Agent when the task involves safety data exposure check planner. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: data exposure check risk identified, data exposure check approval required, data exposure check least privilege.
2. Run the `safety_data_exposure_check_planner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: data exposure check reversibility, data exposure check audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
