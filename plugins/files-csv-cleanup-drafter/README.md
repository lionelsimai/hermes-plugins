# Csv Cleanup Drafter

Csv Cleanup Drafter for Hermes Agent: apply a analyze workflow to csv cleanup work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_csv_cleanup_drafter` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_csv_cleanup_drafter",
  "arguments": {
    "counts": {
      "csv_cleanup_format_fit": 40,
      "csv_cleanup_completeness": 25,
      "csv_cleanup_naming_consistency": 10,
      "csv_cleanup_source_fidelity": 75
    },
    "series": [
      3,
      5,
      4,
      8
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
