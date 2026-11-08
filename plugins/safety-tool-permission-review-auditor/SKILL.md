---
name: safety-tool-permission-review-auditor
description: "Tool Permission Review Auditor for Hermes Agent: apply a audit workflow to tool permission review work — covers risk identified, approval required and audit logged, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Safety, Approvals & Guardrails, Hermes, Plugins]
    category: safety-approvals-guardrails
---

# Tool Permission Review Auditor

Use this skill in Hermes Agent when the task involves safety tool permission review auditor. It sits in the Safety, Approvals & Guardrails category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: tool permission review risk identified, tool permission review approval required, tool permission review least privilege.
2. Run the `safety_tool_permission_review_auditor` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: tool permission review reversibility, tool permission review audit logged.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
