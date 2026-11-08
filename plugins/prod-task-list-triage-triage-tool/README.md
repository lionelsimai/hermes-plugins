# Task List Triage Triage Tool

Task List Triage Triage Tool for Hermes Agent: apply a audit workflow to task list triage work — covers priority clarity, time realism and owner named, using supplied facts only.

- Category: Personal Productivity
- Tool: `prod_task_list_triage_triage_tool` (kind: audit)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "prod_task_list_triage_triage_tool",
  "arguments": {
    "text": "This sample covers task list triage priority clarity and task list triage time realism in detail."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
