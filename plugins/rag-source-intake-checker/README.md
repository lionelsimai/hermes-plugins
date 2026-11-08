# Source Intake Checker

Source Intake Checker for Hermes Agent: apply a prioritize workflow to source intake work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_source_intake_checker` (kind: prioritize)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_source_intake_checker",
  "arguments": {
    "items": [
      {
        "name": "Sample task A",
        "impact": 8,
        "effort": 3
      },
      {
        "name": "Sample task B",
        "impact": 6,
        "effort": 1
      }
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
