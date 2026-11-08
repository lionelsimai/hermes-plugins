# Mcp Server Review Auditor

Mcp Server Review Auditor for Hermes Agent: apply a audit workflow to mcp server review work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_server_review_auditor` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_server_review_auditor",
  "arguments": {
    "text": "This sample covers mcp server review schema validity and mcp server review description clarity in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
