---
name: data-merge-plan-cleaner
description: "Merge Plan Cleaner for Hermes Agent: apply a classify workflow to merge plan work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Merge Plan Cleaner

Use this skill in Hermes Agent when the task involves data merge plan cleaner. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: merge plan data completeness, merge plan column consistency, merge plan outliers flagged.
2. Run the `data_merge_plan_cleaner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: merge plan totals verified, merge plan format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
