"""Hermes plugin entry point for Sync Job Spec Checker.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="api_sync_job_spec_checker", toolset="web",
                      schema={"name": "api_sync_job_spec_checker", "description": 'Sync Job Spec Checker for Hermes Agent: apply a plan workflow to sync job spec work — covers contract fit, auth handled safely and verification call, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
