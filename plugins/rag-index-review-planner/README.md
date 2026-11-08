# Index Review Planner

Index Review Planner for Hermes Agent: apply a score workflow to index review work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_index_review_planner` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_index_review_planner",
  "arguments": {
    "metrics": {
      "index_review_source_fidelity": 80,
      "index_review_retrieval_relevance": 65,
      "index_review_citation_coverage": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
