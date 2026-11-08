---
name: mcp-mcp-security-review-drafter
description: "Mcp Security Review Drafter for Hermes Agent: apply a prioritize workflow to mcp security review work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Mcp Security Review Drafter

Use this skill in Hermes Agent when the task involves mcp mcp security review drafter. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: mcp security review schema validity, mcp security review description clarity, mcp security review least privilege.
2. Run the `mcp_mcp_security_review_drafter` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: mcp security review test coverage, mcp security review error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
