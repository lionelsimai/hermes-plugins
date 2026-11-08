"""Handler for Event Run Sheet Checker (community-event-run-sheet-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['event run sheet member fit', 'event run sheet tone fit', 'event run sheet approval gate', 'event run sheet safety check', 'event run sheet follow up named'], 'slug': 'community-event-run-sheet-checker', 'name': 'Event Run Sheet Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
