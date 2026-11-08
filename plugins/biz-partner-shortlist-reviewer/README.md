# Partner Shortlist Reviewer

Partner Shortlist Reviewer for Hermes Agent: apply a score workflow to partner shortlist work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_partner_shortlist_reviewer` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_partner_shortlist_reviewer",
  "arguments": {
    "metrics": {
      "partner_shortlist_facts_supplied_only": 80,
      "partner_shortlist_audience_fit": 65,
      "partner_shortlist_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
