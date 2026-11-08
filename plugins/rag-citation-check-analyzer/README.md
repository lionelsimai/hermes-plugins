# Citation Check Analyzer

Citation Check Analyzer for Hermes Agent: apply a plan workflow to citation check work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_citation_check_analyzer` (kind: plan)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_citation_check_analyzer",
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
