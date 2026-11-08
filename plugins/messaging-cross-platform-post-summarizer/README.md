# Cross Platform Post Summarizer

Cross Platform Post Summarizer for Hermes Agent: apply a checklist workflow to cross platform post work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_cross_platform_post_summarizer` (kind: checklist)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_cross_platform_post_summarizer",
  "arguments": {
    "completed": [
      "cross platform post audience fit",
      "cross platform post tone fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
