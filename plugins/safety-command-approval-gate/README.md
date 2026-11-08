# Command Approval Gate

Command Approval Gate for Hermes Agent: apply a analyze workflow to command approval work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_command_approval_gate` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_command_approval_gate",
  "arguments": {
    "counts": {
      "command_approval_risk_identified": 40,
      "command_approval_approval_required": 25,
      "command_approval_least_privilege": 10,
      "command_approval_reversibility": 75
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
