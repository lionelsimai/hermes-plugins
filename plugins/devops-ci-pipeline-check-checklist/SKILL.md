---
name: devops-ci-pipeline-check-checklist
description: "Ci Pipeline Check Checklist for Hermes Agent: apply a plan workflow to ci pipeline check work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Ci Pipeline Check Checklist

Use this skill in Hermes Agent when the task involves devops ci pipeline check checklist. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: ci pipeline check risk noted, ci pipeline check rollback step, ci pipeline check verification.
2. Run the `devops_ci_pipeline_check_checklist` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: ci pipeline check owner named, ci pipeline check window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
