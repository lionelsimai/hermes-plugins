# Competitor Page Verifier

Competitor Page Verifier for Hermes Agent: apply a template workflow to competitor page work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_competitor_page_verifier` (kind: template)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_competitor_page_verifier",
  "arguments": {
    "facts": {
      "competitor_page_source_quality": "Sample supplied fact",
      "competitor_page_recency": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
