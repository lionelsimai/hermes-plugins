"""Handler for Deadline Reminder Summarizer (email-deadline-reminder-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['deadline reminder priority accuracy', 'deadline reminder tone fit', 'deadline reminder facts supplied only', 'deadline reminder approval gate', 'deadline reminder next step clarity'], 'slug': 'email-deadline-reminder-summarizer', 'name': 'Deadline Reminder Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
