"""Handler for Event Run Sheet Summarizer (community-event-run-sheet-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['event run sheet member fit', 'event run sheet tone fit', 'event run sheet approval gate', 'event run sheet safety check', 'event run sheet follow up named'], 'slug': 'community-event-run-sheet-summarizer', 'name': 'Event Run Sheet Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
