"""Handler for Result Merge Checker (multi-result-merge-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['result merge scope clarity', 'result merge independence of subtasks', 'result merge merge criteria', 'result merge context budget', 'result merge verification step'], 'slug': 'multi-result-merge-checker', 'name': 'Result Merge Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
