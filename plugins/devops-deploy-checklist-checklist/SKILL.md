---
name: devops-deploy-checklist-checklist
description: "Deploy Checklist Checklist for Hermes Agent: apply a template workflow to deploy checklist work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Deploy Checklist Checklist

Use this skill in Hermes Agent when the task involves devops deploy checklist checklist. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: deploy checklist risk noted, deploy checklist rollback step, deploy checklist verification.
2. Run the `devops_deploy_checklist_checklist` tool (or follow this procedure manually) — kind: template.
3. Check the output against: deploy checklist owner named, deploy checklist window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
