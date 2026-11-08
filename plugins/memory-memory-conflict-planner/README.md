# Memory Conflict Planner

Memory Conflict Planner for Hermes Agent: apply a score workflow to memory conflict work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_memory_conflict_planner` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_memory_conflict_planner",
  "arguments": {
    "metrics": {
      "memory_conflict_fact_accuracy": 80,
      "memory_conflict_size_budget_fit": 65,
      "memory_conflict_staleness": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
