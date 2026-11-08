---
name: terminal-test-run-drafter
description: "Test Run Drafter for Hermes Agent: apply a score workflow to test run work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Test Run Drafter

Use this skill in Hermes Agent when the task involves terminal test run drafter. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: test run command safety, test run expected output, test run timeout set.
2. Run the `terminal_test_run_drafter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: test run rollback step, test run verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
