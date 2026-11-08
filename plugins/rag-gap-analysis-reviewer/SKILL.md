---
name: rag-gap-analysis-reviewer
description: "Gap Analysis Reviewer for Hermes Agent: apply a audit workflow to gap analysis work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Gap Analysis Reviewer

Use this skill in Hermes Agent when the task involves rag gap analysis reviewer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: gap analysis source fidelity, gap analysis retrieval relevance, gap analysis citation coverage.
2. Run the `rag_gap_analysis_reviewer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: gap analysis freshness, gap analysis gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
