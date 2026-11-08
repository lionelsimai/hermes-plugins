# Job Failure Review Auditor

Job Failure Review Auditor for Hermes Agent: apply a audit workflow to job failure review work — covers schedule clarity, delivery target and owner named, using supplied facts only.

- Category: Scheduling & Cron
- Tool: `cron_job_failure_review_auditor` (kind: audit)
- Suggested Hermes toolset: `cron`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "cron_job_failure_review_auditor",
  "arguments": {
    "text": "This sample covers job failure review schedule clarity and job failure review delivery target in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
