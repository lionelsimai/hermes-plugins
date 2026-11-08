"""Handler for Task List Triage Planner (prod-task-list-triage-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['task list triage priority clarity', 'task list triage time realism', 'task list triage next action named', 'task list triage review cadence', 'task list triage owner named'], 'slug': 'prod-task-list-triage-planner', 'name': 'Task List Triage Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
