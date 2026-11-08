# Wiki Outline Reviewer

Wiki Outline Reviewer for Hermes Agent: apply a checklist workflow to wiki outline work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_wiki_outline_reviewer` (kind: checklist)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_wiki_outline_reviewer",
  "arguments": {
    "completed": [
      "wiki outline source fidelity",
      "wiki outline retrieval relevance"
    ]
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
