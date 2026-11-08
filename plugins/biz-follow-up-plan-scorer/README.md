# Follow Up Plan Scorer

Follow Up Plan Scorer for Hermes Agent: apply a template workflow to follow up plan work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_follow_up_plan_scorer` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_follow_up_plan_scorer",
  "arguments": {
    "facts": {
      "follow_up_plan_facts_supplied_only": "Sample supplied fact",
      "follow_up_plan_audience_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
