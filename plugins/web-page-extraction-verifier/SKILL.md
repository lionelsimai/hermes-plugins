---
name: web-page-extraction-verifier
description: "Page Extraction Verifier for Hermes Agent: apply a score workflow to page extraction work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Page Extraction Verifier

Use this skill in Hermes Agent when the task involves web page extraction verifier. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: page extraction source quality, page extraction recency, page extraction corroboration.
2. Run the `web_page_extraction_verifier` tool (or follow this procedure manually) — kind: score.
3. Check the output against: page extraction citation completeness, page extraction scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
