---
name: web-competitor-page-verifier
description: "Competitor Page Verifier for Hermes Agent: apply a template workflow to competitor page work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Competitor Page Verifier

Use this skill in Hermes Agent when the task involves web competitor page verifier. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: competitor page source quality, competitor page recency, competitor page corroboration.
2. Run the `web_competitor_page_verifier` tool (or follow this procedure manually) — kind: template.
3. Check the output against: competitor page citation completeness, competitor page scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
