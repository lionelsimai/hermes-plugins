# Retrieval Test Drafter

Retrieval Test Drafter for Hermes Agent: apply a score workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_retrieval_test_drafter` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_retrieval_test_drafter",
  "arguments": {
    "metrics": {
      "retrieval_test_source_fidelity": 80,
      "retrieval_test_retrieval_relevance": 65,
      "retrieval_test_citation_coverage": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
