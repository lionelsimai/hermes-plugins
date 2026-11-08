"""Handler for Inbox Triage Drafter (email-inbox-triage-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['inbox triage priority accuracy', 'inbox triage tone fit', 'inbox triage facts supplied only', 'inbox triage approval gate', 'inbox triage next step clarity'], 'slug': 'email-inbox-triage-drafter', 'name': 'Inbox Triage Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
