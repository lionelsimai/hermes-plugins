# Wiki Outline Analyzer

Wiki Outline Analyzer for Hermes Agent: apply a analyze workflow to wiki outline work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_wiki_outline_analyzer` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_wiki_outline_analyzer",
  "arguments": {
    "counts": {
      "wiki_outline_source_fidelity": 40,
      "wiki_outline_retrieval_relevance": 25,
      "wiki_outline_citation_coverage": 10,
      "wiki_outline_freshness": 75
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
