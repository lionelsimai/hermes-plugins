"""Handler for Citation List Summarizer (web-citation-list-summarizer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'prioritize', 'items': ['citation list source quality', 'citation list recency', 'citation list corroboration', 'citation list citation completeness', 'citation list scope fit'], 'slug': 'web-citation-list-summarizer', 'name': 'Citation List Summarizer'}
def run(args):
    return run_engine(CONFIG, args or {})
