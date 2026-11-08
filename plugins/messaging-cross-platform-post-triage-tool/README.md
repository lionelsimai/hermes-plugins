# Cross Platform Post Triage Tool

Cross Platform Post Triage Tool for Hermes Agent: apply a score workflow to cross platform post work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_cross_platform_post_triage_tool` (kind: score)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_cross_platform_post_triage_tool",
  "arguments": {
    "metrics": {
      "cross_platform_post_audience_fit": 80,
      "cross_platform_post_tone_fit": 65,
      "cross_platform_post_length_fit": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
