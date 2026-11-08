# Sync Job Spec Mapper

Sync Job Spec Mapper for Hermes Agent: apply a classify workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_sync_job_spec_mapper` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_sync_job_spec_mapper",
  "arguments": {
    "text": "Please review: this concerns sync job spec contract fit and sync job spec error cases covered."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
