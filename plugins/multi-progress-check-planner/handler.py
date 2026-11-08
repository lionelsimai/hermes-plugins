"""Handler for Progress Check Planner (multi-progress-check-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['progress check scope clarity', 'progress check independence of subtasks', 'progress check merge criteria', 'progress check context budget', 'progress check verification step'], 'slug': 'multi-progress-check-planner', 'name': 'Progress Check Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
