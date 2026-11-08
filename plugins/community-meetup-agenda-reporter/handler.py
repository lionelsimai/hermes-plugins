"""Handler for Meetup Agenda Reporter (community-meetup-agenda-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['meetup agenda member fit', 'meetup agenda tone fit', 'meetup agenda approval gate', 'meetup agenda safety check', 'meetup agenda follow up named'], 'slug': 'community-meetup-agenda-reporter', 'name': 'Meetup Agenda Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
