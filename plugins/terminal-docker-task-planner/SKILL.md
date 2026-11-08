---
name: terminal-docker-task-planner
description: "Docker Task Planner for Hermes Agent: apply a template workflow to docker task work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Docker Task Planner

Use this skill in Hermes Agent when the task involves terminal docker task planner. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: docker task command safety, docker task expected output, docker task timeout set.
2. Run the `terminal_docker_task_planner` tool (or follow this procedure manually) — kind: template.
3. Check the output against: docker task rollback step, docker task verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
