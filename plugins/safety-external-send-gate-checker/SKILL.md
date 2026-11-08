---
name: safety-external-send-gate-checker
description: "External Send Gate Checker for Hermes Agent: apply a checklist workflow to external send gate work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# External Send Gate Checker

Use this skill in Hermes Agent when the task involves safety external send gate checker. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: external send gate risk identified, external send gate approval required, external send gate least privilege.
2. Run the `safety_external_send_gate_checker` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: external send gate reversibility, external send gate audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
