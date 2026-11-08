"""Hermes plugin entry point for Markdown Note Planner.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="files_markdown_note_planner", toolset="file",
                      schema={"name": "files_markdown_note_planner", "description": 'Markdown Note Planner for Hermes Agent: apply a prioritize workflow to markdown note work — covers format fit, completeness and output location, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
