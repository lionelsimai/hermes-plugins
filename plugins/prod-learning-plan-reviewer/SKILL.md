---
name: prod-learning-plan-reviewer
description: "Learning Plan Reviewer for Hermes Agent: apply a plan workflow to learning plan work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Learning Plan Reviewer

Use this skill in Hermes Agent when the task involves prod learning plan reviewer. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: learning plan priority clarity, learning plan time realism, learning plan next action named.
2. Run the `prod_learning_plan_reviewer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: learning plan review cadence, learning plan owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
