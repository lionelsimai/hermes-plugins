---
name: multi-task-split-plan-planner
description: "Task Split Plan Planner for Hermes Agent: apply a classify workflow to task split plan work — covers scope clarity, independence of subtasks and verification step, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Multi-Agent & Delegation, Hermes, Plugins]
    category: multi-agent-delegation
---

# Task Split Plan Planner

Use this skill in Hermes Agent when the task involves multi task split plan planner. It sits in the Multi-Agent & Delegation category; the suggested Hermes toolset is `delegation`.

## Workflow
1. Confirm the goal and gather supplied facts about: task split plan scope clarity, task split plan independence of subtasks, task split plan merge criteria.
2. Run the `multi_task_split_plan_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: task split plan context budget, task split plan verification step.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
