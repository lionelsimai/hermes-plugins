# Glossary Build Drafter

Glossary Build Drafter for Hermes Agent: apply a classify workflow to glossary build work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_glossary_build_drafter` (kind: classify)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_glossary_build_drafter",
  "arguments": {
    "text": "Please review: this concerns glossary build source fidelity and glossary build citation coverage."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
