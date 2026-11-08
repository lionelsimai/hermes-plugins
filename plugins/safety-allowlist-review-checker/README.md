# Allowlist Review Checker

Allowlist Review Checker for Hermes Agent: apply a template workflow to allowlist review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_allowlist_review_checker` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_allowlist_review_checker",
  "arguments": {
    "facts": {
      "allowlist_review_risk_identified": "Sample supplied fact",
      "allowlist_review_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
