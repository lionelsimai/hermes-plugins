"""Handler for Debug Session Auditor (terminal-debug-session-auditor). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['debug session command safety', 'debug session expected output', 'debug session timeout set', 'debug session rollback step', 'debug session verification'], 'slug': 'terminal-debug-session-auditor', 'name': 'Debug Session Auditor'}
def run(args):
    return run_engine(CONFIG, args or {})
