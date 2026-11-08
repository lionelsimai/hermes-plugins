# Citation Check Reviewer

Citation Check Reviewer for Hermes Agent: apply a classify workflow to citation check work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_citation_check_reviewer` (kind: classify)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_citation_check_reviewer",
  "arguments": {
    "text": "Please review: this concerns citation check source fidelity and citation check citation coverage."
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
