---
name: prod-task-list-triage-reviewer
description: "Task List Triage Reviewer for Hermes Agent: apply a plan workflow to task list triage work — covers priority clarity, time realism and owner named, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Personal Productivity, Hermes, Plugins]
    category: personal-productivity
---

# Task List Triage Reviewer

Use this skill in Hermes Agent when the task involves prod task list triage reviewer. It sits in the Personal Productivity category; the suggested Hermes toolset is `skills`.

## Workflow
1. Confirm the goal and gather supplied facts about: task list triage priority clarity, task list triage time realism, task list triage next action named.
2. Run the `prod_task_list_triage_reviewer` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: task list triage review cadence, task list triage owner named.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
