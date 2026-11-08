# Registry Entry Drafter

Registry Entry Drafter for Hermes Agent: apply a checklist workflow to registry entry work — covers schema validity, description clarity and error behaviour, using supplied facts only.

- Category: MCP Tooling
- Tool: `mcp_registry_entry_drafter` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "mcp_registry_entry_drafter",
  "arguments": {
    "completed": [
      "registry entry schema validity",
      "registry entry description clarity"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
