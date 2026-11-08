"""Handler for Conflict Resolution Planner (multi-conflict-resolution-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['conflict resolution scope clarity', 'conflict resolution independence of subtasks', 'conflict resolution merge criteria', 'conflict resolution context budget', 'conflict resolution verification step'], 'slug': 'multi-conflict-resolution-planner', 'name': 'Conflict Resolution Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
