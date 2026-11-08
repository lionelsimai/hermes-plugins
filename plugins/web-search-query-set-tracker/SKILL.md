---
name: web-search-query-set-tracker
description: "Search Query Set Tracker for Hermes Agent: apply a score workflow to search query set work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Search Query Set Tracker

Use this skill in Hermes Agent when the task involves web search query set tracker. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: search query set source quality, search query set recency, search query set corroboration.
2. Run the `web_search_query_set_tracker` tool (or follow this procedure manually) — kind: score.
3. Check the output against: search query set citation completeness, search query set scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
