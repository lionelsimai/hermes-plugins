---
name: rag-retrieval-test-planner
description: "Retrieval Test Planner for Hermes Agent: apply a audit workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Retrieval Test Planner

Use this skill in Hermes Agent when the task involves rag retrieval test planner. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: retrieval test source fidelity, retrieval test retrieval relevance, retrieval test citation coverage.
2. Run the `rag_retrieval_test_planner` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: retrieval test freshness, retrieval test gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
