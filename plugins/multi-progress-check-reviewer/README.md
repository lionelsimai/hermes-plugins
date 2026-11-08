# Progress Check Reviewer

Progress Check Reviewer for Hermes Agent: apply a score workflow to progress check work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_progress_check_reviewer` (kind: score)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_progress_check_reviewer",
  "arguments": {
    "metrics": {
      "progress_check_scope_clarity": 80,
      "progress_check_independence_of_subtasks": 65,
      "progress_check_merge_criteria": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
