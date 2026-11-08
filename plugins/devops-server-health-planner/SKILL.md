---
name: devops-server-health-planner
description: "Server Health Planner for Hermes Agent: apply a template workflow to server health work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Server Health Planner

Use this skill in Hermes Agent when the task involves devops server health planner. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: server health risk noted, server health rollback step, server health verification.
2. Run the `devops_server_health_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: server health owner named, server health window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
