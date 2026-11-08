# Preference Notes Summarizer

Preference Notes Summarizer for Hermes Agent: apply a template workflow to preference notes work — covers fact accuracy, size budget fit and source noted, using supplied facts only.

- Category: Memory & Context
- Tool: `memory_preference_notes_summarizer` (kind: template)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "memory_preference_notes_summarizer",
  "arguments": {
    "facts": {
      "preference_notes_fact_accuracy": "Sample supplied fact",
      "preference_notes_size_budget_fit": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
