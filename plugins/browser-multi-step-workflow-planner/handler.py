"""Handler for Multi Step Workflow Planner (browser-multi-step-workflow-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['multi step workflow step clarity', 'multi step workflow fallback step', 'multi step workflow data accuracy', 'multi step workflow confirmation gate', 'multi step workflow completion proof'], 'slug': 'browser-multi-step-workflow-planner', 'name': 'Multi Step Workflow Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
