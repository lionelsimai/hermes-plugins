# Glossary Build Checker

Glossary Build Checker for Hermes Agent: apply a template workflow to glossary build work — covers source fidelity, retrieval relevance and gap honesty, using supplied facts only.

- Category: Knowledge & RAG
- Tool: `rag_glossary_build_checker` (kind: template)
- Suggested Hermes toolset: `memory`
- Formats: `plugin.json` (collection manifest) + `plugin.yaml`/`__init__.py` (verified Hermes plugin format) + `SKILL.md` (Hermes/agentskills.io skill)

## Example call

```json
{
  "tool": "rag_glossary_build_checker",
  "arguments": {
    "facts": {
      "glossary_build_source_fidelity": "Sample supplied fact",
      "glossary_build_retrieval_relevance": "Second supplied fact"
    }
  }
}
```

## Guardrails

- No fabrication: supplied facts only; missing facts are reported, never invented.
- Draft-only for generative output; human approval required before any use or send.
- No auto-send. No credential handling.
