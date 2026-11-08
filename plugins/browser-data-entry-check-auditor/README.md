# Data Entry Check Auditor

Data Entry Check Auditor for Hermes Agent: apply a checklist workflow to data entry check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_data_entry_check_auditor` (kind: checklist)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_data_entry_check_auditor",
  "arguments": {
    "completed": [
      "data entry check step clarity",
      "data entry check fallback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
