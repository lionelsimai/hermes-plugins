"""Hermes plugin entry point for Script Draft Runner Checklist.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="terminal_script_draft_runner_checklist", toolset="terminal",
                      schema={"name": "terminal_script_draft_runner_checklist", "description": 'Script Draft Runner Checklist for Hermes Agent: apply a checklist workflow to script draft work — covers command safety, expected output and verification, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
