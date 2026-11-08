# Chunking Plan Planner

Chunking Plan Planner for Hermes Agent: apply a analyze workflow to chunking plan work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_chunking_plan_planner` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_chunking_plan_planner",
  "arguments": {
    "counts": {
      "chunking_plan_source_fidelity": 40,
      "chunking_plan_retrieval_relevance": 25,
      "chunking_plan_citation_coverage": 10,
      "chunking_plan_freshness": 75
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
