# Cross Platform Post Checker

Cross Platform Post Checker for Hermes Agent: apply a template workflow to cross platform post work — covers audience fit, tone fit and platform fit, using supplied facts only.

- Category: Messaging & Gateway
- Tool: `messaging_cross_platform_post_checker` (kind: template)
- Suggested Hermes toolset: `messaging`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "messaging_cross_platform_post_checker",
  "arguments": {
    "facts": {
      "cross_platform_post_audience_fit": "Sample supplied fact",
      "cross_platform_post_tone_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
