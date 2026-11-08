"""Handler for Parallel Workstream Checker (multi-parallel-workstream-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['parallel workstream scope clarity', 'parallel workstream independence of subtasks', 'parallel workstream merge criteria', 'parallel workstream context budget', 'parallel workstream verification step'], 'slug': 'multi-parallel-workstream-checker', 'name': 'Parallel Workstream Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
