# Gap Analysis Planner

Gap Analysis Planner for Hermes Agent: apply a analyze workflow to gap analysis work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_gap_analysis_planner` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_gap_analysis_planner",
  "arguments": {
    "counts": {
      "gap_analysis_source_fidelity": 40,
      "gap_analysis_retrieval_relevance": 25,
      "gap_analysis_citation_coverage": 10,
      "gap_analysis_freshness": 75
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
