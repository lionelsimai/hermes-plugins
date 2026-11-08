---
name: devops-backup-review-reporter
description: "Backup Review Reporter for Hermes Agent: apply a score workflow to backup review work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Backup Review Reporter

Use this skill in Hermes Agent when the task involves devops backup review reporter. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: backup review risk noted, backup review rollback step, backup review verification.
2. Run the `devops_backup_review_reporter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: backup review owner named, backup review window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
