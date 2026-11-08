"""Handler for Command Approval Auditor (safety-command-approval-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['command approval risk identified', 'command approval approval required', 'command approval least privilege', 'command approval reversibility', 'command approval audit logged'], 'slug': 'safety-command-approval-auditor', 'name': 'Command Approval Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
