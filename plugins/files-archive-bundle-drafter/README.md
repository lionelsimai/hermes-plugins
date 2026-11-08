# Archive Bundle Drafter

Archive Bundle Drafter for Hermes Agent: apply a analyze workflow to archive bundle work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_archive_bundle_drafter` (kind: analyze)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_archive_bundle_drafter",
  "arguments": {
    "counts": {
      "archive_bundle_format_fit": 40,
      "archive_bundle_completeness": 25,
      "archive_bundle_naming_consistency": 10,
      "archive_bundle_source_fidelity": 75
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
