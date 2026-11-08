"""Handler for Travel Hold Summarizer (email-travel-hold-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['travel hold priority accuracy', 'travel hold tone fit', 'travel hold facts supplied only', 'travel hold approval gate', 'travel hold next step clarity'], 'slug': 'email-travel-hold-summarizer', 'name': 'Travel Hold Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
