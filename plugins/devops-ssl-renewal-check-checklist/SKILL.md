---
name: devops-ssl-renewal-check-checklist
description: "Ssl Renewal Check Checklist for Hermes Agent: apply a audit workflow to ssl renewal check work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Ssl Renewal Check Checklist

Use this skill in Hermes Agent when the task involves devops ssl renewal check checklist. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: ssl renewal check risk noted, ssl renewal check rollback step, ssl renewal check verification.
2. Run the `devops_ssl_renewal_check_checklist` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: ssl renewal check owner named, ssl renewal check window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
