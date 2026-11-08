---
name: rag-glossary-build-drafter
description: "Glossary Build Drafter for Hermes Agent: apply a classify workflow to glossary build work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Glossary Build Drafter

Use this skill in Hermes Agent when the task involves rag glossary build drafter. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: glossary build source fidelity, glossary build retrieval relevance, glossary build citation coverage.
2. Run the `rag_glossary_build_drafter` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: glossary build freshness, glossary build gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
