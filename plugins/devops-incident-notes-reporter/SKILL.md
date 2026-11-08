---
name: devops-incident-notes-reporter
description: "Incident Notes Reporter for Hermes Agent: apply a audit workflow to incident notes work — covers risk noted, rollback step and window fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [DevOps & Infra, Hermes, Plugins]
    category: devops-infra
---

# Incident Notes Reporter

Use this skill in Hermes Agent when the task involves devops incident notes reporter. It sits in the DevOps & Infra category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: incident notes risk noted, incident notes rollback step, incident notes verification.
2. Run the `devops_incident_notes_reporter` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: incident notes owner named, incident notes window fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
