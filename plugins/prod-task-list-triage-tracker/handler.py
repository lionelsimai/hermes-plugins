"""Handler for Task List Triage Tracker (prod-task-list-triage-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['task list triage priority clarity', 'task list triage time realism', 'task list triage next action named', 'task list triage review cadence', 'task list triage owner named'], 'slug': 'prod-task-list-triage-tracker', 'name': 'Task List Triage Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
