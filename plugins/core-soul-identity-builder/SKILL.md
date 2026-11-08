---
name: core-soul-identity-builder
description: "Soul Identity Builder for Hermes Agent: apply a classify workflow to SOUL identity work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Soul Identity Builder

Use this skill in Hermes Agent when the task involves core soul identity builder. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: SOUL identity goal clarity, SOUL identity setup completeness, SOUL identity toolset fit.
2. Run the `core_soul_identity_builder` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: SOUL identity guardrail coverage, SOUL identity verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
