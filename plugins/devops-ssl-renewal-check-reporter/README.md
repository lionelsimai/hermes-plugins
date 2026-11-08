# Ssl Renewal Check Reporter

Ssl Renewal Check Reporter for Hermes Agent: apply a checklist workflow to ssl renewal check work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_ssl_renewal_check_reporter` (kind: checklist)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_ssl_renewal_check_reporter",
  "arguments": {
    "completed": [
      "ssl renewal check risk noted",
      "ssl renewal check rollback step"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
