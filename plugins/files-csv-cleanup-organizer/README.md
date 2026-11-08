# Csv Cleanup Organizer

Csv Cleanup Organizer for Hermes Agent: apply a score workflow to csv cleanup work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_csv_cleanup_organizer` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_csv_cleanup_organizer",
  "arguments": {
    "metrics": {
      "csv_cleanup_format_fit": 80,
      "csv_cleanup_completeness": 65,
      "csv_cleanup_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
