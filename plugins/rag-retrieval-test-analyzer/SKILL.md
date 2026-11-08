---
name: rag-retrieval-test-analyzer
description: "Retrieval Test Analyzer for Hermes Agent: apply a checklist workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Retrieval Test Analyzer

Use this skill in Hermes Agent when the task involves rag retrieval test analyzer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: retrieval test source fidelity, retrieval test retrieval relevance, retrieval test citation coverage.
2. Run the `rag_retrieval_test_analyzer` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: retrieval test freshness, retrieval test gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
