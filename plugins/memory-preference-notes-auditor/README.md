# Preference Notes Auditor

Preference Notes Auditor for Hermes Agent: apply a checklist workflow to preference notes work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_preference_notes_auditor` (kind: checklist)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_preference_notes_auditor",
  "arguments": {
    "completed": [
      "preference notes fact accuracy",
      "preference notes size budget fit"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
