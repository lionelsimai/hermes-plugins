"""Handler for Search Query Set Tracker (web-search-query-set-tracker). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={'kind': 'score', 'items': ['search query set source quality', 'search query set recency', 'search query set corroboration', 'search query set citation completeness', 'search query set scope fit'], 'slug': 'web-search-query-set-tracker', 'name': 'Search Query Set Tracker'}
def run(args):
    return run_engine(CONFIG, args or {})
