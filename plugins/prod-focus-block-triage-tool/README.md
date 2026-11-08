# Focus Block Triage Tool

Focus Block Triage Tool for Hermes Agent: apply a template workflow to focus block work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_focus_block_triage_tool` (kind: template)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_focus_block_triage_tool",
  "arguments": {
    "facts": {
      "focus_block_priority_clarity": "Sample supplied fact",
      "focus_block_time_realism": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
