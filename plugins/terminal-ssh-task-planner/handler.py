"""Handler for Ssh Task Planner (terminal-ssh-task-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['ssh task command safety', 'ssh task expected output', 'ssh task timeout set', 'ssh task rollback step', 'ssh task verification'], 'slug': 'terminal-ssh-task-planner', 'name': 'Ssh Task Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
