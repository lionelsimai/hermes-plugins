"""Handler for Shell Command Plan Drafter (terminal-shell-command-plan-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['shell command plan command safety', 'shell command plan expected output', 'shell command plan timeout set', 'shell command plan rollback step', 'shell command plan verification'], 'slug': 'terminal-shell-command-plan-drafter', 'name': 'Shell Command Plan Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
