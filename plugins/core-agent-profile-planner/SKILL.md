---
name: core-agent-profile-planner
description: "Agent Profile Planner for Hermes Agent: apply a template workflow to agent profile work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Agent Profile Planner

Use this skill in Hermes Agent when the task involves core agent profile planner. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: agent profile goal clarity, agent profile setup completeness, agent profile toolset fit.
2. Run the `core_agent_profile_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: agent profile guardrail coverage, agent profile verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
