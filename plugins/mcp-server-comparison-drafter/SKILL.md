---
name: mcp-server-comparison-drafter
description: "Server Comparison Drafter for Hermes Agent: apply a audit workflow to server comparison work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Server Comparison Drafter

Use this skill in Hermes Agent when the task involves mcp server comparison drafter. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: server comparison schema validity, server comparison description clarity, server comparison least privilege.
2. Run the `mcp_server_comparison_drafter` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: server comparison test coverage, server comparison error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
