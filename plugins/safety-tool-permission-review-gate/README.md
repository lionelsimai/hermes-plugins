# Tool Permission Review Gate

Tool Permission Review Gate for Hermes Agent: apply a analyze workflow to tool permission review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_tool_permission_review_gate` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_tool_permission_review_gate",
  "arguments": {
    "counts": {
      "tool_permission_review_risk_identified": 40,
      "tool_permission_review_approval_required": 25,
      "tool_permission_review_least_privilege": 10,
      "tool_permission_review_reversibility": 75
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
