"""Handler for Follow Up Note Triage Tool (email-follow-up-note-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['follow up note priority accuracy', 'follow up note tone fit', 'follow up note facts supplied only', 'follow up note approval gate', 'follow up note next step clarity'], 'slug': 'email-follow-up-note-triage-tool', 'name': 'Follow Up Note Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
