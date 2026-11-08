"""Hermes plugin entry point for Environment Setup Drafter.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="terminal_environment_setup_drafter", toolset="terminal",
                      schema={"name": "terminal_environment_setup_drafter", "description": 'Environment Setup Drafter for Hermes Agent: apply a prioritize workflow to environment setup work — covers command safety, expected output and verification, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
