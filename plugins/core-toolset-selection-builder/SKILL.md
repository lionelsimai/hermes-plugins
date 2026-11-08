---
name: core-toolset-selection-builder
description: "Toolset Selection Builder for Hermes Agent: apply a template workflow to toolset selection work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Toolset Selection Builder

Use this skill in Hermes Agent when the task involves core toolset selection builder. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: toolset selection goal clarity, toolset selection setup completeness, toolset selection toolset fit.
2. Run the `core_toolset_selection_builder` tool (or follow this procedure manually) — kind: template.
3. Check the output against: toolset selection guardrail coverage, toolset selection verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
