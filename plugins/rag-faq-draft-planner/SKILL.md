---
name: rag-faq-draft-planner
description: "Faq Draft Planner for Hermes Agent: apply a classify workflow to faq draft work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Faq Draft Planner

Use this skill in Hermes Agent when the task involves rag faq draft planner. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: faq draft source fidelity, faq draft retrieval relevance, faq draft citation coverage.
2. Run the `rag_faq_draft_planner` tool (or follow this procedure manually) — kind: classify.
3. Check the output against: faq draft freshness, faq draft gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
