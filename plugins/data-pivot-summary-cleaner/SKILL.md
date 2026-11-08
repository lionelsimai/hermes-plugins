---
name: data-pivot-summary-cleaner
description: "Pivot Summary Cleaner for Hermes Agent: apply a plan workflow to pivot summary work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Pivot Summary Cleaner

Use this skill in Hermes Agent when the task involves data pivot summary cleaner. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: pivot summary data completeness, pivot summary column consistency, pivot summary outliers flagged.
2. Run the `data_pivot_summary_cleaner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: pivot summary totals verified, pivot summary format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
