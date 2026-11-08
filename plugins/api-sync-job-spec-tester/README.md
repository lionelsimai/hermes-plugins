# Sync Job Spec Tester

Sync Job Spec Tester for Hermes Agent: apply a template workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_sync_job_spec_tester` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_sync_job_spec_tester",
  "arguments": {
    "facts": {
      "sync_job_spec_contract_fit": "Sample supplied fact",
      "sync_job_spec_auth_handled_safely": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
