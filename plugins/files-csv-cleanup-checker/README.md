# Csv Cleanup Checker

Csv Cleanup Checker for Hermes Agent: apply a template workflow to csv cleanup work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_csv_cleanup_checker` (kind: template)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_csv_cleanup_checker",
  "arguments": {
    "facts": {
      "csv_cleanup_format_fit": "Sample supplied fact",
      "csv_cleanup_completeness": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
