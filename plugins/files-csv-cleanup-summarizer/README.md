# Csv Cleanup Summarizer

Csv Cleanup Summarizer for Hermes Agent: apply a checklist workflow to csv cleanup work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_csv_cleanup_summarizer` (kind: checklist)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_csv_cleanup_summarizer",
  "arguments": {
    "completed": [
      "csv cleanup format fit",
      "csv cleanup completeness"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
