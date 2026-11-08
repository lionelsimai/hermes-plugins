"""Handler for Environment Setup Planner (terminal-environment-setup-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['environment setup command safety', 'environment setup expected output', 'environment setup timeout set', 'environment setup rollback step', 'environment setup verification'], 'slug': 'terminal-environment-setup-planner', 'name': 'Environment Setup Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
