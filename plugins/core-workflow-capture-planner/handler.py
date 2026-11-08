"""Handler for Workflow Capture Planner (core-workflow-capture-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['workflow capture goal clarity', 'workflow capture setup completeness', 'workflow capture toolset fit', 'workflow capture guardrail coverage', 'workflow capture verification step'], 'slug': 'core-workflow-capture-planner', 'name': 'Workflow Capture Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
