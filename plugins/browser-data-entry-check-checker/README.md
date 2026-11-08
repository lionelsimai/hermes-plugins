# Data Entry Check Checker

Data Entry Check Checker for Hermes Agent: apply a score workflow to data entry check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_data_entry_check_checker` (kind: score)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_data_entry_check_checker",
  "arguments": {
    "metrics": {
      "data_entry_check_step_clarity": 80,
      "data_entry_check_fallback_step": 65,
      "data_entry_check_data_accuracy": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
