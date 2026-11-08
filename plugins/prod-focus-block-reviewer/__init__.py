"""Hermes plugin entry point for Focus Block Reviewer.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="prod_focus_block_reviewer", toolset="skills",
                      schema={"name": "prod_focus_block_reviewer", "description": 'Focus Block Reviewer for Hermes Agent: apply a analyze workflow to focus block work — covers priority clarity, time realism and owner named, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
