---
name: devops-backup-review-auditor
description: "Backup Review Auditor for Hermes Agent: apply a plan workflow to backup review work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Backup Review Auditor

Use this skill in Hermes Agent when the task involves devops backup review auditor. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: backup review risk noted, backup review rollback step, backup review verification.
2. Run the `devops_backup_review_auditor` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: backup review owner named, backup review window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
