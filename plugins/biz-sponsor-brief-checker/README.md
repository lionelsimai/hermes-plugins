# Sponsor Brief Checker

Sponsor Brief Checker for Hermes Agent: apply a template workflow to sponsor brief work — covers facts supplied only, audience fit and evidence noted, using supplied facts only.

- Category: Business & GTM Ops
- Tool: `biz_sponsor_brief_checker` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "biz_sponsor_brief_checker",
  "arguments": {
    "facts": {
      "sponsor_brief_facts_supplied_only": "Sample supplied fact",
      "sponsor_brief_audience_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
