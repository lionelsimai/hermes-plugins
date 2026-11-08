---
name: devops-dns-change-plan-reporter
description: "Dns Change Plan Reporter for Hermes Agent: apply a classify workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Dns Change Plan Reporter

Use this skill in Hermes Agent when the task involves devops dns change plan reporter. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: dns change plan risk noted, dns change plan rollback step, dns change plan verification.
2. Run the `devops_dns_change_plan_reporter` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: dns change plan owner named, dns change plan window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
