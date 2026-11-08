# Proposal Outline Scorer

Proposal Outline Scorer for Hermes Agent: apply a analyze workflow to proposal outline work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_proposal_outline_scorer` (kind: analyze)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_proposal_outline_scorer",
  "arguments": {
    "counts": {
      "proposal_outline_facts_supplied_only": 40,
      "proposal_outline_audience_fit": 25,
      "proposal_outline_approval_gate": 10,
      "proposal_outline_next_step_clarity": 75
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
