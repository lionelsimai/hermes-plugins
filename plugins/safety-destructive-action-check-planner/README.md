# Destructive Action Check Planner

Destructive Action Check Planner for Hermes Agent: apply a classify workflow to destructive action check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_destructive_action_check_planner` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_destructive_action_check_planner",
  "arguments": {
    "text": "Please review: this concerns destructive action check risk identified and destructive action check least privilege."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
