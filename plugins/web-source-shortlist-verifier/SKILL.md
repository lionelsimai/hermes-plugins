---
name: web-source-shortlist-verifier
description: "Source Shortlist Verifier for Hermes Agent: apply a analyze workflow to source shortlist work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Source Shortlist Verifier

Use this skill in Hermes Agent when the task involves web source shortlist verifier. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: source shortlist source quality, source shortlist recency, source shortlist corroboration.
2. Run the `web_source_shortlist_verifier` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: source shortlist citation completeness, source shortlist scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
