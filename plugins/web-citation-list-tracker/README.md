# Citation List Tracker

Citation List Tracker for Hermes Agent: apply a score workflow to citation list work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_citation_list_tracker` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_citation_list_tracker",
  "arguments": {
    "metrics": {
      "citation_list_source_quality": 80,
      "citation_list_recency": 65,
      "citation_list_corroboration": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
