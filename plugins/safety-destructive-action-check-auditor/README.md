# Destructive Action Check Auditor

Destructive Action Check Auditor for Hermes Agent: apply a template workflow to destructive action check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_destructive_action_check_auditor` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_destructive_action_check_auditor",
  "arguments": {
    "facts": {
      "destructive_action_check_risk_identified": "Sample supplied fact",
      "destructive_action_check_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
