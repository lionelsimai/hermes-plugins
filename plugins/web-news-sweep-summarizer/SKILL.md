---
name: web-news-sweep-summarizer
description: "News Sweep Summarizer for Hermes Agent: apply a score workflow to news sweep work — covers source quality, recency and scope fit, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web Research & Browsing, Hermes, Plugins]
    category: web-research-browsing
---

# News Sweep Summarizer

Use this skill in Hermes Agent when the task involves web news sweep summarizer. It sits in the Web Research & Browsing category; the suggested Hermes toolset is `web`.

## Workflow
1. Confirm the goal and gather supplied facts about: news sweep source quality, news sweep recency, news sweep corroboration.
2. Run the `web_news_sweep_summarizer` tool (or follow this procedure manually) — kind: score.
3. Check the output against: news sweep citation completeness, news sweep scope fit.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
