---
name: terminal-debug-session-auditor
description: "Debug Session Auditor for Hermes Agent: apply a template workflow to debug session work — covers command safety, expected output and verification, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Terminal & Code Execution, Hermes, Plugins]
    category: terminal-code-execution
---

# Debug Session Auditor

Use this skill in Hermes Agent when the task involves terminal debug session auditor. It sits in the Terminal & Code Execution category; the suggested Hermes toolset is `terminal`.

## Workflow
1. Confirm the goal and gather supplied facts about: debug session command safety, debug session expected output, debug session timeout set.
2. Run the `terminal_debug_session_auditor` tool (or follow this procedure manually) — kind: template.
3. Check the output against: debug session rollback step, debug session verification.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
