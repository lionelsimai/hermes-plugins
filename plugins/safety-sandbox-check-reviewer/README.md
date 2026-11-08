# Sandbox Check Reviewer

Sandbox Check Reviewer for Hermes Agent: apply a audit workflow to sandbox check work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_sandbox_check_reviewer` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_sandbox_check_reviewer",
  "arguments": {
    "text": "This sample covers sandbox check risk identified and sandbox check approval required in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
