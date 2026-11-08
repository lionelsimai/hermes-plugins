# Research Brief Summarizer

Research Brief Summarizer for Hermes Agent: apply a classify workflow to research brief work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_research_brief_summarizer` (kind: classify)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_research_brief_summarizer",
  "arguments": {
    "text": "Please review: this concerns research brief source quality and research brief corroboration."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
