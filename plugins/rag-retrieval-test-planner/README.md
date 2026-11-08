# Retrieval Test Planner

Retrieval Test Planner for Hermes Agent: apply a audit workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_retrieval_test_planner` (kind: audit)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_retrieval_test_planner",
  "arguments": {
    "text": "This sample covers retrieval test source fidelity and retrieval test retrieval relevance in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
