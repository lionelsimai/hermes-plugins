# Data Exposure Check Auditor

Data Exposure Check Auditor for Hermes Agent: apply a classify workflow to data exposure check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_data_exposure_check_auditor` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_data_exposure_check_auditor",
  "arguments": {
    "text": "Please review: this concerns data exposure check risk identified and data exposure check least privilege."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
