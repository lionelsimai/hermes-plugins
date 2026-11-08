"""Handler for Dm Triage Planner (messaging-dm-triage-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['dm triage audience fit', 'dm triage tone fit', 'dm triage length fit', 'dm triage approval gate', 'dm triage platform fit'], 'slug': 'messaging-dm-triage-planner', 'name': 'Dm Triage Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
