# Audit Trail Reviewer

Audit Trail Reviewer for Hermes Agent: apply a checklist workflow to audit trail work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_audit_trail_reviewer` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_audit_trail_reviewer",
  "arguments": {
    "completed": [
      "audit trail risk identified",
      "audit trail approval required"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
