"""Handler for Event Run Sheet Reporter (community-event-run-sheet-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'template', 'items': ['event run sheet member fit', 'event run sheet tone fit', 'event run sheet approval gate', 'event run sheet safety check', 'event run sheet follow up named'], 'slug': 'community-event-run-sheet-reporter', 'name': 'Event Run Sheet Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
