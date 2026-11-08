"""Handler for Task List Triage Reviewer (prod-task-list-triage-reviewer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['task list triage priority clarity', 'task list triage time realism', 'task list triage next action named', 'task list triage review cadence', 'task list triage owner named'], 'slug': 'prod-task-list-triage-reviewer', 'name': 'Task List Triage Reviewer'}
def run(args):
    return run_engine(CONFIG, args or {})
