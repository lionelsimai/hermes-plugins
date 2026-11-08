# Focus Block Tracker

Focus Block Tracker for Hermes Agent: apply a classify workflow to focus block work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_focus_block_tracker` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_focus_block_tracker",
  "arguments": {
    "text": "Please review: this concerns focus block priority clarity and focus block next action named."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
