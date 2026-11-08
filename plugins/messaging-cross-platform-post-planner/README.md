# Cross Platform Post Planner

Cross Platform Post Planner for Hermes Agent: apply a analyze workflow to cross platform post work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_cross_platform_post_planner` (kind: analyze)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_cross_platform_post_planner",
  "arguments": {
    "counts": {
      "cross_platform_post_audience_fit": 40,
      "cross_platform_post_tone_fit": 25,
      "cross_platform_post_length_fit": 10,
      "cross_platform_post_approval_gate": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
