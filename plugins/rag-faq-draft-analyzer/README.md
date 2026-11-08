# Faq Draft Analyzer

Faq Draft Analyzer for Hermes Agent: apply a score workflow to faq draft work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_faq_draft_analyzer` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_faq_draft_analyzer",
  "arguments": {
    "metrics": {
      "faq_draft_source_fidelity": 80,
      "faq_draft_retrieval_relevance": 65,
      "faq_draft_citation_coverage": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
