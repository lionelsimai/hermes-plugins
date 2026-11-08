"""Handler for Calendar Conflict Planner (email-calendar-conflict-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['calendar conflict priority accuracy', 'calendar conflict tone fit', 'calendar conflict facts supplied only', 'calendar conflict approval gate', 'calendar conflict next step clarity'], 'slug': 'email-calendar-conflict-planner', 'name': 'Calendar Conflict Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
