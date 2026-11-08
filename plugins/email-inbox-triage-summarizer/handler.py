"""Handler for Inbox Triage Summarizer (email-inbox-triage-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['inbox triage priority accuracy', 'inbox triage tone fit', 'inbox triage facts supplied only', 'inbox triage approval gate', 'inbox triage next step clarity'], 'slug': 'email-inbox-triage-summarizer', 'name': 'Inbox Triage Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
