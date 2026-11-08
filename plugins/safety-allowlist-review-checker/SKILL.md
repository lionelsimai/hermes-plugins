---
name: safety-allowlist-review-checker
description: "Allowlist Review Checker for Hermes Agent: apply a template workflow to allowlist review work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Allowlist Review Checker

Use this skill in Hermes Agent when the task involves safety allowlist review checker. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: allowlist review risk identified, allowlist review approval required, allowlist review least privilege.
2. Run the `safety_allowlist_review_checker` tool (or follow this procedure manually) — kind: template.
3. Check the output against: allowlist review reversibility, allowlist review audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
