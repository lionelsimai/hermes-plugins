"""Handler for Community Digest Checker (community-community-digest-checker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['community digest member fit', 'community digest tone fit', 'community digest approval gate', 'community digest safety check', 'community digest follow up named'], 'slug': 'community-community-digest-checker', 'name': 'Community Digest Checker'}
def run(args):
    return run_engine(CONFIG, args or {})
