# Retrieval Test Analyzer

Retrieval Test Analyzer for Hermes Agent: apply a checklist workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_retrieval_test_analyzer` (kind: checklist)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_retrieval_test_analyzer",
  "arguments": {
    "completed": [
      "retrieval test source fidelity",
      "retrieval test retrieval relevance"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
