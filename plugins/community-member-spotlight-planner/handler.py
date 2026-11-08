"""Handler for Member Spotlight Planner (community-member-spotlight-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['member spotlight member fit', 'member spotlight tone fit', 'member spotlight approval gate', 'member spotlight safety check', 'member spotlight follow up named'], 'slug': 'community-member-spotlight-planner', 'name': 'Member Spotlight Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
