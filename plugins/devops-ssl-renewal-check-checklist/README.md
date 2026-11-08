# Ssl Renewal Check Checklist

Ssl Renewal Check Checklist for Hermes Agent: apply a audit workflow to ssl renewal check work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_ssl_renewal_check_checklist` (kind: audit)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_ssl_renewal_check_checklist",
  "arguments": {
    "text": "This sample covers ssl renewal check risk noted and ssl renewal check rollback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
