# External Send Gate Planner

External Send Gate Planner for Hermes Agent: apply a template workflow to external send gate work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_external_send_gate_planner` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_external_send_gate_planner",
  "arguments": {
    "facts": {
      "external_send_gate_risk_identified": "Sample supplied fact",
      "external_send_gate_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
