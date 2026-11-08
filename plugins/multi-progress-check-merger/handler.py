"""Handler for Progress Check Merger (multi-progress-check-merger). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['progress check scope clarity', 'progress check independence of subtasks', 'progress check merge criteria', 'progress check context budget', 'progress check verification step'], 'slug': 'multi-progress-check-merger', 'name': 'Progress Check Merger'}
def run(args):
    return run_engine(CONFIG, args or {})
