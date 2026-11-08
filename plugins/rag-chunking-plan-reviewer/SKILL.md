---
name: rag-chunking-plan-reviewer
description: "Chunking Plan Reviewer for Hermes Agent: apply a audit workflow to chunking plan work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Chunking Plan Reviewer

Use this skill in Hermes Agent when the task involves rag chunking plan reviewer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: chunking plan source fidelity, chunking plan retrieval relevance, chunking plan citation coverage.
2. Run the `rag_chunking_plan_reviewer` tool (or follow this procedure manually) — kind: audit.
3. Check the output against: chunking plan freshness, chunking plan gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
