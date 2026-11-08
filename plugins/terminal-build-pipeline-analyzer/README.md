# Build Pipeline Analyzer

Build Pipeline Analyzer for Hermes Agent: apply a analyze workflow to build pipeline work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_build_pipeline_analyzer` (kind: analyze)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_build_pipeline_analyzer",
  "arguments": {
    "counts": {
      "build_pipeline_command_safety": 40,
      "build_pipeline_expected_output": 25,
      "build_pipeline_timeout_set": 10,
      "build_pipeline_rollback_step": 75
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
