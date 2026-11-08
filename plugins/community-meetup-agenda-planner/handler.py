"""Handler for Meetup Agenda Planner (community-meetup-agenda-planner). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['meetup agenda member fit', 'meetup agenda tone fit', 'meetup agenda approval gate', 'meetup agenda safety check', 'meetup agenda follow up named'], 'slug': 'community-meetup-agenda-planner', 'name': 'Meetup Agenda Planner'}
def run(args):
    return run_engine(CONFIG, args or {})
