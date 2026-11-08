# Secret Handling Check Auditor

Secret Handling Check Auditor for Hermes Agent: apply a analyze workflow to secret handling check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_secret_handling_check_auditor` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_secret_handling_check_auditor",
  "arguments": {
    "counts": {
      "secret_handling_check_risk_identified": 40,
      "secret_handling_check_approval_required": 25,
      "secret_handling_check_least_privilege": 10,
      "secret_handling_check_reversibility": 75
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
