"""Handler for Community Digest Reporter (community-community-digest-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'classify', 'items': ['community digest member fit', 'community digest tone fit', 'community digest approval gate', 'community digest safety check', 'community digest follow up named'], 'slug': 'community-community-digest-reporter', 'name': 'Community Digest Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
