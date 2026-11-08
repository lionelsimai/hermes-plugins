# Page Extraction Verifier

Page Extraction Verifier for Hermes Agent: apply a score workflow to page extraction work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_page_extraction_verifier` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_page_extraction_verifier",
  "arguments": {
    "metrics": {
      "page_extraction_source_quality": 80,
      "page_extraction_recency": 65,
      "page_extraction_corroboration": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
