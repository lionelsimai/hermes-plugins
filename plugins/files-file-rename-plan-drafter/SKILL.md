---
name: files-file-rename-plan-drafter
description: "File Rename Plan Drafter for Hermes Agent: apply a template workflow to file rename plan work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# File Rename Plan Drafter

Use this skill in Hermes Agent when the task involves files file rename plan drafter. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: file rename plan format fit, file rename plan completeness, file rename plan naming consistency.
2. Run the `files_file_rename_plan_drafter` tool (or follow this procedure manually) — kind: template.
3. Check the output against: file rename plan source fidelity, file rename plan output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
