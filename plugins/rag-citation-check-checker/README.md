# Citation Check Checker

Citation Check Checker for Hermes Agent: apply a analyze workflow to citation check work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_citation_check_checker` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_citation_check_checker",
  "arguments": {
    "counts": {
      "citation_check_source_fidelity": 40,
      "citation_check_retrieval_relevance": 25,
      "citation_check_citation_coverage": 10,
      "citation_check_freshness": 75
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
