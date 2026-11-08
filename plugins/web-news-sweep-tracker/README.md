# News Sweep Tracker

News Sweep Tracker for Hermes Agent: apply a checklist workflow to news sweep work — covers source quality, recency and scope fit, using supplied facts only.

- Category: Web Research & Browsing
- Tool: `web_news_sweep_tracker` (kind: checklist)
- Suggested Hermes toolset: `web`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "web_news_sweep_tracker",
  "arguments": {
    "completed": [
      "news sweep source quality",
      "news sweep recency"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
