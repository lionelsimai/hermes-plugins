# Build Pipeline Auditor

Build Pipeline Auditor for Hermes Agent: apply a classify workflow to build pipeline work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_build_pipeline_auditor` (kind: classify)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_build_pipeline_auditor",
  "arguments": {
    "text": "Please review: this concerns build pipeline command safety and build pipeline timeout set."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
