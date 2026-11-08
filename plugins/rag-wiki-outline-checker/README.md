# Wiki Outline Checker

Wiki Outline Checker for Hermes Agent: apply a score workflow to wiki outline work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_wiki_outline_checker` (kind: score)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_wiki_outline_checker",
  "arguments": {
    "metrics": {
      "wiki_outline_source_fidelity": 80,
      "wiki_outline_retrieval_relevance": 65,
      "wiki_outline_citation_coverage": 90
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
