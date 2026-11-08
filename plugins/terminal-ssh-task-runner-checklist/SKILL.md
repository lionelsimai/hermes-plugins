---
name: terminal-ssh-task-runner-checklist
description: "Ssh Task Runner Checklist for Hermes Agent: apply a plan workflow to ssh task work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Ssh Task Runner Checklist

Use this skill in Hermes Agent when the task involves terminal ssh task runner checklist. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: ssh task command safety, ssh task expected output, ssh task timeout set.
2. Run the `terminal_ssh_task_runner_checklist` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: ssh task rollback step, ssh task verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
