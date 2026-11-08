# Sandbox Check Planner

Sandbox Check Planner for Hermes Agent: apply a score workflow to sandbox check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_sandbox_check_planner` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_sandbox_check_planner",
  "arguments": {
    "metrics": {
      "sandbox_check_risk_identified": 80,
      "sandbox_check_approval_required": 65,
      "sandbox_check_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
