---
name: web-price-research-extractor
description: "Price Research Extractor for Hermes Agent: apply a analyze workflow to price research work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# Price Research Extractor

Use this skill in Hermes Agent when the task involves web price research extractor. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: price research source quality, price research recency, price research corroboration.
2. Run the `web_price_research_extractor` tool (or follow this procedure manually) — kind: analyze.
3. Check the output against: price research citation completeness, price research scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
