---
name: safety-sandbox-check-checker
description: "Sandbox Check Checker for Hermes Agent: apply a prioritize workflow to sandbox check work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Sandbox Check Checker

Use this skill in Hermes Agent when the task involves safety sandbox check checker. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: sandbox check risk identified, sandbox check approval required, sandbox check least privilege.
2. Run the `safety_sandbox_check_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: sandbox check reversibility, sandbox check audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
