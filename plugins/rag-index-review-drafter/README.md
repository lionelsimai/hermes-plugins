# Index Review Drafter

Index Review Drafter for Hermes Agent: apply a analyze workflow to index review work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_index_review_drafter` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_index_review_drafter",
  "arguments": {
    "counts": {
      "index_review_source_fidelity": 40,
      "index_review_retrieval_relevance": 25,
      "index_review_citation_coverage": 10,
      "index_review_freshness": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
