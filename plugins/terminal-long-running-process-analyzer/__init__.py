"""Hermes plugin entry point for Long Running Process Analyzer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="terminal_long_running_process_analyzer", toolset="terminal",
                      schema={"name": "terminal_long_running_process_analyzer", "description": 'Long Running Process Analyzer for Hermes Agent: apply a checklist workflow to long running process work — covers command safety, expected output and verification, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
