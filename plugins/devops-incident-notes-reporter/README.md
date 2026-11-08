# Incident Notes Reporter

Incident Notes Reporter for Hermes Agent: apply a audit workflow to incident notes work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_incident_notes_reporter` (kind: audit)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_incident_notes_reporter",
  "arguments": {
    "text": "This sample covers incident notes risk noted and incident notes rollback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
