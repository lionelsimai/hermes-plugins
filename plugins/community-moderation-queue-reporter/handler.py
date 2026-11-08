"""Handler for Moderation Queue Reporter (community-moderation-queue-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'checklist', 'items': ['moderation queue member fit', 'moderation queue tone fit', 'moderation queue approval gate', 'moderation queue safety check', 'moderation queue follow up named'], 'slug': 'community-moderation-queue-reporter', 'name': 'Moderation Queue Reporter'}
def run(args):
    return run_engine(CONFIG, args or {})
