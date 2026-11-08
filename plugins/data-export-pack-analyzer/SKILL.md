---
name: data-export-pack-analyzer
description: "Export Pack Analyzer for Hermes Agent: apply a prioritize workflow to export pack work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Export Pack Analyzer

Use this skill in Hermes Agent when the task involves data export pack analyzer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: export pack data completeness, export pack column consistency, export pack outliers flagged.
2. Run the `data_export_pack_analyzer` tool (or follow this procedure manually) — kind: prioritize.
3. Check the output against: export pack totals verified, export pack format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
