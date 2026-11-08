"""Handler for Result Merge Briefer (multi-result-merge-briefer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['result merge scope clarity', 'result merge independence of subtasks', 'result merge merge criteria', 'result merge context budget', 'result merge verification step'], 'slug': 'multi-result-merge-briefer', 'name': 'Result Merge Briefer'}
def run(args):
    return run_engine(CONFIG, args or {})
