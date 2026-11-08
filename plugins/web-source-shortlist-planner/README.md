# Source Shortlist Planner

Source Shortlist Planner for Hermes Agent: apply a checklist workflow to source shortlist work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_source_shortlist_planner` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_source_shortlist_planner",
  "arguments": {
    "completed": [
      "source shortlist source quality",
      "source shortlist recency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
