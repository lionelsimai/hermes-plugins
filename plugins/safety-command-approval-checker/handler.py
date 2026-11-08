"""Handler for Command Approval Checker (safety-command-approval-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['command approval risk identified', 'command approval approval required', 'command approval least privilege', 'command approval reversibility', 'command approval audit logged'], 'slug': 'safety-command-approval-checker', 'name': 'Command Approval Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
