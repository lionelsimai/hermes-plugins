---
name: terminal-environment-setup-auditor
description: "Environment Setup Auditor for Hermes Agent: apply a plan workflow to environment setup work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Environment Setup Auditor

Use this skill in Hermes Agent when the task involves terminal environment setup auditor. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: environment setup command safety, environment setup expected output, environment setup timeout set.
2. Run the `terminal_environment_setup_auditor` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: environment setup rollback step, environment setup verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
