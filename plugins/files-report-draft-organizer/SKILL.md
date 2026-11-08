---
name: files-report-draft-organizer
description: "Report Draft Organizer for Hermes Agent: apply a analyze workflow to report draft work — covers format fit, completeness and output location, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [File & Document Work, Hermes, Plugins]
    category: file-document-work
---

# Report Draft Organizer

Use this skill in Hermes Agent when the task involves files report draft organizer. It sits in the File & Document Work category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: report draft format fit, report draft completeness, report draft naming consistency.
2. Run the `files_report_draft_organizer` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: report draft source fidelity, report draft output location.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
