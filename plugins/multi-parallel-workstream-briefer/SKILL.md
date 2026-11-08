---
name: multi-parallel-workstream-briefer
description: "Parallel Workstream Briefer for Hermes Agent: apply a prioritize workflow to parallel workstream work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Parallel Workstream Briefer

Use this skill in Hermes Agent when the task involves multi parallel workstream briefer. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: parallel workstream scope clarity, parallel workstream independence of subtasks, parallel workstream merge criteria.
2. Run the `multi_parallel_workstream_briefer` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: parallel workstream context budget, parallel workstream verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
