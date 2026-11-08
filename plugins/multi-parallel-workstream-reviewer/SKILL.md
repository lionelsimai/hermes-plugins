---
name: multi-parallel-workstream-reviewer
description: "Parallel Workstream Reviewer for Hermes Agent: apply a template workflow to parallel workstream work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Parallel Workstream Reviewer

Use this skill in Hermes Agent when the task involves multi parallel workstream reviewer. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: parallel workstream scope clarity, parallel workstream independence of subtasks, parallel workstream merge criteria.
2. Run the `multi_parallel_workstream_reviewer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: parallel workstream context budget, parallel workstream verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
