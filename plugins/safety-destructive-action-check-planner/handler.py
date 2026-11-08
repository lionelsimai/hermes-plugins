"""Handler for Destructive Action Check Planner (safety-destructive-action-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['destructive action check risk identified', 'destructive action check approval required', 'destructive action check least privilege', 'destructive action check reversibility', 'destructive action check audit logged'], 'slug': 'safety-destructive-action-check-planner', 'name': 'Destructive Action Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
