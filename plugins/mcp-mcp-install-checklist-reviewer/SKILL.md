---
name: mcp-mcp-install-checklist-reviewer
description: "Mcp Install Checklist Reviewer for Hermes Agent: apply a audit workflow to mcp install checklist work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Mcp Install Checklist Reviewer

Use this skill in Hermes Agent when the task involves mcp mcp install checklist reviewer. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: mcp install checklist schema validity, mcp install checklist description clarity, mcp install checklist least privilege.
2. Run the `mcp_mcp_install_checklist_reviewer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: mcp install checklist test coverage, mcp install checklist error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
