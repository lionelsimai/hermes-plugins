"""Handler for Task Split Plan Merger (multi-task-split-plan-merger). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['task split plan scope clarity', 'task split plan independence of subtasks', 'task split plan merge criteria', 'task split plan context budget', 'task split plan verification step'], 'slug': 'multi-task-split-plan-merger', 'name': 'Task Split Plan Merger'}
def run(args):
    return run_engine(CONFIG, args or {})
