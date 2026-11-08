# Sync Job Spec Auditor

Sync Job Spec Auditor for Hermes Agent: apply a audit workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_sync_job_spec_auditor` (kind: audit)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_sync_job_spec_auditor",
  "arguments": {
    "text": "This sample covers sync job spec contract fit and sync job spec auth handled safely in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
