"""Hermes plugin entry point for Video Shot List Checker.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="media_video_shot_list_checker", toolset="media",
                      schema={"name": "media_video_shot_list_checker", "description": 'Video Shot List Checker for Hermes Agent: apply a classify workflow to video shot list work — covers brief clarity, format spec and approval gate, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
