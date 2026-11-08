---
name: safety-command-approval-reviewer
description: "Command Approval Reviewer for Hermes Agent: apply a classify workflow to command approval work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Command Approval Reviewer

Use this skill in Hermes Agent when the task involves safety command approval reviewer. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: command approval risk identified, command approval approval required, command approval least privilege.
2. Run the `safety_command_approval_reviewer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: command approval reversibility, command approval audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
