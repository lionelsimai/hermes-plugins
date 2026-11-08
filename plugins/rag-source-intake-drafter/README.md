# Source Intake Drafter

Source Intake Drafter for Hermes Agent: apply a checklist workflow to source intake work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_source_intake_drafter` (kind: checklist)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_source_intake_drafter",
  "arguments": {
    "completed": [
      "source intake source fidelity",
      "source intake retrieval relevance"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
