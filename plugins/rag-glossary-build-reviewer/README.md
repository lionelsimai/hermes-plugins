# Glossary Build Reviewer

Glossary Build Reviewer for Hermes Agent: apply a analyze workflow to glossary build work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_glossary_build_reviewer` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_glossary_build_reviewer",
  "arguments": {
    "counts": {
      "glossary_build_source_fidelity": 40,
      "glossary_build_retrieval_relevance": 25,
      "glossary_build_citation_coverage": 10,
      "glossary_build_freshness": 75
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
