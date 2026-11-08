---
name: terminal-script-draft-auditor
description: "Script Draft Auditor for Hermes Agent: apply a analyze workflow to script draft work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Script Draft Auditor

Use this skill in Hermes Agent when the task involves terminal script draft auditor. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: script draft command safety, script draft expected output, script draft timeout set.
2. Run the `terminal_script_draft_auditor` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: script draft rollback step, script draft verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
