# Script Draft Drafter

Script Draft Drafter for Hermes Agent: apply a classify workflow to script draft work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_script_draft_drafter` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_script_draft_drafter",
  "arguments": {
    "text": "Please review: this concerns script draft command safety and script draft timeout set."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
