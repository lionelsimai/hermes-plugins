# Outreach Draft Reviewer

Outreach Draft Reviewer for Hermes Agent: apply a score workflow to outreach draft work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_outreach_draft_reviewer` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_outreach_draft_reviewer",
  "arguments": {
    "metrics": {
      "outreach_draft_facts_supplied_only": 80,
      "outreach_draft_audience_fit": 65,
      "outreach_draft_approval_gate": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
