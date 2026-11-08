---
name: safety-secret-handling-check-gate
description: "Secret Handling Check Gate for Hermes Agent: apply a checklist workflow to secret handling check work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Secret Handling Check Gate

Use this skill in Hermes Agent when the task involves safety secret handling check gate. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: secret handling check risk identified, secret handling check approval required, secret handling check least privilege.
2. Run the `safety_secret_handling_check_gate` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: secret handling check reversibility, secret handling check audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
