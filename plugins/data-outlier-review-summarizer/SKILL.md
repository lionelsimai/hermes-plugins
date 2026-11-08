---
name: data-outlier-review-summarizer
description: "Outlier Review Summarizer for Hermes Agent: apply a classify workflow to outlier review work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Outlier Review Summarizer

Use this skill in Hermes Agent when the task involves data outlier review summarizer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: outlier review data completeness, outlier review column consistency, outlier review outliers flagged.
2. Run the `data_outlier_review_summarizer` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: outlier review totals verified, outlier review format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
