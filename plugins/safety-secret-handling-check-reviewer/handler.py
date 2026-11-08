"""Handler for Secret Handling Check Reviewer (safety-secret-handling-check-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['secret handling check risk identified', 'secret handling check approval required', 'secret handling check least privilege', 'secret handling check reversibility', 'secret handling check audit logged'], 'slug': 'safety-secret-handling-check-reviewer', 'name': 'Secret Handling Check Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
