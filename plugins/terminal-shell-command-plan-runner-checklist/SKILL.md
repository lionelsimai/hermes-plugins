---
name: terminal-shell-command-plan-runner-checklist
description: "Shell Command Plan Runner Checklist for Hermes Agent: apply a analyze workflow to shell command plan work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Shell Command Plan Runner Checklist

Use this skill in Hermes Agent when the task involves terminal shell command plan runner checklist. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: shell command plan command safety, shell command plan expected output, shell command plan timeout set.
2. Run the `terminal_shell_command_plan_runner_checklist` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: shell command plan rollback step, shell command plan verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
