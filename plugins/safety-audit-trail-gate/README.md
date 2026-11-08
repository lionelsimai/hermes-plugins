# Audit Trail Gate

Audit Trail Gate for Hermes Agent: apply a score workflow to audit trail work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_audit_trail_gate` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_audit_trail_gate",
  "arguments": {
    "metrics": {
      "audit_trail_risk_identified": 80,
      "audit_trail_approval_required": 65,
      "audit_trail_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
