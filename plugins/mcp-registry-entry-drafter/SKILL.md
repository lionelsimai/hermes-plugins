---
name: mcp-registry-entry-drafter
description: "Registry Entry Drafter for Hermes Agent: apply a checklist workflow to registry entry work — covers schema validity, description clarity and error behaviour, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP Tooling, Hermes, Plugins]
    category: mcp-tooling
---

# Registry Entry Drafter

Use this skill in Hermes Agent when the task involves mcp registry entry drafter. It sits in the MCP Tooling category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: registry entry schema validity, registry entry description clarity, registry entry least privilege.
2. Run the `mcp_registry_entry_drafter` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: registry entry test coverage, registry entry error behaviour.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
