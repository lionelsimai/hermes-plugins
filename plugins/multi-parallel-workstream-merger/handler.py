"""Handler for Parallel Workstream Merger (multi-parallel-workstream-merger). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['parallel workstream scope clarity', 'parallel workstream independence of subtasks', 'parallel workstream merge criteria', 'parallel workstream context budget', 'parallel workstream verification step'], 'slug': 'multi-parallel-workstream-merger', 'name': 'Parallel Workstream Merger'}
def run(args):
    return run_engine(CONFIG, args or {})
