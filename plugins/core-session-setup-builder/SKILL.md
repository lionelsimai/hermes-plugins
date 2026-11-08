---
name: core-session-setup-builder
description: "Session Setup Builder for Hermes Agent: apply a audit workflow to session setup work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Session Setup Builder

Use this skill in Hermes Agent when the task involves core session setup builder. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: session setup goal clarity, session setup setup completeness, session setup toolset fit.
2. Run the `core_session_setup_builder` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: session setup guardrail coverage, session setup verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
