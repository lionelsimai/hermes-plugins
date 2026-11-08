# Data Entry Check Sequencer

Data Entry Check Sequencer for Hermes Agent: apply a template workflow to data entry check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_data_entry_check_sequencer` (kind: template)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_data_entry_check_sequencer",
  "arguments": {
    "facts": {
      "data_entry_check_step_clarity": "Sample supplied fact",
      "data_entry_check_fallback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
