# Page Extraction Tracker

Page Extraction Tracker for Hermes Agent: apply a template workflow to page extraction work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_page_extraction_tracker` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_page_extraction_tracker",
  "arguments": {
    "facts": {
      "page_extraction_source_quality": "Sample supplied fact",
      "page_extraction_recency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
