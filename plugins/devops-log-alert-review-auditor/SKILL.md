---
name: devops-log-alert-review-auditor
description: "Log Alert Review Auditor for Hermes Agent: apply a classify workflow to log alert review work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Log Alert Review Auditor

Use this skill in Hermes Agent when the task involves devops log alert review auditor. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: log alert review risk noted, log alert review rollback step, log alert review verification.
2. Run the `devops_log_alert_review_auditor` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: log alert review owner named, log alert review window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
