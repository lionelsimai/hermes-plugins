# Registry Entry Auditor

Registry Entry Auditor for Hermes Agent: apply a template workflow to registry entry work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_registry_entry_auditor` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_registry_entry_auditor",
  "arguments": {
    "facts": {
      "registry_entry_schema_validity": "Sample supplied fact",
      "registry_entry_description_clarity": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
