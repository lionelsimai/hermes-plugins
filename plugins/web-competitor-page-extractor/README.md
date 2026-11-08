# Competitor Page Extractor

Competitor Page Extractor for Hermes Agent: apply a checklist workflow to competitor page work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_competitor_page_extractor` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_competitor_page_extractor",
  "arguments": {
    "completed": [
      "competitor page source quality",
      "competitor page recency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
