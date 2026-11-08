# Source Intake Analyzer

Source Intake Analyzer for Hermes Agent: apply a template workflow to source intake work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_source_intake_analyzer` (kind: template)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_source_intake_analyzer",
  "arguments": {
    "facts": {
      "source_intake_source_fidelity": "Sample supplied fact",
      "source_intake_retrieval_relevance": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
