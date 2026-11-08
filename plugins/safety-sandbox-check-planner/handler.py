"""Handler for Sandbox Check Planner (safety-sandbox-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['sandbox check risk identified', 'sandbox check approval required', 'sandbox check least privilege', 'sandbox check reversibility', 'sandbox check audit logged'], 'slug': 'safety-sandbox-check-planner', 'name': 'Sandbox Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
