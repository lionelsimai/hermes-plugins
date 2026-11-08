# Destructive Action Check Gate

Destructive Action Check Gate for Hermes Agent: apply a score workflow to destructive action check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_destructive_action_check_gate` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_destructive_action_check_gate",
  "arguments": {
    "metrics": {
      "destructive_action_check_risk_identified": 80,
      "destructive_action_check_approval_required": 65,
      "destructive_action_check_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
