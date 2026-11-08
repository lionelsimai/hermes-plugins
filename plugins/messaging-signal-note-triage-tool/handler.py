"""Handler for Signal Note Triage Tool (messaging-signal-note-triage-tool). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['signal note audience fit', 'signal note tone fit', 'signal note length fit', 'signal note approval gate', 'signal note platform fit'], 'slug': 'messaging-signal-note-triage-tool', 'name': 'Signal Note Triage Tool'}
def run(args):
    return run_engine(CONFIG, args or {})
