# Partner Shortlist Scorer

Partner Shortlist Scorer for Hermes Agent: apply a checklist workflow to partner shortlist work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_partner_shortlist_scorer` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_partner_shortlist_scorer",
  "arguments": {
    "completed": [
      "partner shortlist facts supplied only",
      "partner shortlist audience fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
