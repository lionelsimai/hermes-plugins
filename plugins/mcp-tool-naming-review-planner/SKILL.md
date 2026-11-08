---
name: mcp-tool-naming-review-planner
description: "Tool Naming Review Planner for Hermes Agent: apply a classify workflow to tool naming review work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Tool Naming Review Planner

Use this skill in Hermes Agent when the task involves mcp tool naming review planner. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: tool naming review schema validity, tool naming review description clarity, tool naming review least privilege.
2. Run the `mcp_tool_naming_review_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: tool naming review test coverage, tool naming review error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
