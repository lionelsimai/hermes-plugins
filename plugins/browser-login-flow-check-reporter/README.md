# Login Flow Check Reporter

Login Flow Check Reporter for Hermes Agent: apply a audit workflow to login flow check work — covers step clarity, fallback step and completion proof, using supplied facts only.

- Category: Browser Automation
- Tool: `browser_login_flow_check_reporter` (kind: audit)
- Suggested Hermes toolset: `browser`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "browser_login_flow_check_reporter",
  "arguments": {
    "text": "This sample covers login flow check step clarity and login flow check fallback step in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
