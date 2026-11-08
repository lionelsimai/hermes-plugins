# Incident Notes Auditor

Incident Notes Auditor for Hermes Agent: apply a analyze workflow to incident notes work — covers risk noted, rollback step and window fit, using supplied facts only.

- Category: DevOps & Infra
- Tool: `devops_incident_notes_auditor` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "devops_incident_notes_auditor",
  "arguments": {
    "counts": {
      "incident_notes_risk_noted": 40,
      "incident_notes_rollback_step": 25,
      "incident_notes_verification": 10,
      "incident_notes_owner_named": 75
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
