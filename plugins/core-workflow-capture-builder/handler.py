"""Handler for Workflow Capture Builder (core-workflow-capture-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['workflow capture goal clarity', 'workflow capture setup completeness', 'workflow capture toolset fit', 'workflow capture guardrail coverage', 'workflow capture verification step'], 'slug': 'core-workflow-capture-builder', 'name': 'Workflow Capture Builder'}
def run(args):
    return run_engine(CONFIG, args or {})
