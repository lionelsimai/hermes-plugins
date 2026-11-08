# Rate Limit Review Auditor

Rate Limit Review Auditor for Hermes Agent: apply a checklist workflow to rate limit review work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_rate_limit_review_auditor` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_rate_limit_review_auditor",
  "arguments": {
    "completed": [
      "rate limit review contract fit",
      "rate limit review auth handled safely"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
