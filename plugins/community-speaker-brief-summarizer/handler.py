"""Handler for Speaker Brief Summarizer (community-speaker-brief-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'audit', 'items': ['speaker brief member fit', 'speaker brief tone fit', 'speaker brief approval gate', 'speaker brief safety check', 'speaker brief follow up named'], 'slug': 'community-speaker-brief-summarizer', 'name': 'Speaker Brief Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
