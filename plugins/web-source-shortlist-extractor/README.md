# Source Shortlist Extractor

Source Shortlist Extractor for Hermes Agent: apply a template workflow to source shortlist work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_source_shortlist_extractor` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_source_shortlist_extractor",
  "arguments": {
    "facts": {
      "source_shortlist_source_quality": "Sample supplied fact",
      "source_shortlist_recency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
