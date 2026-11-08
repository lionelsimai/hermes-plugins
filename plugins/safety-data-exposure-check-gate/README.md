# Data Exposure Check Gate

Data Exposure Check Gate for Hermes Agent: apply a template workflow to data exposure check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_data_exposure_check_gate` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_data_exposure_check_gate",
  "arguments": {
    "facts": {
      "data_exposure_check_risk_identified": "Sample supplied fact",
      "data_exposure_check_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
