"""Handler for Feedback Summary Drafter (community-feedback-summary-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'analyze', 'items': ['feedback summary member fit', 'feedback summary tone fit', 'feedback summary approval gate', 'feedback summary safety check', 'feedback summary follow up named'], 'slug': 'community-feedback-summary-drafter', 'name': 'Feedback Summary Drafter'}
def run(args):
    return run_engine(CONFIG, args or {})
