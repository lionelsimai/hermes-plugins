#!/usr/bin/env python3
"""Full suite: catalogue, folders (all 3 formats), Hermes register()
wiring, registry callability, MCP, REST. Stdlib only.
Run: python3 tests/test_suite.py"""
import importlib.util, json, os, random, subprocess, sys, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
fails = []; passed = 0
def check(name, cond, detail=""):
    global passed
    print(("PASS " if cond else "FAIL ") + name + (f" — {detail}" if detail and not cond else ""))
    if cond: passed += 1
    else: fails.append(name)

catalog = json.load(open(os.path.join(ROOT, "catalog.json")))
plugins = catalog["plugins"]
check("catalogue count = 1000", len(plugins) == 1000, str(len(plugins)))
check("catalogue count field = 1000", catalog["count"] == 1000)
slugs = [p["slug"] for p in plugins]; check("slugs unique", len(set(slugs)) == len(slugs))
tools = [p["tool"] for p in plugins]; check("tool names unique", len(set(tools)) == len(tools))
cats = {p["category"] for p in plugins}; check("20 categories", len(cats) == 20, str(len(cats)))

bad = []
for p in plugins:
    d = os.path.join(ROOT, "plugins", p["slug"])
    try:
        meta = json.load(open(os.path.join(d, "plugin.json")))
        assert meta["version"] == "1.0.0" and meta["license"] == "MIT" and meta["author"]["name"] == "Lionel Sim"
        assert meta["guardrails"]["no_auto_send"] and meta["guardrails"]["no_fabrication"] and meta["guardrails"]["no_credential_handling"]
        assert meta["tools"] and meta["tools"][0]["sample_input"] is not None
        rd = open(os.path.join(d, "README.md")).read(); assert "Guardrails" in rd and "Example call" in rd
        assert os.path.isfile(os.path.join(d, "handler.py"))
        sk = open(os.path.join(d, "SKILL.md")).read()
        assert sk.startswith("---") and f'name: {p["slug"]}' in sk and "description:" in sk
        y = open(os.path.join(d, "plugin.yaml")).read()
        assert f'name: {p["slug"]}' in y and p["tool"] in y and "version: 1.0.0" in y
        init = open(os.path.join(d, "__init__.py")).read()
        assert "def register(ctx)" in init and "ctx.register_tool" in init and p["tool"] in init
    except Exception as e:
        bad.append((p["slug"], str(e)))
        if len(bad) >= 3: break
check("all 1000 folders: plugin.json + plugin.yaml + __init__ + SKILL.md + README + handler", not bad, str(bad[:3]))

# Hermes register() smoke test on a deterministic sample of 30 plugins
class FakeCtx:
    def __init__(self): self.registered = []
    def register_tool(self, **kw): self.registered.append(kw)
random.seed(42); regbad = []
for p in random.sample(plugins, 30):
    d = os.path.join(ROOT, "plugins", p["slug"])
    try:
        spec = importlib.util.spec_from_file_location(
            f"hermes_plugin_{p['slug'].replace('-', '_')}",
            os.path.join(d, "__init__.py"), submodule_search_locations=[d])
        mod = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mod; spec.loader.exec_module(mod)
        ctx = FakeCtx(); mod.register(ctx)
        assert len(ctx.registered) == 1 and ctx.registered[0]["name"] == p["tool"]
        assert ctx.registered[0]["schema"]["description"]
        out = ctx.registered[0]["handler"](p.get("sample_input") or {})
        assert out["plugin"] == p["slug"] and "guardrails" in out
    except Exception as e: regbad.append((p["slug"], str(e)))
check("Hermes register(ctx) wiring + handler on 30 sampled plugins", not regbad, str(regbad[:3]))

from core.registry import get_registry
reg = get_registry()
check("registry tools = 1000", len(reg.tools) == 1000, str(len(reg.tools)))
bad = []
for p in plugins:
    t = p["tool"]; meta = reg.tools[t]["meta"]
    try:
        r = reg.call(t, meta["sample_input"])
        assert r["plugin"] == p["slug"] and r["tool"] == t and "result" in r and "guardrails" in r
        assert r["guardrails"]["human_approval_required"]
        k = p["kind"]; res = r["result"]
        if k == "score": assert "score" in res and "breakdown" in res
        elif k == "classify": assert "label" in res
        elif k in ("checklist", "audit"): assert "completion_pct" in res or "present" in res
        elif k == "template": assert "draft" in res and "DRAFT" in res["status"]
        elif k == "analyze": assert isinstance(res, dict)
        elif k == "prioritize": assert "ranked" in res
        elif k == "plan": assert "steps" in res
    except Exception as e: bad.append((t, str(e)))
check("every one of the 1000 tools callable with sample input + shape + guardrails", not bad, str(bad[:3]))

proc = subprocess.Popen([sys.executable, os.path.join(ROOT, "mcp_server.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
def rpc(o):
    proc.stdin.write(json.dumps(o) + "\n"); proc.stdin.flush(); return json.loads(proc.stdout.readline())
r = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
check("MCP initialize", r["result"]["serverInfo"]["name"] == "lionel-hermes-plugins")
r = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
check("MCP tools/list = 1000", len(r["result"]["tools"]) == 1000, str(len(r["result"]["tools"])))
first = plugins[0]
r = rpc({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": first["tool"], "arguments": reg.tools[first["tool"]]["meta"]["sample_input"]}})
check("MCP tools/call works", json.loads(r["result"]["content"][0]["text"])["plugin"] == first["slug"])
proc.stdin.close(); proc.wait(timeout=5)

srv = subprocess.Popen([sys.executable, os.path.join(ROOT, "rest_server.py"), "--port", "8797"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    ok = False
    for _ in range(50):
        try:
            with urllib.request.urlopen("http://127.0.0.1:8797/health", timeout=1) as resp: ok = json.loads(resp.read())["tools"] == 1000
            if ok: break
        except Exception: time.sleep(0.1)
    check("REST /health tools=1000", ok)
    t = first["tool"]
    req = urllib.request.Request(f"http://127.0.0.1:8797/tools/{t}", data=json.dumps(reg.tools[t]["meta"]["sample_input"]).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as resp: body = json.loads(resp.read())
    check("REST /tools/<first> callable", body["plugin"] == first["slug"])
finally:
    srv.terminate(); srv.wait(timeout=5)

print(f"\n{passed} checks passed, {len(fails)} failed")
if fails: print("FAILURES:", fails)
sys.exit(1 if fails else 0)
