# Proposal Outline Drafter

Proposal Outline Drafter for Hermes Agent: apply a score workflow to proposal outline work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_proposal_outline_drafter` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_proposal_outline_drafter",
  "arguments": {
    "metrics": {
      "proposal_outline_facts_supplied_only": 80,
      "proposal_outline_audience_fit": 65,
      "proposal_outline_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
