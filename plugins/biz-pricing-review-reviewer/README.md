# Pricing Review Reviewer

Pricing Review Reviewer for Hermes Agent: apply a analyze workflow to pricing review work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_pricing_review_reviewer` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_pricing_review_reviewer",
  "arguments": {
    "counts": {
      "pricing_review_facts_supplied_only": 40,
      "pricing_review_audience_fit": 25,
      "pricing_review_approval_gate": 10,
      "pricing_review_next_step_clarity": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
