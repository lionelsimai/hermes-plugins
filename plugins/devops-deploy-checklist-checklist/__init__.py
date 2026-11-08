"""Hermes plugin entry point for Deploy Checklist Checklist.

Verified Hermes format: plugin.yaml + __init__.py exposing
register(ctx); tools are wired with ctx.register_tool().
"""
from .handler import run as _run

SCHEMA = {"type": "object", "properties": {"metrics": {"type": "object"}, "counts": {"type": "object"}, "amounts": {"type": "object"}, "series": {"type": "array", "items": {"type": "number"}}, "text": {"type": "string"}, "completed": {"type": "array", "items": {"type": "string"}}, "facts": {"type": "object"}, "items": {"type": "array"}, "goal": {"type": "string"}, "timeframe_days": {"type": "integer"}}, "required": []}

def _handler(params, **kwargs):
    return _run(params or {})

def register(ctx):
    ctx.register_tool(name="devops_deploy_checklist_checklist", toolset="terminal",
                      schema={"name": "devops_deploy_checklist_checklist", "description": 'Deploy Checklist Checklist for Hermes Agent: apply a template workflow to deploy checklist work — covers risk noted, rollback step and window fit, using supplied facts only.', "parameters": SCHEMA},
                      handler=_handler)
