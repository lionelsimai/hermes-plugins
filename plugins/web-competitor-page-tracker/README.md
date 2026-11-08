# Competitor Page Tracker

Competitor Page Tracker for Hermes Agent: apply a classify workflow to competitor page work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_competitor_page_tracker` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_competitor_page_tracker",
  "arguments": {
    "text": "Please review: this concerns competitor page source quality and competitor page corroboration."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
