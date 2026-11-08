---
name: core-model-routing-optimizer
description: "Model Routing Optimizer for Hermes Agent: apply a analyze workflow to model routing work — covers goal clarity, setup completeness and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Core Agent Ops & Skill Authoring, Hermes, Plugins]
    category: core-agent-ops-skill-authoring
---

# Model Routing Optimizer

Use this skill in Hermes Agent when the task involves core model routing optimizer. It sits in the Core Agent Ops & Skill Authoring category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: model routing goal clarity, model routing setup completeness, model routing toolset fit.
2. Run the `core_model_routing_optimizer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: model routing guardrail coverage, model routing verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
