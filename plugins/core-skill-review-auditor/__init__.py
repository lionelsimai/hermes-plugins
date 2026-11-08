"""Hermes plugin entry point for Skill Review Auditor.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="core_skill_review_auditor", toolset="skills",
                      schema={"name": "core_skill_review_auditor", "description": 'Skill Review Auditor for Hermes Agent: apply a prioritize workflow to skill review work — covers goal clarity, setup completeness and verification step, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
