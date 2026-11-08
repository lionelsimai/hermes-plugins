"""Handler for Docker Task Runner Checklist (terminal-docker-task-runner-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['docker task command safety', 'docker task expected output', 'docker task timeout set', 'docker task rollback step', 'docker task verification'], 'slug': 'terminal-docker-task-runner-checklist', 'name': 'Docker Task Runner Checklist'}
def run(args):
    return run_engine(CONFIG, args or {})
