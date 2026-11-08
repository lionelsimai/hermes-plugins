"""Handler for Member Spotlight Checker (community-member-spotlight-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['member spotlight member fit', 'member spotlight tone fit', 'member spotlight approval gate', 'member spotlight safety check', 'member spotlight follow up named'], 'slug': 'community-member-spotlight-checker', 'name': 'Member Spotlight Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
