---
name: safety-allowlist-review-gate
description: "Allowlist Review Gate for Hermes Agent: apply a prioritize workflow to allowlist review work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Allowlist Review Gate

Use this skill in Hermes Agent when the task involves safety allowlist review gate. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: allowlist review risk identified, allowlist review approval required, allowlist review least privilege.
2. Run the `safety_allowlist_review_gate` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: allowlist review reversibility, allowlist review audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
