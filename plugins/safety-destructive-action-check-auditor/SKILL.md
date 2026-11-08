---
name: safety-destructive-action-check-auditor
description: "Destructive Action Check Auditor for Hermes Agent: apply a template workflow to destructive action check work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Destructive Action Check Auditor

Use this skill in Hermes Agent when the task involves safety destructive action check auditor. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: destructive action check risk identified, destructive action check approval required, destructive action check least privilege.
2. Run the `safety_destructive_action_check_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: destructive action check reversibility, destructive action check audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
