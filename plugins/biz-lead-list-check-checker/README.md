# Lead List Check Checker

Lead List Check Checker for Hermes Agent: apply a score workflow to lead list check work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_lead_list_check_checker` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_lead_list_check_checker",
  "arguments": {
    "metrics": {
      "lead_list_check_facts_supplied_only": 80,
      "lead_list_check_audience_fit": 65,
      "lead_list_check_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
