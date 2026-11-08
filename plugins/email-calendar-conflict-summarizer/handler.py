"""Handler for Calendar Conflict Summarizer (email-calendar-conflict-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['calendar conflict priority accuracy', 'calendar conflict tone fit', 'calendar conflict facts supplied only', 'calendar conflict approval gate', 'calendar conflict next step clarity'], 'slug': 'email-calendar-conflict-summarizer', 'name': 'Calendar Conflict Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
