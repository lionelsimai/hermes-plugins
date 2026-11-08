---
name: mcp-tool-description-audit-drafter
description: "Tool Description Audit Drafter for Hermes Agent: apply a analyze workflow to tool description audit work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Tool Description Audit Drafter

Use this skill in Hermes Agent when the task involves mcp tool description audit drafter. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: tool description audit schema validity, tool description audit description clarity, tool description audit least privilege.
2. Run the `mcp_tool_description_audit_drafter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: tool description audit test coverage, tool description audit error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
