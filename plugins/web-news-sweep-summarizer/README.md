# News Sweep Summarizer

News Sweep Summarizer for Hermes Agent: apply a score workflow to news sweep work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_news_sweep_summarizer` (kind: score)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_news_sweep_summarizer",
  "arguments": {
    "metrics": {
      "news_sweep_source_quality": 80,
      "news_sweep_recency": 65,
      "news_sweep_corroboration": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
