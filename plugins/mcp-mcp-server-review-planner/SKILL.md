---
name: mcp-mcp-server-review-planner
description: "Mcp Server Review Planner for Hermes Agent: apply a plan workflow to mcp server review work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Mcp Server Review Planner

Use this skill in Hermes Agent when the task involves mcp mcp server review planner. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: mcp server review schema validity, mcp server review description clarity, mcp server review least privilege.
2. Run the `mcp_mcp_server_review_planner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: mcp server review test coverage, mcp server review error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
