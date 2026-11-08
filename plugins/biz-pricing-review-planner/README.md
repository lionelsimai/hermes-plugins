# Pricing Review Planner

Pricing Review Planner for Hermes Agent: apply a template workflow to pricing review work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_pricing_review_planner` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_pricing_review_planner",
  "arguments": {
    "facts": {
      "pricing_review_facts_supplied_only": "Sample supplied fact",
      "pricing_review_audience_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
