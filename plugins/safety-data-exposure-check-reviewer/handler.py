"""Handler for Data Exposure Check Reviewer (safety-data-exposure-check-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['data exposure check risk identified', 'data exposure check approval required', 'data exposure check least privilege', 'data exposure check reversibility', 'data exposure check audit logged'], 'slug': 'safety-data-exposure-check-reviewer', 'name': 'Data Exposure Check Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
