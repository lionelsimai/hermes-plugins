# Context Summary Auditor

Context Summary Auditor for Hermes Agent: apply a score workflow to context summary work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_context_summary_auditor` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_context_summary_auditor",
  "arguments": {
    "metrics": {
      "context_summary_fact_accuracy": 80,
      "context_summary_size_budget_fit": 65,
      "context_summary_staleness": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
