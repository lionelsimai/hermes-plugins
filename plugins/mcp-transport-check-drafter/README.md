# Transport Check Drafter

Transport Check Drafter for Hermes Agent: apply a classify workflow to transport check work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_transport_check_drafter` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_transport_check_drafter",
  "arguments": {
    "text": "Please review: this concerns transport check schema validity and transport check least privilege."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
