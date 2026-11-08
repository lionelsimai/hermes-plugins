# Decision Log Planner

Decision Log Planner for Hermes Agent: apply a audit workflow to decision log work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_decision_log_planner` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_decision_log_planner",
  "arguments": {
    "text": "This sample covers decision log priority clarity and decision log time realism in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
