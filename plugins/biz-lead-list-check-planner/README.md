# Lead List Check Planner

Lead List Check Planner for Hermes Agent: apply a template workflow to lead list check work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_lead_list_check_planner` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_lead_list_check_planner",
  "arguments": {
    "facts": {
      "lead_list_check_facts_supplied_only": "Sample supplied fact",
      "lead_list_check_audience_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
