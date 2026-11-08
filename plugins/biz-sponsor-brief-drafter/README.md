# Sponsor Brief Drafter

Sponsor Brief Drafter for Hermes Agent: apply a analyze workflow to sponsor brief work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_sponsor_brief_drafter` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_sponsor_brief_drafter",
  "arguments": {
    "counts": {
      "sponsor_brief_facts_supplied_only": 40,
      "sponsor_brief_audience_fit": 25,
      "sponsor_brief_approval_gate": 10,
      "sponsor_brief_next_step_clarity": 75
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
