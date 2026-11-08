---
name: multi-review-delegation-planner
description: "Review Delegation Planner for Hermes Agent: apply a score workflow to review delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Review Delegation Planner

Use this skill in Hermes Agent when the task involves multi review delegation planner. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: review delegation scope clarity, review delegation independence of subtasks, review delegation merge criteria.
2. Run the `multi_review_delegation_planner` tool (or follow this procedure manually) — kind: score.
3. Check the output against: review delegation context budget, review delegation verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
