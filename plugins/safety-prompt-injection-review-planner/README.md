# Prompt Injection Review Planner

Prompt Injection Review Planner for Hermes Agent: apply a checklist workflow to prompt injection review work — covers risk identified, approval required and audit logged, using supplied facts only.

- Category: Safety, Approvals & Guardrails
- Tool: `safety_prompt_injection_review_planner` (kind: checklist)
- Suggested Hermes toolset: `skills`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "safety_prompt_injection_review_planner",
  "arguments": {
    "completed": [
      "prompt injection review risk identified",
      "prompt injection review approval required"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
