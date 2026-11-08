---
name: rag-freshness-review-planner
description: "Freshness Review Planner for Hermes Agent: apply a plan workflow to freshness review work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Freshness Review Planner

Use this skill in Hermes Agent when the task involves rag freshness review planner. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: freshness review source fidelity, freshness review retrieval relevance, freshness review citation coverage.
2. Run the `rag_freshness_review_planner` tool (or follow this procedure manually) — kind: plan.
3. Check the output against: freshness review freshness, freshness review gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
