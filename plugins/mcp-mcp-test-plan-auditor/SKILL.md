---
name: mcp-mcp-test-plan-auditor
description: "Mcp Test Plan Auditor for Hermes Agent: apply a checklist workflow to mcp test plan work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Mcp Test Plan Auditor

Use this skill in Hermes Agent when the task involves mcp mcp test plan auditor. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: mcp test plan schema validity, mcp test plan description clarity, mcp test plan least privilege.
2. Run the `mcp_mcp_test_plan_auditor` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: mcp test plan test coverage, mcp test plan error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
