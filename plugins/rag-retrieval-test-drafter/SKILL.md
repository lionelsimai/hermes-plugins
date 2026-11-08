---
name: rag-retrieval-test-drafter
description: "Retrieval Test Drafter for Hermes Agent: apply a score workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Retrieval Test Drafter

Use this skill in Hermes Agent when the task involves rag retrieval test drafter. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: retrieval test source fidelity, retrieval test retrieval relevance, retrieval test citation coverage.
2. Run the `rag_retrieval_test_drafter` tool (or follow this procedure manually) — kind: score.
3. Check the output against: retrieval test freshness, retrieval test gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
