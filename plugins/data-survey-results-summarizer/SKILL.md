---
name: data-survey-results-summarizer
description: "Survey Results Summarizer for Hermes Agent: apply a score workflow to survey results work — covers data completeness, column consistency and format fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Data & Spreadsheets, Hermes, Plugins]
    category: data-spreadsheets
---

# Survey Results Summarizer

Use this skill in Hermes Agent when the task involves data survey results summarizer. It sits in the Data & Spreadsheets category; the suggested Hermes toolset is `file`.

## Workflow
1. Confirm the goal and gather supplied facts about: survey results data completeness, survey results column consistency, survey results outliers flagged.
2. Run the `data_survey_results_summarizer` tool (or follow this procedure manually) — kind: score.
3. Check the output against: survey results totals verified, survey results format fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
