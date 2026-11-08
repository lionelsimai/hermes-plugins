# Oauth Flow Check Planner

Oauth Flow Check Planner for Hermes Agent: apply a classify workflow to oauth flow check work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_oauth_flow_check_planner` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_oauth_flow_check_planner",
  "arguments": {
    "text": "Please review: this concerns oauth flow check contract fit and oauth flow check error cases covered."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
