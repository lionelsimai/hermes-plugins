"""Handler for Moderation Queue Summarizer (community-moderation-queue-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['moderation queue member fit', 'moderation queue tone fit', 'moderation queue approval gate', 'moderation queue safety check', 'moderation queue follow up named'], 'slug': 'community-moderation-queue-summarizer', 'name': 'Moderation Queue Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
