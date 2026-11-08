# Mcp Security Review Checker

Mcp Security Review Checker for Hermes Agent: apply a template workflow to mcp security review work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_mcp_security_review_checker` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_mcp_security_review_checker",
  "arguments": {
    "facts": {
      "mcp_security_review_schema_validity": "Sample supplied fact",
      "mcp_security_review_description_clarity": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
