# Review Delegation Reviewer

Review Delegation Reviewer for Hermes Agent: apply a classify workflow to review delegation work — covers scope clarity, independence of subtasks and verification step, using supplied facts only.

- Category: Multi-Agent & Delegation
- Tool: `multi_review_delegation_reviewer` (kind: classify)
- Suggested Hermes toolset: `delegation`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "multi_review_delegation_reviewer",
  "arguments": {
    "text": "Please review: this concerns review delegation scope clarity and review delegation merge criteria."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
