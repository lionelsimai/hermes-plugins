---
name: mcp-transport-check-checker
description: "Transport Check Checker for Hermes Agent: apply a prioritize workflow to transport check work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Transport Check Checker

Use this skill in Hermes Agent when the task involves mcp transport check checker. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: transport check schema validity, transport check description clarity, transport check least privilege.
2. Run the `mcp_transport_check_checker` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: transport check test coverage, transport check error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
