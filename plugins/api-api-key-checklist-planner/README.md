# Api Key Checklist Planner

Api Key Checklist Planner for Hermes Agent: apply a audit workflow to api key checklist work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_api_key_checklist_planner` (kind: audit)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_api_key_checklist_planner",
  "arguments": {
    "text": "This sample covers api key checklist contract fit and api key checklist auth handled safely in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
