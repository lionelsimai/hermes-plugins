---
name: files-archive-bundle-drafter
description: "Archive Bundle Drafter for Hermes Agent: apply a analyze workflow to archive bundle work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Archive Bundle Drafter

Use this skill in Hermes Agent when the task involves files archive bundle drafter. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: archive bundle format fit, archive bundle completeness, archive bundle naming consistency.
2. Run the `files_archive_bundle_drafter` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: archive bundle source fidelity, archive bundle output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
