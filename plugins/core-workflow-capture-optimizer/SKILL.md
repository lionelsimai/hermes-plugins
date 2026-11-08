---
name: core-workflow-capture-optimizer
description: "Workflow Capture Optimizer for Hermes Agent: apply a prioritize workflow to workflow capture work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Workflow Capture Optimizer

Use this skill in Hermes Agent when the task involves core workflow capture optimizer. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: workflow capture goal clarity, workflow capture setup completeness, workflow capture toolset fit.
2. Run the `core_workflow_capture_optimizer` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: workflow capture guardrail coverage, workflow capture verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
