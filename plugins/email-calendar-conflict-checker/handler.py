"""Handler for Calendar Conflict Checker (email-calendar-conflict-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['calendar conflict priority accuracy', 'calendar conflict tone fit', 'calendar conflict facts supplied only', 'calendar conflict approval gate', 'calendar conflict next step clarity'], 'slug': 'email-calendar-conflict-checker', 'name': 'Calendar Conflict Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
