---
name: rag-citation-check-drafter
description: "Citation Check Drafter for Hermes Agent: apply a audit workflow to citation check work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Citation Check Drafter

Use this skill in Hermes Agent when the task involves rag citation check drafter. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: citation check source fidelity, citation check retrieval relevance, citation check citation coverage.
2. Run the `rag_citation_check_drafter` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: citation check freshness, citation check gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
