---
name: mcp-tool-schema-draft-checker
description: "Tool Schema Draft Checker for Hermes Agent: apply a classify workflow to tool schema draft work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Tool Schema Draft Checker

Use this skill in Hermes Agent when the task involves mcp tool schema draft checker. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: tool schema draft schema validity, tool schema draft description clarity, tool schema draft least privilege.
2. Run the `mcp_tool_schema_draft_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: tool schema draft test coverage, tool schema draft error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
