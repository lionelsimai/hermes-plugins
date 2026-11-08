# Decision Log Tracker

Decision Log Tracker for Hermes Agent: apply a score workflow to decision log work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_decision_log_tracker` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_decision_log_tracker",
  "arguments": {
    "metrics": {
      "decision_log_priority_clarity": 80,
      "decision_log_time_realism": 65,
      "decision_log_next_action_named": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
