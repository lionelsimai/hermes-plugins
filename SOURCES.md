# Sources — extracted from the best of the Hermes ecosystem

This collection was designed from primary sources first (Step 1 of the
build), not invented from thin air. Every format claim in this repo
traces to a source below. Research date: 9 Nov 2026.

## Primary sources (Nous Research / official)

1. **Hermes Agent — official repository**
   https://github.com/NousResearch/hermes-agent
   - Extracted: what Hermes is (self-improving agent, built-in learning
     loop, MIT licence); root layout showing first-class `skills/`,
     `optional-skills/`, `plugins/`, `plugin-catalog/`, `cron/`,
     `gateway/`, `providers/`, `tools/` and `toolsets.py`; terminal
     backends (local, Docker, SSH, Modal, Daytona, Vercel Sandbox);
     gateway platforms (Telegram, Discord, Slack, WhatsApp, Signal,
     CLI); cron scheduler with delivery to any platform; subagent
     delegation; agentskills.io compatibility.

2. **Plugins — official docs**
   https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins
   - Extracted (VERIFIED plugin format): a Hermes plugin is a directory
     in `~/.hermes/plugins/` with a **`plugin.yaml`** manifest and an
     **`__init__.py`** exposing `register(ctx)`; tools are wired with
     `ctx.register_tool(name=..., toolset=..., schema=..., handler=...)`;
     the model-facing description belongs in `schema["description"]`;
     plugins are enabled via `hermes plugins enable <name>` /
     `plugins.enabled` in `~/.hermes/config.yaml`; project-local
     plugins are not loaded by the gateway. Platform plugins use
     `kind: platform` + `ctx.register_platform()` and may declare
     `provides_tools`. → Every plugin in this repo ships a real
     `plugin.yaml` + `__init__.py` in exactly this format.

3. **Working with Skills — official docs**
   https://hermes-agent.nousresearch.com/docs/guides/work-with-skills
   - Extracted: skills are on-demand `SKILL.md` documents using
     progressive disclosure (`skills_list()` → `skill_view(name)`);
     installed skills live in `~/.hermes/skills/` (optionally in
     category subdirectories) and become slash commands; install via
     `hermes skills install <id>`; bundled vs optional (Hub) skills.
     → Every plugin here also ships a `SKILL.md` in this format.

4. **Bundled Skills Catalog — official docs**
   https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
   - Extracted (taxonomy + naming conventions): official bundled-skill
     categories — apple, autonomous-ai-agents, creative, devops, email,
     media, note-taking, productivity, research, social-media,
     software-development, web — and real bundled skills used as design
     anchors (e.g. `arxiv`, `obsidian`, `google-workspace`,
     `email-inbox-triage`, `github`, `codebase-inspection`, `xurl`,
     `claude-code`, `codex`, `computer-use`, `hermes-agent`).

5. **Skills system reference (via official-docs mirrors and the
   hermes-agent SKILL.md in community repos)**
   https://github.com/NousResearch/hermes-agent (skills docs)
   - Extracted: `SKILL.md` frontmatter fields actually used by Hermes —
     `name`, `description`, `version`, `platforms`, and
     `metadata.hermes.tags` / `metadata.hermes.category`; memory model
     (`~/.hermes/memories/MEMORY.md` ≈2,200 chars, `USER.md` ≈1,375
     chars, frozen snapshot at session start; FTS5 session search over
     `~/.hermes/state.db`); toolset names (`web`, `browser`,
     `terminal`, `file`, `skills`, `memory`, `messaging`, delegation,
     cron) enabled per platform via `hermes tools`.

## Community sources (best-of survey)

6. **Awesome Hermes Agent — Hermes Atlas (0xNyk)**
   https://hermesatlas.com/projects/0xNyk/awesome-hermes-agent
   - Extracted: the community map — community skills, plugins, memory
     providers, skill registries/discovery; notable patterns surveyed:
     hermes-plugins by 42-evey (Discord/WhatsApp bridges, goal
     management, inter-agent bridge, cost control), hermes-skill-factory
     (meta-skill that generates skills from workflows), oh-my-hermes
     (multi-agent orchestration), hermes-spotify-skill (headless media
     control). These informed the Messaging, Multi-Agent,
     Self-Improvement (folded into Core Agent Ops & Skill Authoring)
     and Media categories. No code was copied — taxonomy and patterns
     only; all plugins here are original.

7. **Community Hermes reference compilations**
   - https://github.com/mode-ai1/mode/blob/HEAD/hermes-agent-docs.md —
     setup notes compiled from the official docs (SOUL.md as primary
     identity, toolset allowlists, provider breadth).
   - https://github.com/yossitv/personalize-skill-factory/blob/HEAD/docs/references/hermes-agent-nousresearch-com.md —
     docs digest (tools table: `web_search`/`web_extract`, `terminal`,
     `skills_list`/`skill_view`/`skill_manage`, `memory`; gateway
     commands; memory limits).
   - https://hermeswatcher.com/hermes-agent — independent overview
     confirming gateway reach (25+ platforms, deny-by-default
     allowlists/DM pairing), `delegate_task`, and the Tool Gateway.

## What was NOT claimed

- There is no verified official "plugin.json" format for Hermes. The
  `plugin.json` in each folder is **this collection's standard
  manifest** (the same format as Lionel Sim's other plugin suites),
  kept alongside — not instead of — the verified Hermes formats
  (`plugin.yaml` + `__init__.py`, and `SKILL.md`).
- No Nous Research code, skills or text were copied. Names of official
  bundled skills above are cited for provenance only.
