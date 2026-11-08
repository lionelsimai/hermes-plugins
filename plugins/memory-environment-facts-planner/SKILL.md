---
name: memory-environment-facts-planner
description: "Environment Facts Planner for Hermes Agent: apply a checklist workflow to environment facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Memory & Context, Hermes, Plugins]
    category: memory-context
---

# Environment Facts Planner

Use this skill in Hermes Agent when the task involves memory environment facts planner. It sits in the Memory & Context category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: environment facts fact accuracy, environment facts size budget fit, environment facts staleness.
2. Run the `memory_environment_facts_planner` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: environment facts duplication, environment facts source noted.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
