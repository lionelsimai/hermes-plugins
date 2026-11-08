# File Rename Plan Summarizer

File Rename Plan Summarizer for Hermes Agent: apply a score workflow to file rename plan work — covers format fit, completeness and output location, using supplied facts only.

- Category: File & Document Work
- Tool: `files_file_rename_plan_summarizer` (kind: score)
- Suggested Hermes toolset: `file`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "files_file_rename_plan_summarizer",
  "arguments": {
    "metrics": {
      "file_rename_plan_format_fit": 80,
      "file_rename_plan_completeness": 65,
      "file_rename_plan_naming_consistency": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
