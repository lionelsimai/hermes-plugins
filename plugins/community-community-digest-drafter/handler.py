"""Handler for Community Digest Drafter (community-community-digest-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['community digest member fit', 'community digest tone fit', 'community digest approval gate', 'community digest safety check', 'community digest follow up named'], 'slug': 'community-community-digest-drafter', 'name': 'Community Digest Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
