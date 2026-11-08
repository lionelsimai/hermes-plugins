# Error Handling Plan Checker

Error Handling Plan Checker for Hermes Agent: apply a checklist workflow to error handling plan work — covers contract fit, auth handled safely and verification call, using supplied facts only.

- Category: APIs & Integrations
- Tool: `api_error_handling_plan_checker` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "api_error_handling_plan_checker",
  "arguments": {
    "completed": [
      "error handling plan contract fit",
      "error handling plan auth handled safely"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
