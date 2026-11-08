# Secret Handling Check Reviewer

Secret Handling Check Reviewer for Hermes Agent: apply a template workflow to secret handling check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_secret_handling_check_reviewer` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_secret_handling_check_reviewer",
  "arguments": {
    "facts": {
      "secret_handling_check_risk_identified": "Sample supplied fact",
      "secret_handling_check_approval_required": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
