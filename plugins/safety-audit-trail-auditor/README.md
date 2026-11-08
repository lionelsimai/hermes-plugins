# Audit Trail Auditor

Audit Trail Auditor for Hermes Agent: apply a template workflow to audit trail work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_audit_trail_auditor` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_audit_trail_auditor",
  "arguments": {
    "facts": {
      "audit_trail_risk_identified": "Sample supplied fact",
      "audit_trail_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
