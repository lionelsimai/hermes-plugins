---
name: safety-audit-trail-gate
description: "Audit Trail Gate for Hermes Agent: apply a score workflow to audit trail work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Audit Trail Gate

Use this skill in Hermes Agent when the task involves safety audit trail gate. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: audit trail risk identified, audit trail approval required, audit trail least privilege.
2. Run the `safety_audit_trail_gate` tool (or follow this procedure manually) — kind: score.
3. Check the output against: audit trail reversibility, audit trail audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
