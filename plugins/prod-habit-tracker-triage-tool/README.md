# Habit Tracker Triage Tool

Habit Tracker Triage Tool for Hermes Agent: apply a classify workflow to habit tracker work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_habit_tracker_triage_tool` (kind: classify)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_habit_tracker_triage_tool",
  "arguments": {
    "text": "Please review: this concerns habit tracker priority clarity and habit tracker next action named."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
