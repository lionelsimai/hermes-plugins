"""Handler for Log Inspection Planner (terminal-log-inspection-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['log inspection command safety', 'log inspection expected output', 'log inspection timeout set', 'log inspection rollback step', 'log inspection verification'], 'slug': 'terminal-log-inspection-planner', 'name': 'Log Inspection Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
