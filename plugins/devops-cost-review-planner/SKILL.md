---
name: devops-cost-review-planner
description: "Cost Review Planner for Hermes Agent: apply a template workflow to cost review work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Cost Review Planner

Use this skill in Hermes Agent when the task involves devops cost review planner. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: cost review risk noted, cost review rollback step, cost review verification.
2. Run the `devops_cost_review_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: cost review owner named, cost review window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
