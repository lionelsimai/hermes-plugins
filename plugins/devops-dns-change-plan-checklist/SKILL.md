---
name: devops-dns-change-plan-checklist
description: "Dns Change Plan Checklist for Hermes Agent: apply a score workflow to dns change plan work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Dns Change Plan Checklist

Use this skill in Hermes Agent when the task involves devops dns change plan checklist. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: dns change plan risk noted, dns change plan rollback step, dns change plan verification.
2. Run the `devops_dns_change_plan_checklist` tool (or follow this procedure manually) — kind: score.
3. Check the output against: dns change plan owner named, dns change plan window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
