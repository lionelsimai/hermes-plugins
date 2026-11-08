# Login Flow Check Checker

Login Flow Check Checker for Hermes Agent: apply a template workflow to login flow check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_login_flow_check_checker` (kind: template)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_login_flow_check_checker",
  "arguments": {
    "facts": {
      "login_flow_check_step_clarity": "Sample supplied fact",
      "login_flow_check_fallback_step": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
