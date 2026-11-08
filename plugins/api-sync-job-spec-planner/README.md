# Sync Job Spec Planner

Sync Job Spec Planner for Hermes Agent: apply a analyze workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_sync_job_spec_planner` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_sync_job_spec_planner",
  "arguments": {
    "counts": {
      "sync_job_spec_contract_fit": 40,
      "sync_job_spec_auth_handled_safely": 25,
      "sync_job_spec_error_cases_covered": 10,
      "sync_job_spec_rate_limits_respected": 75
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
