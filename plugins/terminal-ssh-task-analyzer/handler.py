"""Handler for Ssh Task Analyzer (terminal-ssh-task-analyzer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['ssh task command safety', 'ssh task expected output', 'ssh task timeout set', 'ssh task rollback step', 'ssh task verification'], 'slug': 'terminal-ssh-task-analyzer', 'name': 'Ssh Task Analyzer'}
def run(args):
    return run_engine(CONFIG, args or {})
