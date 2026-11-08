"""Hermes plugin entry point for Transport Check Checker.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="mcp_transport_check_checker", toolset="skills",
                      schema={"name": "mcp_transport_check_checker", "description": 'Transport Check Checker for Hermes Agent: apply a prioritize workflow to transport check work — covers schema validity, description clarity and error behaviour, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
