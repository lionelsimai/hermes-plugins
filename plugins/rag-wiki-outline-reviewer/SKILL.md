---
name: rag-wiki-outline-reviewer
description: "Wiki Outline Reviewer for Hermes Agent: apply a checklist workflow to wiki outline work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Knowledge & RAG, Hermes, Plugins]
    category: knowledge-rag
---

# Wiki Outline Reviewer

Use this skill in Hermes Agent when the task involves rag wiki outline reviewer. It sits in the Knowledge & RAG category; the suggested Hermes toolset is `memory`.

## Workflow
1. Confirm the goal and gather supplied facts about: wiki outline source fidelity, wiki outline retrieval relevance, wiki outline citation coverage.
2. Run the `rag_wiki_outline_reviewer` tool (or follow this procedure manually) — kind: checklist.
3. Check the output against: wiki outline freshness, wiki outline gap honesty.
4. Show the result to the human. Drafts stay drafts until a human approves.

## Guardrails
- Use supplied facts only. Never invent facts, metrics or proof.
- No auto-send and no external action without human approval.
- Never handle credentials, tokens or passwords.
