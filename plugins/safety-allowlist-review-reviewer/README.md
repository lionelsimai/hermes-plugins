# Allowlist Review Reviewer

Allowlist Review Reviewer for Hermes Agent: apply a score workflow to allowlist review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_allowlist_review_reviewer` (kind: score)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_allowlist_review_reviewer",
  "arguments": {
    "metrics": {
      "allowlist_review_risk_identified": 80,
      "allowlist_review_approval_required": 65,
      "allowlist_review_least_privilege": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
