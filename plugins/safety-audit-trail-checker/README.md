# Audit Trail Checker

Audit Trail Checker for Hermes Agent: apply a analyze workflow to audit trail work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_audit_trail_checker` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_audit_trail_checker",
  "arguments": {
    "counts": {
      "audit_trail_risk_identified": 40,
      "audit_trail_approval_required": 25,
      "audit_trail_least_privilege": 10,
      "audit_trail_reversibility": 75
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
