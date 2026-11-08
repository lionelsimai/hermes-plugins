"""Handler for Debug Session Planner (terminal-debug-session-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['debug session command safety', 'debug session expected output', 'debug session timeout set', 'debug session rollback step', 'debug session verification'], 'slug': 'terminal-debug-session-planner', 'name': 'Debug Session Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
