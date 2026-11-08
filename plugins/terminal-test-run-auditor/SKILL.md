---
name: terminal-test-run-auditor
description: "Test Run Auditor for Hermes Agent: apply a prioritize workflow to test run work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Test Run Auditor

Use this skill in Hermes Agent when the task involves terminal test run auditor. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: test run command safety, test run expected output, test run timeout set.
2. Run the `terminal_test_run_auditor` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: test run rollback step, test run verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
