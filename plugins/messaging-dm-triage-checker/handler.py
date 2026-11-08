"""Handler for Dm Triage Checker (messaging-dm-triage-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['dm triage audience fit', 'dm triage tone fit', 'dm triage length fit', 'dm triage approval gate', 'dm triage platform fit'], 'slug': 'messaging-dm-triage-checker', 'name': 'Dm Triage Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
