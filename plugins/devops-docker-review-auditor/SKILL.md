---
name: devops-docker-review-auditor
description: "Docker Review Auditor for Hermes Agent: apply a audit workflow to docker review work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Docker Review Auditor

Use this skill in Hermes Agent when the task involves devops docker review auditor. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: docker review risk noted, docker review rollback step, docker review verification.
2. Run the `devops_docker_review_auditor` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: docker review owner named, docker review window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
