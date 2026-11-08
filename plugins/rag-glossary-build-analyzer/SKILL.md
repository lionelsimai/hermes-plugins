---
name: rag-glossary-build-analyzer
description: "Glossary Build Analyzer for Hermes Agent: apply a audit workflow to glossary build work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Glossary Build Analyzer

Use this skill in Hermes Agent when the task involves rag glossary build analyzer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: glossary build source fidelity, glossary build retrieval relevance, glossary build citation coverage.
2. Run the `rag_glossary_build_analyzer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: glossary build freshness, glossary build gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
