# Sponsor Brief Planner

Sponsor Brief Planner for Hermes Agent: apply a classify workflow to sponsor brief work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_sponsor_brief_planner` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_sponsor_brief_planner",
  "arguments": {
    "text": "Please review: this concerns sponsor brief facts supplied only and sponsor brief approval gate."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
