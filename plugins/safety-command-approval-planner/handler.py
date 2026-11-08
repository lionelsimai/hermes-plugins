"""Handler for Command Approval Planner (safety-command-approval-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['command approval risk identified', 'command approval approval required', 'command approval least privilege', 'command approval reversibility', 'command approval audit logged'], 'slug': 'safety-command-approval-planner', 'name': 'Command Approval Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
