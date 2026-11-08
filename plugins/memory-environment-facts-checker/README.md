# Environment Facts Checker

Environment Facts Checker for Hermes Agent: apply a score workflow to environment facts work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_environment_facts_checker` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_environment_facts_checker",
  "arguments": {
    "metrics": {
      "environment_facts_fact_accuracy": 80,
      "environment_facts_size_budget_fit": 65,
      "environment_facts_staleness": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
