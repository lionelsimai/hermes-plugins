# Source Shortlist Summarizer

Source Shortlist Summarizer for Hermes Agent: apply a classify workflow to source shortlist work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_source_shortlist_summarizer` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_source_shortlist_summarizer",
  "arguments": {
    "text": "Please review: this concerns source shortlist source quality and source shortlist corroboration."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
