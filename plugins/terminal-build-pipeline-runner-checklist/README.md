# Build Pipeline Runner Checklist

Build Pipeline Runner Checklist for Hermes Agent: apply a template workflow to build pipeline work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_build_pipeline_runner_checklist` (kind: template)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_build_pipeline_runner_checklist",
  "arguments": {
    "facts": {
      "build_pipeline_command_safety": "Sample supplied fact",
      "build_pipeline_expected_output": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
