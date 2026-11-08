# External Send Gate Auditor

External Send Gate Auditor for Hermes Agent: apply a score workflow to external send gate work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_external_send_gate_auditor` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_external_send_gate_auditor",
  "arguments": {
    "metrics": {
      "external_send_gate_risk_identified": 80,
      "external_send_gate_approval_required": 65,
      "external_send_gate_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
