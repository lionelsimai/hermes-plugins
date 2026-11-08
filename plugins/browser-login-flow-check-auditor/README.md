# Login Flow Check Auditor

Login Flow Check Auditor for Hermes Agent: apply a analyze workflow to login flow check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_login_flow_check_auditor` (kind: analyze)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_login_flow_check_auditor",
  "arguments": {
    "counts": {
      "login_flow_check_step_clarity": 40,
      "login_flow_check_fallback_step": 25,
      "login_flow_check_data_accuracy": 10,
      "login_flow_check_confirmation_gate": 75
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
