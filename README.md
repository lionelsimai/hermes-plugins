# Lionel Hermes Plugins — 1,000 plugins for Hermes Agent

1,000 plugins for **Hermes Agent**, the self-improving open-source AI
agent built by [Nous Research](https://github.com/NousResearch/hermes-agent)
(MIT). Extracted from the best of the Hermes ecosystem — the official
repo, official docs, bundled-skills taxonomy and the leading community
collections — then rebuilt as one consistent, tested, guardrailed
suite. Full provenance: [SOURCES.md](SOURCES.md).

Built and maintained by [Lionel Sim](https://sg.linkedin.com/in/lionelshen)
(The AI Capitol), founder of the Hermes AI Agent Singapore Community.
MIT licensed — free to use, fork and build on.

> **Not a Nous Research product.** Hermes Agent is MIT-licensed work of
> Nous Research. This collection is Lionel Sim's original work that
> plugs into it; it is not affiliated with or endorsed by Nous Research.

## How each plugin works in Hermes (verified formats)

Every plugin folder ships **three** formats, so nothing here is a
paper claim:

| File | What it is |
|---|---|
| `plugin.yaml` + `__init__.py` | The **verified Hermes plugin format** (official docs): drop the folder into `~/.hermes/plugins/`, enable it, and `register(ctx)` wires its tool via `ctx.register_tool()` |
| `SKILL.md` | A **Hermes skill** (agentskills.io format): copy into `~/.hermes/skills/` and Hermes loads it on demand — it also becomes a slash command |
| `plugin.json` | This collection's standard manifest (same as Lionel's other suites) — drives the shared MCP/REST servers below. Hermes itself has no plugin.json format; we say so plainly |

## Use it three more ways

- **MCP** — `python3 mcp_server.py` exposes all 1,000 tools over MCP
  stdio for Claude Code, Codex, Cursor or any MCP client (see
  `.mcp.json` / `.claude-plugin/plugin.json`).
- **REST** — `python3 rest_server.py --port 8787`, then
  `POST /tools/{tool_name}` (spec: `openapi.json`, manifest:
  `ai-plugin.json`, health: `GET /health`, catalogue: `GET /catalog`).
- **Direct** — `from core.registry import get_registry` and
  `get_registry().call(tool_name, args)`.

## The 20 categories (1,000 plugins)

- **Core Agent Ops & Skill Authoring** — 50 plugins
- **Memory & Context** — 50 plugins
- **Terminal & Code Execution** — 50 plugins
- **File & Document Work** — 50 plugins
- **Web Research & Browsing** — 50 plugins
- **Browser Automation** — 50 plugins
- **Messaging & Gateway** — 50 plugins
- **Scheduling & Cron** — 50 plugins
- **Email & Calendar** — 50 plugins
- **Data & Spreadsheets** — 50 plugins
- **APIs & Integrations** — 50 plugins
- **MCP Tooling** — 50 plugins
- **Multi-Agent & Delegation** — 50 plugins
- **Media (Image Audio Video)** — 50 plugins
- **Knowledge & RAG** — 50 plugins
- **Personal Productivity** — 50 plugins
- **Business & GTM Ops** — 50 plugins
- **Community Ops** — 50 plugins
- **DevOps & Infra** — 50 plugins
- **Safety, Approvals & Guardrails** — 50 plugins

Full list: [CATALOG.md](CATALOG.md) / [catalog.json](catalog.json).

## Guardrails (in code, not just docs)

Every tool result carries a `guardrails` block: supplied facts only,
no fabrication, drafts stay drafts, **human approval required**,
**no auto-send**, and **no credential handling** — no plugin in this
collection asks for, stores or uses tokens, passwords or API keys.
Sample data is fictional.

## Test

```bash
python3 tests/test_suite.py
```

Verifies: exactly 1,000 plugins, unique slugs and tool names, every
folder complete (plugin.json, plugin.yaml, __init__.py, SKILL.md,
README, handler), all 1,000 tools callable with their sample inputs,
Hermes `register(ctx)` wiring on a sampled set, MCP tools/list = 1,000,
and REST /health + a live tool call.

## Licence

MIT — see [LICENSE](LICENSE). Hermes Agent itself is MIT-licensed by
Nous Research; this collection is original work by Lionel Sim.
