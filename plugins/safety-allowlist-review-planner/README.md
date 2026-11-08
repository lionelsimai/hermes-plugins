# Allowlist Review Planner

Allowlist Review Planner for Hermes Agent: apply a analyze workflow to allowlist review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_allowlist_review_planner` (kind: analyze)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_allowlist_review_planner",
  "arguments": {
    "counts": {
      "allowlist_review_risk_identified": 40,
      "allowlist_review_approval_required": 25,
      "allowlist_review_least_privilege": 10,
      "allowlist_review_reversibility": 75
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
