# Follow Up Plan Planner

Follow Up Plan Planner for Hermes Agent: apply a score workflow to follow up plan work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_follow_up_plan_planner` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_follow_up_plan_planner",
  "arguments": {
    "metrics": {
      "follow_up_plan_facts_supplied_only": 80,
      "follow_up_plan_audience_fit": 65,
      "follow_up_plan_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
