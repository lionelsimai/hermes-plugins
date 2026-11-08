---
name: multi-delegation-retrospective-checker
description: "Delegation Retrospective Checker for Hermes Agent: apply a classify workflow to delegation retrospective work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Delegation Retrospective Checker

Use this skill in Hermes Agent when the task involves multi delegation retrospective checker. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: delegation retrospective scope clarity, delegation retrospective independence of subtasks, delegation retrospective merge criteria.
2. Run the `multi_delegation_retrospective_checker` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: delegation retrospective context budget, delegation retrospective verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
