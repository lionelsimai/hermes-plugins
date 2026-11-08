"""Handler for Dm Triage Summarizer (messaging-dm-triage-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'plan', 'items': ['dm triage audience fit', 'dm triage tone fit', 'dm triage length fit', 'dm triage approval gate', 'dm triage platform fit'], 'slug': 'messaging-dm-triage-summarizer', 'name': 'Dm Triage Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
