# Transport Check Auditor

Transport Check Auditor for Hermes Agent: apply a audit workflow to transport check work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_transport_check_auditor` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_transport_check_auditor",
  "arguments": {
    "text": "This sample covers transport check schema validity and transport check description clarity in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
