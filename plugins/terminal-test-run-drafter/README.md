# Test Run Drafter

Test Run Drafter for Hermes Agent: apply a score workflow to test run work — covers command safety, expected output and verification, using supplied facts only.

- Category: Terminal & Code Execution
- Tool: `terminal_test_run_drafter` (kind: score)
- Suggested Hermes toolset: `terminal`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "terminal_test_run_drafter",
  "arguments": {
    "metrics": {
      "test_run_command_safety": 80,
      "test_run_expected_output": 65,
      "test_run_timeout_set": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
