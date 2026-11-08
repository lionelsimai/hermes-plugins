# Retrieval Test Checker

Retrieval Test Checker for Hermes Agent: apply a plan workflow to retrieval test work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_retrieval_test_checker` (kind: plan)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_retrieval_test_checker",
  "arguments": {
    "goal": "Sample goal for this workflow",
    "timeframe_days": 14
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
