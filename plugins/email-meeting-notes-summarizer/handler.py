"""Handler for Meeting Notes Summarizer (email-meeting-notes-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['meeting notes priority accuracy', 'meeting notes tone fit', 'meeting notes facts supplied only', 'meeting notes approval gate', 'meeting notes next step clarity'], 'slug': 'email-meeting-notes-summarizer', 'name': 'Meeting Notes Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
