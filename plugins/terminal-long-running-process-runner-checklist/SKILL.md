---
name: terminal-long-running-process-runner-checklist
description: "Long Running Process Runner Checklist for Hermes Agent: apply a score workflow to long running process work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Long Running Process Runner Checklist

Use this skill in Hermes Agent when the task involves terminal long running process runner checklist. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: long running process command safety, long running process expected output, long running process timeout set.
2. Run the `terminal_long_running_process_runner_checklist` tool (or follow this procedure manually) — kind: score.
3. Check the output against: long running process rollback step, long running process verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
