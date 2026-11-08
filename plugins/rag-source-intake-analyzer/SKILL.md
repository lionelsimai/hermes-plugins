---
name: rag-source-intake-analyzer
description: "Source Intake Analyzer for Hermes Agent: apply a template workflow to source intake work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Source Intake Analyzer

Use this skill in Hermes Agent when the task involves rag source intake analyzer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: source intake source fidelity, source intake retrieval relevance, source intake citation coverage.
2. Run the `rag_source_intake_analyzer` tool (or follow this procedure manually) — kind: template.
3. Check the output against: source intake freshness, source intake gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
