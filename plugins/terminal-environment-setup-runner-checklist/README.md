# Environment Setup Runner Checklist

Environment Setup Runner Checklist for Hermes Agent: apply a classify workflow to environment setup work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_environment_setup_runner_checklist` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_environment_setup_runner_checklist",
  "arguments": {
    "text": "Please review: this concerns environment setup command safety and environment setup timeout set."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
