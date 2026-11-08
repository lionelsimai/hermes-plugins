# Context Summary Planner

Context Summary Planner for Hermes Agent: apply a analyze workflow to context summary work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_context_summary_planner` (kind: analyze)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_context_summary_planner",
  "arguments": {
    "counts": {
      "context_summary_fact_accuracy": 40,
      "context_summary_size_budget_fit": 25,
      "context_summary_staleness": 10,
      "context_summary_duplication": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
