"""Handler for Sandbox Check Auditor (safety-sandbox-check-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['sandbox check risk identified', 'sandbox check approval required', 'sandbox check least privilege', 'sandbox check reversibility', 'sandbox check audit logged'], 'slug': 'safety-sandbox-check-auditor', 'name': 'Sandbox Check Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
